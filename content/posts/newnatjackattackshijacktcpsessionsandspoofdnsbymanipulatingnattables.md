---
title: "New NatJack Attacks Hijack TCP Sessions and Spoof DNS by Manipulating NAT Tables"
date: 2026-08-07T10:58:38+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Security researcher Malcolm Stagg has disclosed a new attack class called NatJack, which manipulates network address translation (NAT) connection state to hijack active TCP sessions, spoof DNS responses, and expose mapped ports. The attack requires the attacker to have privileged access to a system behind the same NAT as the victim. Stagg's research found that the attack affects multiple implementations, including Windows and Linux, and has identified two implementation-specific flaws, assigned CVE-2026-56181 and CVE-2026-63913.

The NatJack attack exploits an assumption built into many NAT implementations that hosts behind the same NAT do not manipulate each other's connection state. An attacker controlling a system behind the same NAT can manipulate connection-tracking entries belonging to another system, allowing them to redirect traffic, interfere with DNS requests, and disclose externally mapped ports. The research describes four main paths of attack and has been tested against dozens of real-world network infrastructure products from multiple vendors.

To mitigate the NatJack attack, organizations are advised to apply available Windows and Linux updates, encrypt traffic even within internal networks, and use Internet Protocol (IP) Source Guard where applicable. There is no single patch for the broader attack class, and the research emphasizes the importance of separating untrusted workloads from trusted systems that share NAT infrastructure. The affected vendors have released patches, including Linux kernel updates and Windows security updates, to address the implementation-specific flaws. However, the researcher notes that the kernel change only mitigates the broader downstream-spoofing technique, increasing attack complexity rather than fully addressing it.

---

> *In the end we retain from our studies only that which we practically apply.
Author: Johann Wolfgang von Goethe*

Source: [New NatJack Attacks Hijack TCP Sessions and Spoof DNS by Manipulating NAT Tables](https://thehackernews.com/2026/08/new-natjack-attacks-hijack-tcp-sessions.html)
