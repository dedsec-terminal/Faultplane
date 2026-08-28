---
title: "Some Malicious PE Stats"
description: "The author shares a Python script that uses the pefile library to parse PE headers of malicious binaries, extracting metadata such as compiler informa..."
source: "SANS Internet Storm Center"
source_url: "https://isc.sans.edu/diary/rss/33292"
published: "2026-08-28T07:04:13+00:00"
ingested_at: "2026-08-28T08:51:31.262240+00:00"
date: "2026-08-28T08:51:31.262240+00:00"
category: "threat-intel"
tags:
  - "malware"
  - "pe"
  - "statistics"
  - "python"
  - "pefile"
slug: "2026-08-28-some-malicious-pe-stats"
quote: "There never was a good knife made of bad steel."
quote_author: "Benjamin Franklin"
---

### Executive Summary
The author shares a Python script that uses the pefile library to parse PE headers of malicious binaries, extracting metadata such as compiler information and architecture (32‑bit vs 64‑bit). The script builds on earlier statistics about 64‑bit versus 32‑bit malware and provides deeper insights into the tools used to build malicious PE files. The post references Detect It Easy and was posted on the SANS Internet Storm Center.

---
**Intelligence Metadata**
- **Source Publisher:** SANS Internet Storm Center
- **Published Date:** 2026-08-28T07:04:13+00:00
- **Category:** threat-intel

**Original Description:**
During my last FOR610 session, a student asked me if I had some statistics in mind about the compilers used to generate malicious PE files&#x3f; A couple of months ago, I shared some stats about the trend in 64bits VS. 32bits malware&#x5b;1&#x5d;. Can we go a bit further&#x3f; I (vibe-)coded a Python script based on the pefile library&#x5b;2&#x5d; to extract some info from the PE headers. Indeed, the PE file format contains a lot of metadata&#x21; They can be accessed using a lot of tools, li...
