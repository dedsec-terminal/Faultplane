---
title: "GnuPG Warns Critical GPGME Flaw Could Expose App Data via Malicious OpenPGP Keys"
description: "A malicious OpenPGP key with an unusually long user ID can trigger a critical memory bug in GPGME, the library used by applications to interface with ..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/11/gnupg-warns-critical-gpgme-flaw-could.html"
published: "2026-11-21T11:05:53+00:00"
ingested_at: "2026-11-22T04:51:57.885819+00:00"
date: "2026-11-22T04:51:57.885819+00:00"
category: "cves"
tags:
  - "GnuPG"
  - "GPGME"
  - "CVE-2026-129975"
  - "OpenPGP"
  - "memory-bug"
  - "malicious-key"
slug: "2026-11-22-gnupg-warns-critical-gpgme-flaw-could-expose-app-data-via-ma"
quote: "You get peace of mind not by thinking about it or imagining it, but by quietening and relaxing the restless mind."
quote_author: "Remez Sasson"
---

### Executive Summary
A malicious OpenPGP key with an unusually long user ID can trigger a critical memory bug in GPGME, the library used by applications to interface with GnuPG. The flaw, CVE‑2026‑129975, affects all software using GPGME before version 2.3.0 and could allow attackers to steal data from those applications. GnuPG has released patched versions to mitigate the issue.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-11-21T11:05:53+00:00
- **Category:** cves

**Original Description:**
A malicious OpenPGP key with an unusually long user ID can trigger a critical memory bug in GPGME, the standard library that programs use to work with GnuPG. The GnuPG project warned yesterday that the flaw could be used to steal data from affected applications and has released fixed versions. The bug, tracked as CVE-2026-129975, affects all software that uses GPGME before version 2.3.0,
