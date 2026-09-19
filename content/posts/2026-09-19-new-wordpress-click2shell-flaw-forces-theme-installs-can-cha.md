---
title: "New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code Execution"
description: "WordPress released patches for a new core vulnerability that lets a crafted link, opened by a logged\u2011in administrator, automatically install a theme f..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/09/new-wordpress-click2shell-flaw-forces.html"
published: "2026-09-18T16:56:19+00:00"
ingested_at: "2026-09-19T02:56:05.500398+00:00"
date: "2026-09-19T02:56:05.500398+00:00"
category: "vulnerabilities"
tags:
  - "WordPress"
  - "Click2Shell"
  - "theme-installation"
  - "admin"
  - "pwn.ai"
  - "vulnerability"
slug: "2026-09-19-new-wordpress-click2shell-flaw-forces-theme-installs-can-cha"
quote: "You only lose what you cling to."
quote_author: "Buddha"
---

### Executive Summary
WordPress released patches for a new core vulnerability that lets a crafted link, opened by a logged‑in administrator, automatically install a theme from the official WordPress.org directory without user interaction. The flaw, dubbed Click2Shell by pwn.ai researchers, can be chained to achieve code execution.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-09-18T16:56:19+00:00
- **Category:** vulnerabilities

**Original Description:**
WordPress today released patches to fix a new set of vulnerabilities in its core software, one of which could allow a crafted web link, opened by a logged-in administrator, to install a theme from the official WordPress.org directory without anyone clicking Install. The security firm pwn.ai, whose researchers reported the flaw, calls the attack chain Click2Shell. On its own the flaw only
