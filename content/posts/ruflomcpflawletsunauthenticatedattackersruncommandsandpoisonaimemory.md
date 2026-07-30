---
title: "Ruflo MCP Flaw Lets Unauthenticated Attackers Run Commands and Poison AI Memory"
date: 2026-07-29T15:39:30+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here is a summary of the article in 3 concise paragraphs:

A critical security flaw, codenamed RufRoot, has been discovered in Ruflo, an open-source AI multi-agent orchestration platform. The vulnerability, tracked as CVE-2026-59726, allows unauthenticated remote code execution and affects all versions of the project before version 3.16.3. This means that an attacker can run commands and poison the AI memory without needing any authentication, potentially leading to a full compromise of the system.

The vulnerability is caused by Ruflo's exposure of 233 tools, including shell command execution and database operations, through an unauthenticated Model Context Protocol (MCP) bridge that is open to the network by default. An attacker can exploit this by sending a single unauthenticated HTTP POST request to port 3001, allowing them to gain full remote code execution inside the susceptible Ruflo deployment. This can lead to the theft of API keys, conversation harvesting, and interference with the AI system's memory, enabling the attacker to influence model responses and behavior.

A fix for the vulnerability was pushed by the project's maintainer within 24 hours of responsible disclosure. The patch includes changes to bind the MCP bridge to the loopback interface by default, gate "terminal_execute" behind server-side controls, and enable MongoDB authentication. Operators running an exposed instance are recommended to take immediate action, including closing firewall ports, rotating API keys, and auditing the AgentDB pattern store for injected entries. Remediation requires more than just a software update, as AI provider credentials should be treated as compromised and rotated, and the platform's AI memory should be audited for tampering.

---

> *We are the leaves of one branch, the drops of one sea, the flowers of one garden.
Author: Jean Lacordaire*

Source: [Ruflo MCP Flaw Lets Unauthenticated Attackers Run Commands and Poison AI Memory](https://thehackernews.com/2026/07/ruflo-mcp-flaw-lets-unauthenticated.html)
