---
title: "A \u201cproof\u201d of Fermat\u2019s Last Theorem that fits the margin"
description: "A bug in Lean 4\u2019s string\u2011slicing function (String.Pos.Raw.extract) allowed a false proof of Fermat\u2019s Last Theorem. The logical definition returned an ..."
source: "Trail of Bits"
source_url: "https://blog.trailofbits.com/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin/"
published: "2026-09-09T11:00:00+00:00"
ingested_at: "2026-09-10T02:53:38.189571+00:00"
date: "2026-09-10T02:53:38.189571+00:00"
category: "research"
tags:
  - "lean"
  - "proof-bug"
  - "Fermat"
  - "formalization"
  - "software-security"
slug: "2026-09-10-a-proof-of-fermat-s-last-theorem-that-fits-the-margin"
quote: "Keep yourself to the sunshine and you cannot see the shadow."
quote_author: "Helen Keller"
---

### Executive Summary
A bug in Lean 4’s string‑slicing function (String.Pos.Raw.extract) allowed a false proof of Fermat’s Last Theorem. The logical definition returned an empty string for a huge index, while native code returned the full string, creating a contradiction that let Lean prove any statement. The issue was reported to Trail of Bits, patched in Lean 4.34.0‑rc1, and highlights the need for careful validation of machine‑checked proofs.

---
**Intelligence Metadata**
- **Source Publisher:** Trail of Bits
- **Published Date:** 2026-09-09T11:00:00+00:00
- **Category:** research

**Original Description:**
Fermat famously claimed to have a “truly marvelous proof” of his Last Theorem, but he never wrote it down, insisting the margin of his page was too narrow to contain it. A few centuries later, Anthropic announced a complete formalization of Fermat&rsquo;s Last Theorem using 13 million lines of Lean code (clearly not what Fermat intended). Luckily, we found a wonderfully cursed Lean bug, shown below, that suggests the proof may have fit the margin after all. The issue affects all stable versio...
