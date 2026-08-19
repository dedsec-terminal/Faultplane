# Faultplane

Faultplane is an automated cybersecurity intelligence platform that continuously aggregates, summarizes, and classifies threat intelligence, malware analysis, data breach reports, and vulnerability disclosures from authoritative open-source intelligence feeds in real time.

**Live Platform:** [Faultplane](https://dedsec-terminal.github.io/Faultplane/)

---

## Platform Screenshot

<div align="center">
  <img src="https://raw.githubusercontent.com/dedsec-terminal/Faultplane/main/assets/screenshot.png" alt="Faultplane Dashboard" width="900" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
</div>

---

## Intelligence Coverage

| Category                | Primary Focus & Sources                                                                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Threat Intelligence** | State-sponsored operations, APT campaigns, phishing campaigns, identity threats (_The Hacker News, Krebs on Security, Bleeping Computer, Schneier on Security, Microsoft Security Response Center_) |
| **Malware & Threats**   | Reverse engineering, ransomware operations, loader/botnet analysis (_Securelist, SentinelOne Labs, Malwarebytes Labs_)                                                      |
| **Data Breaches**       | Verified breaches, leaks, credential dump disclosures (_DataBreaches.net, Have I Been Pwned / Troy Hunt_)                                                                   |
| **Security Research**   | Zero-day vulnerability research, protocol desyncs, fuzzing, PoCs (_Cisco Talos, Unit 42, Google Project Zero, PortSwigger Research, Trail of Bits_)                         |
| **Authoritative CVEs**  | Newly published/modified vulnerabilities and active exploitation enrichment (_NVD 2.0 API, CISA KEV, Zero Day Initiative, CISA Advisories_)                                 |

---

## Architecture & Automation

```
[ Curated RSS Feeds ] ───► [ rss_fetcher.py ] ───► [ Groq API ] ───► [ content/posts/*.md ] ───┐
                                                                                                  ├──► [ build_site.py ] ──► [ dist/ ] ──► [ GitHub Pages ]
[ NVD 2.0 API + KEV ] ───► [ cve_fetcher.py ] ───► [ Groq API ] ───► [ content/cves/*.md ] ────┘
```

1. **Daily Automation (24h Cycle):** GitHub Actions triggers ingestion at `00:00 UTC` daily, batching updates while conserving API tokens.
2. **Two-Source CVE Ingestion:** Primary vulnerability data is pulled from the official NVD 2.0 API and cross-referenced with CISA's Known Exploited Vulnerabilities (KEV) catalog for real-world exploitation context.
3. **Groq AI Pipeline (`groq_client.py`):** Uses high-throughput LLM chat completions (`openai/gpt-oss-20b` with fallback support) to produce structured, hallucination-free executive summaries and strategic classifications.
4. **Persistent Quote System:** Each article is permanently assigned a curated security/philosophical quote from `data/quotes.json` in its YAML frontmatter upon generation, ensuring consistent article identity.
5. **Static Site Generator (`build_site.py`):** Lightweight, zero-framework Python generator compiling Markdown into responsive, high-performance HTML/CSS with balanced category sections (4 items per row).

---

## Post Structure

All posts and CVEs are rendered in a clean, semantic reading order:

1. **Header & Metadata:** Title, publish date, category tag.
2. **Executive Summary:** Concise AI summary of technical facts.
3. **Authoritative Context:** CVE CVSS scores, KEV alerts, or key points.
4. **Persistent Quote:** Curated `<blockquote>` and `<cite>` permanently bound to the post.
5. **Canonical Source:** Clear outbound reference to the original publisher or NVD advisory.

---

## Repository Structure

```
Faultplane/
├── .github/workflows/
│   └── rss-update.yml         # Daily automation workflow (runs every 24 hours)
├── config/
│   └── feeds.yaml             # Curated RSS feed definitions
├── content/
│   ├── posts/                 # Generated Markdown intelligence posts
│   └── cves/                  # Generated Markdown CVE vulnerability posts
├── data/
│   ├── quotes.json            # Curated quote collection
│   ├── rss_state.json         # Deduplication state for RSS ingestion
│   └── cve_state.json         # Deduplication state for CVE ingestion
├── scripts/
│   ├── groq_client.py         # Shared Groq AI integration with retry & fallback
│   ├── quote.py               # Quote loader and random selection module
│   ├── rss_fetcher.py         # RSS fetcher, deduplicator, and post generator
│   ├── cve_fetcher.py         # NVD 2.0 + CISA KEV pipeline
│   └── build_site.py          # Static site generator and homepage builder
├── src/
│   ├── css/style.css          # Dark-mode intelligence dashboard stylesheet
│   └── templates/             # HTML templates (base, landing, post, index)
└── requirements.txt           # Python dependencies
```

---

## Local Development

### 1. Setup Environment

```bash
git clone https://github.com/dedsec-terminal/Faultplane.git
cd Faultplane
pip install -r requirements.txt
```

### 2. Configure Environment Variables (Optional for Fetchers)

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_api_key_here
```

### 3. Build & Serve

```bash
# Build the static site into dist/
python scripts/build_site.py

# Serve locally
python -m http.server 8000 -d dist
```

Navigate to `http://localhost:8000/Faultplane/` in your browser.

---

## License

Created and maintained by [DedSec-Terminal](https://github.com/dedsec-terminal).
