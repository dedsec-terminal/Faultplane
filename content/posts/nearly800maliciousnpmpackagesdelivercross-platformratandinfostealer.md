---
title: "Nearly 800 Malicious npm Packages Deliver Cross-Platform RAT and Infostealer"
date: 2026-08-07T18:48:17+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

A massive campaign has been discovered on the npm registry, with nearly 800 malicious packages designed to deliver cross-platform malware to Windows, Mac, and Linux systems. These packages use randomly generated names and instruct developers to load them using the `require()` function, leading to the execution of a downloader named WEL1DROPPER. This malware identifies the host operating system and processor architecture, fetching a compatible payload from one of three Cloudflare Workers hosts.

The payloads are tailored to each operating system and CPU architecture, with domains such as "wel1.ru" used to deliver the malware. The final stage of the attack involves writing the payload to a temporary folder and executing it using system-specific commands. The malware also takes steps to evade detection, including patching Event Tracing for Windows (ETW) and Antimalware Scan Interface (AMSI) on Windows, and setting up persistence through Registry Run keys and scheduled tasks. On macOS, the malware employs similar tactics, while on Linux, it downloads auxiliary payloads leading to the deployment of the Sliver command-and-control (C2) framework.

The campaign is suspected to be an evolution of a previous dependency confusion campaign and may be targeting Russian financial institutions and mobile payments. The attack highlights the growing threat of software supply chain attacks, with multiple campaigns targeting npm and the Python Package Index (PyPI) repository. Threat actors are also using other tactics, such as malicious Chrome extensions, to compromise systems and steal sensitive information. The discovery of these malicious packages and extensions underscores the need for developers and users to be vigilant when installing software and extensions, and to carefully review their code and permissions.

---

> *There are only two mistakes one can make along the road to truth; not going all the way, and not starting.
Author: Buddha*

Source: [Nearly 800 Malicious npm Packages Deliver Cross-Platform RAT and Infostealer](https://thehackernews.com/2026/08/nearly-800-malicious-npm-packages.html)
