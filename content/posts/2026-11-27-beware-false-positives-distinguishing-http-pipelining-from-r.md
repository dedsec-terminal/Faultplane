---
title: 'Beware false positives: distinguishing HTTP pipelining from request smuggling'
description: The article explains that many reported HTTP request smuggling findings
  are actually false positives caused by HTTP keep‑alive or pipelining, a claim...
source: PortSwigger Research
source_url: https://portswigger.net/research/how-to-distinguish-http-pipelining-from-request-smuggling
published: '2025-08-19T14:30:44+00:00'
ingested_at: '2026-11-27T19:47:03.183902+00:00'
date: '2026-11-27T19:47:03.183902+00:00'
category: research
tags:
- HTTP request smuggling
- connection reuse
- false positives
- Burp Suite
- HTTP pipelining
slug: 2026-11-27-beware-false-positives-distinguishing-http-pipelining-from-r
quote: Keep yourself to the sunshine and you cannot see the shadow.
quote_author: Helen Keller
---

### Executive Summary

The article explains that many reported HTTP request smuggling findings are actually false positives caused by HTTP keep‑alive or pipelining, a claim supported by examples from tools such as Turbo Intruder and Burp Suite. It identifies three legitimate vulnerability classes that legitimately require connection reuse—connection‑locked request smuggling, connection‑state attacks, and client‑side desync attacks—and notes that these can still be exploited for cache poisoning, header disclosure, or bypassing front‑end controls. Defensive guidance includes disabling connection reuse during testing, using Burp extensions like HTTP Hacker to observe low‑level behavior, and confirming real impact by looking for nested HTTP/1 responses in HTTP/2 traffic or evidence beyond a surprising response. The article is a research discussion rather than a report of an active exploit.

### Original Overview

Sometimes people think they've found HTTP request smuggling , when they're actually just observing HTTP keep-alive or pipelining. This is usually a false positive, but sometimes there's actually a real vulnerability there! In this post I'll explore how to tell the two apart. This post was triggered by the publication of http1mustdie.com which resulted in me getting a bunch of messages from people confused and intrigued by connection reuse. The answer is too nuanced to put into a quick reply so I'm writing it up here instead. If you see a request smuggling proof of concept that only works when you reuse connections, it's probably a false positive. Here are some common examples of connection reuse: Turbo Intruder PoCs where requestsPerConnection is greater than 1 Burp Intruder when...
