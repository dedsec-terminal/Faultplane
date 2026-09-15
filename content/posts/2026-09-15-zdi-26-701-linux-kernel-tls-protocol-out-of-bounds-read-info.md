---
title: "ZDI-26-701: Linux Kernel TLS Protocol Out-Of-Bounds Read Information Disclosure Vulnerability"
description: "A local privilege escalation is required to exploit the Linux kernel TLS protocol out-of-bounds read vulnerability (CVE-2026-64046). The flaw allows a..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-701/"
published: "2026-09-14T05:00:00+00:00"
ingested_at: "2026-09-15T03:11:38.092593+00:00"
date: "2026-09-15T03:11:38.092593+00:00"
category: "cves"
tags:
  - "Linux Kernel"
  - "TLS"
  - "Out-of-bounds read"
  - "Information Disclosure"
  - "CVE-2026-64046"
  - "ZDI-26-701"
slug: "2026-09-15-zdi-26-701-linux-kernel-tls-protocol-out-of-bounds-read-info"
quote: "I believe that every person is born with talent."
quote_author: "Maya Angelou"
---

### Executive Summary
A local privilege escalation is required to exploit the Linux kernel TLS protocol out-of-bounds read vulnerability (CVE-2026-64046). The flaw allows attackers to read sensitive kernel memory, potentially exposing confidential data. The Zero Day Initiative assigned CVSS 6.7. This issue affects kernel versions that implement the TLS protocol without proper bounds checks.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-14T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows local attackers to disclose sensitive information on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 6.7. The following CVEs are assigned: CVE-2026-64046.
