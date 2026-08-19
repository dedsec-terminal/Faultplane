---
title: "On the Effectiveness of Mutational Grammar Fuzzing"
description: "Mutational grammar fuzzing uses a predefined grammar to mutate inputs while preserving syntactic structure. In coverage\u2011guided mode, new samples that ..."
source: "Google Project Zero"
source_url: "https://projectzero.google/2026/03/mutational-grammar-fuzzing.html"
date: "2026-03-05T08:00:00+00:00"
category: "research"
tags:
  - "fuzzing"
  - "grammar fuzzing"
  - "coverage‑guided"
  - "mutational fuzzing"
  - "XSLT"
  - "JIT bugs"
  - "Google Project Zero"
slug: "2026-03-05-on-the-effectiveness-of-mutational-grammar-fuzzing"
quote: "Some people are always grumbling because roses have thorns; I am thankful that thorns have roses."
quote_author: "Alphonse Karr"
---

Mutational grammar fuzzing uses a predefined grammar to mutate inputs while preserving syntactic structure. In coverage‑guided mode, new samples that trigger unseen code paths are saved for future mutations. The technique has uncovered complex bugs in XSLT engines of web browsers and JIT compilers. However, the author notes subtle flaws that casual users may miss and presents a simple countermeasure to mitigate them.
