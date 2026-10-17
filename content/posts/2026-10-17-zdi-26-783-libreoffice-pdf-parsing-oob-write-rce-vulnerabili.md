---
title: "ZDI-26-783: LibreOffice PDF Parsing OOB Write RCE Vulnerability"
description: "A zero\u2011day vulnerability (ZDI\u201126\u2011783) in LibreOffice\u2019s PDF parser allows remote attackers to trigger an out\u2011of\u2011bounds write and execute arbitrary code..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-783/"
published: "2026-10-16T05:00:00+00:00"
ingested_at: "2026-10-17T02:49:47.419220+00:00"
date: "2026-10-17T02:49:47.419220+00:00"
category: "cves"
tags:
  - "LibreOffice"
  - "PDF"
  - "Remote code execution"
  - "CVE-2026-63273"
slug: "2026-10-17-zdi-26-783-libreoffice-pdf-parsing-oob-write-rce-vulnerabili"
quote: "Fear not for the future, weep not for the past."
quote_author: "Percy Shelley"
---

### Executive Summary
A zero‑day vulnerability (ZDI‑26‑783) in LibreOffice’s PDF parser allows remote attackers to trigger an out‑of‑bounds write and execute arbitrary code when a user opens a malicious PDF. The flaw requires user interaction and is rated CVSS 7.8. It is tracked as CVE‑2026‑63273.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-10-16T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of LibreOffice. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-63273.
