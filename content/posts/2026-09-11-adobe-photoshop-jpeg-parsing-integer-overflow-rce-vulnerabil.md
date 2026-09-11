---
title: "Adobe Photoshop JPEG Parsing Integer Overflow RCE Vulnerability (ZDI-26-679)"
description: "Adobe Photoshop is vulnerable to an integer overflow in JPEG image parsing that can lead to remote code execution. The flaw, identified as ZDI-26-679 ..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-679/"
published: "2026-09-10T05:00:00+00:00"
ingested_at: "2026-09-11T02:47:53.662589+00:00"
date: "2026-09-11T02:47:53.662589+00:00"
category: "cves"
tags:
  - "Adobe Photoshop"
  - "JPEG parsing"
  - "integer overflow"
  - "remote code execution"
  - "CVE-2026-75862"
  - "ZDI-26-679"
  - "Zero Day Initiative"
slug: "2026-09-11-adobe-photoshop-jpeg-parsing-integer-overflow-rce-vulnerabil"
quote: "Life is not measured by the breaths you take, but by its breathtaking moments."
quote_author: "Michael Vance"
---

### Executive Summary
Adobe Photoshop is vulnerable to an integer overflow in JPEG image parsing that can lead to remote code execution. The flaw, identified as ZDI-26-679 and assigned CVE-2026-75862, requires user interaction such as opening a malicious file or visiting a malicious page. The CVSS score is 7.8.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-10T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Photoshop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-75862.
