---
title: "ZDI-26-575: Linux Kernel Net Scheduler Packet Classifier API Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability"
date: 2026-08-13T05:00:00+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Linux Kernel Net Scheduler Packet Classifier API Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability
Vulnerability Details
This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability.
The specific flaw exists within the traffic classifier. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.
Additional Details
Linux has issued an update to correct this vulnerability. More details can be found at:
                            
                            https://github.com/torvalds/linux/commit/8b519cbcabe836a441369fbec1a8a6518a709251
                            
                        
Disclosure Timeline
- 2026-06-25 - Vulnerability reported 

---

> *Life is the flower for which love is the honey.
Author: Victor Hugo*

Source: [ZDI-26-575: Linux Kernel Net Scheduler Packet Classifier API Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability](http://www.zerodayinitiative.com/advisories/ZDI-26-575/)
