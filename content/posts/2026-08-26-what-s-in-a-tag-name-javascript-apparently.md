---
title: "What's in a tag name? JavaScript, apparently"
description: "The article investigates the syntax rules governing tag names in HTML and JavaScript. It confirms that tag names must start with a letter (a\u2011z or A\u2011Z)..."
source: "PortSwigger Research"
source_url: "https://portswigger.net/research/whats-in-a-tag-name-javascript-apparently"
published: "2026-08-25T14:24:32+00:00"
ingested_at: "2026-08-26T01:07:22.248865+00:00"
date: "2026-08-26T01:07:22.248865+00:00"
category: "research"
tags:
  - "html"
  - "tag-names"
  - "javascript"
  - "web-security"
slug: "2026-08-26-what-s-in-a-tag-name-javascript-apparently"
quote: "He who knows himself is enlightened."
quote_author: "Lao Tzu"
---

### Executive Summary
The article investigates the syntax rules governing tag names in HTML and JavaScript. It confirms that tag names must start with a letter (a‑z or A‑Z) and may subsequently contain letters, digits, hyphens, underscores, colons, and periods. It explains how browsers parse these names, the restrictions that prevent spaces or other special characters, and the implications for custom elements and potential security considerations.

---
**Intelligence Metadata**
- **Source Publisher:** PortSwigger Research
- **Published Date:** 2026-08-25T14:24:32+00:00
- **Category:** research

**Original Description:**
I was on my laptop, as I often am when there's rubbish on telly, and found myself wondering what characters are allowed in a tag. I knew they had to begin with "a-zA-Z", but what about after that? I t
