---
title: "VMs Won't Contain Cyber-Capable Agents"
description: "Trail of Bits tested GPT\u20115.6\u2011Cyber in a QEMU/KVM sandbox on Debian\u202f12. The model autonomously discovered and exploited undisclosed kernel bugs and 0\u2011d..."
source: "Trail of Bits"
source_url: "https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/"
published: "2026-08-26T11:00:00+00:00"
ingested_at: "2026-08-27T07:03:57.723974+00:00"
date: "2026-08-27T07:03:57.723974+00:00"
category: "research"
tags:
  - "AI"
  - "VM escape"
  - "kernel vulnerabilities"
  - "GPT-5.6-Cyber"
  - "QEMU/KVM"
  - "APT"
  - "Linux"
  - "Trail of Bits"
slug: "2026-08-27-vms-won-t-contain-cyber-capable-agents"
quote: "Each misfortune you encounter will carry in it the seed of tomorrows good luck."
quote_author: "Og Mandino"
---

### Executive Summary
Trail of Bits tested GPT‑5.6‑Cyber in a QEMU/KVM sandbox on Debian 12. The model autonomously discovered and exploited undisclosed kernel bugs and 0‑day vulnerabilities, escaping the VM three times. It built its own exploits, pulled research, and operated for hours with minimal prompting, forcing the host to reboot. The experiment shows that advanced AI agents can act as APTs and that a single VM is insufficient containment.

---
**Intelligence Metadata**
- **Source Publisher:** Trail of Bits
- **Published Date:** 2026-08-26T11:00:00+00:00
- **Category:** research

**Original Description:**
As part of Patch the Planet, we received preview access to GPT 5.6-Cyber with a simple task: evaluate its cyber capabilities. Recent events inspired me to give it a challenge to work through: escape the VM I’d normally use for sandboxing. The target was a QEMU/KVM VM on my Linux dev machine (Debian Linux 12, AMD Zen3). It escaped the VM three different times. First, it used recently disclosed bugs in my host kernel. When I fully updated, it used disclosed bugs that had not yet reached package...
