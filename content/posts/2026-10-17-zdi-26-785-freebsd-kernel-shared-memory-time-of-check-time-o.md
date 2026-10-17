---
title: "ZDI-26-785: FreeBSD Kernel Shared Memory Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability"
description: "A local privilege escalation vulnerability (CVE-2026-58094) in the FreeBSD kernel\u2019s shared memory subsystem allows attackers who can execute low\u2011privi..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-785/"
published: "2026-10-16T05:00:00+00:00"
ingested_at: "2026-10-17T02:49:27.246491+00:00"
date: "2026-10-17T02:49:27.246491+00:00"
category: "cves"
tags:
  - "FreeBSD"
  - "kernel"
  - "privilege-escalation"
  - "time-of-check-time-of-use"
  - "CVE-2026-58094"
slug: "2026-10-17-zdi-26-785-freebsd-kernel-shared-memory-time-of-check-time-o"
quote: "We never understand how little we need in this world until we know the loss of it."
quote_author: "James Barrie"
---

### Executive Summary
A local privilege escalation vulnerability (CVE-2026-58094) in the FreeBSD kernel’s shared memory subsystem allows attackers who can execute low‑privileged code to gain higher privileges via a time‑of‑check/time‑of‑use flaw. The Zero Day Initiative rated it CVSS 7.8.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-10-16T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows local attackers to escalate privileges on affected installations of FreeBSD Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-58094.
