---
title: "Cloudflare Workers Spectre Attack Leaks JWT From Co-Located Worker at 12 Bits/Second"
description: "Researchers demonstrated a remote Spectre attack on Cloudflare Workers that extracted a JSON Web Token (JWT) from a co\u2011located worker in production. T..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/08/cloudflare-workers-spectre-attack-leaks.html"
published: "2026-08-19T19:02:40+00:00"
ingested_at: "2026-08-20T00:59:57.977444+00:00"
date: "2026-08-20T00:59:57.977444+00:00"
category: "threat-intel"
tags:
  - "Spectre"
  - "Cloudflare Workers"
  - "JWT"
  - "remote attack"
  - "information leakage"
slug: "2026-08-20-cloudflare-workers-spectre-attack-leaks-jwt-from-co-located"
quote: "He that is giddy thinks the world turns round."
quote_author: "William Shakespeare"
---

### Executive Summary
Researchers demonstrated a remote Spectre attack on Cloudflare Workers that extracted a JSON Web Token (JWT) from a co‑located worker in production. The leak rate reached 12 bits per second, 360× faster than the 2021 proof‑of‑concept. The experiment used attacker and victim workers controlled by the researchers.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-08-19T19:02:40+00:00
- **Category:** threat-intel

**Original Description:**
Cybersecurity researchers have disclosed details of a&nbsp;remote Spectre attack&nbsp;against Cloudflare Workers that leaked a JSON Web Token (JWT) from a co-located Worker in the production environment at up to 12 bits per second, 360 times the rate of an earlier attack demonstrated in 2021. The end-to-end experiment used an attacker Worker and a victim Worker controlled by the researchers,
