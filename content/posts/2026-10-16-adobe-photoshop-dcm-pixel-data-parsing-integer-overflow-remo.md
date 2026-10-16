---
title: "Adobe Photoshop DCM Pixel Data Parsing Integer Overflow Remote Code Execution Vulnerability"
description: "Adobe Photoshop is vulnerable to an integer overflow in DCM pixel data parsing that can lead to remote code execution. The flaw requires user interact..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-778/"
published: "2026-10-15T05:00:00+00:00"
ingested_at: "2026-10-16T02:58:28.692265+00:00"
date: "2026-10-16T02:58:28.692265+00:00"
category: "cves"
tags:
  - "Adobe Photoshop"
  - "integer overflow"
  - "remote code execution"
  - "CVE-2026-95636"
  - "Zero Day Initiative"
slug: "2026-10-16-adobe-photoshop-dcm-pixel-data-parsing-integer-overflow-remo"
quote: "Every person, all the events of your life are there because you have drawn them there. What you choose to do with them is up to you."
quote_author: "Richard Bach"
---

### Executive Summary
Adobe Photoshop is vulnerable to an integer overflow in DCM pixel data parsing that can lead to remote code execution. The flaw requires user interaction, such as opening a malicious file or visiting a malicious page. CVE-2026-95636 has a CVSS score of 7.8. Zero Day Initiative identified the issue.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-10-15T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Photoshop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-95636.
