---
title: "ZDI-26-747: Wireshark RF4CE Packet Parsing Buffer Overflow RCE Vulnerability"
description: "A buffer overflow in Wireshark\u2019s RF4CE packet parser allows remote attackers to execute arbitrary code when a user opens a malicious file or visits a ..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-747/"
published: "2026-09-23T05:00:00+00:00"
ingested_at: "2026-09-24T02:57:41.797599+00:00"
date: "2026-09-24T02:57:41.797599+00:00"
category: "cves"
tags:
  - "Wireshark"
  - "RF4CE"
  - "buffer overflow"
  - "remote code execution"
  - "CVE-2026-96417"
  - "Zero Day Initiative"
slug: "2026-09-24-zdi-26-747-wireshark-rf4ce-packet-parsing-buffer-overflow-rc"
quote: "Life is 10% what happens to you and 90% how you react to it."
quote_author: "Charles Swindoll"
---

### Executive Summary
A buffer overflow in Wireshark’s RF4CE packet parser allows remote attackers to execute arbitrary code when a user opens a malicious file or visits a malicious page. The vulnerability, identified as CVE-2026-96417, has a CVSS score of 7.8 and was disclosed by Zero Day Initiative.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-23T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of Wireshark. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-96417.
