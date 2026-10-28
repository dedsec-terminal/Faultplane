---
title: "Fuzzers vs. AI: Comparing Fuzzilli and BigSleep on JavaScript Engines"
description: "Project Zero compared Google\u2019s fuzzing tool Fuzzilli with LLM-based BigSleep for finding bugs in Chrome\u2019s V8 engine. Over six months BigSleep uncovere..."
source: "Google Project Zero"
source_url: "https://projectzero.google/2026/10/fuzzing-v-AI.html"
published: "2026-10-27T07:00:00+00:00"
ingested_at: "2026-10-28T03:47:58.435064+00:00"
date: "2026-10-28T03:47:58.435064+00:00"
category: "research"
tags:
  - "fuzzing"
  - "LLM"
  - "vulnerabilities"
  - "JavaScript"
  - "Chrome"
slug: "2026-10-28-fuzzers-vs-ai-comparing-fuzzilli-and-bigsleep-on-javascript"
quote: "The least movement is of importance to all nature. The entire ocean is affected by a pebble."
quote_author: "Blaise Pascal"
---

### Executive Summary
Project Zero compared Google’s fuzzing tool Fuzzilli with LLM-based BigSleep for finding bugs in Chrome’s V8 engine. Over six months BigSleep uncovered 45 bugs vs. 37 by Fuzzilli, with ~25% overlap (estimated up to 60% in dedicated tests). Many vulnerabilities were unique to each approach, showing LLMs and fuzzers are complementary. The study recommends vendors use both methods to maximize pre‑release bug detection.

---
**Intelligence Metadata**
- **Source Publisher:** Google Project Zero
- **Published Date:** 2026-10-27T07:00:00+00:00
- **Category:** research

**Original Description:**
Summary Project Zero compared two automated tools used by Google to find vulnerabilities in Chrome’s JavaScript engine, V8, on a regular basis. Fuzzilli is a generative JavaScript engine fuzzer and BigSleep is an LLM-based bug finding system. In the past six months, BigSleep found more vulnerabilities than Fuzzilli (45 versus 37) with a 25% overlap in the specific bugs reported. Since this comparison methodology has a tendency to underestimate overlap, we also performed dedicated experiments ...
