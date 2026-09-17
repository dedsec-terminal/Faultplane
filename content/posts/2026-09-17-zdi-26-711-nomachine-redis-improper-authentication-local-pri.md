---
title: "ZDI-26-711: NoMachine Redis Improper Authentication Local Privilege Escalation Vulnerability"
description: "The Zero Day Initiative (ZDI) identified a local privilege escalation vulnerability (CVE-2026-92209) in NoMachine's Redis component. The flaw allows a..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-711/"
published: "2026-09-16T05:00:00+00:00"
ingested_at: "2026-09-17T03:12:21.397259+00:00"
date: "2026-09-17T03:12:21.397259+00:00"
category: "cves"
tags:
  - "NoMachine"
  - "Redis"
  - "local privilege escalation"
  - "CVE-2026-92209"
  - "ZDI-26-711"
slug: "2026-09-17-zdi-26-711-nomachine-redis-improper-authentication-local-pri"
quote: "I have always thought the actions of men the best interpreters of their thoughts."
quote_author: "John Locke"
---

### Executive Summary
The Zero Day Initiative (ZDI) identified a local privilege escalation vulnerability (CVE-2026-92209) in NoMachine's Redis component. The flaw allows an attacker who can execute low‑privileged code to bypass authentication and gain higher privileges on affected installations. The vulnerability has a CVSS score of 7.8.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-16T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows local attackers to escalate privileges on affected installations of NoMachine. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-92209.
