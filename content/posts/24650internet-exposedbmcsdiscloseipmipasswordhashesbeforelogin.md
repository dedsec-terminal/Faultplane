---
title: "24,650 Internet-Exposed BMCs Disclose IPMI Password Hashes Before Login"
date: 2026-07-28T14:41:36+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here is a summary of the article in three concise paragraphs:

Cybersecurity researchers have discovered over 36,000 Baseboard Management Controller (BMC) management interfaces exposed to the public internet, with 24,650 of them disclosing IPMI password hashes before login due to a vulnerability in the IPMI v2.0 specification. This vulnerability, known as CVE-2013-4786, allows remote attackers to obtain password hashes for valid accounts and conduct offline password guessing attacks. The issue is inherent to the IPMI v2.0 specification, and there is no patch available.

The exposed BMCs are a significant security risk, as they can be used by attackers to gain remote control and deploy persistent malware. BMCs are specialized management processors that control power, firmware, and remote console access, and are used in data centers to monitor hardware telemetry and facilitate mass deployment of firmware updates and BIOS configurations. The privileged position of BMCs makes them an ideal target for bad actors, and compromising an exposed BMC can allow attackers to sidestep traditional security controls and maintain access even after operating system reinstalls.

To counter the risk, organizations are advised to block UDP port 623 at the network edge, rotate factory-issued passwords, and restrict BMC access to a dedicated private management network. The vulnerability is particularly concerning in modern AI data centers, where a single exposed BMC can potentially place multiple organizations' workloads at risk. The researchers warn that the risk around CVE-2013-4786 has changed due to the increased use of GPU cracking, which has made offline password recovery faster, and the growing importance of securing the infrastructure underlying AI data centers.

---

> *People may doubt what you say, but they will believe what you do.
Author: Lewis Cass*

Source: [24,650 Internet-Exposed BMCs Disclose IPMI Password Hashes Before Login](https://thehackernews.com/2026/07/24650-internet-exposed-bmcs-disclose.html)
