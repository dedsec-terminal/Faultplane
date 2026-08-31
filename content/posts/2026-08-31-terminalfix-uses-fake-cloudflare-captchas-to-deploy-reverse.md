---
title: "TerminalFix Uses Fake Cloudflare CAPTCHAs to Deploy Reverse-Tunnel Backdoor"
description: "Microsoft disclosed a new ClickFix variant, TerminalFix, that tricks users into running a malicious command in Windows Terminal or PowerShell. It uses..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/08/terminalfix-uses-fake-cloudflare.html"
published: "2026-08-30T07:36:33+00:00"
ingested_at: "2026-08-31T03:18:20.902301+00:00"
date: "2026-08-31T03:18:20.902301+00:00"
category: "threat-intel"
tags:
  - "TerminalFix"
  - "ClickFix"
  - "Cloudflare CAPTCHA"
  - "reverse-tunnel"
  - "backdoor"
  - "Windows Terminal"
  - "PowerShell"
slug: "2026-08-31-terminalfix-uses-fake-cloudflare-captchas-to-deploy-reverse"
quote: "He who knows, does not speak. He who speaks, does not know."
quote_author: "Lao Tzu"
---

### Executive Summary
Microsoft disclosed a new ClickFix variant, TerminalFix, that tricks users into running a malicious command in Windows Terminal or PowerShell. It uses fake Cloudflare CAPTCHAs to lure victims, then deploys a reverse‑tunnel backdoor, expanding the attack surface and enabling remote control.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-08-30T07:36:33+00:00
- **Category:** threat-intel

**Original Description:**
Microsoft has disclosed details of a new ClickFix variant, dubbed TerminalFix, that aims to trick users into running a malicious command in Windows Terminal or PowerShell. "While traditional ClickFix campaigns direct victims to the Windows Run dialog, TerminalFix campaigns apply the same technique but direct users to Windows Terminal or PowerShell instead, increasing the likelihood that complex
