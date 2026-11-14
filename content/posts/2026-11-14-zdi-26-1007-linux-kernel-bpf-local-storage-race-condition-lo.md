---
title: "ZDI-26-1007: Linux Kernel BPF Local Storage Race Condition Local Privilege Escalation Vulnerability"
description: "A race condition in the Linux kernel's BPF local storage can lead to local privilege escalation. The flaw requires the attacker to already run privile..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-1007/"
published: "2026-11-13T06:00:00+00:00"
ingested_at: "2026-11-14T04:46:39.110995+00:00"
date: "2026-11-14T04:46:39.110995+00:00"
category: "cves"
tags:
  - "linux"
  - "kernel"
  - "bpf"
  - "privilege-escalation"
  - "race-condition"
slug: "2026-11-14-zdi-26-1007-linux-kernel-bpf-local-storage-race-condition-lo"
quote: "We must not say every mistake is a foolish one."
quote_author: "Cicero"
---

### Executive Summary
A race condition in the Linux kernel's BPF local storage can lead to local privilege escalation. The flaw requires the attacker to already run privileged code, but once triggered it allows them to gain higher privileges. The Zero Day Initiative assigned CVSS 7.5. The vulnerability is identified as ZDI-26-1007.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-11-13T06:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.5.
