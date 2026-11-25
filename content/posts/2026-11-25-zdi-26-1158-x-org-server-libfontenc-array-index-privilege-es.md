---
title: "ZDI-26-1158: X.Org Server libfontenc Array Index Privilege Escalation Vulnerability"
description: "A local privilege escalation vulnerability exists in X.Org Server's libfontenc component due to improper array index validation when parsing encoding ..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-1158/"
published: "2026-11-24T06:00:00+00:00"
ingested_at: "2026-11-25T06:48:30.569986+00:00"
date: "2026-11-25T06:48:30.569986+00:00"
category: "cves"
tags:
  - "X.Org"
  - "libfontenc"
  - "privilege escalation"
  - "CVE-2026-109908"
  - "Zero Day Initiative"
slug: "2026-11-25-zdi-26-1158-x-org-server-libfontenc-array-index-privilege-es"
quote: "He that is giddy thinks the world turns round."
quote_author: "William Shakespeare"
---

### Executive Summary
A local privilege escalation vulnerability exists in X.Org Server's libfontenc component due to improper array index validation when parsing encoding files. Attackers who can execute low‑privileged code can exploit the flaw to gain higher privileges. The issue is assigned CVE‑2026‑109908 with a CVSS score of 7.8. Zero Day Initiative identified the flaw.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-11-24T06:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows local attackers to escalate privileges on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-109908.
