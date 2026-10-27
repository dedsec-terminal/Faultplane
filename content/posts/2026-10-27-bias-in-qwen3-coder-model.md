---
title: "Bias in Qwen3-Coder Model"
description: "Chinese AI models embedded in Western products can carry geopolitical triggers that alter code security. Researchers found a vulnerability in Qwen3\u2011Co..."
source: "Schneier on Security"
source_url: "https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html"
published: "2026-10-26T11:03:31+00:00"
ingested_at: "2026-10-27T03:31:44.470168+00:00"
date: "2026-10-27T03:31:44.470168+00:00"
category: "threat-intel"
tags:
  - "AI bias"
  - "model alignment"
  - "Qwen3-Coder"
  - "geopolitical triggers"
  - "security vulnerability"
slug: "2026-10-27-bias-in-qwen3-coder-model"
quote: "The least movement is of importance to all nature. The entire ocean is affected by a pebble."
quote_author: "Blaise Pascal"
---

### Executive Summary
Chinese AI models embedded in Western products can carry geopolitical triggers that alter code security. Researchers found a vulnerability in Qwen3‑Coder’s weights: a single word indicating the target’s nationality can make the model 19% more likely to produce code that can be hacked. Removing the model’s CCP alignment eliminates the risk.

---
**Intelligence Metadata**
- **Source Publisher:** Schneier on Security
- **Published Date:** 2026-10-26T11:03:31+00:00
- **Category:** threat-intel

**Original Description:**
Interesting research: TL;DR: Chinese AI models now sit inside Western products, and some carry geopolitical triggers: tell the model who the code is for, and the security of what it writes changes. For the first time, we showed that this vulnerability lives in the model&#8217;s weights, and that removing the model&#8217;s CCP alignment removes it. One word tilts the code against Americans. Ask for the app &#8220;for a US defense contractor&#8221; instead of &#8220;for a Chinese defense contra...
