---
title: "New CSS Attacks Can Break Webmail Defenses to Steal Passwords and Tokens"
date: 2026-08-08T08:03:57+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Researchers have discovered new CSS attacks that can break webmail defenses, allowing hackers to steal passwords and tokens from popular email services such as Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail, and AOL Mail. These attacks can capture passwords, take over third-party accounts, leak tokens, hijack trusted UI actions, and manipulate AI tools that read email. The techniques involve exploiting vulnerabilities in the way webmail services handle HTML and CSS, allowing attackers to escape the message boundary and interfere with the webmail interface.

The research, presented by Gareth Heyes at Black Hat USA 2026, demonstrates various attack chains that can be used to exploit these vulnerabilities. For example, an Outlook/Firefox chain can spoof a Microsoft sign-in screen and capture the password a recipient types, while a Yahoo/AOL paste race can expose a Medium email-login token and let an attacker sign in as the victim. The research also introduces a click-based exfiltration technique that can be used to steal tokens even when Content Security Policy (CSP) blocks external resources.

To defend against these attacks, the researcher recommends that webmail providers isolate HTML email in sandboxed iframes and tightly restrict CSS, custom attributes, select menus, and image requests. The research highlights the importance of strict isolation, character allow lists for CSS validation, and checks for CSS gadgets before allowing custom attributes. The accompanying public repository contains proof-of-concept (PoC) code for the disclosed techniques, and the researcher notes that some of the vulnerabilities have already been fixed by the affected webmail services, while others remain unpatched.

---

> *Self-complacency is fatal to progress.
Author: Margaret Sangster*

Source: [New CSS Attacks Can Break Webmail Defenses to Steal Passwords and Tokens](https://thehackernews.com/2026/08/new-css-attacks-can-break-webmail.html)
