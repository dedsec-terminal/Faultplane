---
title: "Ruby Fixes Three Regex Engine Bugs Responsible for Four Critical GitLab RCE Flaws"
description: "Ruby released patches for its Onigmo regex engine, fixing three bugs that caused four critical remote code execution (RCE) vulnerabilities in GitLab. ..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/10/ruby-fixes-three-regex-engine-bugs.html"
published: "2026-10-23T17:54:08+00:00"
ingested_at: "2026-10-24T03:05:31.613776+00:00"
date: "2026-10-24T03:05:31.613776+00:00"
category: "vulnerabilities"
tags:
  - "ruby"
  - "regex"
  - "gitlab"
  - "rce"
  - "onigmo"
slug: "2026-10-24-ruby-fixes-three-regex-engine-bugs-responsible-for-four-crit"
quote: "Successful people ask better questions, and as a result, they get better answers."
quote_author: "Tony Robbins"
---

### Executive Summary
Ruby released patches for its Onigmo regex engine, fixing three bugs that caused four critical remote code execution (RCE) vulnerabilities in GitLab. The flaws allowed specially crafted patterns to corrupt memory during compilation, potentially enabling code execution on GitLab’s servers. The updates (Ruby 4.0.9, 3.4.12, 3.3.13) address the memory corruption and mitigate the RCE risk.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-10-23T17:54:08+00:00
- **Category:** vulnerabilities

**Original Description:**
Ruby has released versions 4.0.9, 3.4.12, and 3.3.13 to fix three bugs in Onigmo, the regular expression engine built into the language. The bugs lie behind four critical security flaws that GitLab patched over the past month. GitLab found that a specially crafted pattern could corrupt memory while Ruby compiles it, potentially leading to code execution on its own servers. Ruby says any
