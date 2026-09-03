---
title: "Malicious .git Configs Can Make AI Agents Run Attacker Code"
description: "Manifold Security uncovered eight security flaws in seven command\u2011line AI coding agents (Claude, Codex, Cursor, etc.). A malicious repository\u2019s .git/c..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html"
published: "2026-09-02T14:06:59+00:00"
ingested_at: "2026-09-03T02:44:50.307322+00:00"
date: "2026-09-03T02:44:50.307322+00:00"
category: "threat-intel"
tags:
  - "git config"
  - "AI coding agents"
  - "command injection"
  - "Manifold Security"
slug: "2026-09-03-malicious-git-configs-can-make-ai-agents-run-attacker-code"
quote: "When you arise in the morning, think of what a precious privilege it is to be alive \ufffd to breathe, to think, to enjoy, to love."
quote_author: "Marcus Aurelius"
---

### Executive Summary
Manifold Security uncovered eight security flaws in seven command‑line AI coding agents (Claude, Codex, Cursor, etc.). A malicious repository’s .git/config can specify a command that the agent automatically executes on the developer’s machine, running as the user outside the agent’s sandbox and without any approval prompt. Exploitation requires the repository to be cloned, and four of the eight vulnerabilities remain unpatched at the time of disclosure.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-09-02T14:06:59+00:00
- **Category:** threat-intel

**Original Description:**
Manifold Security has disclosed eight security flaws across seven command-line AI coding agents in which a repository's own Git configuration names a command that the agent runs on the developer's machine, four of them still unpatched at publication. The command executes as the user, outside the agent's sandbox and without an approval prompt, and exploitation requires the repository to arrive
