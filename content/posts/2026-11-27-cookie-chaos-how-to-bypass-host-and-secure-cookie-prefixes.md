---
title: 'Cookie Chaos: How to bypass __Host and __Secure cookie prefixes'
description: Researchers from PortSwigger demonstrated that inconsistencies between
  browser and server cookie parsing can allow attackers to bypass the security gu...
source: PortSwigger Research
source_url: https://portswigger.net/research/cookie-chaos-how-to-bypass-host-and-secure-cookie-prefixes
published: '2025-09-03T14:46:23+00:00'
ingested_at: '2026-11-27T19:47:03.181902+00:00'
date: '2026-11-27T19:47:03.181902+00:00'
category: research
tags:
- cookie security
- prefix bypass
- web application security
slug: 2026-11-27-cookie-chaos-how-to-bypass-host-and-secure-cookie-prefixes
quote: If you have knowledge, let others light their candles in it.
quote_author: Margaret Fuller
---

### Executive Summary

Researchers from PortSwigger demonstrated that inconsistencies between browser and server cookie parsing can allow attackers to bypass the security guarantees of the __Host- and __Secure- prefixes. By inserting Unicode whitespace characters (e.g., U+2000) or exploiting legacy parsing modes triggered by a $Version=1 header, an attacker can cause a server to normalize a cookie name to a protected prefix while the browser treats it as an ordinary cookie. The effect is that the attacker can set high‑privilege cookies from subdomains or insecure origins, potentially leading to session fixation, CSRF, or reflected XSS when the cookie value is reflected without proper escaping. The research notes that frameworks such as Django, ASP.NET, Apache Tomcat, and Jetty apply trimming or legacy parsing that enable this attack, while Safari’s stricter handling mitigates it. Defensive guidance implied by the findings includes avoiding whitespace trimming of cookie names, disabling legacy parsing modes, and ensuring consistent server‑side decoding of cookie headers.

### Original Overview

Browsers added cookie prefixes to protect your sessions and stop attackers from setting harmful cookies. In this post, you’ll see how to bypass cookie defenses using discrepancies in browser and server logic. For a visual walk‑through, see the SteelCon livestream recording: Cookie prefixes were introduced in RFC 6265bis to strengthen cookie security through naming rules: A cookie with the __Host- prefix must be host-only, meaning it cannot be shared across subdomains A cookie with the __Secure- prefix must be set from a secure origin. These restrictions are enforced by browsers to prevent attacks like cookie tossing or session fixation. However, inconsistencies in how browsers and servers handle cookie encoding and parsing can introduce subtle but dangerous flaws. According to the...
