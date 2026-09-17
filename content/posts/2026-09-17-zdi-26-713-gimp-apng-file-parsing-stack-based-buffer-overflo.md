---
title: "ZDI-26-713: GIMP APNG File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability"
description: "A stack-based buffer overflow in GIMP's APNG file parser allows remote attackers to execute arbitrary code when a user opens a malicious file or visit..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-713/"
published: "2026-09-16T05:00:00+00:00"
ingested_at: "2026-09-17T03:12:10.404169+00:00"
date: "2026-09-17T03:12:10.404169+00:00"
category: "cves"
tags:
  - "gimp"
  - "apng"
  - "buffer-overflow"
  - "remote-code-execution"
  - "cve-2026-92183"
  - "zero-day-initiative"
slug: "2026-09-17-zdi-26-713-gimp-apng-file-parsing-stack-based-buffer-overflo"
quote: "The bird of paradise alights only upon the hand that does not grasp."
quote_author: "John Berry"
---

### Executive Summary
A stack-based buffer overflow in GIMP's APNG file parser allows remote attackers to execute arbitrary code when a user opens a malicious file or visits a malicious page. The vulnerability, identified as CVE-2026-92183, has a CVSS score of 7.8 and was disclosed by Zero Day Initiative (ZDI-26-713).

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-16T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of GIMP. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-92183.
