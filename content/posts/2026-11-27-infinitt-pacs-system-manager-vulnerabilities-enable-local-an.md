---
title: INFINITT PACS System Manager Vulnerabilities Enable Local and Remote Code Execution
description: INFINITT Healthcare disclosed that versions 3.0.11.3 and 3.0.11.5 of
  its PACS System Manager contain two separate code‑execution vulnerabilities (CVE‑...
source: CERT/CC Vulnerability Notes
source_url: https://kb.cert.org/vuls/id/203719
published: '2026-11-02T15:38:19+00:00'
ingested_at: '2026-11-27T19:47:03.209902+00:00'
date: '2026-11-27T19:47:03.209902+00:00'
category: vulnerabilities
tags:
- INFINITT
- PACS
- CVE-2026-16305
- CVE-2026-16306
- remote code execution
- local code execution
slug: 2026-11-27-infinitt-pacs-system-manager-vulnerabilities-enable-local-an
quote: If you have knowledge, let others light their candles in it.
quote_author: Margaret Fuller
---

### Executive Summary

INFINITT Healthcare disclosed that versions 3.0.11.3 and 3.0.11.5 of its PACS System Manager contain two separate code‑execution vulnerabilities (CVE‑2026‑16305 and CVE‑2026‑16306). The first flaw allows a local, low‑privileged user to modify an update manifest and execute arbitrary commands with administrative rights, while the second flaw permits a remote attacker to trigger unsafe command dispatch via a crafted imodular:// URI, potentially accessing local files or establishing outbound connections. No evidence of exploitation has been reported, but the vulnerabilities could enable attackers to install malware, modify or exfiltrate data, and maintain persistence on affected workstations. INFINITT recommends upgrading to the patched 3.0.12.3 or 3.0.12.5 releases as soon as operationally feasible.

### Original Overview

Overview INFINITT PACS installations using System Manager versions 3.0.11.3 and 3.0.11.5 contain vulnerabilities that may allow an attacker to execute arbitrary code. INFINITT Healthcare has remediated the issues in System Manager versions 3.0.12.3 and 3.0.12.5. Description INFINITT PACS is an enterprise web-based medical imaging platform that stores, retrieves, and displays patient scans. CVE-2026-16305 An improperly protected update manifest may allow a local attacker to execute commands with administrative privileges when an update is approved. SmartExecute.exe reads and runs commands from execlist.txt after an update. Because of insecure file permissions on execlist.txt , a low-privileged attacker can modify the file before it is processed to add arbitrary malicious commands....
