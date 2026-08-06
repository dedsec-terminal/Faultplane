---
title: "Paperclip AI Flaws Let Attackers Run Host Commands via Malicious Agent Imports"
date: 2026-08-05T15:14:05+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the security flaws in Paperclip AI:

Paperclip, an open-source control plane for AI agents, has been found to have two severe security flaws that allow attackers to execute commands on a network server or a developer's computer. The first flaw, tracked as CVE-2026-41679, can be exploited by importing a malicious agent and starting it, with no pre-existing account or victim interaction required. The second flaw, tracked as GHSA-x8hx-rhr2-9rf7, requires a user to open an attacker-controlled page while Paperclip is running in its default local_trusted mode.

The vulnerabilities arise from Paperclip's agent configuration becoming executable behavior, allowing unauthorized users or browser-originated requests to introduce and activate malicious configuration. The server-side chain applies to network-accessible authenticated deployments, while the localhost chain applies when a user opens an attacker-controlled page while Paperclip is running in its default local_trusted configuration. A third flaw, tracked as GHSA-xfqj-r5qw-8g4j, exposes sensitive data and control-plane details through API routes that did not enforce access checks.

To mitigate these flaws, operators should update to Paperclip version v2026.416.0 or later, which contains the import-authorization fix and hostname-validation guard. Rapid7 has published a Metasploit module for CVE-2026-41679, and CISA's Stakeholder-Specific Vulnerability Categorization (SSVC) enrichment marks the flaw as automatable with proof-of-concept exploitation. While there is no reported exploitation in the wild as of August 5, 2026, operators should review their registration and deployment exposure configurations to ensure they are secure.

---

> *I am not afraid of tomorrow, for I have seen yesterday and I love today.
Author: William White*

Source: [Paperclip AI Flaws Let Attackers Run Host Commands via Malicious Agent Imports](https://thehackernews.com/2026/08/paperclip-ai-flaws-let-attackers-run.html)
