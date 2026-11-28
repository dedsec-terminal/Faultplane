---
title: Autodesk AutoCAD DWG File Parsing Integer Overflow Remote Code Execution Vulnerability
description: A flaw in Autodesk AutoCAD’s DWG file parser allows remote attackers
  to trigger an integer overflow and execute arbitrary code in the context of the
  c...
source: Zero Day Initiative
source_url: http://www.zerodayinitiative.com/advisories/ZDI-26-1148/
published: '2026-11-24T06:00:00+00:00'
ingested_at: '2026-11-28T06:05:31.053979+00:00'
date: '2026-11-28T06:05:31.053979+00:00'
category: vulnerabilities
tags:
- autodesk
- autocad
- integer-overflow
- remote-code-execution
slug: 2026-11-28-autodesk-autocad-dwg-file-parsing-integer-overflow-remote-co
quote: Character develops itself in the stream of life.
quote_author: Johann Wolfgang von Goethe
---

### Executive Summary

A flaw in Autodesk AutoCAD’s DWG file parser allows remote attackers to trigger an integer overflow and execute arbitrary code in the context of the current process, but only if the victim opens a malicious file or visits a malicious page. The vulnerability, reported to Autodesk on 2026‑10‑01, was publicly disclosed on 2026‑11‑24 and is mitigated by a vendor‑issued update. Users and administrators should apply the Autodesk patch immediately to prevent exploitation.

### Original Overview

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk AutoCAD. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DWG files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process. Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2026-0021 2026-10-01 - Vulnerability reported to vendor 2026-11-24 - Coordinated public release...
