---
title: "Smashing the token limit with overlapping fragments"
description: "PortSwigger researcher demonstrates how overlapping fragments can bypass token size limits, enabling exfiltration of larger tokens than previously pos..."
source: "PortSwigger Research"
source_url: "https://portswigger.net/research/smashing-the-token-limit"
published: "2026-10-05T15:04:55+00:00"
ingested_at: "2026-10-06T04:38:28.663314+00:00"
date: "2026-10-06T04:38:28.663314+00:00"
category: "research"
tags:
  - "token exfiltration"
  - "DOM Invader"
  - "PortSwigger"
  - "web security"
  - "research"
slug: "2026-10-06-smashing-the-token-limit-with-overlapping-fragments"
quote: "Some people are always grumbling because roses have thorns; I am thankful that thorns have roses."
quote_author: "Alphonse Karr"
---

### Executive Summary
PortSwigger researcher demonstrates how overlapping fragments can bypass token size limits, enabling exfiltration of larger tokens than previously possible. The technique, showcased with DOM Invader, highlights a new method for covert data extraction in web applications.

---
**Intelligence Metadata**
- **Source Publisher:** PortSwigger Research
- **Published Date:** 2026-10-05T15:04:55+00:00
- **Category:** research

**Original Description:**
I'm delighted to introduce Alex, my fellow swigger who I've collaborated with in the past with tools like DOM Invader. He showed me that it's possible to exfiltrate larger tokens than demonstrated in
