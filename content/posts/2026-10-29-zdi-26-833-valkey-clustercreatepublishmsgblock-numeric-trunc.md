---
title: "ZDI-26-833: Valkey clusterCreatePublishMsgBlock Numeric Truncation Error Remote Code Execution Vulnerability"
description: "A numeric truncation error in Valkey's clusterCreatePublishMsgBlock function allows authenticated remote attackers to execute arbitrary code. The vuln..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-833/"
published: "2026-10-28T05:00:00+00:00"
ingested_at: "2026-10-29T04:10:55.032037+00:00"
date: "2026-10-29T04:10:55.032037+00:00"
category: "cves"
tags:
  - "Valkey"
  - "remote code execution"
  - "numeric truncation"
  - "ZDI"
  - "CVSS 8.8"
slug: "2026-10-29-zdi-26-833-valkey-clustercreatepublishmsgblock-numeric-trunc"
quote: "We must not say every mistake is a foolish one."
quote_author: "Cicero"
---

### Executive Summary
A numeric truncation error in Valkey's clusterCreatePublishMsgBlock function allows authenticated remote attackers to execute arbitrary code. The vulnerability, identified as ZDI-26-833, carries a CVSS score of 8.8 and requires authentication to exploit.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-10-28T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Valkey. Authentication is required to exploit this vulnerability. The ZDI has assigned a CVSS rating of 8.8.
