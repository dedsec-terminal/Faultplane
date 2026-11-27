---
title: 'ZDI-26-1152: Oracle Outside In Technology TIFF File Parsing Out-Of-Bounds
  Write Remote Code Execution Vulnerability'
description: A vulnerability in Oracle Outside In Technology’s TIFF file parsing component
  allows remote attackers to trigger an out‑of‑bounds write, potentially l...
source: Zero Day Initiative
source_url: http://www.zerodayinitiative.com/advisories/ZDI-26-1152/
published: '2026-11-24T06:00:00+00:00'
ingested_at: '2026-11-27T19:47:03.200902+00:00'
date: '2026-11-27T19:47:03.200902+00:00'
category: vulnerabilities
tags:
- Oracle
- Out-of-bounds write
- Remote code execution
- CVE-2026-91460
slug: 2026-11-27-zdi-26-1152-oracle-outside-in-technology-tiff-file-parsing-o
quote: Simply put, you believer that things or people make you unhappy, but this is
  not accurate. You make yourself unhappy.
quote_author: Wayne Dyer
---

### Executive Summary

A vulnerability in Oracle Outside In Technology’s TIFF file parsing component allows remote attackers to trigger an out‑of‑bounds write, potentially leading to arbitrary code execution. The flaw requires interaction with the library, though specific attack vectors may differ across implementations. Zero Day Initiative has assigned a CVSS score of 7.8 and published CVE‑2026‑91460 for this issue. No defensive guidance is provided in the source.

### Original Overview

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle Outside In Technology. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-91460.
