---
title: Mutation testing comes to DAML
description: In April we released Mewt , our open-source mutation-testing engine that
  finds the gaps in your test suite. Today we’re expanding it with support for...
source: Trail of Bits
source_url: https://blog.trailofbits.com/2026/07/08/mutation-testing-comes-to-daml/
published: '2026-07-08T11:00:00+00:00'
ingested_at: '2026-11-27T19:39:14.670005+00:00'
date: '2026-11-27T19:39:14.670005+00:00'
category: research
tags:
- research
slug: 2026-11-27-mutation-testing-comes-to-daml
quote: When one tugs at a single thing in nature, he finds it attached to the rest
  of the world.
quote_author: John Muir
---

### Executive Summary

In April we released Mewt , our open-source mutation-testing engine that finds the gaps in your test suite. Today we’re expanding it with support for DAML, the language Canton Network applications are written in. Mewt now reads DAML, generates several classes of mutants (including two built for DAML’s authorization primitives), and runs them through your existing test suite to count how many mutants survive. If you want to try it, simply install Mewt from the repository , point a mewt.toml at your project and its test command, and use mewt run . For a team shipping DAML to production, that count is what a passing test run is actually worth: it puts a number on how much your suite checks, whereas a green run on its own does not. Why DAML’s coverage reports lie Test coverage is the most...
