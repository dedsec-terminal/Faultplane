---
title: "Blind Trust: Stealing Credentials Through CSP"
description: "PortSwigger Research details how a misconfigured Content Security Policy (CSP) that allow\u2011lists a domain can be abused to steal user credentials. By i..."
source: "PortSwigger Research"
source_url: "https://portswigger.net/research/blind-trust-stealing-credentials-through-csp"
published: "2026-11-11T14:26:01+00:00"
ingested_at: "2026-11-12T05:36:16.677251+00:00"
date: "2026-11-12T05:36:16.677251+00:00"
category: "research"
tags:
  - "CSP"
  - "credential theft"
  - "XSS"
  - "web security"
  - "PortSwigger"
slug: "2026-11-12-blind-trust-stealing-credentials-through-csp"
quote: "Some people are always grumbling because roses have thorns; I am thankful that thorns have roses."
quote_author: "Alphonse Karr"
---

### Executive Summary
PortSwigger Research details how a misconfigured Content Security Policy (CSP) that allow‑lists a domain can be abused to steal user credentials. By injecting malicious HTML that targets the allowed domain, attackers can bypass CSP’s XSS protection, capture login data, and exfiltrate it. The paper outlines the attack flow, real‑world examples, and recommends tightening CSP directives and validating third‑party domains.

---
**Intelligence Metadata**
- **Source Publisher:** PortSwigger Research
- **Published Date:** 2026-11-11T14:26:01+00:00
- **Category:** research

**Original Description:**
Content Security Policy is supposed to be the safety net that stops an HTML injection from turning into XSS. Usually it works. But sometimes it doesn't, because the policy allows-lists a domain that h
