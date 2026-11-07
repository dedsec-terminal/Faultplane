---
title: "ZDI-26-896: (Pwn2Own) Home Assistant Green Cleartext Storage of Credentials Local Privilege Escalation Vulnerability"
description: "A local privilege escalation vulnerability (CVE-2026-91131) in Home Assistant Green allows attackers who can execute low\u2011privileged code in a containe..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-896/"
published: "2026-11-06T06:00:00+00:00"
ingested_at: "2026-11-07T04:27:16.247841+00:00"
date: "2026-11-07T04:27:16.247841+00:00"
category: "cves"
tags:
  - "homeassistant"
  - "privilege-escalation"
  - "cve-2026-91131"
  - "pwn2own"
  - "zero-day-initiative"
slug: "2026-11-07-zdi-26-896-pwn2own-home-assistant-green-cleartext-storage-of"
quote: "A life spent making mistakes is not only more honourable but more useful than a life spent in doing nothing."
quote_author: "Bernard Shaw"
---

### Executive Summary
A local privilege escalation vulnerability (CVE-2026-91131) in Home Assistant Green allows attackers who can execute low‑privileged code in a container to read cleartext credentials and elevate privileges. The flaw, identified by Zero Day Initiative as ZDI‑26‑896, carries a CVSS score of 8.8.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-11-06T06:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows local attackers to escalate privileges on affected installations of Home Assistant Green. An attacker must first obtain the ability to execute low-privileged code within a container on the target system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 8.8. The following CVEs are assigned: CVE-2026-91131.
