---
title: "Adobe Campaign Classic CVSS 10.0 Flaw Could Run Code Without User Interaction"
date: 2026-08-01T07:12:42+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Adobe has released security updates to address a critical vulnerability in its Campaign Classic marketing automation platform. The flaw, tracked as CVE-2026-48449, has a severity score of 10.0 on the CVSS scoring system and could allow arbitrary code execution without requiring user interaction. This is due to incorrect authorization, which could lead to code execution in the context of the current user.

In addition to the CVE-2026-48449 flaw, Adobe has also addressed another high-severity vulnerability (CVE-2026-48448) stemming from SQL injection, which could allow arbitrary file reads. Both of these vulnerabilities have been resolved in the latest update for Campaign Classic (v7: 7.4.3 build 9398) for Windows and Linux. Adobe is not aware of any of these flaws being exploited in the wild, but users are still advised to apply the latest updates for optimal protection.

Separately, Adobe has also released updates to address eight critical-rated flaws in Adobe Bridge, which could lead to privilege escalation and arbitrary code execution. These vulnerabilities, tracked as CVE-2026-48395 to CVE-2026-48394, have CVSS scores ranging from 7.8 to 8.6 and were discovered by security researchers Kieran and "yjdfy". Users are advised to apply the latest updates to ensure their systems are protected from potential exploits.

---

> *There are two kinds of failures: those who thought and never did, and those who did and never thought.
Author: Laurence J. Peter*

Source: [Adobe Campaign Classic CVSS 10.0 Flaw Could Run Code Without User Interaction](https://thehackernews.com/2026/08/adobe-campaign-classic-cvss-100-flaw.html)
