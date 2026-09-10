---
title: "ZDI-26-646: Progress Software Kemp LoadMaster escape_quotes Uninitialized Memory RCE Vulnerability"
description: "A remote code execution vulnerability (CVE-2026-8037) exists in Progress Software's Kemp LoadMaster due to an uninitialized memory issue in the escape..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-646/"
published: "2026-09-09T05:00:00+00:00"
ingested_at: "2026-09-10T02:53:50.875773+00:00"
date: "2026-09-10T02:53:50.875773+00:00"
category: "cves"
tags:
  - "remote-code-execution"
  - "uninitialized-memory"
  - "authentication-required"
  - "Progress-Software"
  - "Kemp-LoadMaster"
  - "CVE-2026-8037"
slug: "2026-09-10-zdi-26-646-progress-software-kemp-loadmaster-escape-quotes-u"
quote: "Everything can be taken from a man but ... the last of the human freedoms \ufffd to choose ones attitude in any given set of circumstances, to choose ones own way."
quote_author: "Victor Frankl"
---

### Executive Summary
A remote code execution vulnerability (CVE-2026-8037) exists in Progress Software's Kemp LoadMaster due to an uninitialized memory issue in the escape_quotes function. Authentication is required to exploit. The Zero Day Initiative rated it CVSS 7.2.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-09T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Progress Software Kemp LoadMaster. Authentication is required to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.2. The following CVEs are assigned: CVE-2026-8037.
