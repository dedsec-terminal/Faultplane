---
title: "ZDI-26-1159: X.Org Server PCF Font Parsing Out-Of-Bounds Read Information Disclosure Vulnerability"
description: "A local out-of-bounds read in X.Org Server's PCF font parsing can leak sensitive data. The flaw requires low\u2011privilege code execution and is rated CVS..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-1159/"
published: "2026-11-24T06:00:00+00:00"
ingested_at: "2026-11-25T06:48:27.723998+00:00"
date: "2026-11-25T06:48:27.723998+00:00"
category: "cves"
tags:
  - "xorg"
  - "font parsing"
  - "out-of-bounds"
  - "information disclosure"
  - "CVE-2026-109909"
slug: "2026-11-25-zdi-26-1159-x-org-server-pcf-font-parsing-out-of-bounds-read"
quote: "Skill to do comes of doing."
quote_author: "Ralph Emerson"
---

### Executive Summary
A local out-of-bounds read in X.Org Server's PCF font parsing can leak sensitive data. The flaw requires low‑privilege code execution and is rated CVSS 6.1. CVE‑2026‑109909 was assigned by Zero Day Initiative (ZDI‑26‑1159).

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-11-24T06:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows local attackers to disclose sensitive information on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 6.1. The following CVEs are assigned: CVE-2026-109909.
