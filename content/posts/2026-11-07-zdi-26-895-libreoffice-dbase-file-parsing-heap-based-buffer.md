---
title: "ZDI-26-895: LibreOffice dBase File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability"
description: "A heap-based buffer overflow in LibreOffice\u2019s dBase file parser allows remote attackers to execute arbitrary code when a user opens a malicious file o..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-895/"
published: "2026-11-06T06:00:00+00:00"
ingested_at: "2026-11-07T04:27:31.123382+00:00"
date: "2026-11-07T04:27:31.123382+00:00"
category: "cves"
tags:
  - "LibreOffice"
  - "heap-buffer-overflow"
  - "remote-code-execution"
  - "CVE-2026-76181"
slug: "2026-11-07-zdi-26-895-libreoffice-dbase-file-parsing-heap-based-buffer"
quote: "When one tugs at a single thing in nature, he finds it attached to the rest of the world."
quote_author: "John Muir"
---

### Executive Summary
A heap-based buffer overflow in LibreOffice’s dBase file parser allows remote attackers to execute arbitrary code when a user opens a malicious file or visits a malicious page. The vulnerability, identified as CVE-2026-76181 and assigned CVSS 7.8, requires user interaction and was disclosed by Zero Day Initiative (ZDI-26-895).

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-11-06T06:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of LibreOffice. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-76181.
