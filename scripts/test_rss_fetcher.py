import sys
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import build_site
import cve_fetcher
import groq_client
import quote
import rss_fetcher


class TestSSRFAndURL(unittest.TestCase):
    def test_safe_urls(self):
        self.assertTrue(rss_fetcher.is_safe_url("http://example.com"))
        self.assertTrue(rss_fetcher.is_safe_url("https://google.com"))

    def test_unsafe_urls(self):
        self.assertFalse(rss_fetcher.is_safe_url("http://localhost"))
        self.assertFalse(rss_fetcher.is_safe_url("http://127.0.0.1"))
        self.assertFalse(rss_fetcher.is_safe_url("http://192.168.1.1"))
        self.assertFalse(rss_fetcher.is_safe_url("http://10.0.0.1"))
        self.assertFalse(rss_fetcher.is_safe_url("http://172.16.0.1"))
        self.assertFalse(rss_fetcher.is_safe_url("http://169.254.169.254/latest/meta-data/"))
        self.assertFalse(rss_fetcher.is_safe_url("file:///etc/passwd"))
        self.assertFalse(rss_fetcher.is_safe_url("ftp://example.com"))
        self.assertFalse(rss_fetcher.is_safe_url("http://0.0.0.0"))

    def test_fetch_article_unsafe_url(self):
        self.assertEqual(rss_fetcher.fetch_article("http://127.0.0.1"), "")
        self.assertEqual(rss_fetcher.fetch_article("http://localhost"), "")

    def test_normalize_url_relative_and_tracking(self):
        resolved = rss_fetcher.normalize_url("/news/advisory?id=&utm_source=rss&a=1#frag", base_url="https://example.com/feed")
        self.assertEqual(resolved, "https://example.com/news/advisory?id=&a=1")
        self.assertEqual(rss_fetcher.normalize_url("javascript:alert(1)"), "")


class TestRSSParsing(unittest.TestCase):
    def test_capped_feed_retries_without_validators(self):
        url = "https://example.com/feed"
        entries = [
            {"link": f"https://example.com/news/{i}", "title": f"News {i}", "summary": "A report. " * 45}
            for i in range(3)
        ]
        state = {"feed_cache": {url: {"etag": "old"}}}
        fetched = {"entries": entries, "ok": True, "cache": {"etag": "current"}}
        with (
            patch.object(rss_fetcher, "MAX_ITEMS_PER_FEED", 2),
            patch.object(rss_fetcher.GroqClient, "validate_models", return_value=False),
            patch.object(rss_fetcher, "load_feeds", return_value=[{"url": url, "name": "Example"}]),
            patch.object(rss_fetcher, "load_state", return_value=state),
            patch.object(rss_fetcher, "save_state"),
            patch.object(rss_fetcher, "fetch_feed", return_value=fetched) as fetch,
            patch.object(rss_fetcher, "write_post_markdown") as write,
        ):
            rss_fetcher.main()
            self.assertEqual(write.call_count, 2)
            self.assertNotIn(url, state["feed_cache"])
            rss_fetcher.main()
            fetch.assert_called_with({"url": url, "name": "Example"}, None)
            self.assertEqual(write.call_count, 3)
            self.assertEqual(state["feed_cache"][url], {"etag": "current"})

    def test_clean_title_sans_stormcast(self):
        raw = "ISC Stormcast For Wednesday, November 25th, 2026 https://isc.sans.edu/podcastdetail/10194, (Wed, Nov"
        self.assertEqual(rss_fetcher.clean_title(raw), "ISC Stormcast For Wednesday, November 25th, 2026")

    def test_clean_html_preserves_paragraphs_and_decodes_entities(self):
        raw_html = "<p>First &amp; second</p><p>Third paragraph.</p><script>evil()</script><p>The post Foo appeared first on Bar.</p>"
        cleaned = rss_fetcher.clean_html_to_text(raw_html)
        self.assertEqual(cleaned, "First & second Third paragraph.")

    def test_plain_text_preserves_angle_brackets(self):
        cleaned = rss_fetcher.clean_html_to_text("Use <Directory> safely", content_type="text/plain")
        self.assertEqual(cleaned, "Use <Directory> safely")

    def test_extract_entry_content_prefers_richer_content(self):
        entry = {
            "description": "Short teaser [...]",
            "content": [{"type": "text/html", "value": "<p>Full detailed security analysis covering CVE-2026-1234 and lateral movement.</p>" * 5}],
        }
        extracted = rss_fetcher.extract_entry_content(entry)
        self.assertIn("Full detailed security analysis", extracted)


class TestBuildSiteAndDates(unittest.TestCase):
    def test_post_and_cve_rank_by_displayed_publication_date(self):
        import tempfile

        records = [
            ("old-post", "post", "2026-11-12", "2026-11-27"),
            ("new-post", "post", "2026-11-17", "2026-11-19"),
            ("CVE-2026-1234", "cve", "2026-11-13", "2026-11-28"),
            ("undated-post", "post", "", "2026-11-14"),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            compiled = []
            for slug, kind, published, fallback in records:
                path = Path(tmp) / f"{slug}.md"
                path.write_text(
                    f'---\ntitle: "{slug}"\npublished: "{published}"\n'
                    f'date: "{fallback}"\ningested_at: "{fallback}"\n---\nBody\n',
                    encoding="utf-8",
                )
                compiled.append(build_site.compile_markdown_item(path, kind))
        compiled.sort(key=lambda item: item["sort_ts"], reverse=True)
        self.assertEqual([item["slug"] for item in compiled], [
            "new-post", "undated-post", "CVE-2026-1234", "old-post",
        ])
        self.assertEqual([item["formatted_date"] for item in compiled], [
            "17-11-26", "14-11-26", "13-11-26", "12-11-26",
        ])

    def test_universal_dd_mm_yy_date_format(self):
        self.assertEqual(build_site.format_date_short("2026-11-27T22:06:11+05:30"), "27-11-26")
        self.assertEqual(build_site.format_date_short("2025-05-27T21:15:23.197Z"), "27-05-25")
        self.assertEqual(build_site.format_date_short("invalid"), "")

    def test_xss_escaping_and_callout_rendering(self):
        raw_md = (
            "### Executive Summary\n\n"
            "Payload <script>alert(1)</script> and <Directory> tag.\n\n"
            "> [!CAUTION]\n"
            "> **Known Exploited Vulnerability:** YES (CISA KEV Added: 2026-07-13)\n"
        )
        norm = build_site.normalize_markdown_body(raw_md, is_cve=True)
        safe = build_site.escape_raw_html_outside_code(norm)
        raw_html = build_site.md.convert(safe)
        build_site.md.reset()
        rendered = build_site.sanitize_and_enhance_html(raw_html)

        self.assertNotIn("<script>", rendered)
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", rendered)
        self.assertIn("&lt;Directory&gt;", rendered)
        self.assertIn('class="callout callout-caution"', rendered)
        self.assertIn("13-07-26", rendered)

    def test_metadata_list_normalization(self):
        raw_md = (
            "---\n"
            "**Authoritative CVE Metadata**\n"
            "- **CVSS Base Score:** 7.5 (HIGH)\n"
            "- **Published:** 2026-06-25T17:17:04.180\n"
            "- **Last Modified:** 2026-09-13T01:16:38.340\n"
        )
        norm = build_site.normalize_markdown_body(raw_md, is_cve=True)
        raw_html = build_site.md.convert(build_site.escape_raw_html_outside_code(norm))
        build_site.md.reset()
        rendered = build_site.sanitize_and_enhance_html(raw_html)
        self.assertIn("<ul>", rendered)
        self.assertIn("<li>", rendered)
        self.assertNotIn("Published:", rendered)
        self.assertIn("13-09-26", rendered)


class TestQuotesAndGroq(unittest.TestCase):
    def test_cve_cap_preserves_failed_writes(self):
        pending = [
            {"id": f"CVE-2026-{i:04d}", "description": "Description.", "modified": "2026-01-01"}
            for i in range(3)
        ]
        state = {"seen_cves": {}, "last_run": None, "pending_cves": pending, "pending_kev_ids": []}
        with (
            patch.object(cve_fetcher.GroqClient, "validate_models", return_value=False),
            patch.object(cve_fetcher, "MAX_CVES_PER_RUN", 1),
            patch.object(cve_fetcher, "load_state", return_value=state),
            patch.object(cve_fetcher, "save_state"),
            patch.object(cve_fetcher, "fetch_kev_catalog", return_value=({}, True, set())),
            patch.object(cve_fetcher, "fetch_nvd_window", return_value=[]),
            patch.object(cve_fetcher, "write_cve_markdown", side_effect=[OSError("Write failed"), None]),
        ):
            cve_fetcher.main()
        self.assertEqual(state["pending_cves"], [pending[0], pending[2]])

    def test_quotes_have_no_replacement_char(self):
        quotes = quote.load_quotes()
        self.assertGreater(len(quotes), 100)
        for q in quotes:
            self.assertNotIn("\ufffd", q["quote"])

    def test_groq_tag_normalization_never_splits_chars(self):
        self.assertEqual(groq_client._normalize_tags("malware, ransomware"), ["malware", "ransomware"])
        self.assertEqual(groq_client._normalize_tags(["CVE-2026-1", 42]), ["CVE-2026-1", "42"])

    def test_cve_id_validation(self):
        self.assertIsNone(cve_fetcher.extract_nvd_metadata({"cve": {"id": "../../etc/passwd"}}))
        meta = cve_fetcher.extract_nvd_metadata({
            "cve": {
                "id": "CVE-2026-12345",
                "vulnStatus": "Analyzed",
                "descriptions": [{"lang": "en", "value": "Buffer overflow."}],
                "metrics": {"cvssMetricV40": [{"type": "Primary", "cvssData": {"baseScore": 9.8, "baseSeverity": "CRITICAL"}}]},
                "published": "2026-11-20T10:00:00.000",
                "lastModified": "2026-11-21T10:00:00.000",
            }
        })
        self.assertEqual(meta["cvss"], "9.8")
        self.assertEqual(meta["severity"], "CRITICAL")

    def test_cve_alias_formatting(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            p1 = Path(tmp) / "CVE-2026-1001.md"
            p1.write_text("---\ntitle: \"CVE-2026-1001\"\ncve: \"CVE-2026-1001\"\ncve_name: \"php2shell\"\n---\nBody\n", encoding="utf-8")
            p2 = Path(tmp) / "CVE-2026-1002.md"
            p2.write_text("---\ntitle: \"CVE-2026-1002\"\ncve: \"CVE-2026-1002\"\n---\nBody\n", encoding="utf-8")
            self.assertEqual(build_site.compile_markdown_item(p1, "cve")["title"], "CVE-2026-1001 (php2shell)")
            self.assertEqual(build_site.compile_markdown_item(p2, "cve")["title"], "CVE-2026-1002")
            cve_fetcher.write_cve_markdown(
                {"id": "CVE-2026-1001", "description": "Source description.", "cvss": "Unknown", "severity": "Unknown"},
                "Updated summary.", [], False, None, "2026-11-27T00:00:00Z", p1,
            )
            self.assertEqual(build_site.compile_markdown_item(p1, "cve")["title"], "CVE-2026-1001 (php2shell)")


if __name__ == "__main__":
    unittest.main()
