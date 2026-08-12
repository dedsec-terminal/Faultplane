---
title: "Sandworm-Linked UAC-0145 Uses Fake Job Interviews to Push VPN That Can Run Commands"
date: 2026-08-11T18:36:47+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are 3 concise paragraphs summarizing the article:

The Computer Emergency Response Team of Ukraine (CERT-UA) has revealed a new social engineering campaign by Russian nation-state threat actors, specifically the UAC-0145 subgroup within the Sandworm hacking group. The campaign targets IT workers in Ukraine by masquerading as recruiters, using fake job interviews to trick victims into installing malware. The attackers contact potential victims on job search websites, then shift the conversation to messaging apps like Telegram, where they pose as HR managers from legitimate companies.

The attackers invite victims to a Zoom videoconference call, followed by a technical interview that requires connecting to a corporate VPN using WireGuard. However, the provided configuration files contain errors, prompting the attackers to recommend downloading a custom VPN solution called SopraVPN. This VPN client is actually a modified version of WireGuard that allows the attackers to run arbitrary commands on the victim's host without their knowledge. The poisoned VPN client can also download secondary payloads from remote URLs.

CERT-UA is warning IT professionals to be cautious of social engineering techniques and urging organizations to take protective measures, such as allowing access to corporate resources only from managed devices with security software installed. This campaign is part of a growing trend of fake recruitment campaigns used by nation-state threat actors, including Russian, Chinese, Iranian, and North Korean adversaries, to gain unauthorized access to targeted systems. The agency is recommending continuous monitoring and enforcement of security policies to stay protected against potential malware attacks.

---

> *Our doubts are traitors and make us lose the good we often might win, by fearing to attempt.
Author: Jane Addams*

Source: [Sandworm-Linked UAC-0145 Uses Fake Job Interviews to Push VPN That Can Run Commands](https://thehackernews.com/2026/08/sandworm-linked-uac-0145-uses-fake-job.html)
