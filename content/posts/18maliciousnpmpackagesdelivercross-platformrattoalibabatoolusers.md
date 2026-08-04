---
title: "18 Malicious npm Packages Deliver Cross-Platform RAT to Alibaba Tool Users"
date: 2026-08-03T18:43:53+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

Cybersecurity researchers have discovered 18 malicious npm packages that target users of Alibaba developer tools with a cross-platform remote access trojan (RAT). The packages, including "lib-mtop" and "local-config-parser", were designed to fetch a remote JavaScript payload and execute it, allowing attackers to gain control over the victim's system. The packages were published by a maintainer account "ch4ce", which has since been taken down, and were likely used in a targeted software supply chain attack against Chinese-speaking developers using Alibaba tools.

The malicious packages were designed to deliver a complex backdoor with comprehensive command execution, file upload and download, and lateral movement capabilities. The payload was retrieved from a domain masquerading as Alibaba and was capable of persisting by injecting malicious code into common enterprise collaboration applications. The attack was sophisticated, with multiple layers of dependencies and a rule engine that used the vm module to implement the final phase of the payload download. The attackers' goal appears to be industrial espionage, targeting Chinese-speaking developers and companies using Alibaba tools.

Users who have installed any of the malicious packages should assume compromise and take immediate action to rotate sensitive credentials and audit their systems for signs of suspicious activity. The discovery of these malicious packages comes as another incident was reported, where a poisoned version of the mrmustard Python library was published to steal sensitive information, including SSH private keys and AWS credentials. The incidents highlight the importance of vigilance and security measures in the software development supply chain, particularly in targeted attacks against specific industries or regions.

---

> *Gratitude is not only the greatest of virtues, but the paren't of all the others.
Author: Cicero*

Source: [18 Malicious npm Packages Deliver Cross-Platform RAT to Alibaba Tool Users](https://thehackernews.com/2026/08/18-malicious-npm-packages-deliver-cross.html)
