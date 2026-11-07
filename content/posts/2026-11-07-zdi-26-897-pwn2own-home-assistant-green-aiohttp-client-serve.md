---
title: "ZDI-26-897: (Pwn2Own) Home Assistant Green aiohttp_client Server-Side Request Forgery Vulnerability"
description: "A server\u2011side request forgery (SSRF) flaw in Home Assistant Green\u2019s aiohttp_client component lets unauthenticated, network\u2011adjacent attackers trigger ..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-897/"
published: "2026-11-06T06:00:00+00:00"
ingested_at: "2026-11-07T04:27:08.811814+00:00"
date: "2026-11-07T04:27:08.811814+00:00"
category: "cves"
tags:
  - "Home Assistant"
  - "SSRF"
  - "aiohttp"
  - "CVE-2026-91131"
  - "ZDI-26-897"
  - "Pwn2Own"
slug: "2026-11-07-zdi-26-897-pwn2own-home-assistant-green-aiohttp-client-serve"
quote: "Better to have loved and lost, than to have never loved at all."
quote_author: "St. Augustine"
---

### Executive Summary
A server‑side request forgery (SSRF) flaw in Home Assistant Green’s aiohttp_client component lets unauthenticated, network‑adjacent attackers trigger arbitrary outbound requests. The vulnerability, identified as CVE‑2026‑91131 and assigned CVSS 5.4, was showcased in the Pwn2Own contest (ZDI‑26‑897). No authentication is required, making it exploitable by local network actors.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-11-06T06:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows network-adjacent attackers to initiate arbitrary server-side requests on affected installations of Home Assistant Green. Authentication is not required to exploit this vulnerability. The ZDI has assigned a CVSS rating of 5.4. The following CVEs are assigned: CVE-2026-91131.
