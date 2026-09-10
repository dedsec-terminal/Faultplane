---
title: "ZDI-26-645: Fortinet FortiSandbox write_remote_backup_to_crontab Command Injection RCE Vulnerability"
description: "A command injection flaw in Fortinet FortiSandbox\u2019s write_remote_backup_to_crontab function allows authenticated attackers to inject arbitrary cron co..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-645/"
published: "2026-09-09T05:00:00+00:00"
ingested_at: "2026-09-10T02:53:58.275373+00:00"
date: "2026-09-10T02:53:58.275373+00:00"
category: "cves"
tags:
  - "Fortinet"
  - "FortiSandbox"
  - "command injection"
  - "remote code execution"
  - "CVE-2026-84387"
slug: "2026-09-10-zdi-26-645-fortinet-fortisandbox-write-remote-backup-to-cron"
quote: "A thing long expected takes the form of the unexpected when at last it comes."
quote_author: "Mark Twain"
---

### Executive Summary
A command injection flaw in Fortinet FortiSandbox’s write_remote_backup_to_crontab function allows authenticated attackers to inject arbitrary cron commands, leading to remote code execution. The vulnerability, identified as CVE-2026-84387, carries a CVSS score of 7.2 and was disclosed by Zero Day Initiative.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-09T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fortinet FortiSandbox. Authentication is required to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.2. The following CVEs are assigned: CVE-2026-84387.
