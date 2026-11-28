---
title: You’re Not Supposed To ShareFile With Everyone (Progress ShareFile Pre-Auth
  RCE Chain CVE-2026-2699 & CVE-2026-2701)
description: Researchers identified two critical vulnerabilities in the Progress ShareFile
  Storage Zone Controller (branch 5.x), specifically in version 5.12.3. CV...
source: watchTowr Labs
source_url: https://labs.watchtowr.com/youre-not-supposed-to-sharefile-with-everyone-progress-sharefile-pre-auth-rce-chain-cve-2026-2699-cve-2026-2701/
published: '2026-04-02T10:00:42+00:00'
ingested_at: '2026-11-28T06:05:31.049979+00:00'
date: '2026-11-28T06:05:31.049979+00:00'
category: research
tags:
- Progress ShareFile
- CVE-2026-2699
- CVE-2026-2701
- pre-auth RCE
- file transfer
slug: 2026-11-28-you-re-not-supposed-to-sharefile-with-everyone-progress-shar
quote: If one advances confidently in the direction of his dream, and endeavours to
  live the life which he had imagines, he will meet with a success unexpected in common
  hours.
quote_author: Henry David Thoreau
---

### Executive Summary

Researchers identified two critical vulnerabilities in the Progress ShareFile Storage Zone Controller (branch 5.x), specifically in version 5.12.3. CVE‑2026‑2699 allows an unauthenticated attacker to bypass authentication, while CVE‑2026‑2701 enables remote code execution once the bypass is achieved. The issues were patched in version 5.12.4, released to customers on March 10 2026. Approximately 30,000 on‑premises instances of the Storage Zone Controller were potentially exposed, allowing attackers to run arbitrary code on the underlying IIS server. Defenders should verify that their ShareFile deployments are updated to the patched version and monitor for signs of exploitation.

### Original Overview

If you squint and look at the CISA KEV list, you might think it's made up exclusively of vulnerabilities in file transfer solutions. While this would be wrong (and you shouldn’t squint, it’s bad for your eyes), file transfer solutions do play a decent role in the CISA KEV list due to how fondly threat actors, APT groups, and ransomware gangs alike perceive them. The following represent industry-defining historical incidents: The MOVEit breach in 2023 , Cleo Harmony, VLTrader and LexiCom in 2024, or, Fortra’s GoAnywhere, with mysterious active exploitation in 2025 . Today, we find ourselves analyzing the journey we took to discover multiple vulnerabilities in Progress ShareFile, ultimately chained together to achieve Pre-Authenticated Remote Code Execution - and sharing more memes....
