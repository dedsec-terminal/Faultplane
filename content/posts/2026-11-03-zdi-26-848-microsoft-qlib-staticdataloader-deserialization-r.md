---
title: "ZDI-26-848: Microsoft Qlib StaticDataLoader Deserialization Remote Code Execution Vulnerability"
description: "A remote code execution vulnerability (CVSS 7.8) in Microsoft Qlib\u2019s StaticDataLoader allows attackers to execute arbitrary code via deserialization o..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-848/"
published: "2026-11-02T06:00:00+00:00"
ingested_at: "2026-11-03T05:09:51.456825+00:00"
date: "2026-11-03T05:09:51.456825+00:00"
category: "cves"
tags:
  - "Microsoft"
  - "Qlib"
  - "deserialization"
  - "remote-code-execution"
  - "ZDI"
slug: "2026-11-03-zdi-26-848-microsoft-qlib-staticdataloader-deserialization-r"
quote: "Keep yourself to the sunshine and you cannot see the shadow."
quote_author: "Helen Keller"
---

### Executive Summary
A remote code execution vulnerability (CVSS 7.8) in Microsoft Qlib’s StaticDataLoader allows attackers to execute arbitrary code via deserialization of untrusted data. Exploitation requires user interaction, such as visiting a malicious page or opening a malicious file. The Zero Day Initiative (ZDI) identified the flaw, assigning it CVE-2026-848.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-11-02T06:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Qlib. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8.
