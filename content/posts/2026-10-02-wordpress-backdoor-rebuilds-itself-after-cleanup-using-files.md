---
title: "WordPress Backdoor Rebuilds Itself After Cleanup Using Files, Database, and Shared Memory"
description: "Researchers uncovered a WordPress backdoor that self\u2011heals after cleanup by re\u2011injecting code via files, database entries, and shared memory. The malw..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/10/wordpress-backdoor-rebuilds-itself.html"
published: "2026-10-01T14:37:35+00:00"
ingested_at: "2026-10-02T03:51:05.715198+00:00"
date: "2026-10-02T03:51:05.715198+00:00"
category: "threat-intel"
tags:
  - "WordPress"
  - "backdoor"
  - "self-healing"
  - "persistence"
  - "SC"
  - "Sucuri"
slug: "2026-10-02-wordpress-backdoor-rebuilds-itself-after-cleanup-using-files"
quote: "A rolling stone gathers no moss."
quote_author: "Publilius Syrus"
---

### Executive Summary
Researchers uncovered a WordPress backdoor that self‑heals after cleanup by re‑injecting code via files, database entries, and shared memory. The malware, codenamed SC due to SC_ markers, uses multiple persistence mechanisms so the final payload returns without re‑infection. Sucuri calls it a “self‑healing mesh.”

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-10-01T14:37:35+00:00
- **Category:** threat-intel

**Original Description:**
Cybersecurity researchers have shed light on a WordPress compromise in which threat actors deployed multiple persistence mechanisms to ensure that the final payload kept returning without having to infect the site again. The backdoor has been codenamed SC after the "SC_" markers present in the injected content. Sucuri has described the malware as a "self-healing mesh" that's
