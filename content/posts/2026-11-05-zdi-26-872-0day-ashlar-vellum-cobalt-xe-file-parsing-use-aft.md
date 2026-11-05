---
title: "ZDI-26-872: (0Day) Ashlar-Vellum Cobalt XE File Parsing Use-After-Free Remote Code Execution Vulnerability"
description: "Zero Day Initiative (ZDI) disclosed a 7.8 CVSS use\u2011after\u2011free vulnerability (CVE\u20112026\u2011121753) in Ashlar\u2011Vellum Cobalt\u202fXE\u2019s file\u2011parsing logic. Remote ..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-872/"
published: "2026-11-04T06:00:00+00:00"
ingested_at: "2026-11-05T04:56:00.082540+00:00"
date: "2026-11-05T04:56:00.082540+00:00"
category: "cves"
tags:
  - "Ashlar-Vellum"
  - "Cobalt XE"
  - "Use-After-Free"
  - "Remote Code Execution"
  - "Zero Day Initiative"
  - "CVE-2026-121753"
slug: "2026-11-05-zdi-26-872-0day-ashlar-vellum-cobalt-xe-file-parsing-use-aft"
quote: "Success means having the courage, the determination, and the will to become the person you believe you were meant to be."
quote_author: "George Sheehan"
---

### Executive Summary
Zero Day Initiative (ZDI) disclosed a 7.8 CVSS use‑after‑free vulnerability (CVE‑2026‑121753) in Ashlar‑Vellum Cobalt XE’s file‑parsing logic. Remote attackers can trigger RCE by delivering a crafted file or malicious web page, requiring user interaction. The flaw allows arbitrary code execution on affected installations.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-11-04T06:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Cobalt. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-121753.
