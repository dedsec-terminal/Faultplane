---
title: "Unpatched Cacti Zero-Day Enables RCE in Four HTTP Requests via Guest Access"
description: "A new zero\u2011day vulnerability in the open\u2011source network monitoring tool Cacti allows attackers to achieve remote code execution with just four unauthe..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/11/unpatched-cacti-zero-day-enables-rce-in.html"
published: "2026-11-27T05:48:20+00:00"
ingested_at: "2026-11-27T06:29:57.068768+00:00"
date: "2026-11-27T06:29:57.068768+00:00"
category: "threat-intel"
tags:
  - "Cacti"
  - "zero-day"
  - "RCE"
  - "guest access"
  - "4HTTP2SHELL"
  - "4HTTP2ROOT"
slug: "2026-11-27-unpatched-cacti-zero-day-enables-rce-in-four-http-requests-v"
quote: "You can't let praise or criticism get to you. It's a weakness to get caught up in either one."
quote_author: "John Wooden"
---

### Executive Summary
A new zero‑day vulnerability in the open‑source network monitoring tool Cacti allows attackers to achieve remote code execution with just four unauthenticated HTTP requests. The proof‑of‑concept, dubbed 4HTTP2SHELL and 4HTTP2ROOT, demonstrates a path from a fresh guest session to command execution on the Cacti server. No CVE has been assigned yet.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-11-27T05:48:20+00:00
- **Category:** threat-intel

**Original Description:**
Details have emerged about a new zero-day vulnerability in Cacti, an open-source network monitoring tool, that could be exploited to achieve remote code execution. The proof-of-concept (PoC) exploit, which has yet to be assigned a CVE identifier, has been tracked as 4HTTP2SHELL and 4HTTP2ROOT. "I found a path from a fresh, unauthenticated HTTP session to command execution as the Cacti server
