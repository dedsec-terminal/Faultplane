---
title: "APT group HoneyMyte upgrades CoolClient: the backdoor gets a kernel-level Windows rootkit"
date: 2026-08-14T09:00:14+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

The HoneyMyte APT group, also known as Mustang Panda, has upgraded its CoolClient backdoor with a kernel-level Windows rootkit. CoolClient is a malware family used in cyber-espionage campaigns targeting organizations in Asia and Russia, and has been continuously evolving since its first public disclosure in 2022. The latest variant can deploy a signed kernel-mode driver as a Windows service, enhancing the malware's stealth and allowing it to hide its process, protect related files and registry entries, and prevent them from being inspected or modified.

The updated CoolClient variant uses a multi-stage execution chain, with each component performing a distinct role during execution. The malware begins with a legitimate Sangfor application (defender.exe or Sang.exe) loading the malicious libngs.dll through DLL sideloading. The libngs.dll then loads and decrypts the second-stage DLL, loadcert.ini, which prepares the execution environment and performs initial setup, including persistence, UAC bypass, and process injection. The malware injects into synchost.exe and establishes AutoRun persistence, allowing it to launch itself with the work parameter whenever the user logs on.

The second-stage DLL, loadcert.ini, also deploys a kernel-mode driver, which extends CoolClient with rootkit capabilities. The driver hides the CoolClient process, protects related files and registry entries, and prevents them from being inspected or modified. The malware uses a command handler to control execution, with three command-line parameters: install, work, and passuac. The install parameter performs initial setup, including persistence and privilege checks, while the work parameter executes the primary second-stage functionality, including driver deployment and third-stage loading. The passuac parameter continues execution after privilege elevation, allowing the malware to relaunch itself with elevated privileges while concealing its true parent process.

---

> *These days people seek knowledge, not wisdom. Knowledge is of the past, wisdom is of the future.
Author: Vernon Cooper*

Source: [APT group HoneyMyte upgrades CoolClient: the backdoor gets a kernel-level Windows rootkit](https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/)
