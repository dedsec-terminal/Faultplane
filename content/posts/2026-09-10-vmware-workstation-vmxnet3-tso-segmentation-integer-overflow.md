---
title: "VMware Workstation VMXNET3 TSO Segmentation Integer Overflow Local Privilege Escalation Vulnerability"
description: "A local integer overflow in VMware Workstation's VMXNET3 TSO segmentation can lead to privilege escalation. The flaw requires the attacker to already ..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-647/"
published: "2026-09-09T05:00:00+00:00"
ingested_at: "2026-09-10T02:53:48.047692+00:00"
date: "2026-09-10T02:53:48.047692+00:00"
category: "cves"
tags:
  - "vmware"
  - "workstation"
  - "local-privilege-escalation"
  - "integer-overflow"
  - "cve-2026-59346"
slug: "2026-09-10-vmware-workstation-vmxnet3-tso-segmentation-integer-overflow"
quote: "Slow down and everything you are chasing will come around and catch you."
quote_author: "John De Paola"
---

### Executive Summary
A local integer overflow in VMware Workstation's VMXNET3 TSO segmentation can lead to privilege escalation. The flaw requires the attacker to already run high‑privileged code on the guest OS. The Zero Day Initiative rated the vulnerability CVSS 7.5 and assigned CVE‑2026‑59346.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-09T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows local attackers to escalate privileges on affected installations of VMware Workstation. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.5. The following CVEs are assigned: CVE-2026-59346.
