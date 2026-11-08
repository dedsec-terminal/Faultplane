---
title: "Claude Code's 'Don't Ask Again' File Exposes Passwords and Keys in 1,122 Public GitHub Repositories"
description: "Anthropic\u2019s Claude Code AI coding assistant, when users select \u201cYes, and don\u2019t ask again,\u201d can save commands\u2014including any passwords or API keys typed..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html"
published: "2026-11-07T06:44:17+00:00"
ingested_at: "2026-11-08T04:10:09.050398+00:00"
date: "2026-11-08T04:10:09.050398+00:00"
category: "threat-intel"
tags:
  - "Anthropic"
  - "Claude Code"
  - "GitHub"
  - "API keys"
  - "password leakage"
slug: "2026-11-08-claude-code-s-don-t-ask-again-file-exposes-passwords-and-key"
quote: "When fate hands us a lemon, lets try to make lemonade."
quote_author: "Dale Carnegie"
---

### Executive Summary
Anthropic’s Claude Code AI coding assistant, when users select “Yes, and don’t ask again,” can save commands—including any passwords or API keys typed—into a project settings file. A security firm found 1,122 public GitHub repositories containing such files, exposing sensitive credentials. The leak demonstrates a flaw in the assistant’s handling of secrets and highlights the need for better secret management in AI‑assisted coding.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-11-07T06:44:17+00:00
- **Category:** threat-intel

**Original Description:**
Passwords and API keys that developers typed into commands they approved in Claude Code are sitting in public GitHub repositories, where anyone can read them. When a user selects "Yes, and don't ask again," Anthropic's AI coding assistant can save the command, word-for-word, including the secret, in a project settings file. Software security company Apiiro said yesterday that 1,122 public
