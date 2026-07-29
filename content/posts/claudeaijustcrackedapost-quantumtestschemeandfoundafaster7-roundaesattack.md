---
title: "Claude AI Just Cracked a Post-Quantum Test Scheme and Found a Faster 7-Round AES Attack"
date: 2026-07-28T18:59:07+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

Anthropic's AI model, Claude Mythos Preview, has achieved a significant breakthrough in cryptography by cracking a post-quantum test scheme and finding a faster attack on the Advanced Encryption Standard (AES). The model discovered a previously unused symmetry in the lattice behind the HAWK-256 signature scheme, allowing for an end-to-end key-recovery attack with an expected runtime of approximately three hours and 42 minutes on a 96-core server. This result does not affect production systems, as HAWK remains a candidate in the National Institute of Standards and Technology (NIST) post-quantum standardization process.

The AI model also developed a faster attack on seven-round AES-128, removing a 256-way guessing step from an existing meet-in-the-middle attack. This attack, which applies to seven of AES-128's ten rounds, requires an impractical number of chosen plaintexts and is still far from being a practical threat. The model's discovery, known as the Möbius Bridge, allows for a 200 to 800-fold speedup in the attack, depending on how runtime is measured. However, the attack remains infeasible at a realistic scale, and no production software needs to change as a result.

The breakthroughs were achieved through a combination of human guidance and AI-driven research, with the model conducting the majority of the research itself. The results were published alongside two technical papers and reproducibility artifacts, allowing for independent verification and validation. Anthropic estimates that the expected HAWK-256 key-recovery work factor falls from 264 to 238, and the gate-count estimate falls from 2150 to 2108 for HAWK-512 and from 2288 to 2182 for HAWK-1024. However, the attack remains exponential and does not extend to other NIST signature candidates or lattice cryptography generally.

---

> *What you are is what you have been. What you�ll be is what you do now.
Author: Buddha*

Source: [Claude AI Just Cracked a Post-Quantum Test Scheme and Found a Faster 7-Round AES Attack](https://thehackernews.com/2026/07/claude-ai-just-cracked-post-quantum.html)
