---
title: "New Spectre-v2 BTR Attack Leaks Linux Memory Despite Existing Defenses"
description: "A new Spectre\u2011v2 variant, dubbed Branch Target Reuse (BTR), has been disclosed by researchers from VUSec and Scuola Superiore Sant'Anna. The flaw targ..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/09/new-spectre-v2-btr-attack-leaks-linux.html"
published: "2026-09-29T17:20:17+00:00"
ingested_at: "2026-09-30T03:46:33.086464+00:00"
date: "2026-09-30T03:46:33.086464+00:00"
category: "threat-intel"
tags:
  - "Spectre"
  - "CPU vulnerability"
  - "JIT"
  - "Linux"
  - "BTR"
slug: "2026-09-30-new-spectre-v2-btr-attack-leaks-linux-memory-despite-existin"
quote: "When you arise in the morning, think of what a precious privilege it is to be alive \ufffd to breathe, to think, to enjoy, to love."
quote_author: "Marcus Aurelius"
---

### Executive Summary
A new Spectre‑v2 variant, dubbed Branch Target Reuse (BTR), has been disclosed by researchers from VUSec and Scuola Superiore Sant'Anna. The flaw targets Just‑In‑Time (JIT) engines in web browsers, language runtimes, and the Linux kernel, enabling attackers to leak kernel memory even when standard mitigations are in place. The vulnerability is effective across multiple CPU vendors and demonstrates that current defenses are insufficient against this new branch‑target reuse technique.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-09-29T17:20:17+00:00
- **Category:** threat-intel

**Original Description:**
A group of academics from VUSec and Scuola Superiore Sant'Anna have disclosed details of a new Spectre CPU vulnerability variant that affects Just-In-Time (JIT) engines present in web browsers, language runtimes, and the operating system kernel, across multiple CPU vendors. The new Spectre-v2 variant has been codenamed Branch Target Reuse (BTR). "The key insight is that, while modern CPUs
