---
title: "ZDI-26-850: Microsoft Qlib MLflowRecorder Deserialization of Untrusted Data Remote Code Execution Vulnerability"
description: "A remote code execution vulnerability (CVSS 7.8) exists in Microsoft Qlib's MLflowRecorder component due to deserialization of untrusted data. Attacke..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-850/"
published: "2026-11-02T06:00:00+00:00"
ingested_at: "2026-11-03T05:09:39.188462+00:00"
date: "2026-11-03T05:09:39.188462+00:00"
category: "cves"
tags:
  - "Microsoft"
  - "Qlib"
  - "MLflowRecorder"
  - "deserialization"
  - "remote code execution"
  - "ZDI-26-850"
slug: "2026-11-03-zdi-26-850-microsoft-qlib-mlflowrecorder-deserialization-of"
quote: "Character is like a tree and reputation like a shadow. The shadow is what we think of it; the tree is the real thing."
quote_author: "Abraham Lincoln"
---

### Executive Summary
A remote code execution vulnerability (CVSS 7.8) exists in Microsoft Qlib's MLflowRecorder component due to deserialization of untrusted data. Attackers can exploit it by delivering a malicious page or file that the user must interact with. The flaw is identified as ZDI-26-850.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-11-02T06:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Qlib. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8.
