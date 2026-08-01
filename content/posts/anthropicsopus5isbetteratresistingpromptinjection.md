---
title: "Anthropic’s Opus 5 Is Better at Resisting Prompt Injection"
date: 2026-07-31T17:23:16+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Anthropic's Opus 5 model has shown significant improvement in resisting prompt injection attacks. According to the IPI benchmark, Opus 5 reduced the probability of a successful attack within 15 attempts from 5.5% to 2.0%, outperforming its predecessor Opus 4.8 and other models such as Sonnet 5 and Mythos 5. This makes Opus 5 the most robust model evaluated, with a success rate more than eight times lower than the most robust non-Claude model, Muse Spark.

The results also highlight the differences in robustness between Opus 5 and other models, including GPT 5.6 variants. The most capable GPT 5.6 variant, Sol, had a success rate of 20.0% within 15 attempts, which is 10 times higher than Opus 5's rate. Other GPT 5.6 variants, such as Terra and Luna, had even higher success rates, at 30.4% and 43.9%, respectively. This demonstrates the significant improvement in Opus 5's ability to resist prompt injection attacks compared to other models.

The improvement in Opus 5's robustness is notable, but it is also acknowledged that preventing prompt injection is a challenging task. While it is possible to block prompt injection in specific cases, it is unclear whether it is fundamentally impossible to prevent it in the general case. Some argue that alternative architectures may be able to mitigate this issue, and that the current architecture's limitations may not be inherent to all language models. Further research is needed to explore the possibilities of developing more robust models that can effectively resist prompt injection attacks.

---

> *The pessimist sees difficulty in every opportunity. The optimist sees the opportunity in every difficulty.
Author: Winston Churchill*

Source: [Anthropic’s Opus 5 Is Better at Resisting Prompt Injection](https://www.schneier.com/blog/archives/2026/07/anthropics-opus-5-is-better-at-resisting-prompt-injection.html)
