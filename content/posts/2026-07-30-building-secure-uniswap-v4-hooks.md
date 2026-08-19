---
title: "Building secure Uniswap v4 hooks"
description: "Uniswap v4 introduces hooks that let developers add custom logic to pools, shifting security responsibility to application code. Two app\u2011level exploit..."
source: "Trail of Bits"
source_url: "https://blog.trailofbits.com/2026/07/30/building-secure-uniswap-v4-hooks/"
date: "2026-07-30T11:00:00+00:00"
category: "research"
tags:
  - "uniswap"
  - "v4"
  - "hooks"
  - "smart-contract"
  - "security"
  - "audit"
slug: "2026-07-30-building-secure-uniswap-v4-hooks"
quote: "A rolling stone gathers no moss."
quote_author: "Publilius Syrus"
---

### Executive Summary
Uniswap v4 introduces hooks that let developers add custom logic to pools, shifting security responsibility to application code. Two app‑level exploits (Cork and Bunni) caused over $20M in losses, stemming from faulty hook logic rather than the core protocol. Trail of Bits identified seven recurring failure patterns—such as missing caller checks and accounting bugs—that can bypass the PoolManager’s settlement invariant. The article offers a secure‑development checklist for builders and a focused audit guide for reviewers.

---
**Intelligence Metadata**
- **Source Publisher:** Trail of Bits
- **Published Date:** 2026-07-30T11:00:00+00:00
- **Category:** research
