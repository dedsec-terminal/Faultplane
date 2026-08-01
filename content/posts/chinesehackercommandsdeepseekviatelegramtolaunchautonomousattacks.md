---
title: "Chinese Hacker Commands DeepSeek via Telegram to Launch Autonomous Attacks"
date: 2026-07-31T11:21:27+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

A Chinese-speaking threat actor, tracked through the aliases "knaithe" and "KnYuan", has been using a framework called Hermes Agent to launch autonomous attacks. The actor uses DeepSeek, a reasoning model, to select public exploits and target internet-facing systems. The attacks are initiated through Telegram instructions, after which the agent operates autonomously, selecting vulnerabilities and exploiting them without further operator input.

The attacks targeted over 460 systems, using seven exploit tracks spanning eight Common Vulnerabilities and Exposures (CVE) identifiers. The actor attempted to exploit vulnerabilities in Langflow, n8n, and Marimo systems, but was unsuccessful due to configuration requirements not being met. However, the actor was able to exfiltrate data from three organizations using the NetScaler memory-overread flaw CVE-2026-3055 and execute commands on 11 Marimo instances using CVE-2026-39987. Despite this, only three targets were confirmed to have been successfully exploited.

The Hermes Agent framework, which includes DeepSeek, was found to be operating through Telegram and was capable of running commands and scheduling unattended tasks. The framework's documentation confirms its ability to operate autonomously. The actor's use of DeepSeek and Hermes Agent demonstrates a high level of sophistication and automation in their attacks. Organizations are advised to patch exposed systems, remove unnecessary public access to workflow and notebook interfaces, and update their systems to prevent similar attacks. The actor is assessed to be based in Zhuhai, China, although their legal identity and any state connection remain unclear.

---

> *He who obtains has little. He who scatters has much.
Author: Lao Tzu*

Source: [Chinese Hacker Commands DeepSeek via Telegram to Launch Autonomous Attacks](https://thehackernews.com/2026/07/chinese-hacker-commands-deepseek-via.html)
