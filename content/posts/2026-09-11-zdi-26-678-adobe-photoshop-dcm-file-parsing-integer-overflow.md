---
title: "ZDI-26-678: Adobe Photoshop DCM File Parsing Integer Overflow Remote Code Execution Vulnerability"
description: "Adobe Photoshop is vulnerable to an integer overflow in DCM file parsing that can lead to remote code execution. The flaw requires user interaction, s..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-678/"
published: "2026-09-10T05:00:00+00:00"
ingested_at: "2026-09-11T02:47:56.016856+00:00"
date: "2026-09-11T02:47:56.016856+00:00"
category: "cves"
tags:
  - "Adobe"
  - "Photoshop"
  - "integer overflow"
  - "remote code execution"
  - "CVE-2026-75863"
slug: "2026-09-11-zdi-26-678-adobe-photoshop-dcm-file-parsing-integer-overflow"
quote: "Learn wisdom from the ways of a seedling. A seedling which is never hardened off through stressful situations will never become a strong productive plant."
quote_author: "Stephen Sigmund"
---

### Executive Summary
Adobe Photoshop is vulnerable to an integer overflow in DCM file parsing that can lead to remote code execution. The flaw requires user interaction, such as opening a malicious file or visiting a malicious page. The Zero Day Initiative assigned CVE-2026-75863 and a CVSS score of 7.8.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-10T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Photoshop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-75863.
