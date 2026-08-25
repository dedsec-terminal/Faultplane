---
title: "ZDI-26-609: Linux Kernel Net Scheduler Packet Classifier Use-After-Free Local Privilege Escalation Vulnerability"
description: "A local privilege escalation vulnerability (CVE-2026-609) in the Linux kernel's net scheduler packet classifier allows attackers with low-privileged c..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-609/"
published: "2026-08-24T05:00:00+00:00"
ingested_at: "2026-08-25T01:03:20.686264+00:00"
date: "2026-08-25T01:03:20.686264+00:00"
category: "cves"
tags:
  - "Linux kernel"
  - "privilege escalation"
  - "use-after-free"
  - "Zero Day Initiative"
  - "CVE-2026-609"
slug: "2026-08-25-zdi-26-609-linux-kernel-net-scheduler-packet-classifier-use"
quote: "We may encounter many defeats but we must not be defeated."
quote_author: "Maya Angelou"
---

### Executive Summary
A local privilege escalation vulnerability (CVE-2026-609) in the Linux kernel's net scheduler packet classifier allows attackers with low-privileged code execution to trigger a use‑after‑free, potentially gaining root access. The Zero Day Initiative rated it CVSS 7.8.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-08-24T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.8.
