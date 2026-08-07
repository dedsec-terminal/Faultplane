---
title: "New Interrupt Injection Attack Can Bypass Spectre v2 Defenses on Intel and AMD CPUs"
date: 2026-08-06T16:17:13+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Researchers from MIT CSAIL have discovered a new attack technique called Interrupt Injection, which can bypass Spectre v2 defenses on Intel and AMD CPUs. The attack involves timing a hardware interrupt to land in the gap between a processor sanitizing its branch predictor and the kernel using it, effectively re-poisoning the predictor after the defense has run. This allows an unprivileged Linux program to leak arbitrary kernel memory, potentially leading to the disclosure of sensitive information such as password hashes.

The researchers demonstrated the attack on an AMD Zen 2 machine running Linux 6.14 with default Spectre v2 mitigations, achieving a leak rate of 5.47 bytes per second with 91.97% accuracy. They also tested the attack on Intel CPUs, including Arrow Lake and Cascade Lake Refresh, and found that while the success rate was lower, the attack was still possible. The researchers believe that an end-to-end attack is possible on Intel CPUs by combining the Interrupt Injection technique with existing disclosure gadgets.

A fix for the vulnerability has been implemented in the Linux kernel, and AMD has published a bulletin (AMD-SB-7061) acknowledging the issue and listing affected processors, including Zen 1 through Zen 4. However, Intel does not consider a mitigation necessary, citing that the technique is covered by existing guidance. The researchers presented their work at Black Hat USA and will also present it at USENIX Security in Baltimore. The vulnerability highlights the importance of considering the timing of hardware interrupts in the design of Spectre v2 defenses, and the need for ongoing research and development to stay ahead of potential attacks.

---

> *The most decisive actions of our life... are most often unconsidered actions.
Author: Andr� Gide*

Source: [New Interrupt Injection Attack Can Bypass Spectre v2 Defenses on Intel and AMD CPUs](https://thehackernews.com/2026/08/new-interrupt-injection-attack-can.html)
