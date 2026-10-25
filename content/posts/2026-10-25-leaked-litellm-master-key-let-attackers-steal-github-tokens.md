---
title: "Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline"
description: "In late May 2026, a configuration file containing LiteLLM\u2019s Agent Platform master key was accidentally committed to the public LiteLLM\u2011Labs/lite\u2011harne..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/10/leaked-litellm-master-key-let-attackers.html"
published: "2026-10-24T11:03:33+00:00"
ingested_at: "2026-10-25T02:59:54.979629+00:00"
date: "2026-10-25T02:59:54.979629+00:00"
category: "threat-intel"
tags:
  - "LiteLLM"
  - "GitHub"
  - "master key leak"
  - "malicious package"
  - "token theft"
slug: "2026-10-25-leaked-litellm-master-key-let-attackers-steal-github-tokens"
quote: "If you have knowledge, let others light their candles in it."
quote_author: "Margaret Fuller"
---

### Executive Summary
In late May 2026, a configuration file containing LiteLLM’s Agent Platform master key was accidentally committed to the public LiteLLM‑Labs/lite‑harness GitHub repository. The exposed key enabled threat actors to authenticate to the deployment, push a malicious version of the popular Python package, steal GitHub access tokens, and hijack the release pipeline. The incident highlights the risks of accidental credential exposure in public code repositories.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-10-24T11:03:33+00:00
- **Category:** threat-intel

**Original Description:**
LiteLLM on Friday revealed that an Agent Platform master key accidentally published to a public GitHub repository in late May 2026 ultimately allowed the threat actor to push a malicious version of the popular Python package. "On May 27, 2026, a configuration file was committed to the public LiteLLM-Labs/lite-harness repository which inadvertently contained the master key to a deployment of
