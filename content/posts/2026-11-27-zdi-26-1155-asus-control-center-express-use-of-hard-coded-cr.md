---
title: 'ZDI-26-1155: ASUS Control Center Express Use of Hard-coded Cryptographic Key
  Authentication Bypass Vulnerability'
description: A vulnerability in ASUS Control Center Express allows remote attackers
  to bypass authentication by exploiting a hard‑coded cryptographic key used in t...
source: Zero Day Initiative
source_url: http://www.zerodayinitiative.com/advisories/ZDI-26-1155/
published: '2026-11-24T06:00:00+00:00'
ingested_at: '2026-11-27T19:47:03.197902+00:00'
date: '2026-11-27T19:47:03.197902+00:00'
category: vulnerabilities
tags:
- authentication bypass
- hard-coded key
- ASUS Control Center Express
slug: 2026-11-27-zdi-26-1155-asus-control-center-express-use-of-hard-coded-cr
quote: In separateness lies the world's great misery, in compassion lies the world's
  true strength.
quote_author: Buddha
---

### Executive Summary

A vulnerability in ASUS Control Center Express allows remote attackers to bypass authentication by exploiting a hard‑coded cryptographic key used in token handling. The flaw means authentication is not required to exploit the system, potentially granting unauthorized access. ASUS has released an update to fix the issue. Users should apply the vendor patch to mitigate the risk.

### Original Overview

This vulnerability allows remote attackers to bypass authentication on affected installations of ASUS Control Center Express. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of authentication tokens. The issue results from the use of a hard-coded cryptographic key. An attacker can leverage this vulnerability to bypass authentication on the system. ASUS has issued an update to correct this vulnerability. More details can be found at: https://www.asus.com/security-advisory/ 2026-09-02 - Vulnerability reported to vendor 2026-11-24 - Coordinated public release of advisory 2026-11-24 - Advisory Updated
