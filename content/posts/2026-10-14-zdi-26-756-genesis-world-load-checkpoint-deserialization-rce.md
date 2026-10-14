---
title: "ZDI-26-756: Genesis World load_checkpoint Deserialization RCE Vulnerability"
description: "A zero-day vulnerability (ZDI-26-756) in Genesis World\u2019s load_checkpoint function allows remote attackers to execute arbitrary code via deserializatio..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-756/"
published: "2026-10-13T05:00:00+00:00"
ingested_at: "2026-10-14T03:22:19.703782+00:00"
date: "2026-10-14T03:22:19.703782+00:00"
category: "cves"
tags:
  - "ZeroDay"
  - "GenesisWorld"
  - "RCE"
  - "Deserialization"
  - "CVSS-7.8"
slug: "2026-10-14-zdi-26-756-genesis-world-load-checkpoint-deserialization-rce"
quote: "We all have problems. The way we solve them is what makes us different."
quote_author: "Unknown"
---

### Executive Summary
A zero-day vulnerability (ZDI-26-756) in Genesis World’s load_checkpoint function allows remote attackers to execute arbitrary code via deserialization of untrusted data. The flaw can be triggered by interacting with the library, with attack vectors depending on the implementation. The Zero Day Initiative rated the vulnerability CVSS 7.8.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-10-13T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Genesis World. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The ZDI has assigned a CVSS rating of 7.8.
