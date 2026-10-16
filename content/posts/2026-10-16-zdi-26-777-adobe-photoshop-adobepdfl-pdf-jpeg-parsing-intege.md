---
title: "ZDI-26-777: Adobe Photoshop AdobePDFL PDF JPEG Parsing Integer Overflow Remote Code Execution Vulnerability"
description: "Adobe Photoshop is vulnerable to a remote code execution flaw triggered by parsing malicious PDF or JPEG files. The integer overflow in AdobePDFL pars..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-777/"
published: "2026-10-15T05:00:00+00:00"
ingested_at: "2026-10-16T02:58:31.895197+00:00"
date: "2026-10-16T02:58:31.895197+00:00"
category: "cves"
tags:
  - "Adobe Photoshop"
  - "AdobePDFL"
  - "PDF"
  - "JPEG"
  - "Integer Overflow"
  - "Remote Code Execution"
  - "CVE-2026-83661"
  - "Zero Day Initiative"
slug: "2026-10-16-zdi-26-777-adobe-photoshop-adobepdfl-pdf-jpeg-parsing-intege"
quote: "Being right is highly overrated. Even a stopped clock is right twice a day."
quote_author: "Unknown"
---

### Executive Summary
Adobe Photoshop is vulnerable to a remote code execution flaw triggered by parsing malicious PDF or JPEG files. The integer overflow in AdobePDFL parsing can be exploited when a user opens a crafted file or visits a malicious page. CVE-2026-83661, CVSS 7.8, identified by Zero Day Initiative.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-10-15T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Photoshop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-83661.
