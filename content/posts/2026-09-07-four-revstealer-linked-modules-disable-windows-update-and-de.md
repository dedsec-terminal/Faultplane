---
title: "Four REVSTEALER-Linked Modules Disable Windows Update and Defender to Run a Crypto Miner"
description: "Elastic Security Labs uncovered four previously unknown modules linked to the REVSTEALER Windows information stealer. The modules\u2014ProManager, WinUpdat..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/09/four-revstealer-linked-modules-disable.html"
published: "2026-09-06T08:34:20+00:00"
ingested_at: "2026-09-07T02:39:14.980605+00:00"
date: "2026-09-07T02:39:14.980605+00:00"
category: "threat-intel"
tags:
  - "REVSTEALER"
  - "crypto-mining"
  - "Windows Update"
  - "Microsoft Defender"
  - "malware"
slug: "2026-09-07-four-revstealer-linked-modules-disable-windows-update-and-de"
quote: "It is only with the heart that one can see rightly, what is essential is invisible to the eye."
quote_author: "Antoine de Saint-Exupery"
---

### Executive Summary
Elastic Security Labs uncovered four previously unknown modules linked to the REVSTEALER Windows information stealer. The modules—ProManager, WinUpdate, SoftManager, and an unnamed program—persist after the main stealer deletes itself. One module disables Windows Update and Microsoft Defender before launching a cryptocurrency miner, enabling stealthy mining operations.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-09-06T08:34:20+00:00
- **Category:** threat-intel

**Original Description:**
Elastic Security Labs has documented four previously unreported programs associated with REVSTEALER, an emerging Windows information stealer, that remain on an infected machine after the stealer deletes itself. One of them switches off Windows Update and Microsoft Defender before running a cryptocurrency miner. The company named the four programs ProManager, WinUpdate, SoftManager, and
