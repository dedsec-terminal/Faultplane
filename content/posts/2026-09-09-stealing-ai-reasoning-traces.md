---
title: "Stealing AI Reasoning Traces"
description: "Researchers discovered that encrypted chain\u2011of\u2011thought traces returned by LLM providers are interchangeable across sessions and models, enabling a sca..."
source: "Schneier on Security"
source_url: "https://www.schneier.com/blog/archives/2026/09/stealing-ai-reasoning-traces.html"
published: "2026-09-08T10:20:04+00:00"
ingested_at: "2026-09-09T02:51:45.659250+00:00"
date: "2026-09-09T02:51:45.659250+00:00"
category: "vulnerabilities"
tags:
  - "LLM"
  - "encryption"
  - "jailbreak"
  - "data-exfiltration"
  - "prompt-injection"
slug: "2026-09-09-stealing-ai-reasoning-traces"
quote: "Imagination is not a talent of some men but is the health of every man."
quote_author: "Ralph Waldo Emerson"
---

### Executive Summary
Researchers discovered that encrypted chain‑of‑thought traces returned by LLM providers are interchangeable across sessions and models, enabling a scalable decryption jailbreak. By injecting a trace from a powerful model into a weaker one, attackers can force plaintext output, bypass anti‑distillation, extract PII and credentials from public logs, reveal hidden hazardous content, and perform invisible prompt injections. The study covers Anthropic, OpenAI, and Google, and proposes cryptographic mitigations.

---
**Intelligence Metadata**
- **Source Publisher:** Schneier on Security
- **Published Date:** 2026-09-08T10:20:04+00:00
- **Category:** vulnerabilities

**Original Description:**
Interesting research: &#8220;Stealing Reasoning Traces from Proprietary LLM APIs&#8220;: Abstract: Leading large language model providers now conceal their models&#8217; step-by-step reasoning, or chain-of-thought, to protect intellectual property and limit information leakage. Rather than storing these traces server-side, providers return them to the client as blocks of encrypted text, which the client passes back with each subsequent request. Building on prior research, we identify an archi...
