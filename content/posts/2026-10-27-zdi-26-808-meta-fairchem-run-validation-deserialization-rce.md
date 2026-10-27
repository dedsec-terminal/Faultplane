---
title: "ZDI-26-808: Meta FAIRChem run_validation Deserialization RCE Vulnerability"
description: "A deserialization flaw in Meta FAIRChem\u2019s run_validation function allows remote attackers to execute arbitrary code. Exploitation requires user intera..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-808/"
published: "2026-10-26T05:00:00+00:00"
ingested_at: "2026-10-27T03:32:17.083839+00:00"
date: "2026-10-27T03:32:17.083839+00:00"
category: "cves"
tags:
  - "Meta FAIRChem"
  - "deserialization"
  - "remote code execution"
  - "ZDI"
  - "CVSS-7.8"
slug: "2026-10-27-zdi-26-808-meta-fairchem-run-validation-deserialization-rce"
quote: "It is only with the heart that one can see rightly, what is essential is invisible to the eye."
quote_author: "Antoine de Saint-Exupery"
---

### Executive Summary
A deserialization flaw in Meta FAIRChem’s run_validation function allows remote attackers to execute arbitrary code. Exploitation requires user interaction, such as visiting a malicious page or opening a malicious file. The vulnerability carries a CVSS score of 7.8 and was disclosed by Zero Day Initiative.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-10-26T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Meta FAIRChem. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8.
