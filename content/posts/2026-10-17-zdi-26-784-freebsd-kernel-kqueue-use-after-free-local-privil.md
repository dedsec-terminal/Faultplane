---
title: "ZDI-26-784: FreeBSD Kernel kqueue Use-After-Free Local Privilege Escalation Vulnerability"
description: "The Zero Day Initiative (ZDI) has identified a use\u2011after\u2011free flaw in FreeBSD\u2019s kernel kqueue subsystem that allows local attackers to gain elevated p..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-784/"
published: "2026-10-16T05:00:00+00:00"
ingested_at: "2026-10-17T02:49:42.072668+00:00"
date: "2026-10-17T02:49:42.072668+00:00"
category: "cves"
tags:
  - "FreeBSD"
  - "kernel"
  - "privilege escalation"
  - "use-after-free"
  - "ZDI"
  - "CVE-2026-58093"
slug: "2026-10-17-zdi-26-784-freebsd-kernel-kqueue-use-after-free-local-privil"
quote: "Meaning is not what you start with but what you end up with."
quote_author: "Peter Elbow"
---

### Executive Summary
The Zero Day Initiative (ZDI) has identified a use‑after‑free flaw in FreeBSD’s kernel kqueue subsystem that allows local attackers to gain elevated privileges. The vulnerability requires the attacker to already have low‑privileged code execution on the target. CVE‑2026‑58093 has been assigned with a CVSS score of 8.8.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-10-16T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows local attackers to escalate privileges on affected installations of FreeBSD Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 8.8. The following CVEs are assigned: CVE-2026-58093.
