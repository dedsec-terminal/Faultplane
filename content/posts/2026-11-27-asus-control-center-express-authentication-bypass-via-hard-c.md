---
title: ASUS Control Center Express Authentication Bypass via Hard-Coded Key
description: A vulnerability in ASUS Control Center Express allows remote attackers
  to bypass authentication by exploiting a hard‑coded cryptographic key used in J...
source: Zero Day Initiative
source_url: http://www.zerodayinitiative.com/advisories/ZDI-26-1156/
published: '2026-11-24T06:00:00+00:00'
ingested_at: '2026-11-27T19:47:03.196902+00:00'
date: '2026-11-27T19:47:03.196902+00:00'
category: vulnerabilities
tags:
- authentication bypass
- hard‑coded key
- JWT
- ASUS Control Center Express
- Zero Day Initiative
slug: 2026-11-27-asus-control-center-express-authentication-bypass-via-hard-c
quote: I'm a great believer in luck and I find the harder I work, the more I have
  of it.
quote_author: Thomas Jefferson
---

### Executive Summary

A vulnerability in ASUS Control Center Express allows remote attackers to bypass authentication by exploiting a hard‑coded cryptographic key used in JWT handling. No authentication is required to exploit the flaw, and attackers can gain unauthorized access to the system. ASUS has released an update to fix the issue; users should apply the patch as soon as possible.

### Original Overview

This vulnerability allows remote attackers to bypass authentication of affected installations of ASUS Control Center Express. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of JWT authentication tokens. The issue results from the use of a hard-coded cryptographic key. An attacker can leverage this vulnerability to bypass authentication on the system. ASUS has issued an update to correct this vulnerability. More details can be found at: https://www.asus.com/security-advisory/ 2026-08-20 - Vulnerability reported to vendor 2026-11-24 - Coordinated public release of advisory 2026-11-24 - Advisory Updated
