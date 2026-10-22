---
title: "Critical GitLab Flaw (CVSS 10.0) Could Allow Unauthenticated RCE Across 12 Years of Releases"
description: "GitLab released patches on Oct\u202f21 fixing a critical flaw (CVSS\u202f10.0) that allows unauthenticated remote code execution on self\u2011managed installations. ..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html"
published: "2026-10-21T18:57:34+00:00"
ingested_at: "2026-10-22T03:06:04.907437+00:00"
date: "2026-10-22T03:06:04.907437+00:00"
category: "vulnerabilities"
tags:
  - "GitLab"
  - "RCE"
  - "CVSS 10.0"
  - "unauthenticated"
  - "self-managed"
slug: "2026-10-22-critical-gitlab-flaw-cvss-10-0-could-allow-unauthenticated-r"
quote: "The heart has eyes which the brain knows nothing of."
quote_author: "Charles Perkhurst"
---

### Executive Summary
GitLab released patches on Oct 21 fixing a critical flaw (CVSS 10.0) that allows unauthenticated remote code execution on self‑managed installations. The vulnerability spans all releases from version 7.0 (2014) through the latest, affecting over a decade of software. The earlier Oct 12 update only covered 19.2+, leaving many versions exposed until the newer patch. Administrators must apply the latest fix to mitigate the risk.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-10-21T18:57:34+00:00
- **Category:** vulnerabilities

**Original Description:**
GitLab released fixes on October 21 for a flaw that lets an attacker run code on a self-managed server without logging in, and it affects every version of the software going back to 7.0, released in 2014. The fix matters even for administrators who patched nine days earlier: the October 12 update covered only versions 19.2 and later, and the new fixed versions sit one patch above it, so an
