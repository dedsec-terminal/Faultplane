---
title: "AutomationDirect C-More EA9 Programming Software Vulnerability CVE-2026-127280"
description: "CVE-2026-127280 is a heap-based buffer overflow in AutomationDirect C-More EA9 Programming Software <=V6.80. A crafted project file can corrupt heap m..."
source: "CISA Cyber Advisories"
source_url: "https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-01"
published: "2026-11-24T12:00:00+00:00"
ingested_at: "2026-11-26T06:40:13.809554+00:00"
date: "2026-11-26T06:40:13.809554+00:00"
category: "cves"
tags:
  - "automationdirect"
  - "cve-2026-127280"
  - "heap-buffer-overflow"
  - "industrial-control"
  - "critical-infrastructure"
slug: "2026-11-26-automationdirect-c-more-ea9-programming-software-vulnerabili"
quote: "A life spent making mistakes is not only more honourable but more useful than a life spent in doing nothing."
quote_author: "Bernard Shaw"
---

### Executive Summary
CVE-2026-127280 is a heap-based buffer overflow in AutomationDirect C-More EA9 Programming Software <=V6.80. A crafted project file can corrupt heap memory, causing instability or crash, potentially enabling arbitrary code execution if a user opens the file. The flaw affects worldwide installations in critical manufacturing, energy, water and wastewater sectors. AutomationDirect released a fix in V6.81; mitigations include isolating affected workstations, restricting remote access, and using dedicated OT networks.

---
**Intelligence Metadata**
- **Source Publisher:** CISA Cyber Advisories
- **Published Date:** 2026-11-24T12:00:00+00:00
- **Category:** cves

**Original Description:**
View CSAF Summary Successful exploitation of this vulnerability could allow attackers to corrupt application memory and cause instability or a crash, potentially leading to arbitrary code execution, if a user is convinced to open a malicious file. The following versions of AutomationDirect C-More EA9 Programming Software are affected: C-More EA9 Programming Software &lt;=V6.80 (CVE-2026-127280) CVSS Vendor Equipment v3 7.8 AutomationDirect C-More EA9 Programming Software 1 Vulnerability Heap-...
