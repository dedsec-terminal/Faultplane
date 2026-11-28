---
title: Autodesk AutoCAD DDS File Parsing Heap-based Buffer Overflow Vulnerability
  (ZDI-26-1147)
description: A heap-based buffer overflow in Autodesk AutoCAD’s parsing of DDS files
  allows remote attackers to execute arbitrary code when a user opens a maliciou...
source: Zero Day Initiative
source_url: http://www.zerodayinitiative.com/advisories/ZDI-26-1147/
published: '2026-11-24T06:00:00+00:00'
ingested_at: '2026-11-28T06:05:31.054979+00:00'
date: '2026-11-28T06:05:31.054979+00:00'
category: vulnerabilities
tags:
- autodesk
- autocad
- dds
- heap-buffer-overflow
- remote-code-execution
slug: 2026-11-28-autodesk-autocad-dds-file-parsing-heap-based-buffer-overflow
quote: Character is like a tree and reputation like a shadow. The shadow is what we
  think of it; the tree is the real thing.
quote_author: Abraham Lincoln
---

### Executive Summary

A heap-based buffer overflow in Autodesk AutoCAD’s parsing of DDS files allows remote attackers to execute arbitrary code when a user opens a malicious file or visits a malicious page. The flaw stems from insufficient validation of user-supplied data length before copying it to a heap buffer, enabling code execution in the context of the current process. Autodesk has released an update to fix the issue; users are advised to apply the patch promptly.

### Original Overview

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk AutoCAD. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DDS files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process. Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2026-0021 2026-09-03 - Vulnerability reported to vendor 2026-11-24 - Coordinated public release of advisory...
