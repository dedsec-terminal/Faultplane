---
title: "ZDI-26-748: Luxion KeyShot BIP File Parsing Uncontrolled Search Path Element Remote Code Execution Vulnerability"
description: "A remote code execution vulnerability (CVE-2026-92202) in Luxion KeyShot\u2019s BIP file parser allows attackers to execute arbitrary code when a user open..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-748/"
published: "2026-09-23T05:00:00+00:00"
ingested_at: "2026-09-24T02:57:31.617672+00:00"
date: "2026-09-24T02:57:31.617672+00:00"
category: "cves"
tags:
  - "Luxion KeyShot"
  - "BIP file parsing"
  - "remote code execution"
  - "CVE-2026-92202"
  - "Zero Day Initiative"
slug: "2026-09-24-zdi-26-748-luxion-keyshot-bip-file-parsing-uncontrolled-sear"
quote: "There is nothing so useless as doing efficiently that which should not be done at all."
quote_author: "Peter Drucker"
---

### Executive Summary
A remote code execution vulnerability (CVE-2026-92202) in Luxion KeyShot’s BIP file parser allows attackers to execute arbitrary code when a user opens a malicious file or visits a malicious page. The flaw stems from uncontrolled search path elements during BIP file parsing. Exploitation requires user interaction and has a CVSS score of 7.8.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-23T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Luxion KeyShot. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-92202.
