---
title: "ZDI-26-700: Linux Kernel QFQ Plus Scheduler Use-After-Free Local Privilege Escalation Vulnerability"
description: "A use\u2011after\u2011free flaw in the Linux Kernel QFQ Plus scheduler allows local attackers who can execute low\u2011privileged code to elevate privileges. The vul..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-700/"
published: "2026-09-14T05:00:00+00:00"
ingested_at: "2026-09-15T03:11:40.797974+00:00"
date: "2026-09-15T03:11:40.797974+00:00"
category: "cves"
tags:
  - "Linux Kernel"
  - "Use-After-Free"
  - "Local Privilege Escalation"
  - "QFQ Plus Scheduler"
  - "CVE-2026-22999"
  - "Zero Day Initiative"
slug: "2026-09-15-zdi-26-700-linux-kernel-qfq-plus-scheduler-use-after-free-lo"
quote: "Every person, all the events of your life are there because you have drawn them there. What you choose to do with them is up to you."
quote_author: "Richard Bach"
---

### Executive Summary
A use‑after‑free flaw in the Linux Kernel QFQ Plus scheduler allows local attackers who can execute low‑privileged code to elevate privileges. The vulnerability carries a CVSS score of 7.8 and is identified as CVE-2026-22999. It was disclosed by the Zero Day Initiative.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-14T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-22999.
