# Faultplane

A cybersecurity intelligence platform that aggregates vulnerability disclosures, malware campaigns, breach reports, and security research into a structured, searchable knowledge base.

Intended for cybersecurity enthusiasts looking for a consolidated reference point.

---

## Coverage

| Domain | What's tracked |
|---|---|
| **Vulnerabilities** | CVEs, patch advisories, exploit disclosures |
| **Malware** | Campaign TTPs, IOCs, attribution |
| **Breaches** | Disclosure timelines, scope, impact |
| **Threat Actors** | Group profiles, tooling, targeting |
| **Research** | Papers, conference talks, PoC writeups |
| **OSINT** | Open-source intelligence curation |

---

## Stack

- Completely Static site hosted via GitHub Pages (No Hugo/Jekyll/JS frameworks)
- AI-assisted intelligence collection and summarization (`scripts/rss_fetcher.py`)
- Automated Static Builder (`scripts/build_site.py`)
- Structured markdown knowledge base in `content/posts/`

---

## Local Development

To test the site locally, first install dependencies and run the build script:

```bash
pip install -r requirements.txt
python scripts/build_site.py
```

Then serve the static `dist/` directory:

```bash
python -m http.server 8000 -d dist
```

---

**Live →** [dedsec-terminal.github.io/Faultplane](https://dedsec-terminal.github.io/Faultplane)
