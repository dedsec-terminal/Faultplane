---
title: "WordPress Issues Patch for Critical Flaw That Can Enable Code Execution on Some Servers"
description: "WordPress released a security patch (v7.1.2) on September 22 to fix a critical core flaw that allows unauthenticated attackers to load external PHP fi..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/09/wordpress-issues-patch-for-critical.html"
published: "2026-09-22T18:03:10+00:00"
ingested_at: "2026-09-23T03:05:30.221857+00:00"
date: "2026-09-23T03:05:30.221857+00:00"
category: "vulnerabilities"
tags:
  - "WordPress"
  - "critical flaw"
  - "code execution"
  - "PHP"
  - "security patch"
slug: "2026-09-23-wordpress-issues-patch-for-critical-flaw-that-can-enable-cod"
quote: "The best cure for the body is a quiet mind."
quote_author: "Napoleon Bonaparte"
---

### Executive Summary
WordPress released a security patch (v7.1.2) on September 22 to fix a critical core flaw that allows unauthenticated attackers to load external PHP files, potentially enabling code execution on certain servers. The update covers all supported branches back to 4.7.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-09-22T18:03:10+00:00
- **Category:** vulnerabilities

**Original Description:**
WordPress has fixed a critical flaw in its core software that lets an attacker with no account make a site load a PHP file from outside its theme folders. On some servers, that can go further, allowing the attacker to run their own code. The fix shipped on September 22 in WordPress 7.1.2, with fixes for every branch the project still supports, back to 4.7, and WordPress is telling site owners
