---
title: "ZDI-26-776: QNAP TS-453E syslog log_message Format String Remote Code Execution Vulnerability"
description: "Zero Day Initiative identified a format string vulnerability in the syslog log_message function of QNAP TS-453E devices. The flaw allows unauthenticat..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-776/"
published: "2026-10-15T05:00:00+00:00"
ingested_at: "2026-10-16T02:58:34.655064+00:00"
date: "2026-10-16T02:58:34.655064+00:00"
category: "cves"
tags:
  - "QNAP"
  - "TS-453E"
  - "syslog"
  - "format string"
  - "remote code execution"
  - "CVE-2018-10388"
  - "CVE-2018-10389"
  - "Zero Day Initiative"
slug: "2026-10-16-zdi-26-776-qnap-ts-453e-syslog-log-message-format-string-rem"
quote: "The least movement is of importance to all nature. The entire ocean is affected by a pebble."
quote_author: "Blaise Pascal"
---

### Executive Summary
Zero Day Initiative identified a format string vulnerability in the syslog log_message function of QNAP TS-453E devices. The flaw allows unauthenticated, network‑adjacent attackers to execute arbitrary code, with a CVSS score of 7.5. The issue is tracked by CVE‑2018‑10388 and CVE‑2018‑10389.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-10-15T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of QNAP TS-453E devices. Authentication is not required to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.5. The following CVEs are assigned: CVE-2018-10388, CVE-2018-10389.
