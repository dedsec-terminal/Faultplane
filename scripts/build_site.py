import concurrent.futures
import hashlib
import html
import json
import math
import os
import pickle
import re
import shutil
import time
from datetime import datetime, timezone
from html.parser import HTMLParser
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

try:
    from yaml import CSafeLoader as Loader
except ImportError:
    from yaml import SafeLoader as Loader

BASE_DIR = Path(__file__).resolve().parent.parent
POSTS_DIR = BASE_DIR / "content" / "posts"
CVES_DIR = BASE_DIR / "content" / "cves"
CONFIG_FILE = BASE_DIR / "config" / "feeds.yaml"
SRC_DIR = BASE_DIR / "src"
DIST_DIR = BASE_DIR / "dist"
TEMPLATES_DIR = SRC_DIR / "templates"
DATA_DIR = DIST_DIR / "data"
CACHE_DIR = BASE_DIR / ".build_cache"
CACHE_FILE = CACHE_DIR / "content_cache_v2.pkl"

BASE_URL = os.getenv("FAULTPLANE_BASE_URL", "/Faultplane").rstrip("/")
POSTS_PER_PAGE = 20

VALID_CATEGORIES = {
    "threat-intel",
    "malware",
    "vulnerabilities",
    "cves",
    "data-breaches",
    "research",
    "campaigns",
    "other",
}

ALLOWED_HTML_TAGS = {
    "h1", "h2", "h3", "h4", "h5", "h6",
    "p", "ul", "ol", "li", "blockquote",
    "pre", "code", "strong", "em", "a",
    "hr", "br", "table", "thead", "tbody", "tr", "th", "td",
    "div", "span",
}
STRIP_COMPLETELY_TAGS = {"script", "style", "iframe", "object", "embed", "form"}

FRONTMATTER_RE = re.compile(r"^---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n(.*))?$", re.DOTALL)
FENCE_RE = re.compile(r"^\s*(```|~~~)")
ISO_IN_TEXT_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?)?)\b")

md = markdown.Markdown(extensions=["extra", "codehilite", "sane_lists"])


def parse_iso_utc(val):
    """Parse an ISO date/datetime value into an aware UTC datetime, or return None."""
    if not val:
        return None
    if isinstance(val, datetime):
        dt = val
    else:
        raw = str(val).strip()
        if not raw:
            return None
        try:
            dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except ValueError:
            try:
                dt = datetime.strptime(raw[:10], "%Y-%m-%d")
            except ValueError:
                return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def format_date_short(val):
    """Format any date/ISO timestamp universally as dd-mm-yy."""
    dt = parse_iso_utc(val)
    return dt.strftime("%d-%m-%y") if dt else ""


def parse_frontmatter(content):
    """Extract YAML frontmatter only when bounded by standalone --- delimiter lines."""
    match = FRONTMATTER_RE.match(content)
    if not match:
        return {}, content
    try:
        frontmatter = yaml.load(match.group(1), Loader=Loader) or {}
        if not isinstance(frontmatter, dict):
            frontmatter = {}
        return frontmatter, match.group(2) or ""
    except Exception as e:
        print(f"Error parsing frontmatter: {e}")
        return {}, content


def is_safe_href(url):
    """Allow only http(s) and site-relative URLs in links."""
    if not isinstance(url, str):
        return False
    u = url.strip()
    lower = u.lower()
    return lower.startswith("https://") or lower.startswith("http://") or u.startswith("/")


def repair_mojibake_and_entities(text):
    """Decode HTML entities, repair UTF-8-as-cp1252 mojibake, and strip invisible junk."""
    decoded = html.unescape(text)
    # Repair sequences like â€“ / â€™ / â€œ produced by UTF-8 bytes decoded as cp1252/latin-1
    if "â€" in decoded or "Ã" in decoded:
        def _fix_chunk(match):
            chunk = match.group(0)
            try:
                return chunk.encode("cp1252").decode("utf-8")
            except (UnicodeEncodeError, UnicodeDecodeError):
                return chunk
        decoded = re.sub(r"(?:[\u00c0-\u00ff][\u0080-\u024f\u2018-\u203a\u20ac™šžŸ]+)+", _fix_chunk, decoded)
    return decoded.replace("\u200b", "").replace("\ufeff", "").replace("\r", "")


def normalize_markdown_body(body, is_cve=False):
    """Repair legacy Markdown quirks, strip redundant dates/metadata, and format inline dates."""
    text = body.replace(" \ufffd ", " — ").replace("\ufffd", "—")

    # Remove redundant Intelligence Metadata block (Category, Date, Source are already on the page)
    text = re.sub(
        r"\n*---\s*\n\*\*Intelligence Metadata\*\*\s*\n(?:- \*\*.*?\n)+",
        "\n\n",
        text,
        flags=re.MULTILINE,
    )

    # Drop pointless "Original Description: No description provided." or whitespace/zwsp-only sections
    text = re.sub(
        r"\n*(?:\*\*Original Description:\*\*|### Original Description)\s*\n+(?:No description provided\.?|[\s\r]*)(?=\n*$)",
        "\n",
        text,
        flags=re.IGNORECASE,
    )

    # Upgrade bold section labels to proper headings with blank lines so lists/paragraphs parse cleanly
    text = re.sub(r"\*\*Original Description:\*\*\s*\n+", "### Original Description\n\n", text)
    text = re.sub(r"\*\*Original Overview:\*\*\s*\n+", "### Original Overview\n\n", text)

    if is_cve:
        text = re.sub(
            r"\*\*Authoritative CVE Metadata\*\*\s*\n+",
            "### Authoritative CVE Metadata\n\n",
            text,
        )
        # Drop redundant Published bullet from body since header already carries publication date
        text = re.sub(r"^- \*\*Published:\*\*.*(?:\r?\n)?", "", text, flags=re.MULTILINE)

        # Format ISO dates inside Last Modified / KEV lines to dd-mm-yy
        def _fmt_iso_match(m):
            formatted = format_date_short(m.group(1))
            return formatted or m.group(1)

        text = re.sub(
            r"^(- \*\*Last Modified:\*\*\s*)(.+)$",
            lambda m: m.group(1) + ISO_IN_TEXT_RE.sub(_fmt_iso_match, m.group(2)),
            text,
            flags=re.MULTILINE,
        )
        text = re.sub(
            r"(CISA KEV Added:\s*)([^\)\n]+)",
            lambda m: m.group(1) + ISO_IN_TEXT_RE.sub(_fmt_iso_match, m.group(2)),
            text,
        )

    return text


def escape_raw_html_outside_code(md_text):
    """Escape raw angle-bracket HTML outside code blocks while preserving Markdown blockquotes."""
    lines = md_text.splitlines()
    out = []
    in_fence = False
    fence_char = None

    for line in lines:
        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)[0]
            if not in_fence:
                in_fence = True
                fence_char = marker
            elif marker == fence_char:
                in_fence = False
                fence_char = None
            out.append(line)
            continue

        if in_fence or line.startswith("    ") or line.startswith("\t"):
            out.append(line)
            continue

        # Preserve leading Markdown blockquote marker '>'
        bq_match = re.match(r"^(\s*(?:>\s*)+)(.*)$", line)
        if bq_match:
            prefix, rest = bq_match.group(1), bq_match.group(2)
        else:
            prefix, rest = "", line

        # Decode legacy HTML entities once, then escape literal < and > outside inline `code`
        segments = re.split(r"(`[^`]+`)", rest)
        safe_segments = []
        for idx, seg in enumerate(segments):
            if idx % 2 == 1:
                safe_segments.append(seg)
            else:
                decoded = repair_mojibake_and_entities(seg)
                decoded = decoded.replace("<", "&lt;").replace(">", "&gt;")
                safe_segments.append(decoded)

        out.append(prefix + "".join(safe_segments))

    return "\n".join(out)


CALLOUT_BQ_RE = re.compile(
    r"<blockquote>\s*<p>\s*\[!(CAUTION|WARNING|NOTE|IMPORTANT)\]\s*(?:<br\s*/?>)?\s*",
    re.IGNORECASE,
)
CALLOUT_TITLES = {
    "caution": "CAUTION",
    "warning": "WARNING",
    "important": "IMPORTANT",
    "note": "NOTE",
}
VOID_HTML_TAGS = {"hr", "br"}


class _FastAllowlistSanitizer(HTMLParser):
    """Lightweight single-pass HTML allowlist sanitizer (no heavy DOM tree allocation)."""

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.parts = []
        self.skip_depth = 0
        self.skip_tag = None

    def handle_starttag(self, tag, attrs):
        tag_l = tag.lower()
        if self.skip_depth > 0:
            if tag_l == self.skip_tag:
                self.skip_depth += 1
            return
        if tag_l in STRIP_COMPLETELY_TAGS:
            self.skip_depth = 1
            self.skip_tag = tag_l
            return
        if tag_l not in ALLOWED_HTML_TAGS:
            return

        safe_attrs = []
        attr_map = dict(attrs)
        if tag_l == "a":
            href = attr_map.get("href") or ""
            if is_safe_href(href):
                safe_attrs.append(f'href="{html.escape(href, quote=True)}"')
                if href.startswith(("http://", "https://")):
                    safe_attrs.append('target="_blank"')
                    safe_attrs.append('rel="noopener noreferrer"')
        elif tag_l in ("div", "span", "pre", "code") and attr_map.get("class"):
            classes = [c for c in str(attr_map["class"]).split() if re.match(r"^[a-zA-Z0-9_-]+$", c)]
            if classes:
                safe_attrs.append(f'class="{" ".join(classes)}"')

        attr_str = (" " + " ".join(safe_attrs)) if safe_attrs else ""
        self.parts.append(f"<{tag_l}{attr_str}>")

    def handle_endtag(self, tag):
        tag_l = tag.lower()
        if self.skip_depth > 0:
            if tag_l == self.skip_tag:
                self.skip_depth -= 1
                if self.skip_depth == 0:
                    self.skip_tag = None
            return
        if tag_l in ALLOWED_HTML_TAGS and tag_l not in VOID_HTML_TAGS:
            self.parts.append(f"</{tag_l}>")

    def handle_startendtag(self, tag, attrs):
        tag_l = tag.lower()
        if self.skip_depth == 0 and tag_l in VOID_HTML_TAGS:
            self.parts.append(f"<{tag_l}>")

    def handle_data(self, data):
        if self.skip_depth == 0:
            self.parts.append(html.escape(data, quote=False))

    def handle_entityref(self, name):
        if self.skip_depth == 0:
            self.parts.append(f"&{name};")

    def handle_charref(self, name):
        if self.skip_depth == 0:
            self.parts.append(f"&#{name};")


def sanitize_and_enhance_html(raw_html):
    """Transform GitHub-style callouts and enforce fast allowlist HTML sanitization."""
    def _replace_callout(match):
        kind = match.group(1).lower()
        title = CALLOUT_TITLES.get(kind, kind.upper())
        # Replace opening <blockquote><p>[!KIND] ... with callout div and marker for closing blockquote
        return f'<div class="callout callout-{kind}" data-callout="1"><div class="callout-title">{title}</div><p>'

    enhanced = raw_html
    if "[!" in enhanced:
        # Transform callout blockquotes cleanly (only the first matching blockquote block)
        parts = enhanced.split("<blockquote>")
        rebuilt = [parts[0]]
        for seg in parts[1:]:
            m = re.match(r"\s*<p>\s*\[!(CAUTION|WARNING|NOTE|IMPORTANT)\]\s*(?:<br\s*/?>)?\s*", seg, re.IGNORECASE)
            if m and "</blockquote>" in seg:
                kind = m.group(1).lower()
                title = CALLOUT_TITLES.get(kind, kind.upper())
                body_seg = seg[m.end():].replace("</blockquote>", "</div>", 1)
                rebuilt.append(
                    f'<div class="callout callout-{kind}"><div class="callout-title">{title}</div><p>{body_seg}'
                )
            else:
                rebuilt.append("<blockquote>" + seg)
        enhanced = "".join(rebuilt)

    sanitizer = _FastAllowlistSanitizer()
    sanitizer.feed(enhanced)
    sanitizer.close()
    return "".join(sanitizer.parts)


def compile_markdown_item(md_file: Path, item_type: str):
    """Read, parse, normalize, and safely render a single Markdown post or CVE."""
    content = md_file.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(content)

    if frontmatter.get("draft", False):
        return None

    normalized_body = normalize_markdown_body(body, is_cve=(item_type == "cve"))
    safe_md = escape_raw_html_outside_code(normalized_body)
    # Remove any ### Original Description heading left empty after mojibake/zwsp cleanup
    safe_md = re.sub(r"\n*### Original Description\s*\Z", "\n", safe_md)
    try:
        raw_html = md.convert(safe_md)
    finally:
        md.reset()
    html_body = sanitize_and_enhance_html(raw_html)

    slug = md_file.stem
    raw_date = frontmatter.get("date")
    raw_published = frontmatter.get("published")
    raw_ingested = frontmatter.get("ingested_at")

    display_dt = parse_iso_utc(raw_published) or parse_iso_utc(raw_date) or parse_iso_utc(raw_ingested)
    sort_ts = display_dt.timestamp() if display_dt else float("-inf")
    formatted_date = display_dt.strftime("%d-%m-%y") if display_dt else ""

    category = str(frontmatter.get("category", "other")).lower().strip().replace(" ", "-")
    if category not in VALID_CATEGORIES:
        category = "other"

    raw_tags = frontmatter.get("tags", [])
    tags = [str(t).strip() for t in raw_tags if isinstance(t, (str, int, float)) and str(t).strip()] if isinstance(raw_tags, list) else []

    raw_title = html.unescape(str(frontmatter.get("title") or "Untitled")).strip()
    raw_desc = html.unescape(str(frontmatter.get("description") or "")).strip()
    raw_quote = frontmatter.get("quote")
    quote = html.unescape(str(raw_quote)).replace(" \ufffd ", " — ").replace("\ufffd", "—").strip() if raw_quote else None
    quote_author = html.unescape(str(frontmatter.get("quote_author") or "Unknown")).strip()

    source_url = frontmatter.get("source_url")
    if source_url and not is_safe_href(str(source_url)):
        source_url = None

    item = {
        "title": raw_title,
        "description": raw_desc,
        "formatted_date": formatted_date,
        "date_iso": display_dt.date().isoformat() if display_dt else "",
        "sort_ts": sort_ts,
        "category": category,
        "tags": tags,
        "slug": slug,
        "body": html_body,
        "type": item_type,
        "quote": quote,
        "quote_author": quote_author,
        "source": str(frontmatter.get("source") or "").strip() or None,
        "source_url": str(source_url).strip() if source_url else None,
    }

    if item_type == "cve":
        cve_id = str(frontmatter.get("cve") or slug).strip().upper()
        alias = frontmatter.get("cve_name") or frontmatter.get("alias")
        cve_name = html.unescape(alias).strip() if isinstance(alias, str) else ""
        if len(cve_name) > 60 or cve_name.casefold().rstrip(".") in (
            cve_id.casefold(), "null", "none", "n/a", "unknown", "no alias",
        ):
            cve_name = ""
        item["title"] = f"{cve_id} ({cve_name})" if cve_name else cve_id
        item["url"] = f"{BASE_URL}/cves/{slug}.html"
        item["cve"] = cve_id
        item["cvss"] = str(frontmatter.get("cvss") or "Unknown")
        item["severity"] = str(frontmatter.get("severity") or "Unknown").upper() if frontmatter.get("severity") else "Unknown"
        if item["severity"] == "UNKNOWN":
            item["severity"] = "Unknown"
        item["severity_slug"] = re.sub(r"[^a-z0-9]+", "-", item["severity"].lower()).strip("-") or "unknown"
        item["kev"] = bool(frontmatter.get("kev", False))
    else:
        item["url"] = f"{BASE_URL}/posts/{slug}.html"

    return item


def get_renderer_fingerprint():
    """Invalidate compiled items when their renderer or dependencies change."""
    h = hashlib.sha256()
    h.update(Path(__file__).read_bytes())
    h.update(BASE_URL.encode("utf-8"))
    for package in ("Markdown", "Pygments", "PyYAML"):
        try:
            package_version = version(package)
        except PackageNotFoundError:
            package_version = "missing"
        h.update(f"{package}={package_version}\n".encode("utf-8"))
    return h.hexdigest()[:16]


def load_all_items_cached():
    """Load posts and CVEs using an mtime+size+renderer cache to skip unchanged Markdown."""
    fingerprint = get_renderer_fingerprint()
    cached_entries = {}
    if CACHE_FILE.exists():
        try:
            payload = pickle.loads(CACHE_FILE.read_bytes())
            if isinstance(payload, dict) and payload.get("fingerprint") == fingerprint:
                cached_entries = payload.get("entries", {})
        except Exception:
            cached_entries = {}

    new_cache = {}
    posts = []
    cves = []
    cache_hits = 0
    cache_misses = 0

    for directory, item_type, target_list in ((POSTS_DIR, "post", posts), (CVES_DIR, "cve", cves)):
        if not directory.exists():
            continue
        for md_file in directory.glob("*.md"):
            st = md_file.stat()
            cache_key = f"{item_type}/{md_file.name}"
            cached = cached_entries.get(cache_key)
            if cached and cached[0] == st.st_mtime_ns and cached[1] == st.st_size:
                item = cached[2]
                cache_hits += 1
            else:
                item = compile_markdown_item(md_file, item_type)
                cache_misses += 1
            new_cache[cache_key] = (st.st_mtime_ns, st.st_size, item)
            if item is not None:
                target_list.append(item)

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_bytes(pickle.dumps({"fingerprint": fingerprint, "entries": new_cache}, protocol=pickle.HIGHEST_PROTOCOL))
    print(f"Loaded {len(posts)} posts & {len(cves)} CVEs (cache hits={cache_hits}, compiled={cache_misses}).")
    return posts, cves


def build_nav_items():
    """Return ordered primary navigation entries across all active intelligence views."""
    return [
        {"id": "home", "label": "Overview", "href": f"{BASE_URL}/index.html"},
        {"id": "feed", "label": "Live Feed", "href": f"{BASE_URL}/feed/index.html"},
        {"id": "threat-intel", "label": "Threat Intel", "href": f"{BASE_URL}/categories/threat-intel.html"},
        {"id": "data-breaches", "label": "Data Breaches", "href": f"{BASE_URL}/categories/data-breaches.html"},
        {"id": "cves", "label": "CVEs (NVD)", "href": f"{BASE_URL}/cves/index.html"},
        {"id": "vulnerabilities", "label": "Vulnerabilities", "href": f"{BASE_URL}/categories/vulnerabilities.html"},
        {"id": "malware", "label": "Malware", "href": f"{BASE_URL}/categories/malware.html"},
        {"id": "research", "label": "Research", "href": f"{BASE_URL}/categories/research.html"},
        {"id": "campaigns", "label": "Campaigns", "href": f"{BASE_URL}/categories/campaigns.html"},
        {"id": "other", "label": "Other", "href": f"{BASE_URL}/categories/other.html"},
    ]


def build_pagination_links(page, total_pages, filename_base):
    """Build compact windowed pagination links (1 ... p-1 p p+1 ... N)."""
    if total_pages <= 1:
        return []

    def href_for(p):
        return f"{filename_base}.html" if p == 1 else f"{filename_base}-{p}.html"

    pages_to_show = sorted({1, total_pages, max(1, page - 1), page, min(total_pages, page + 1)})
    links = []
    prev_num = None
    for num in pages_to_show:
        if prev_num is not None and num - prev_num > 1:
            links.append({"ellipsis": True})
        links.append({"num": num, "href": href_for(num), "current": num == page, "ellipsis": False})
        prev_num = num
    return links


def count_enabled_sources():
    """Count enabled RSS sources in config/feeds.yaml for landing telemetry."""
    if not CONFIG_FILE.exists():
        return 0
    try:
        data = yaml.load(CONFIG_FILE.read_text(encoding="utf-8"), Loader=Loader) or []
        return sum(1 for item in data if isinstance(item, dict) and item.get("enabled", True))
    except Exception:
        return 0


def build_site():
    t0 = time.perf_counter()
    print("Starting static build process...")

    required_templates = ("base.html", "index.html", "post.html", "landing.html")
    for tmpl_name in required_templates:
        if not (TEMPLATES_DIR / tmpl_name).exists():
            print(f"Missing required template: {TEMPLATES_DIR / tmpl_name}")
            raise SystemExit(1)

    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)

    DIST_DIR.mkdir(parents=True)
    (DIST_DIR / "posts").mkdir(parents=True)
    (DIST_DIR / "cves").mkdir(parents=True)
    (DIST_DIR / "categories").mkdir(parents=True)
    (DIST_DIR / "feed").mkdir(parents=True)
    DATA_DIR.mkdir(parents=True)

    for asset_type in ("css", "js", "images"):
        asset_src = SRC_DIR / asset_type
        if asset_src.exists():
            shutil.copytree(asset_src, DIST_DIR / asset_type)

    favicon_src = SRC_DIR / "images" / "favicon.ico"
    if favicon_src.exists():
        shutil.copy2(favicon_src, DIST_DIR / "favicon.ico")

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    base_tmpl = env.get_template("base.html")
    index_tmpl = env.get_template("index.html")
    post_tmpl = env.get_template("post.html")
    landing_tmpl = env.get_template("landing.html")

    nav_items = build_nav_items()
    posts, cves = load_all_items_cached()

    all_content = posts + cves
    all_content.sort(key=lambda x: (x["sort_ts"], x["slug"]), reverse=True)
    posts.sort(key=lambda x: (x["sort_ts"], x["slug"]), reverse=True)
    cves.sort(key=lambda x: (x["sort_ts"], x["slug"]), reverse=True)

    # Compact minified search index
    search_index = []
    for item in all_content:
        entry = {
            "t": item["title"],
            "u": item["url"],
            "d": item["formatted_date"],
            "c": item["category"],
            "g": item["tags"],
        }
        if item["type"] == "cve":
            if item.get("severity") and item["severity"] != "Unknown":
                entry["s"] = item["severity"]
            if item.get("kev"):
                entry["k"] = 1
        search_index.append(entry)
    (DATA_DIR / "content.json").write_text(
        json.dumps(search_index, separators=(",", ":"), ensure_ascii=False),
        encoding="utf-8",
    )

    write_jobs = []

    # Render individual post and CVE pages
    for item in all_content:
        is_cve = item["type"] == "cve"
        cat_href = f"{BASE_URL}/cves/index.html" if is_cve else f"{BASE_URL}/categories/{item['category']}.html"
        post_html = post_tmpl.render(item=item, category_href=cat_href)
        meta_desc = item["description"] or f"{item['title']} — Faultplane Cyber Threat Intelligence"
        full_html = base_tmpl.render(
            title=f"{item['title']} - Faultplane",
            meta_description=meta_desc,
            base_url=BASE_URL,
            nav_items=nav_items,
            active_nav="cves" if is_cve else item["category"],
            content=post_html,
        )
        out_path = (DIST_DIR / "cves" / f"{item['slug']}.html") if is_cve else (DIST_DIR / "posts" / f"{item['slug']}.html")
        write_jobs.append((out_path, full_html))

    # Group all items by category
    category_map = {cat: [] for cat in VALID_CATEGORIES}
    for item in all_content:
        category_map.setdefault(item["category"], []).append(item)

    def queue_paginated_index(post_list, title, folder, active_nav, filename_base="index", show_category_pill=False):
        total_items = len(post_list)
        total_pages = max(1, math.ceil(total_items / POSTS_PER_PAGE))

        for page in range(1, total_pages + 1):
            start_idx = (page - 1) * POSTS_PER_PAGE
            page_posts = post_list[start_idx : start_idx + POSTS_PER_PAGE]
            prev_href = (f"{filename_base}.html" if page == 2 else f"{filename_base}-{page - 1}.html") if page > 1 else None
            next_href = f"{filename_base}-{page + 1}.html" if page < total_pages else None
            page_links = build_pagination_links(page, total_pages, filename_base)

            page_content = index_tmpl.render(
                title_header=title,
                total_items=total_items,
                page_posts=page_posts,
                base_url=BASE_URL,
                show_category_pill=show_category_pill,
                page=page,
                total_pages=total_pages,
                prev_href=prev_href,
                next_href=next_href,
                page_links=page_links,
            )
            full_html = base_tmpl.render(
                title=f"{title} - Faultplane",
                meta_description=f"{title} — Faultplane Cyber Threat Intelligence Archive",
                base_url=BASE_URL,
                nav_items=nav_items,
                active_nav=active_nav,
                content=page_content,
            )
            filename = f"{filename_base}.html" if page == 1 else f"{filename_base}-{page}.html"
            write_jobs.append((folder / filename, full_html))

    queue_paginated_index(all_content, "Live Intelligence Feed", DIST_DIR / "feed", "feed", show_category_pill=True)
    queue_paginated_index(cves, "Latest Vulnerabilities (CVEs)", DIST_DIR / "cves", "cves")

    for cat, cat_items in category_map.items():
        pretty_title = cat.replace("-", " ").title()
        queue_paginated_index(
            cat_items,
            f"Category: {pretty_title}",
            DIST_DIR / "categories",
            cat,
            filename_base=cat,
        )

    # Landing Page
    kev_count = sum(1 for c in cves if c.get("kev"))
    sections = [
        {
            "title": "Threat Intelligence",
            "href": f"{BASE_URL}/categories/threat-intel.html",
            "link_label": "View All Intelligence",
            "items": category_map.get("threat-intel", [])[:4],
            "full_width": False,
        },
        {
            "title": "Latest Vulnerabilities (CVEs)",
            "href": f"{BASE_URL}/cves/index.html",
            "link_label": "View All CVEs",
            "items": cves[:4],
            "full_width": False,
        },
        {
            "title": "Data Breaches",
            "href": f"{BASE_URL}/categories/data-breaches.html",
            "link_label": "View All Breaches",
            "items": category_map.get("data-breaches", [])[:4],
            "full_width": False,
        },
        {
            "title": "Security Research",
            "href": f"{BASE_URL}/categories/research.html",
            "link_label": "View All Research",
            "items": category_map.get("research", [])[:4],
            "full_width": False,
        },
        {
            "title": "Malware & Threat Actors",
            "href": f"{BASE_URL}/categories/malware.html",
            "link_label": "View All Malware",
            "items": category_map.get("malware", [])[:4],
            "full_width": False,
        },
        {
            "title": "Vulnerability Advisories",
            "href": f"{BASE_URL}/categories/vulnerabilities.html",
            "link_label": "View All Advisories",
            "items": category_map.get("vulnerabilities", [])[:4],
            "full_width": False,
        },
        {
            "title": "Campaigns",
            "href": f"{BASE_URL}/categories/campaigns.html",
            "link_label": "View All Campaigns",
            "items": category_map.get("campaigns", [])[:4],
            "full_width": False,
        },
        {
            "title": "Other",
            "href": f"{BASE_URL}/categories/other.html",
            "link_label": "View All Other Posts",
            "items": category_map.get("other", [])[:4],
            "full_width": False,
        },
    ]

    landing_content = landing_tmpl.render(
        sections=sections,
        stats={
            "total_items": len(all_content),
            "total_cves": len(cves),
            "kev_count": kev_count,
            "source_count": count_enabled_sources(),
        },
    )
    full_landing = base_tmpl.render(
        title="Faultplane - Cyber Threat Intelligence",
        meta_description="Faultplane automated cyber threat intelligence, CVE tracking, and malware research platform.",
        base_url=BASE_URL,
        nav_items=nav_items,
        active_nav="home",
        content=landing_content,
    )
    write_jobs.append((DIST_DIR / "index.html", full_landing))

    # Parallel disk writes
    def _write_file(job):
        path, html_str = job
        path.write_text(html_str, encoding="utf-8")

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        list(executor.map(_write_file, write_jobs))

    elapsed = time.perf_counter() - t0
    print(f"Build complete! Generated {len(all_content)} items ({len(write_jobs)} pages) in {DIST_DIR} in {elapsed:.2f}s.")


if __name__ == "__main__":
    build_site()
