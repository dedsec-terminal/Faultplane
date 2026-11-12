---
title: "Critical Apache HTTP/2 Flaw Could Let Unauthenticated Attackers Execute Code Remotely"
description: "A critical vulnerability (CVE\u20112026\u2011119618) in Apache HTTP Server\u2019s HTTP/2 module (mod_http2) allows unauthenticated remote attackers to execute arbitr..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/11/critical-apache-http2-flaw-could-let.html"
published: "2026-11-12T05:12:26+00:00"
ingested_at: "2026-11-12T05:34:50.996346+00:00"
date: "2026-11-12T05:34:50.996346+00:00"
category: "cves"
tags:
  - "Apache"
  - "HTTP/2"
  - "CVE-2026-119618"
  - "remote code execution"
  - "Red Hat Enterprise Linux"
  - "mod_http2"
slug: "2026-11-12-critical-apache-http-2-flaw-could-let-unauthenticated-attack"
quote: "We must embrace pain and burn it as fuel for our journey."
quote_author: "Kenji Miyazawa"
---

### Executive Summary
A critical vulnerability (CVE‑2026‑119618) in Apache HTTP Server’s HTTP/2 module (mod_http2) allows unauthenticated remote attackers to execute arbitrary code on affected servers. The flaw impacts versions 2.4.55 through 2.4.70 and is fixed in 2.4.71. Only servers with HTTP/2 enabled are vulnerable, including Red Hat Enterprise Linux distributions.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-11-12T05:12:26+00:00
- **Category:** cves

**Original Description:**
A critical flaw in Apache HTTP Server's HTTP/2 module, mod_http2, can let a remote attacker run code on the server. Tracked as CVE-2026-119618, it affects versions 2.4.55 through 2.4.70 and is fixed in version 2.4.71, released yesterday. Only servers with HTTP/2 enabled are affected, according to Red Hat, which ships the server as part of Red Hat Enterprise Linux. An attacker who can reach the
