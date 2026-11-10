---
title: "Hackers Compromise Ethersphere's bee-js and Swarm Desktop to Deliver Wallet-Stealing Malware"
description: "Attackers hijacked Ethersphere\u2019s automated release pipeline to publish malicious bee\u2011js 13.3.0 and Swarm Desktop 0.56.2 binaries. The compromised rele..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/11/hackers-compromise-etherspheres-bee-js.html"
published: "2026-11-09T17:36:28+00:00"
ingested_at: "2026-11-10T05:47:23.209991+00:00"
date: "2026-11-10T05:47:23.209991+00:00"
category: "threat-intel"
tags:
  - "Ethersphere"
  - "bee-js"
  - "Swarm Desktop"
  - "wallet theft"
  - "backdoor"
  - "malware"
  - "release automation"
  - "decentralized storage"
slug: "2026-11-10-hackers-compromise-ethersphere-s-bee-js-and-swarm-desktop-to"
quote: "We must become the change we want to see."
quote_author: "Mahatma Gandhi"
---

### Executive Summary
Attackers hijacked Ethersphere’s automated release pipeline to publish malicious bee‑js 13.3.0 and Swarm Desktop 0.56.2 binaries. The compromised releases download and execute code that steals the wallet key and password stored by Swarm Desktop, and install a backdoor for persistence.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-11-09T17:36:28+00:00
- **Category:** threat-intel

**Original Description:**
Attackers used the Ethersphere project's own release automation to publish malicious versions of two of its tools for the Swarm decentralized storage network: bee-js 13.3.0 and Swarm Desktop 0.56.2. Both releases download and run code built to steal the wallet key that Swarm Desktop keeps for its node, along with the stored password that unlocks it. The code is also built to install a backdoor
