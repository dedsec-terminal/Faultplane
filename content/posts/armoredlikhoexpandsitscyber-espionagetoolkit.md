---
title: "Armored Likho expands its cyber-espionage toolkit"
date: 2026-08-13T08:00:15+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

The Armored Likho group, also known as Eagle Werewolf, has expanded its cyber-espionage toolkit with a new campaign targeting private individuals and organizations in Russia. The attackers use a fake app that mimics a donation service as bait, which decrypts and launches a malicious payload in the background. The payload includes a new cyber-espionage toolkit called the Still Toolkit, which consists of two components: Still Sync and Still Audio.

Still Sync is a stealer that targets Telegram session data, allowing the attackers to log in to the victim's account and pull messages and media files through the Telegram API. It also collects system information, such as motherboard serial number and CPU ID, and sends it to the command-and-control server. Still Sync can also carry out full-scale collection of user information from the messaging app, including user details, private chats, and media files. The malware uses various mechanisms to communicate with the C2 server, including gRPC and FlatBuffers.

Still Audio is an audio surveillance implant that analyzes the incoming audio stream and starts recording voice when certain conditions are met. It uses the same mechanisms as Still Sync to communicate with the C2 server and can create a service to run in the background. The attackers can use the Dead Drop Resolver technique as a fallback mechanism to obtain the C2 address if the current server is unreachable. The Still Toolkit is a significant expansion of Armored Likho's arsenal, and Kaspersky products detect this threat as Trojan.Win64.Agent.* and HEUR:Backdoor.Win32.Generic. The campaign shows significant overlap with previous Armored Likho campaigns, but the new toolkit points to the attackers expanding their capabilities.

---

> *Take things as they are. Punch when you have to punch. Kick when you have to kick.
Author: Bruce Lee*

Source: [Armored Likho expands its cyber-espionage toolkit](https://securelist.com/armored-likho-still-toolkit/121033/)
