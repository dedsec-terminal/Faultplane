---
title: "ZDI-26-906: X.Org Server libX11 XkbGetMap Reply Heap-based Buffer Overflow Remote Code Execution Vulnerability"
description: "A heap-based buffer overflow in X.Org Server's libX11 XkbGetMap Reply allows remote attackers to execute arbitrary code when a target connects to a ma..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-906/"
published: "2026-11-10T06:00:00+00:00"
ingested_at: "2026-11-11T04:31:08.299685+00:00"
date: "2026-11-11T04:31:08.299685+00:00"
category: "cves"
tags:
  - "X.Org"
  - "libX11"
  - "buffer-overflow"
  - "remote-code-execution"
  - "CVE-2026-88806"
slug: "2026-11-11-zdi-26-906-x-org-server-libx11-xkbgetmap-reply-heap-based-bu"
quote: "If we learn to open our hearts, anyone, including the people who drive us crazy, can be our teacher."
quote_author: "Pema Chodron"
---

### Executive Summary
A heap-based buffer overflow in X.Org Server's libX11 XkbGetMap Reply allows remote attackers to execute arbitrary code when a target connects to a malicious X11 server. CVE-2026-88806, CVSS 8.8.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-11-10T06:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of X.Org Server. User interaction is required to exploit this vulnerability in that the target must connect to a malicious X11 server. The ZDI has assigned a CVSS rating of 8.8. The following CVEs are assigned: CVE-2026-88806.
