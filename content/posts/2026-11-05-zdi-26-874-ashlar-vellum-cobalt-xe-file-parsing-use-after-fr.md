---
title: "ZDI-26-874: Ashlar-Vellum Cobalt XE File Parsing Use-After-Free RCE Vulnerability"
description: "A zero\u2011day use\u2011after\u2011free vulnerability (CVE\u20112026\u2011121742) in Ashlar\u2011Vellum Cobalt XE\u2019s file\u2011parsing logic allows remote attackers to execute arbitrary..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-874/"
published: "2026-11-04T06:00:00+00:00"
ingested_at: "2026-11-05T04:55:54.827862+00:00"
date: "2026-11-05T04:55:54.827862+00:00"
category: "cves"
tags:
  - "ashlar-vellum"
  - "cobalt"
  - "use-after-free"
  - "remote-code-execution"
  - "cve-2026-121742"
slug: "2026-11-05-zdi-26-874-ashlar-vellum-cobalt-xe-file-parsing-use-after-fr"
quote: "There never was a good knife made of bad steel."
quote_author: "Benjamin Franklin"
---

### Executive Summary
A zero‑day use‑after‑free vulnerability (CVE‑2026‑121742) in Ashlar‑Vellum Cobalt XE’s file‑parsing logic allows remote attackers to execute arbitrary code when a user opens a malicious file or visits a malicious page. The flaw is rated CVSS 7.8 and requires user interaction.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-11-04T06:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Cobalt. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-121742.
