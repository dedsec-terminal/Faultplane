---
title: "ZDI-26-749: WatchGuard FireWare OS samld SAMLSession RCE Vulnerability"
description: "A remote code execution vulnerability (CVE-2026-13046) exists in WatchGuard FireWare OS's samld SAMLSession component. The flaw allows attackers who c..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-749/"
published: "2026-09-30T05:00:00+00:00"
ingested_at: "2026-10-01T03:55:18.714140+00:00"
date: "2026-10-01T03:55:18.714140+00:00"
category: "vulnerabilities"
tags:
  - "WatchGuard"
  - "FireWare OS"
  - "SAMLSession"
  - "Remote Code Execution"
  - "CVE-2026-13046"
slug: "2026-10-01-zdi-26-749-watchguard-fireware-os-samld-samlsession-rce-vuln"
quote: "Adversity has the effect of eliciting talents, which in prosperous circumstances would have lain dormant."
quote_author: "Horace"
---

### Executive Summary
A remote code execution vulnerability (CVE-2026-13046) exists in WatchGuard FireWare OS's samld SAMLSession component. The flaw allows attackers who can write to the samld session directory to deserialize untrusted data, leading to arbitrary code execution. The Zero Day Initiative assigned a CVSS score of 7.5.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-09-30T05:00:00+00:00
- **Category:** vulnerabilities

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of WatchGuard FireWare OS. An attacker must first obtain the ability to write to the samld session directory on the target system in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.5. The following CVEs are assigned: CVE-2026-13046.
