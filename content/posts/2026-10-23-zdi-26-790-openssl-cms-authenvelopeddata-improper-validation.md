---
title: "ZDI-26-790: OpenSSL CMS AuthEnvelopedData Improper Validation of Integrity Check Value Vulnerability"
description: "Zero Day Initiative (ZDI) identified CVE-2026-34182, an OpenSSL vulnerability that allows network\u2011adjacent attackers to tamper with CMS AuthEnvelopedD..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-790/"
published: "2026-10-22T05:00:00+00:00"
ingested_at: "2026-10-23T03:11:23.558142+00:00"
date: "2026-10-23T03:11:23.558142+00:00"
category: "cves"
tags:
  - "OpenSSL"
  - "CMS"
  - "AuthEnvelopedData"
  - "CVE-2026-34182"
  - "Zero Day Initiative"
  - "Integrity Check"
  - "Network Adjacent"
slug: "2026-10-23-zdi-26-790-openssl-cms-authenvelopeddata-improper-validation"
quote: "An ant on the move does more than a dozing ox"
quote_author: "Lao Tzu"
---

### Executive Summary
Zero Day Initiative (ZDI) identified CVE-2026-34182, an OpenSSL vulnerability that allows network‑adjacent attackers to tamper with CMS AuthEnvelopedData messages by bypassing integrity‑check validation. The flaw requires the attacker to modify CMS messages, and the CVSS score is 3.1. Exploitation could compromise message authenticity on affected installations.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-10-22T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows network-adjacent attackers to tamper with CMS AuthEnvelopedData messages on affected installations of OpenSSL. An attacker must first obtain the ability to modify CMS AuthEnvelopedData messages in order to exploit this vulnerability. The ZDI has assigned a CVSS rating of 3.1. The following CVEs are assigned: CVE-2026-34182.
