---
title: "1Password's AI patching benchmark is misleading"
description: "1Password\u2019s August\u202f2026 report claimed AI models produced clean fixes only 26% of the time, but the figure is misleading. The benchmark included trial..."
source: "Trail of Bits"
source_url: "https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/"
published: "2026-09-15T11:00:00+00:00"
ingested_at: "2026-09-16T03:08:02.113249+00:00"
date: "2026-09-16T03:08:02.113249+00:00"
category: "research"
tags:
  - "AI patching"
  - "benchmark"
  - "misleading"
  - "vulnerability patching"
  - "Trail of Bits"
slug: "2026-09-16-1password-s-ai-patching-benchmark-is-misleading"
quote: "I am a man of fixed and unbending principles, the first of which is to be flexible at all times."
quote_author: "Everett Dirksen"
---

### Executive Summary
1Password’s August 2026 report claimed AI models produced clean fixes only 26% of the time, but the figure is misleading. The benchmark included trials where agents were told to apply wrong fixes, experiments that prohibited testing, and a sample of six difficult bugs. Reanalysis of trials where agents could run code and were not misdirected shows 86% of patches blocked the exploit. The headline may discourage defenders from using AI patching, while Trail of Bits released two agent skills—post‑patch‑validation and review‑walkthrough—to improve patch quality.

---
**Intelligence Metadata**
- **Source Publisher:** Trail of Bits
- **Published Date:** 2026-09-15T11:00:00+00:00
- **Category:** research

**Original Description:**
1Password’s FLAWED report, published on August 6, 2026, gives defenders a misleading picture of AI patching. Its headline says models produced clean fixes only 26% of the time. That figure includes experiments that deliberately instructed agents to apply the wrong fix, along with experiments in which agents could not compile or test their patches. The report risks making defenders less effective by discouraging them from using technology that could help them fix more vulnerabilities. Teams th...
