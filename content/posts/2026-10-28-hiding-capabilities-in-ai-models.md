---
title: "Hiding Capabilities in AI Models"
description: "Researchers demonstrate that hidden capabilities can be embedded in neural network weights via encrypted backdoors that activate only with a secret tr..."
source: "Schneier on Security"
source_url: "https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html"
published: "2026-10-27T11:01:26+00:00"
ingested_at: "2026-10-28T03:47:24.783775+00:00"
date: "2026-10-28T03:47:24.783775+00:00"
category: "research"
tags:
  - "AI"
  - "backdoor"
  - "cryptography"
  - "model-hiding"
  - "capability-evaluation"
  - "adversarial"
slug: "2026-10-28-hiding-capabilities-in-ai-models"
quote: "To give hope to someone occurs when you teach them how to use the tools to do it for themselves."
quote_author: "Byron Pulsifer"
---

### Executive Summary
Researchers demonstrate that hidden capabilities can be embedded in neural network weights via encrypted backdoors that activate only with a secret trigger. Using cryptographic techniques, they prove these hidden circuits are hard to elicit or interpret even with full weight access, challenging existing capability audits. The proof‑of‑concept, implemented in PyTorch, resists fine‑tuning, weight noise, gradient‑based trigger search, and latent adversarial training on a chemical reaction prediction task. Models are released to aid defense development.

---
**Intelligence Metadata**
- **Source Publisher:** Schneier on Security
- **Published Date:** 2026-10-27T11:01:26+00:00
- **Category:** research

**Original Description:**
Interesting research: &#8220;AI Models Can Provably Hide Arbitrary Capabilities&#8221; Abstract: Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on the assumption that hidden capabilities can be elicited. We show this assumption does not hold under adversarial conditions by constructing backdoor attacks that embed encrypted neural networks within host model weights, decrypting and executing them only upon receiving a secret trig...
