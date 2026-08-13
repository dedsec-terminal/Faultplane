---
title: "OpenAI, Anthropic, Google API Flaw Let Weaker AI Models Decode Stronger Models' Reasoning"
date: 2026-08-12T11:47:38+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

A recently discovered flaw in the APIs of OpenAI, Anthropic, and Google has allowed researchers to recover internal reasoning and secrets from session logs, including API keys and passwords. The weakness lies in the way these providers handle encrypted reasoning objects, which can be replayed across sessions and models. This enables a weaker model to act as a "fuzzy" decoder, revealing the hidden content of the encrypted objects. The researchers demonstrated four abuse paths, including stealing proprietary reasoning, extracting private data, and recovering harmful content.

The team behind the research decoded over 315,000 thinking blocks from 6,708 public agent trajectories, extracting 704 distinct privacy artifacts, including 62 API keys, 33 passwords, and 24 access tokens. The attack requires obtaining an encrypted reasoning block and API access to a compatible model from the same provider. The researchers disclosed their findings to the affected providers, and the demonstrated attacks are no longer reproducible as of August 2026. However, the report does not document malicious exploitation in the wild, and developers are advised to strip reasoning blocks and opaque reasoning fields from shared traces to prevent similar attacks.

The flaw is bounded, affecting developers who published raw agent logs with intact reasoning objects, but the exposure is still significant. The researchers caution that they cannot guarantee the accuracy of the reconstructed traces, and the fidelity of the extracted secrets is based on qualitative comparisons. The vendors have updated their documentation to reflect changes in handling encrypted reasoning, but no public acknowledgment of the flaw has been made. The research builds on previous work by Johns Hopkins cryptographer Matthew Green, who demonstrated the replay behavior of encrypted reasoning blocks, but the new paper takes it further by developing a reliable secret-extraction technique and documenting the privacy consequences at scale.

---

> *Don't let what you can't do stop you from doing what you can do.*

Source: [OpenAI, Anthropic, Google API Flaw Let Weaker AI Models Decode Stronger Models' Reasoning](https://thehackernews.com/2026/08/openai-anthropic-google-api-flaw-let.html)
