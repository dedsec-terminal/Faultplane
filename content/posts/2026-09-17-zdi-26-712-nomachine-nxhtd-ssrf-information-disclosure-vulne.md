---
title: "ZDI-26-712: NoMachine nxhtd SSRF Information Disclosure Vulnerability"
description: "A server\u2011side request forgery (SSRF) flaw in NoMachine\u2019s nxhtd component allows unauthenticated attackers to trigger arbitrary outbound requests, pote..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-712/"
published: "2026-09-16T05:00:00+00:00"
ingested_at: "2026-09-17T03:12:13.620928+00:00"
date: "2026-09-17T03:12:13.620928+00:00"
category: "cves"
tags:
  - "NoMachine"
  - "SSRF"
  - "Information Disclosure"
  - "CVE-2026-92210"
  - "Zero Day Initiative"
slug: "2026-09-17-zdi-26-712-nomachine-nxhtd-ssrf-information-disclosure-vulne"
quote: "We are Divine enough to ask and we are important enough to receive."
quote_author: "Wayne Dyer"
---

### Executive Summary
A server‑side request forgery (SSRF) flaw in NoMachine’s nxhtd component allows unauthenticated attackers to trigger arbitrary outbound requests, potentially exposing sensitive data. The vulnerability, identified as CVE‑2026‑92210, carries a CVSS score of 7.2 and was disclosed by the Zero Day Initiative.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-16T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to initiate arbitrary server-side requests on affected installations of NoMachine. Authentication is not required to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.2. The following CVEs are assigned: CVE-2026-92210.
