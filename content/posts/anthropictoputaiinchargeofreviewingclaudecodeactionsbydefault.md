---
title: "Anthropic to put AI in charge of reviewing Claude Code actions by default"
date: 2026-08-10T09:13:29+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

Anthropic, the company behind Claude Code, is making auto mode the default for new sessions on Pro, Max, and Team plans starting August 14. In auto mode, AI reviews Claude Code actions, reducing the risk of dangerous commands. According to a controlled experiment with 1,053 paid testers, auto mode caught 89% of dangerous commands, while human review caught only 13.6%. This feature will be optional on other platforms, including Claude Enterprise and the Claude API, but is expected to become the default across all platforms over the next month.

Auto mode works by routing every tool call through a classifier designed to block irreversible or destructive actions. If the classifier blocks an action, Claude either finds a safer alternative or asks for user approval. Anthropic has tested auto mode extensively, including internal and independent testing, and found it to be safer than manual approvals. In fact, analysis of real-world sessions found that manual approval was more than twice as likely to result in harmful actions. Auto mode also adds an extra layer of protection against prompt injection attacks, which attempt to trick the agent into ignoring user instructions.

Anthropic uses auto mode internally across all Claude Code workflows and has seen significant benefits, including increased productivity and safety. The company has also introduced additional features to make auto mode safer for production use, such as hard denies and prompt injection screening. According to Anthropic, auto mode allows Claude to work autonomously for longer periods, reducing user overhead while increasing output. The company recommends that users still review Claude's actions before making high-risk changes, but auto mode provides an additional layer of protection against dangerous commands.

---

> *We aim above the mark to hit the mark.
Author: Ralph Emerson*

Source: [Anthropic to put AI in charge of reviewing Claude Code actions by default](https://www.helpnetsecurity.com/2026/08/10/anthropic-claude-code-auto-mode/)
