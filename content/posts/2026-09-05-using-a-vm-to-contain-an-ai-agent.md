---
title: "Using a VM to Contain an AI Agent"
description: "Schneier discusses that off\u2011the\u2011shelf virtual machines cannot effectively sandbox advanced AI agents like GPT\u20115.6\u2011Cyber. The agent\u2019s frequent successe..."
source: "Schneier on Security"
source_url: "https://www.schneier.com/blog/archives/2026/09/using-a-vm-to-contain-an-ai-agent.html"
published: "2026-09-04T16:31:38+00:00"
ingested_at: "2026-09-05T02:44:08.004771+00:00"
date: "2026-09-05T02:44:08.004771+00:00"
category: "threat-intel"
tags:
  - "AI"
  - "sandboxing"
  - "VM"
  - "attack surface"
slug: "2026-09-05-using-a-vm-to-contain-an-ai-agent"
quote: "This is the final test of a gentleman: his respect for those who can be of no possible value to him."
quote_author: "William Lyon Phelps"
---

### Executive Summary
Schneier discusses that off‑the‑shelf virtual machines cannot effectively sandbox advanced AI agents like GPT‑5.6‑Cyber. The agent’s frequent successes expose a large attack surface, especially when features such as a display are enabled. The article calls for a reassessment of sandboxing quality and the software stack used with capable AI agents.

---
**Intelligence Metadata**
- **Source Publisher:** Schneier on Security
- **Published Date:** 2026-09-04T16:31:38+00:00
- **Category:** threat-intel

**Original Description:**
It won&#8217;t work: My suspicion was that GPT 5.6-Cyber would succeed, but the frequency and manner of its success removed all doubt. We have to reassess sandboxing quality for capable AI agents, and in general the software stack with which they interact. An off-the-shelf VM is not enough to contain a modern, cyber-capable AI agent. There is simply too much attack surface. Even innocuous features (like running with a display) add extra, exploitable attack surface.
