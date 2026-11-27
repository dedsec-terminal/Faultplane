---
title: 'HTTP/1.1 must die: the desync endgame'
description: The paper argues that HTTP/1.1’s lack of clear request boundaries creates
  a fundamental protocol flaw that enables request‑smuggling attacks. The auth...
source: PortSwigger Research
source_url: https://portswigger.net/research/http1-must-die
published: '2025-08-06T22:20:00+00:00'
ingested_at: '2026-11-27T19:47:03.184902+00:00'
date: '2026-11-27T19:47:03.184902+00:00'
category: research
tags:
- HTTP
- request smuggling
- web security
slug: 2026-11-27-http-1-1-must-die-the-desync-endgame
quote: Great indeed is the sublimity of the Creative, to which all beings owe their
  beginning and which permeates all heaven.
quote_author: Lao Tzu
---

### Executive Summary

The paper argues that HTTP/1.1’s lack of clear request boundaries creates a fundamental protocol flaw that enables request‑smuggling attacks. The author demonstrates several new desync techniques that, according to the report, have compromised tens of millions of sites behind Akamai, Cloudflare, and Netlify, and claims to have earned over $200,000 in bug‑bounty rewards in a two‑week period. While the author reports that many of these vulnerabilities have been patched, the article maintains that sites remain vulnerable to future variants because patching individual implementations does not eliminate the underlying flaw. Defensive guidance offered includes moving to HTTP/2 for upstream connections, avoiding downgrades from HTTP/2 to HTTP/1.1, and employing systematic detection of parser discrepancies to mitigate desync attacks.

### Original Overview

Upstream HTTP/1.1 is inherently insecure and regularly exposes millions of websites to hostile takeover. Six years of attempted mitigations have hidden the issue, but failed to fix it. This paper introduces several novel classes of HTTP desync attack capable of mass compromise of user credentials. These techniques are demonstrated through detailed case studies, including critical vulnerabilities which exposed tens of millions of websites by subverting core infrastructure within Akamai, Cloudflare, and Netlify. I also introduce an open-source toolkit that enables systematic detection of parser discrepancies and target-specific weak spots. Combined, this toolkit and these techniques yielded over $200,000 in bug bounties in a two-week period. Ultimately, I argue that HTTP request...
