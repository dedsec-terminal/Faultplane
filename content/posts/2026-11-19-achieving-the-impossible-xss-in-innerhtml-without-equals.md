---
title: "Achieving the impossible: XSS in innerHTML without equals"
description: "PortSwigger Research presents a guest lecture by Masato Kinugawa, a renowned web security expert. The talk focuses on a novel cross\u2011site scripting (XS..."
source: "PortSwigger Research"
source_url: "https://portswigger.net/research/achieving-the-impossible-xss-in-innerhtml-without-equals"
published: "2026-11-18T14:39:45+00:00"
ingested_at: "2026-11-19T05:45:31.975567+00:00"
date: "2026-11-19T05:45:31.975567+00:00"
category: "research"
tags:
  - "XSS"
  - "innerHTML"
  - "web security"
  - "PortSwigger"
  - "research"
slug: "2026-11-19-achieving-the-impossible-xss-in-innerhtml-without-equals"
quote: "To give hope to someone occurs when you teach them how to use the tools to do it for themselves."
quote_author: "Byron Pulsifer"
---

### Executive Summary
PortSwigger Research presents a guest lecture by Masato Kinugawa, a renowned web security expert. The talk focuses on a novel cross‑site scripting (XSS) technique that exploits the innerHTML property without using the equals operator, demonstrating how seemingly innocuous assignments can lead to code execution. Kinugawa explains the underlying vulnerability, its impact on modern browsers, and mitigation strategies for developers.

---
**Intelligence Metadata**
- **Source Publisher:** PortSwigger Research
- **Published Date:** 2026-11-18T14:39:45+00:00
- **Category:** research

**Original Description:**
Introduction I'm delighted to introduce Masato Kinugawa as a guest web security researcher on the PortSwigger research channel. Masato is a well known web security expert who has found countless high
