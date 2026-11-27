---
title: Siemens RUGGEDCOM APE1808 Affected by Fortinet Double Free Vulnerability (CVE-2026-106175)
description: Fortinet disclosed a Double Free vulnerability (CVE-2026-106175) in FortiOS,
  FortiProxy, and FortiSwitch that could allow a local authenticated attack...
source: CISA Cyber Advisories
source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-07
published: '2026-11-17T12:00:00+00:00'
ingested_at: '2026-11-27T19:47:03.204902+00:00'
date: '2026-11-27T19:47:03.204902+00:00'
category: vulnerabilities
tags:
- CVE-2026-106175
- FortiOS
- Siemens RUGGEDCOM
- Double Free
- Industrial Control Systems
slug: 2026-11-27-siemens-ruggedcom-ape1808-affected-by-fortinet-double-free-v
quote: If we learn to open our hearts, anyone, including the people who drive us crazy,
  can be our teacher.
quote_author: Pema Chodron
---

### Executive Summary

Fortinet disclosed a Double Free vulnerability (CVE-2026-106175) in FortiOS, FortiProxy, and FortiSwitch that could allow a local authenticated attacker to crash the newcli daemon on Siemens RUGGEDCOM APE1808 devices. Siemens confirmed that the affected product is the RUGGEDCOM APE1808 when paired with Fortigate NGFW and recommends updating the Fortigate firmware to version 7.6.9 or later following the secure update procedure. Defensive guidance from Siemens and CISA includes isolating control‑system networks from the internet, protecting device access with firewalls or VPNs, and following Siemens’ operational guidelines for industrial security. Users are advised to contact Siemens ProductCERT for detailed remediation information and to perform risk assessments before deploying defensive measures.

### Original Overview

View CSAF Summary Fortinet has published information on a Double Free vulnerability in FortiOS. This advisory lists the related Siemens Industrial products. Siemens recommends to update Fortigate NGFW to V7.6.9 or later following the secure update recommendation procedure. Contact customer support to receive detailed information The following versions of Siemens RUGGEDCOM APE1808 are affected: RUGGEDCOM APE1808 vers:all/* (CVE-2026-106175) CVSS Vendor Equipment v3 2.3 Siemens RUGGEDCOM APE1808 1 Vulnerability Double Free Background Critical Infrastructure Sectors: Critical Manufacturing Countries/Areas Deployed: Worldwide Company Headquarters Location: Germany Vulnerabilities CVE-2026-106175 A Double Free vulnerability [CWE-415] in FortiOS, FortiProxy and FortiSwitch may allow a local...
