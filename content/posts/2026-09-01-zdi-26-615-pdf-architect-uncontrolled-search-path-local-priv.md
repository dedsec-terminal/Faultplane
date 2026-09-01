---
title: "ZDI-26-615: PDF Architect Uncontrolled Search Path Local Privilege Escalation"
description: "A local privilege\u2011escalation flaw in pdfforge PDF Architect\u2019s Update Service allows an attacker who can execute low\u2011privileged code to gain higher pri..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-615/"
published: "2026-08-31T05:00:00+00:00"
ingested_at: "2026-09-01T03:23:15.209325+00:00"
date: "2026-09-01T03:23:15.209325+00:00"
category: "cves"
tags:
  - "pdf"
  - "privilege-escalation"
  - "local"
  - "ZDI"
  - "pdf-architect"
slug: "2026-09-01-zdi-26-615-pdf-architect-uncontrolled-search-path-local-priv"
quote: "They must often change, who would be constant in happiness or wisdom."
quote_author: "Confucius"
---

### Executive Summary
A local privilege‑escalation flaw in pdfforge PDF Architect’s Update Service allows an attacker who can execute low‑privileged code to gain higher privileges. The vulnerability stems from an uncontrolled search path element, enabling the attacker to load malicious DLLs. Zero Day Initiative rated the flaw CVSS 7.8. The issue is publicly disclosed and requires local code execution to exploit.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-08-31T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows local attackers to escalate privileges on affected installations of pdfforge PDF Architect. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.8.
