---
title: "Critical OpenWrt DHCPv6 Flaw Could Let Unauthenticated Attackers Run Code as Root"
date: 2026-07-28T12:56:14+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the critical OpenWrt DHCPv6 flaw:

A critical vulnerability has been discovered in OpenWrt's DHCPv6 stack, allowing an unauthenticated attacker to run code as root. The issue, tracked as CVE-2026-53921, is a stack overflow vulnerability in the odhcpd service, which runs as root. An attacker can exploit this vulnerability by sending a crafted DHCPv6 REQUEST to the server, potentially gaining control of the router. OpenWrt has released version 24.10.8 to address this issue, and users are advised to update their firmware as soon as possible.

The vulnerability is considered critical, with a CVSS score of 9.8, and can be exploited by an attacker with network access to the DHCPv6 service. The issue is particularly concerning because embedded hardware often lacks security features such as stack canaries and address space layout randomization (ASLR), making code execution a realistic outcome. OpenWrt has also identified other vulnerabilities in its network services, including command-injection, path-traversal, and cross-site scripting (XSS) weaknesses in optional LuCI components. These issues are being addressed in separate updates.

The discovery of these vulnerabilities was aided by an AI-assisted audit conducted by Hacker House, which used a four-stage inference-fuzzing process to identify potential vulnerabilities. The audit identified several issues, including pre-authentication paths to device compromise, which have been addressed in OpenWrt's updates. OpenWrt has also used AI in its own patch review process to help identify and address vulnerabilities. The project recommends that users migrate to the 25.12 series before the end of life of the 24.10 series, which is projected for September 2026. Users are advised to keep their firmware up to date to protect against potential exploits.

---

> *The greatest good you can do for another is not just to share your riches but to reveal to him his own.
Author: Benjamin Disraeli*

Source: [Critical OpenWrt DHCPv6 Flaw Could Let Unauthenticated Attackers Run Code as Root](https://thehackernews.com/2026/07/critical-openwrt-dhcpv6-flaw-could-let.html)
