---
title: "China-Linked Hackers Deploy New StormEncryptor Ransomware, Likely via N-central Flaw"
date: 2026-08-10T16:38:37+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Microsoft has disclosed that a China-linked threat actor, known as Storm-1175, has deployed a new ransomware strain called StormEncryptor. This marks a shift from the group's previous use of Medusa ransomware. StormEncryptor is written in C++ and appends the file name extension .encrypted to files it encrypts, dropping a ransom note named !!!README_FIRST!!!.txt in every scanned directory.

The exact vulnerability exploited by Storm-1175 is unclear, but Microsoft believes it likely involves the exploitation of a newly disclosed security flaw in N-able N-central, specifically CVE-2026-18577. This vulnerability is a patch bypass for CVE-2026-18556, allowing authentication bypass and account takeover in susceptible versions. The US Cybersecurity and Infrastructure Security Agency (CISA) has flagged these vulnerabilities as actively exploited in the wild.

Storm-1175 is a financially motivated threat actor with a history of exploiting security flaws in various software to deploy ransomware. The group uses a combination of zero-days and N-day vulnerabilities to carry out high-velocity attacks, often breaking into susceptible internet-facing systems within a short window between vulnerability disclosure and patch adoption. Microsoft warns that Storm-1175 can rapidly move from initial access to data exfiltration and ransomware deployment, making it essential for customers to apply patches as soon as possible to prevent attacks.

---

> *He that never changes his opinions, never corrects his mistakes, and will never be wiser on the morrow than he is today.
Author: Tryon Edwards*

Source: [China-Linked Hackers Deploy New StormEncryptor Ransomware, Likely via N-central Flaw](https://thehackernews.com/2026/08/china-linked-hackers-deploy-new.html)
