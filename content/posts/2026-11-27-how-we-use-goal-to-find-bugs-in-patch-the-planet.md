---
title: How we use /goal to find bugs in Patch the Planet
description: Codex’s /goal feature amplifies bug hunting, but getting good results
  requires the right prompt, the right scope, and the right number of outcomes per...
source: Trail of Bits
source_url: https://blog.trailofbits.com/2026/07/28/how-we-use-goal-to-find-bugs-in-patch-the-planet/
published: '2026-07-28T11:00:00+00:00'
ingested_at: '2026-11-27T19:39:14.668005+00:00'
date: '2026-11-27T19:39:14.668005+00:00'
category: research
tags:
- research
slug: 2026-11-27-how-we-use-goal-to-find-bugs-in-patch-the-planet
quote: A really great talent finds its happiness in execution.
quote_author: Johann Wolfgang von Goethe
---

### Executive Summary

Codex’s /goal feature amplifies bug hunting, but getting good results requires the right prompt, the right scope, and the right number of outcomes per run. For Patch the Planet , our joint initiative with OpenAI to find and fix bugs in open-source software, we pointed Codex at some of the most widely used, heavily audited codebases in the world, like Rust, curl, and zlib. One tool came up again and again in our internal bug-report channels: /goal , which hands Codex an open-ended objective and lets it work independently toward a success condition. Here are a few highlights: /goal found every Rust bug we submitted, including a soundness hole and a miscompilation now patched in Rust 1.98, from a single variant-analysis pipeline. It turned every project’s past CVEs into Semgrep rules...
