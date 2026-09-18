---
title: "Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone"
description: "Unbound DNS resolver versions prior to 1.26.1 contain a critical heap overflow in the DNSSEC validator. An attacker controlling a malicious DNS zone c..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html"
published: "2026-09-17T12:30:00+00:00"
ingested_at: "2026-09-18T02:58:18.943002+00:00"
date: "2026-09-18T02:58:18.943002+00:00"
category: "cves"
tags:
  - "Unbound"
  - "DNSSEC"
  - "heap overflow"
  - "remote code execution"
  - "CVE-2026-81642"
slug: "2026-09-18-critical-unbound-dnssec-validator-flaw-could-allow-rce-via-a"
quote: "I believe that every person is born with talent."
quote_author: "Maya Angelou"
---

### Executive Summary
Unbound DNS resolver versions prior to 1.26.1 contain a critical heap overflow in the DNSSEC validator. An attacker controlling a malicious DNS zone can trigger the flaw by querying a vulnerable resolver, leading to remote code execution. The issue is fixed in Unbound 1.26.1 and is tracked as CVE-2026-81642.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-09-17T12:30:00+00:00
- **Category:** cves

**Original Description:**
Every release of the Unbound DNS resolver before 1.26.1 has a critical heap overflow in its DNSSEC validator, maintainer NLnet Labs said in an&nbsp;advisory&nbsp;on Wednesday. An attacker who controls a malicious zone and queries a vulnerable resolver can trigger it, enabling remote code execution. Unbound 1.26.1, released the same day, fixes the bug, tracked as&nbsp;CVE-2026-81642, along with
