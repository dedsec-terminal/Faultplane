---
title: "Fake Notepad++ Plugin Delivers MATCHBOIL.V2 in UAC-0099 Attacks"
date: 2026-07-24T06:50:57+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

The Computer Emergency Response Team of Ukraine (CERT-UA) has warned of a new campaign by the Russia-aligned threat group UAC-0099, which involves a malicious Notepad++ plugin to compromise Windows systems. The attack begins with a phishing email containing an image attachment that, when clicked, downloads a ZIP archive containing a Visual Basic Script (VBScript) masquerading as a PDF document. The script silently downloads a second archive, which includes a malicious DLL plugin that loads a modified version of the MATCHBOIL malware, codenamed MATCHBOIL.V2.

The MATCHBOIL.V2 malware is a C#-based loader capable of delivering secondary payloads, and it is loaded by the "RemoteLibUpdater.exe" binary, which is launched every three minutes via a scheduled task. If launched incorrectly, the binary exhausts computer resources instead. CERT-UA recommends updating WinRAR, 7-Zip, and Notepad++ software to prevent exploitation of known vulnerabilities. The UAC-0099 group has previously been observed using phishing emails and exploiting security flaws in WinRAR software to deliver malware.

The disclosure of this campaign comes as the US government highlights a phishing campaign by the Russia-linked threat actor Laundry Bear, targeting Zimbra mail servers belonging to Western government and commercial organizations. The campaign employs a novel "half-click" exploit to deliver malicious JavaScript, and its covert and persistent nature suggests involvement in espionage activities with Russian government backing. Additionally, a report from Proofpoint reveals that Russian threat actors continue to target webmail services using half-click cross-site scripting (XSS) exploits, with the goal of siphoning valuable data as part of a campaign referred to as Operation RoundPress.

---

> *Everything in the universe goes by indirection. There are no straight lines.
Author: Ralph Emerson*

Source: [Fake Notepad++ Plugin Delivers MATCHBOIL.V2 in UAC-0099 Attacks](https://thehackernews.com/2026/07/fake-notepad-plugin-delivers.html)
