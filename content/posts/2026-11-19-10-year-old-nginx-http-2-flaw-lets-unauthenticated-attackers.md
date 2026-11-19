---
title: "10-Year-Old NGINX HTTP/2 Flaw Lets Unauthenticated Attackers Execute Code on Servers"
description: "A decade\u2011old flaw in NGINX\u2019s HTTP/2 support (CVE\u20112026\u2011123007, nicknamed \"nginx2root\") allows unauthenticated attackers to execute code on any server w..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/11/10-year-old-nginx-http2-flaw-lets.html"
published: "2026-11-18T18:31:17+00:00"
ingested_at: "2026-11-19T05:43:50.303347+00:00"
date: "2026-11-19T05:43:50.303347+00:00"
category: "vulnerabilities"
tags:
  - "nginx"
  - "http2"
  - "cve-2026-123007"
  - "code-execution"
  - "unauthenticated"
  - "open-source"
slug: "2026-11-19-10-year-old-nginx-http-2-flaw-lets-unauthenticated-attackers"
quote: "An ant on the move does more than a dozing ox"
quote_author: "Lao Tzu"
---

### Executive Summary
A decade‑old flaw in NGINX’s HTTP/2 support (CVE‑2026‑123007, nicknamed "nginx2root") allows unauthenticated attackers to execute code on any server with HTTP/2 enabled. The vulnerability has existed since NGINX 1.9.5 (released 2015) and is fixed in versions 1.31.9 and 1.30.7 released today.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-11-18T18:31:17+00:00
- **Category:** vulnerabilities

**Original Description:**
A flaw in NGINX's HTTP/2 support can allow an attacker to run code on servers with HTTP/2 enabled, without needing to log in. The decade-old flaw, CVE-2026-123007, dubbed "nginx2root," has been present in NGINX's open-source code since version 1.9.5, released on September 22, 2015. Fixed versions 1.31.9 and 1.30.7 came out today. F5, the company behind NGINX, says attackers can run code where
