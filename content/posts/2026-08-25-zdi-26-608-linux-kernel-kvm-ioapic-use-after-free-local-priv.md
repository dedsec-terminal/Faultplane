---
title: "ZDI-26-608: Linux Kernel KVM IOAPIC Use-After-Free Local Privilege Escalation Vulnerability"
description: "A local privilege escalation vulnerability (ZDI-26-608) in the Linux kernel\u2019s KVM IOAPIC subsystem allows an attacker with local code execution to exp..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-608/"
published: "2026-08-24T05:00:00+00:00"
ingested_at: "2026-08-25T01:03:30.838340+00:00"
date: "2026-08-25T01:03:30.838340+00:00"
category: "cves"
tags:
  - "Linux Kernel"
  - "KVM"
  - "IOAPIC"
  - "Use-After-Free"
  - "Privilege Escalation"
  - "Local"
  - "Zero Day Initiative"
  - "ZDI-26-608"
slug: "2026-08-25-zdi-26-608-linux-kernel-kvm-ioapic-use-after-free-local-priv"
quote: "The beginning of knowledge is the discovery of something we do not understand."
quote_author: "Frank Herbert"
---

### Executive Summary
A local privilege escalation vulnerability (ZDI-26-608) in the Linux kernel’s KVM IOAPIC subsystem allows an attacker with local code execution to exploit a use‑after‑free bug, raising privileges. The Zero Day Initiative rated it CVSS 8.2.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-08-24T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 8.2.
