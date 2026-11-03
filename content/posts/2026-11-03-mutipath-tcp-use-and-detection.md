---
title: "Mutipath TCP: Use and Detection"
description: "The article discusses the Mutipath TCP option, introduced in 2020, and its recent vulnerability in Linux's implementation (CVE\u20112026\u201198432). It highlig..."
source: "SANS Internet Storm Center"
source_url: "https://isc.sans.edu/diary/rss/33482"
published: "2026-11-02T14:52:05+00:00"
ingested_at: "2026-11-03T05:08:47.286048+00:00"
date: "2026-11-03T05:08:47.286048+00:00"
category: "vulnerabilities"
tags:
  - "Mutipath TCP"
  - "Linux"
  - "CVE-2026-98432"
  - "TCP option"
  - "vulnerability"
  - "SANS Internet Storm Center"
slug: "2026-11-03-mutipath-tcp-use-and-detection"
quote: "Setting an example is not the main means of influencing another, it is the only means."
quote_author: "Albert Einstein"
---

### Executive Summary
The article discusses the Mutipath TCP option, introduced in 2020, and its recent vulnerability in Linux's implementation (CVE‑2026‑98432). It highlights how the flaw can be exploited, the impact on network traffic, and detection techniques recommended by the SANS Internet Storm Center.

---
**Intelligence Metadata**
- **Source Publisher:** SANS Internet Storm Center
- **Published Date:** 2026-11-02T14:52:05+00:00
- **Category:** vulnerabilities

**Original Description:**
Last week, an often-ignored&&#x23&#x3b;x26&#x3b;&#x23&#x3b;xc2&#x3b;&&#x23&#x3b;x26&#x3b;&#x23&#x3b;xa0&#x3b;TCP option, introduced in 2020, made the news due to a new vulnerability in Linux&&#x23&#x3b;x26&#x3b;&#x23&#x3b;39&#x3b;s implementation (RFC&&#x23&#x3b;x26&#x3b;&#x23&#x3b;xc2&#x3b;&&#x23&#x3b;x26&#x3b;&#x23&#x3b;xa0&#x3b;8684, &&#x23&#x3b;x26&#x3b;&#x23&#x3b;xc2&#x3b;&&#x23&#x3b;x26&#x3b;&#x23&#x3b;xa0&#x3b;CVE-2026-98432)&#xd;
