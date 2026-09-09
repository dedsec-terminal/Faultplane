---
title: "ClickFix moves into the browser: Cryptocurrency theft with Google-hosted C2"
description: "Cisco Talos reports a cryptocurrency\u2011stealing campaign that uses the Google Visualization API as a command\u2011and\u2011control channel. The attackers host obf..."
source: "Cisco Talos"
source_url: "https://blog.talosintelligence.com/clickfix-moves-into-the-browser/"
published: "2026-09-08T10:00:38+00:00"
ingested_at: "2026-09-09T02:52:15.754288+00:00"
date: "2026-09-09T02:52:15.754288+00:00"
category: "campaigns"
tags:
  - "cryptocurrency-theft"
  - "google-visualization-api"
  - "command-and-control"
  - "browser-injection"
  - "obfuscated-javascript"
slug: "2026-09-09-clickfix-moves-into-the-browser-cryptocurrency-theft-with-go"
quote: "It is only with the heart that one can see rightly, what is essential is invisible to the eye."
quote_author: "Antoine de Saint-Exupery"
---

### Executive Summary
Cisco Talos reports a cryptocurrency‑stealing campaign that uses the Google Visualization API as a command‑and‑control channel. The attackers host obfuscated JavaScript in a publicly accessible Google Sheets document, which is fetched and injected into victims’ browser sessions, enabling the theft of crypto assets.

---
**Intelligence Metadata**
- **Source Publisher:** Cisco Talos
- **Published Date:** 2026-09-08T10:00:38+00:00
- **Category:** campaigns

**Original Description:**
Cisco Talos is tracking a cryptocurrency-stealing campaign that abuses the Google Visualization API for command and control (C2), retrieving obfuscated JavaScript from a publicly published Google Sheets document and injecting it into the victim's browser session.
