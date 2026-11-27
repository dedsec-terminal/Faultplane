---
title: Oracle Outside In Technology BMP File Parsing Out-Of-Bounds Write Remote Code
  Execution Vulnerability
description: A vulnerability in Oracle Outside In Technology’s BMP file parsing allows
  remote attackers to execute arbitrary code on affected installations. The fl...
source: Zero Day Initiative
source_url: http://www.zerodayinitiative.com/advisories/ZDI-26-1153/
published: '2026-11-24T06:00:00+00:00'
ingested_at: '2026-11-27T19:47:03.199902+00:00'
date: '2026-11-27T19:47:03.199902+00:00'
category: vulnerabilities
tags:
- Oracle
- Out-of-bounds write
- Remote code execution
- CVE-2026-91459
slug: 2026-11-27-oracle-outside-in-technology-bmp-file-parsing-out-of-bounds
quote: No one has ever become poor by giving.
quote_author: Anne Frank
---

### Executive Summary

A vulnerability in Oracle Outside In Technology’s BMP file parsing allows remote attackers to execute arbitrary code on affected installations. The flaw is an out‑of‑bounds write that can be triggered by interacting with the library, though specific attack vectors may differ by implementation. Zero Day Initiative has assigned CVE‑2026‑91459 a CVSS score of 7.8. No defensive guidance is provided in the source, but patching or disabling the vulnerable component is implied.

### Original Overview

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle Outside In Technology. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-91459.
