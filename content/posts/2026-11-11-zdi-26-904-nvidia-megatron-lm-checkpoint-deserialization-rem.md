---
title: "ZDI-26-904: NVIDIA Megatron-LM Checkpoint Deserialization Remote Code Execution Vulnerability"
description: "A remote code execution vulnerability (CVE-2026-65110) exists in NVIDIA Megatron-LM's checkpoint deserialization. Attackers can trigger it by opening ..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-904/"
published: "2026-11-10T06:00:00+00:00"
ingested_at: "2026-11-11T04:31:19.586312+00:00"
date: "2026-11-11T04:31:19.586312+00:00"
category: "cves"
tags:
  - "NVIDIA"
  - "Megatron-LM"
  - "deserialization"
  - "remote-code-execution"
  - "CVE-2026-65110"
slug: "2026-11-11-zdi-26-904-nvidia-megatron-lm-checkpoint-deserialization-rem"
quote: "If we are facing in the right direction, all we have to do is keep on walking."
quote_author: "Unknown"
---

### Executive Summary
A remote code execution vulnerability (CVE-2026-65110) exists in NVIDIA Megatron-LM's checkpoint deserialization. Attackers can trigger it by opening a malicious file, requiring user interaction. The Zero Day Initiative rated it CVSS 7.8. This flaw allows arbitrary code execution on affected installations.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-11-10T06:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of NVIDIA Megatron-LM. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-65110.
