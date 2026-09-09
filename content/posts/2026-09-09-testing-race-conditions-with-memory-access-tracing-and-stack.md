---
title: "Testing race conditions with memory access tracing and stack-based delay injection"
description: "The article discusses techniques for detecting and reproducing race conditions in concurrent programs. It introduces memory\u2011access tracing to observe ..."
source: "Google Project Zero"
source_url: "https://projectzero.google/2026/09/maccconc-race-condition.html"
published: "2026-09-08T07:00:00+00:00"
ingested_at: "2026-09-09T02:52:29.851279+00:00"
date: "2026-09-09T02:52:29.851279+00:00"
category: "research"
tags:
  - "race conditions"
  - "memory tracing"
  - "delay injection"
  - "regression testing"
  - "fuzzing"
slug: "2026-09-09-testing-race-conditions-with-memory-access-tracing-and-stack"
quote: "One who asks a question is a fool for five minutes; one who does not ask a question remains a fool forever."
quote_author: "Unknown"
---

### Executive Summary
The article discusses techniques for detecting and reproducing race conditions in concurrent programs. It introduces memory‑access tracing to observe interleavings and a stack‑based delay injection mechanism to force specific execution orders, enabling reliable regression tests and automated bug discovery. The methods help confirm manual or static‑analysis findings and improve fuzzing coverage for race‑related bugs.

---
**Intelligence Metadata**
- **Source Publisher:** Google Project Zero
- **Published Date:** 2026-09-08T07:00:00+00:00
- **Category:** research

**Original Description:**
Many security bugs are race conditions, where multi-threaded execution has to occur with the right interleaving for a negative effect to appear. This creates challenges for several use cases: Confirming bug candidates that have been discovered manually or through static analysis. Regression tests: After fixing a race condition bug, there is often no good way to write a regression test that reliably triggers the bug as part of a test suite. Automatic bug discovery, such as fuzzing: It is hard ...
