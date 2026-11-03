---
title: "ZDI-26-849: Microsoft Qlib RestrictedUnpickler Deserialization Remote Code Execution Vulnerability"
description: "A remote code execution vulnerability (CVSS 7.8) exists in Microsoft Qlib's RestrictedUnpickler deserialization logic. Attackers can exploit it by del..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-849/"
published: "2026-11-02T06:00:00+00:00"
ingested_at: "2026-11-03T05:09:42.620722+00:00"
date: "2026-11-03T05:09:42.620722+00:00"
category: "cves"
tags:
  - "Microsoft"
  - "Qlib"
  - "deserialization"
  - "remote-code-execution"
  - "ZDI"
slug: "2026-11-03-zdi-26-849-microsoft-qlib-restrictedunpickler-deserializatio"
quote: "Some people are always grumbling because roses have thorns; I am thankful that thorns have roses."
quote_author: "Alphonse Karr"
---

### Executive Summary
A remote code execution vulnerability (CVSS 7.8) exists in Microsoft Qlib's RestrictedUnpickler deserialization logic. Attackers can exploit it by delivering malicious content that forces the target to visit a malicious page or open a malicious file. The flaw allows arbitrary code execution on affected installations.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-11-02T06:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Qlib. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8.
