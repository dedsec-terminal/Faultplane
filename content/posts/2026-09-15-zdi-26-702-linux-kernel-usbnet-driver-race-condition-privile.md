---
title: "ZDI-26-702: Linux Kernel usbnet Driver Race Condition Privilege Escalation Vulnerability"
description: "A race condition in the Linux kernel usbnet driver allows physically present attackers to gain root privileges without authentication. The vulnerabili..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-702/"
published: "2026-09-14T05:00:00+00:00"
ingested_at: "2026-09-15T03:11:35.858969+00:00"
date: "2026-09-15T03:11:35.858969+00:00"
category: "cves"
tags:
  - "Linux kernel"
  - "usbnet driver"
  - "privilege escalation"
  - "race condition"
  - "CVE-2025-22050"
slug: "2026-09-15-zdi-26-702-linux-kernel-usbnet-driver-race-condition-privile"
quote: "Fortune favours the brave."
quote_author: "Virgil"
---

### Executive Summary
A race condition in the Linux kernel usbnet driver allows physically present attackers to gain root privileges without authentication. The vulnerability, rated CVSS 7.1, is identified as CVE-2025-22050 and can be exploited on affected kernel installations.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-14T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows physically present attackers to escalate privileges on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.1. The following CVEs are assigned: CVE-2025-22050.
