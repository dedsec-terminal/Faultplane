---
title: "ZDI-26-620: Microsoft Windows UMPDDrvPlgBlt Improper Object Management Local Privilege Escalation Vulnerability"
description: "The Zero Day Initiative (ZDI) identified a local privilege escalation vulnerability (CVE-2026-62712) in Microsoft Windows' UMPDDrvPlgBlt driver. The f..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-620/"
published: "2026-09-08T05:00:00+00:00"
ingested_at: "2026-09-09T02:52:56.351691+00:00"
date: "2026-09-09T02:52:56.351691+00:00"
category: "cves"
tags:
  - "CVE-2026-62712"
  - "Windows"
  - "Privilege Escalation"
  - "Local"
  - "ZDI"
  - "UMPDDrvPlgBlt"
slug: "2026-09-09-zdi-26-620-microsoft-windows-umpddrvplgblt-improper-object-m"
quote: "The beginning of knowledge is the discovery of something we do not understand."
quote_author: "Frank Herbert"
---

### Executive Summary
The Zero Day Initiative (ZDI) identified a local privilege escalation vulnerability (CVE-2026-62712) in Microsoft Windows' UMPDDrvPlgBlt driver. The flaw arises from improper object management, allowing an attacker who can execute low‑privileged code to gain higher privileges on the affected system. The vulnerability has a CVSS score of 7.8.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-08T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-62712.
