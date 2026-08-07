---
title: "New Zapscape KVM Flaw Could Let Privileged L1 Guest Code Escape to Linux Hosts"
date: 2026-08-06T17:58:30+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A new Linux kernel vulnerability, known as Zapscape, has been discovered, which could allow an attacker with kernel privileges inside an L1 guest virtual machine (VM) to escape KVM isolation and execute code on the host. The flaw, tracked as CVE-2026-64561, affects KVM/x86's shadow memory management unit (MMU) and is caused by a stale-root check ordering issue that can lead to a use-after-free. This vulnerability can be exploited when nested virtualization is exposed to untrusted guests.

The vulnerability can be exploited by an attacker with kernel privileges inside an L1 guest VM, which typically means guest root. Additionally, Intel systems require specific conditions to be met, including EPT page-walk length 4 and 5 to be exposed to the L1 guest, while AMD systems have no equivalent condition. A proof-of-concept exploit has been released, which can create a root-owned file on the host running the vulnerable KVM. The exploit is not considered "weaponized" and would require adaptation to the host kernel configuration and memory backend to be used in a real-world attack.

The upstream fix for the vulnerability has been merged, and administrators running KVM hosts that expose nested virtualization to untrusted guests are advised to update to a fixed stable kernel or a vendor package that backports the patch. The National Vulnerability Database lists Linux 5.9 and later as affected until fixed stable releases, and Linux vendors such as Red Hat and Debian have released advisories and patches for the vulnerability. The fix moves the stale-root check after making MMU pages available, preventing the use-after-free issue and ensuring that KVM restarts the fault with RET_PF_RETRY instead of continuing to map or fetch under the invalid root.

---

> *If you must tell me your opinions, tell me what you believe in. I have plenty of douts of my own.
Author: Johann Wolfgang von Goethe*

Source: [New Zapscape KVM Flaw Could Let Privileged L1 Guest Code Escape to Linux Hosts](https://thehackernews.com/2026/08/new-zapscape-kvm-flaw-could-let.html)
