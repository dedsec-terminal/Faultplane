---
title: Death By A Thousand PaperCuts (PaperCut Pre-Auth RCE Chain and Patch Bypasses
  WT-2026-0141-0144/CVE-2026-82077/CVE-2026-82078/CVE-2026-81578)
description: Before we begin, yes - it's confusing. There are more vulnerabilities
  with watchTowr IDs in this blog post than there are CVE IDs (assigned by PaperCu...
source: watchTowr Labs
source_url: https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/
published: '2026-10-09T17:31:14+00:00'
ingested_at: '2026-11-27T19:39:14.678005+00:00'
date: '2026-11-27T19:39:14.678005+00:00'
category: research
tags:
- research
slug: 2026-11-27-death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-an
quote: Setting an example is not the main means of influencing another, it is the
  only means.
quote_author: Albert Einstein
---

### Executive Summary

Before we begin, yes - it's confusing. There are more vulnerabilities with watchTowr IDs in this blog post than there are CVE IDs (assigned by PaperCut), due to PaperCut bundling vulnerabilities and then patch bypasses for those same vulnerabilities into singular CVE IDs. Paper! It still exists. We have to admit it - so much is happening right now (F1, GTA6, breakfast) that we barely have time to lovingly tease our most favoritest vendors. On Thursday, 27 August 2026, PaperCut published an advisory claiming that a mysterious vulnerability was being exploited in-the-wild, leading to system compromise. The watchTowr Intel team has documented the in-the-wild exploitation that our global honeypot network, Attacker Eye, captured here . To add insult to injury, when PaperCut released their...
