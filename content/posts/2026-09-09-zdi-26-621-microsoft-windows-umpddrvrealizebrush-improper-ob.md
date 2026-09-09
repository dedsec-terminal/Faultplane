---
title: "ZDI-26-621: Microsoft Windows UMPDDrvRealizeBrush Improper Object Management Local Privilege Escalation Vulnerability"
description: "A local privilege escalation vulnerability (CVE-2026-62712) in Microsoft Windows' UMPDDrvRealizeBrush driver allows attackers who can execute low\u2011priv..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-621/"
published: "2026-09-08T05:00:00+00:00"
ingested_at: "2026-09-09T02:52:42.177322+00:00"
date: "2026-09-09T02:52:42.177322+00:00"
category: "cves"
tags:
  - "Windows"
  - "privilege escalation"
  - "local"
  - "CVE-2026-62712"
  - "Zero Day Initiative"
  - "UMPDDrvRealizeBrush"
  - "improper object management"
slug: "2026-09-09-zdi-26-621-microsoft-windows-umpddrvrealizebrush-improper-ob"
quote: "Better to have loved and lost, than to have never loved at all."
quote_author: "St. Augustine"
---

### Executive Summary
A local privilege escalation vulnerability (CVE-2026-62712) in Microsoft Windows' UMPDDrvRealizeBrush driver allows attackers who can execute low‑privileged code to gain higher privileges. The flaw stems from improper object management. Zero Day Initiative assigned CVSS 7.8.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-08T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-62712.
