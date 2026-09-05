---
title: "PostgreSQL Fixes 12-Year-Old Logical Decoding Flaw Enabling Replication-Role Code Execution"
description: "PostgreSQL released security updates to fix a 12\u2011year\u2011old logical decoding vulnerability (CVE\u20112026\u20116471, CVSS 7.2) that allowed users with the REPLICA..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/09/postgresql-fixes-12-year-old-logical.html"
published: "2026-09-04T15:20:19+00:00"
ingested_at: "2026-09-05T02:43:52.563972+00:00"
date: "2026-09-05T02:43:52.563972+00:00"
category: "vulnerabilities"
tags:
  - "PostgreSQL"
  - "CVE-2026-6471"
  - "logical decoding"
  - "replication"
  - "code execution"
  - "database security"
slug: "2026-09-05-postgresql-fixes-12-year-old-logical-decoding-flaw-enabling"
quote: "When you meet someone better than yourself, turn your thoughts to becoming his equal. When you meet someone not as good as you are, look within and examine your own self."
quote_author: "Confucius"
---

### Executive Summary
PostgreSQL released security updates to fix a 12‑year‑old logical decoding vulnerability (CVE‑2026‑6471, CVSS 7.2) that allowed users with the REPLICATION role to execute arbitrary code as the database server’s OS user. The flaw existed since PostgreSQL 9.4 and is fixed in versions 18.6, 17.11, 16.15, 15.19, and 14.24.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-09-04T15:20:19+00:00
- **Category:** vulnerabilities

**Original Description:**
PostgreSQL has released updates to address a security flaw that allows an account with the REPLICATION attribute to run arbitrary code as the operating-system user running the database server. The flaw, tracked as CVE-2026-6471 (CVSS score: 7.2), has been present since logical decoding was introduced in PostgreSQL 9.4 in 2014. Versions before PostgreSQL 18.6, 17.11, 16.15, 15.19, and 14.24 are
