---
title: "ZDI-26-677: Adobe Photoshop DCM JPEG-LS Image Parsing Integer Overflow Remote Code Execution Vulnerability"
description: "Adobe Photoshop is vulnerable to an integer overflow in the DCM JPEG-LS image parser that can lead to remote code execution. The flaw requires user in..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-677/"
published: "2026-09-10T05:00:00+00:00"
ingested_at: "2026-09-11T02:48:07.913520+00:00"
date: "2026-09-11T02:48:07.913520+00:00"
category: "cves"
tags:
  - "Adobe Photoshop"
  - "JPEG-LS"
  - "integer overflow"
  - "remote code execution"
  - "CVE-2026-75771"
slug: "2026-09-11-zdi-26-677-adobe-photoshop-dcm-jpeg-ls-image-parsing-integer"
quote: "Time stays long enough for anyone who will use it."
quote_author: "Leonardo da Vinci"
---

### Executive Summary
Adobe Photoshop is vulnerable to an integer overflow in the DCM JPEG-LS image parser that can lead to remote code execution. The flaw requires user interaction, such as opening a malicious file or visiting a malicious page. The Zero Day Initiative assigned CVE-2026-75771 and a CVSS score of 7.8.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-10T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Photoshop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-75771.
