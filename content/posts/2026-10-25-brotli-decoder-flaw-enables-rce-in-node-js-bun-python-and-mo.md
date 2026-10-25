---
title: "Brotli Decoder Flaw Enables RCE in Node.js, Bun, Python, and More"
description: "A memory\u2011corruption bug in Google's Brotli decoder (CVE\u20112026\u2011111497) lets attackers craft compressed data that overflows a buffer, corrupting memory a..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/10/brotli-decoder-flaw-behind-nodejs-rce.html"
published: "2026-10-24T11:09:29+00:00"
ingested_at: "2026-10-25T02:59:52.422066+00:00"
date: "2026-10-25T02:59:52.422066+00:00"
category: "threat-intel"
tags:
  - "Brotli"
  - "memory corruption"
  - "CVE-2026-111497"
  - "Node.js"
  - "Python"
  - "Bun"
  - "Envoy"
  - "RCE"
slug: "2026-10-25-brotli-decoder-flaw-enables-rce-in-node-js-bun-python-and-mo"
quote: "Better than a thousand hollow words, is one word that brings peace."
quote_author: "Buddha"
---

### Executive Summary
A memory‑corruption bug in Google's Brotli decoder (CVE‑2026‑111497) lets attackers craft compressed data that overflows a buffer, corrupting memory and enabling remote code execution. The flaw is present in many Brotli‑decompressing applications, including Node.js, Bun, Python’s Brotli and brotlicffi packages, and Envoy proxies configured to decompress Brotli.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-10-24T11:09:29+00:00
- **Category:** threat-intel

**Original Description:**
A memory-corruption flaw in Google's Brotli decoder sits in many programs that unpack Brotli-compressed data, among them Bun, the Python&nbsp;Brotli&nbsp;and&nbsp;brotlicffi&nbsp;packages, and Envoy proxies set up to decompress Brotli. Tracked as&nbsp;CVE-2026-111497, the flaw allows crafted compressed data to overwrite past the end of a buffer and corrupt a program's memory, potentially
