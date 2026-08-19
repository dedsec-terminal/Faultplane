---
title: "CRLF-Powered Desync Attacks: Beheading HTTP Streams"
description: "The paper demonstrates that CRLF injection can cause HTTP header desynchronization, enabling attackers to truncate or manipulate HTTP responses. By in..."
source: "PortSwigger Research"
source_url: "https://portswigger.net/research/crlf-powered-desync-attacks"
date: "2026-08-05T23:30:00+00:00"
category: "research"
tags:
  - "CRLF"
  - "HTTP Header Injection"
  - "Desync Attacks"
  - "Web Security"
  - "PortSwigger"
slug: "2026-08-05-crlf-powered-desync-attacks-beheading-http-streams"
quote: "Every day may not be good, but there's something good in every day."
quote_author: "Unknown"
---

### Executive Summary
The paper demonstrates that CRLF injection can cause HTTP header desynchronization, enabling attackers to truncate or manipulate HTTP responses. By injecting CRLF sequences, an attacker can behead a response stream, causing browsers to ignore content after the injection point. The study highlights the severity of header injection beyond typical XSS or open redirect risks, and outlines mitigation strategies such as strict header validation and output encoding.

---
**Intelligence Metadata**
- **Source Publisher:** PortSwigger Research
- **Published Date:** 2026-08-05T23:30:00+00:00
- **Category:** research
