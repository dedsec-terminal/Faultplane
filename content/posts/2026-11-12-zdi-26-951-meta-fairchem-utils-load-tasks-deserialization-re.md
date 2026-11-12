---
title: "ZDI-26-951: Meta FAIRChem utils load_tasks Deserialization Remote Code Execution Vulnerability"
description: "A deserialization flaw in Meta FAIRChem's utils load_tasks allows remote attackers to execute arbitrary code when a user visits a malicious page or op..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-951/"
published: "2026-11-11T06:00:00+00:00"
ingested_at: "2026-11-12T05:36:29.740094+00:00"
date: "2026-11-12T05:36:29.740094+00:00"
category: "vulnerabilities"
tags:
  - "Meta FAIRChem"
  - "deserialization"
  - "remote code execution"
  - "Zero Day Initiative"
  - "ZDI-26-951"
slug: "2026-11-12-zdi-26-951-meta-fairchem-utils-load-tasks-deserialization-re"
quote: "Many of life's failures are people who did not realize how close they were to success when they gave up."
quote_author: "Thomas Edison"
---

### Executive Summary
A deserialization flaw in Meta FAIRChem's utils load_tasks allows remote attackers to execute arbitrary code when a user visits a malicious page or opens a malicious file. The vulnerability requires user interaction and has a CVSS score of 7.8. Zero Day Initiative identified the issue as ZDI-26-951.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-11-11T06:00:00+00:00
- **Category:** vulnerabilities

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Meta FAIRChem. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8.
