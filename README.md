# Faultplane

Faultplane is an automated cybersecurity intelligence platform that continuously aggregates, summarizes, and classifies threat intelligence, malware analysis, data breach reports, and vulnerabilities into a lightweight static site and dashboard.

**Live Platform:** [Faultplane](https://dedsec-terminal.github.io/Faultplane/)

---

## Screenshots

Click any thumbnail to open the full-size image in a new tab.

[![Dashboard — 14:08:16](https://raw.githubusercontent.com/dedsec-terminal/Faultplane/main/assets/Screenshot%202026-08-19%20140816.png)](https://raw.githubusercontent.com/dedsec-terminal/Faultplane/main/assets/Screenshot%202026-08-19%20140816.png)
[![Dashboard — 14:09:14](https://raw.githubusercontent.com/dedsec-terminal/Faultplane/main/assets/Screenshot%202026-08-19%20140914.png)](https://raw.githubusercontent.com/dedsec-terminal/Faultplane/main/assets/Screenshot%202026-08-19%20140914.png)

---

## Intelligence Coverage

| Category                | Primary Focus & Sources                                                                                                                                                 |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Threat Intelligence** | State-sponsored operations, APT campaigns, phishing campaigns, identity threats (The Hacker News, Krebs on Security, Bleeping Computer, Schneier on Security, Microsoft) |
| **Malware & Threats**   | Reverse engineering, ransomware operations, loader/botnet analysis (Securelist, SentinelOne Labs, Malwarebytes Labs)                                                   |
| **Data Breaches**       | Verified breaches, leaks, credential dump disclosures (DataBreaches.net, Have I Been Pwned / Troy Hunt)                                                                |
| **Security Research**   | Zero-day vulnerability research, protocol desyncs, fuzzing, PoCs (Cisco Talos, Unit 42, Google Project Zero, PortSwigger Research, Trail of Bits)                     |
| **Authoritative CVEs**  | Newly published/modified vulnerabilities and active exploitation enrichment (NVD 2.0 API, CISA KEV, Zero Day Initiative, CISA Advisories)                              |

---

## Architecture & Automation

```
[ Curated RSS Feeds ] ───► [ rss_fetcher.py ] ───► [ Groq API ] ───► [ content/posts/*.md ] ───┐
                                                                                                  ├──► [ build_site.py ] ──► [ dist/ ] ──► [ GitHub Pages ]
[ NVD 2.0 API + KEV ] ───► [ cve_fetcher.py ] ───► [ Groq API ] ───► [ content/cves/*.md ] ────┘
```

1. **Daily Automation (24h Cycle):** GitHub Actions triggers ingestion at `00:00 UTC` daily, batching updates while conserving API tokens.
2. **Two-Source CVE Ingestion:** Primary vulnerability data is pulled from the official NVD 2.0 API and cross-referenced with CISA's Known Exploited Vulnerabilities (KEV) catalog.
3. **Groq AI Pipeline (`groq_client.py`):** Uses high-throughput LLM chat completions to produce structured executive summaries and extract technical facts.
4. **Persistent Quote System:** Each article is permanently assigned a curated security/philosophical quote from `data/quotes.json` in its YAML frontmatter.
5. **Static Site Generator (`build_site.py`):** Lightweight Python generator compiling Markdown into responsive HTML/CSS.

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
