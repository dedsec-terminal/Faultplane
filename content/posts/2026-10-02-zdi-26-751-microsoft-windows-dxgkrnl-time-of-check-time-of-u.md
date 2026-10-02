---
title: "ZDI-26-751: Microsoft Windows dxgkrnl Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability"
description: "A local privilege escalation vulnerability (CVE-2026-50375) in Microsoft Windows' dxgkrnl driver allows attackers who can execute low\u2011privileged code ..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-751/"
published: "2026-10-01T05:00:00+00:00"
ingested_at: "2026-10-02T03:52:25.699392+00:00"
date: "2026-10-02T03:52:25.699392+00:00"
category: "cves"
tags:
  - "Windows"
  - "dxgkrnl"
  - "privilege escalation"
  - "ZDI"
  - "CVE-2026-50375"
slug: "2026-10-02-zdi-26-751-microsoft-windows-dxgkrnl-time-of-check-time-of-u"
quote: "What matters is the value we've created in our lives, the people we've made happy and how much we've grown as people."
quote_author: "Daisaku Ikeda"
---

### Executive Summary
A local privilege escalation vulnerability (CVE-2026-50375) in Microsoft Windows' dxgkrnl driver allows attackers who can execute low‑privileged code to gain higher privileges. The flaw is a time‑of‑check/time‑of‑use bug rated CVSS 8.8 by Zero Day Initiative.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-10-01T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 8.8. The following CVEs are assigned: CVE-2026-50375.
