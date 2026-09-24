---
title: "MikroTrick Chain Let Attackers Take Over MikroTik Routers Without a Password or SSH Key"
description: "Two RouterOS SSH vulnerabilities (CVE\u20112026\u201167279 and CVE\u20112026\u201186060) can be chained to give attackers full administrative control of MikroTik routers ..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/09/mikrotrick-chain-let-attackers-take.html"
published: "2026-09-23T16:06:41+00:00"
ingested_at: "2026-09-24T02:56:39.259855+00:00"
date: "2026-09-24T02:56:39.259855+00:00"
category: "threat-intel"
tags:
  - "MikroTik"
  - "RouterOS"
  - "SSH"
  - "CVE-2026-67279"
  - "CVE-2026-86060"
  - "MikroTrick"
  - "vulnerability chain"
slug: "2026-09-24-mikrotrick-chain-let-attackers-take-over-mikrotik-routers-wi"
quote: "An optimist is a person who sees a green light everywhere, while the pessimist sees only the red spotlight... The truly wise person is colour-blind."
quote_author: "Albert Schweitzer"
---

### Executive Summary
Two RouterOS SSH vulnerabilities (CVE‑2026‑67279 and CVE‑2026‑86060) can be chained to give attackers full administrative control of MikroTik routers that are exposed to the Internet, even when no password or SSH key is set. CERT Polska calls the exploit MikroTrick. The first flaw is an SSH state‑machine bug; the second is an argument‑injection bug in the login process.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-09-23T16:06:41+00:00
- **Category:** threat-intel

**Original Description:**
Two MikroTik RouterOS SSH vulnerabilities chained together let attackers take full administrative control of Internet-exposed routers without a password, SSH key, or completed authentication. The chain, which CERT Polska calls MikroTrick, combines an SSH state-machine flaw (CVE-2026-67279) with an argument-injection bug in the RouterOS login process (CVE-2026-86060). Attack logs date to at
