---
title: "ZDI-26-905: X.Org Server libXrender RenderQueryPictFormats Reply Heap-based Buffer Overflow Remote Code Execution Vulnerability"
description: "A heap-based buffer overflow in X.Org Server's libXrender RenderQueryPictFormats Reply allows remote code execution when a client connects to a malici..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-905/"
published: "2026-11-10T06:00:00+00:00"
ingested_at: "2026-11-11T04:31:11.305417+00:00"
date: "2026-11-11T04:31:11.305417+00:00"
category: "cves"
tags:
  - "xorg"
  - "heap-overflow"
  - "remote-code-execution"
  - "cve-2026-88807"
  - "zero-day-initiative"
slug: "2026-11-11-zdi-26-905-x-org-server-libxrender-renderquerypictformats-re"
quote: "What lies behind us and what lies before us are tiny matters compared to what lies within us."
quote_author: "Walt Emerson"
---

### Executive Summary
A heap-based buffer overflow in X.Org Server's libXrender RenderQueryPictFormats Reply allows remote code execution when a client connects to a malicious X11 server. The vulnerability, identified as CVE‑2026‑88807, requires user interaction and has a CVSS score of 8.8. Zero Day Initiative (ZDI) released the advisory under ZDI‑26‑905.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-11-10T06:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of X.Org Server. User interaction is required to exploit this vulnerability in that the target must connect to a malicious X11 server. The ZDI has assigned a CVSS rating of 8.8. The following CVEs are assigned: CVE-2026-88807.
