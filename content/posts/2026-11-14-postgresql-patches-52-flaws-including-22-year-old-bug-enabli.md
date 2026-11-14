---
title: "PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE"
description: "A type\u2011confusion flaw (CVE\u20112026\u20116460) in PostgreSQL allows a database user who can create objects to execute code on the server with OS privileges. Th..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html"
published: "2026-11-13T16:53:08+00:00"
ingested_at: "2026-11-14T04:45:05.006918+00:00"
date: "2026-11-14T04:45:05.006918+00:00"
category: "vulnerabilities"
tags:
  - "PostgreSQL"
  - "CVE-2026-6460"
  - "RCE"
  - "type confusion"
  - "database"
slug: "2026-11-14-postgresql-patches-52-flaws-including-22-year-old-bug-enabli"
quote: "Character is like a tree and reputation like a shadow. The shadow is what we think of it; the tree is the real thing."
quote_author: "Abraham Lincoln"
---

### Executive Summary
A type‑confusion flaw (CVE‑2026‑6460) in PostgreSQL allows a database user who can create objects to execute code on the server with OS privileges. The vulnerability, exploitable by authenticated users, is part of a set of 52 security bugs fixed in the latest patch release. Full protection also requires rebuilding any C‑language extensions. The flaw has a CVSS score of 8.8.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-11-13T16:53:08+00:00
- **Category:** vulnerabilities

**Original Description:**
A type confusion flaw in PostgreSQL lets a database user who can create objects run code on the server. Updates released yesterday fix it, along with 51 other security flaws. Full protection from this flaw also requires rebuilding any C-language extensions installed on the server. The flaw, tracked as CVE-2026-6460, has a CVSS score of 8.8. Any code run this way has the rights of the operating
