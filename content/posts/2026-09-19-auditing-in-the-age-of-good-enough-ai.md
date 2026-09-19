---
title: "Auditing in the age of (good enough) AI"
description: "Trail of Bits used AI agents to build custom tooling\u2014an LSP server, decompiler, static analyzer, and Lean model\u2014for auditing the Miden zero\u2011knowledge ..."
source: "Trail of Bits"
source_url: "https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai/"
published: "2026-09-18T11:00:00+00:00"
ingested_at: "2026-09-19T02:57:14.423247+00:00"
date: "2026-09-19T02:57:14.423247+00:00"
category: "research"
tags:
  - "AI"
  - "code review"
  - "zero-knowledge VM"
  - "Miden"
  - "security auditing"
  - "tooling"
slug: "2026-09-19-auditing-in-the-age-of-good-enough-ai"
quote: "We never understand how little we need in this world until we know the loss of it."
quote_author: "James Barrie"
---

### Executive Summary
Trail of Bits used AI agents to build custom tooling—an LSP server, decompiler, static analyzer, and Lean model—for auditing the Miden zero‑knowledge VM before launch. Over six months, the agents produced a full stack‑machine language server, uncovered a critical flaw allowing malicious provers to forge Falcon signatures, and delivered 95 machine‑checked proofs of core library correctness. The effort demonstrates how AI can accelerate security reviews of low‑level, custom assembly code.

---
**Intelligence Metadata**
- **Source Publisher:** Trail of Bits
- **Published Date:** 2026-09-18T11:00:00+00:00
- **Category:** research

**Original Description:**
Security firms have published numerous blog posts describing how they pointed their agent harness at a codebase and found dozens of bugs (we’re one of them). However, these posts tend to focus on agentic code review, which is just one aspect of how we use AI in our security reviews. We want to give a different perspective: before code review even starts, agents now allow us to build custom tooling and formal models that improve the quality and depth of our reviews. We recently reviewed the Mi...
