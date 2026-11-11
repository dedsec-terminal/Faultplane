---
title: "Git Patches Flaw That Lets Malicious Repositories Execute Code During Recursive Clones"
description: "A Git integer truncation flaw (CVE\u20112026\u2011111760) allows malicious repositories to execute arbitrary code when cloned recursively, including submodules...."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/11/git-patches-flaw-that-lets-malicious.html"
published: "2026-11-10T19:23:10+00:00"
ingested_at: "2026-11-11T04:29:35.488741+00:00"
date: "2026-11-11T04:29:35.488741+00:00"
category: "cves"
tags:
  - "git"
  - "cve-2026-111760"
  - "integer truncation"
  - "recursive clone"
  - "submodule"
  - "security patch"
  - "git-2.56.1"
slug: "2026-11-11-git-patches-flaw-that-lets-malicious-repositories-execute-co"
quote: "Difficulties are things that show a person what they are."
quote_author: "Epictetus"
---

### Executive Summary
A Git integer truncation flaw (CVE‑2026‑111760) allows malicious repositories to execute arbitrary code when cloned recursively, including submodules. The Git project released fixes in Git 2.56.1 and backported patches to versions 2.50‑2.55. The vulnerability arises from improper index handling during recursive clone operations.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-11-10T19:23:10+00:00
- **Category:** cves

**Original Description:**
A flaw in Git can let a malicious repository run an attacker's code on a computer that clones it recursively, together with its submodules. The Git project fixed it this week in Git 2.56.1, with matching fixes for the 2.50 through 2.55 series in 2.50.2, 2.51.3, 2.52.1, 2.53.1, 2.54.1 and 2.55.1. The flaw, tracked as CVE-2026-111760, is an integer truncation in how Git handles its index. An
