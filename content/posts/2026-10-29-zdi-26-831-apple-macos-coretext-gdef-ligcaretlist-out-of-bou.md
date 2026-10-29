---
title: "ZDI-26-831: Apple macOS CoreText GDEF LigCaretList Out-Of-Bounds Read Information Disclosure Vulnerability"
description: "Apple macOS CoreText library has an out-of-bounds read in the GDEF LigCaretList parsing, allowing remote attackers to disclose sensitive information w..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-831/"
published: "2026-10-28T05:00:00+00:00"
ingested_at: "2026-10-29T04:11:04.614214+00:00"
date: "2026-10-29T04:11:04.614214+00:00"
category: "cves"
tags:
  - "Apple"
  - "macOS"
  - "CoreText"
  - "GDEF"
  - "LigCaretList"
  - "Out-of-bounds"
  - "Information Disclosure"
  - "CVE-2026-112656"
  - "Zero Day Initiative"
  - "ZDI-26-831"
slug: "2026-10-29-zdi-26-831-apple-macos-coretext-gdef-ligcaretlist-out-of-bou"
quote: "Work out your own salvation. Do not depend on others."
quote_author: "Buddha"
---

### Executive Summary
Apple macOS CoreText library has an out-of-bounds read in the GDEF LigCaretList parsing, allowing remote attackers to disclose sensitive information when a user visits a malicious page or opens a malicious file. The vulnerability, identified as ZDI-26-831, has a CVSS score of 3.3 and is assigned CVE-2026-112656 by Zero Day Initiative.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-10-28T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 3.3. The following CVEs are assigned: CVE-2026-112656.
