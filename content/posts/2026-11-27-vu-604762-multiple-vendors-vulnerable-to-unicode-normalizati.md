---
title: 'VU#604762: Multiple vendors vulnerable to Unicode Normalization Collision
  on macOS (APFS)'
description: Overview A mismatch between Apple File System (APFS) filesystem and path
  resolution for multiple applications allows attackers to bypass security excl...
source: CERT/CC Vulnerability Notes
source_url: https://kb.cert.org/vuls/id/604762
published: '2026-11-16T16:17:31+00:00'
ingested_at: '2026-11-27T19:39:14.687005+00:00'
date: '2026-11-27T19:39:14.687005+00:00'
category: vulnerabilities
tags:
- vulnerabilities
slug: 2026-11-27-vu-604762-multiple-vendors-vulnerable-to-unicode-normalizati
quote: You, yourself, as much as anybody in the entire universe, deserve your love
  and affection.
quote_author: Buddha
---

### Executive Summary

Overview A mismatch between Apple File System (APFS) filesystem and path resolution for multiple applications allows attackers to bypass security exclusions using alternative Unicode spellings. By supplying an alternative Unicode spelling or case-folded variant (such as ß versus ss ) that bypasses the application's file write checks, a local attacker can overwrite files wherever the process has write permissions, potentially leading to data corruption, configuration hijacking, or code execution. Multiple vendors have assigned CVEs and issued patches to address this flaw. Description Several archive tools, packaging systems, and runtimes enforce exclusion filters using pathname comparisons that do not match the underlying filesystem's resolution behavior. By using a byte-for-byte...
