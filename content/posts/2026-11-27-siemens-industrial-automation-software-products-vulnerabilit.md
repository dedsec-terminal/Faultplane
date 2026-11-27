---
title: Siemens Industrial Automation Software Products Vulnerability (CVE-2026-111497)
description: On October 21, 2026, the Node.js project released security updates for
  a critical out‑of‑bounds write in the Brotli decoder, known as Node2Shell (CVE‑...
source: CISA Cyber Advisories
source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-03
published: '2026-11-17T12:00:00+00:00'
ingested_at: '2026-11-27T19:47:03.203902+00:00'
date: '2026-11-27T19:47:03.203902+00:00'
category: vulnerabilities
tags:
- CVE-2026-111497
- Brotli
- Siemens
- Industrial Automation
slug: 2026-11-27-siemens-industrial-automation-software-products-vulnerabilit
quote: We are Divine enough to ask and we are important enough to receive.
quote_author: Wayne Dyer
---

### Executive Summary

On October 21, 2026, the Node.js project released security updates for a critical out‑of‑bounds write in the Brotli decoder, known as Node2Shell (CVE‑2026‑111497). The flaw could allow a remote attacker to corrupt memory, cause a denial of service, or potentially execute arbitrary code. Siemens identified a wide range of its industrial automation products—such as COMOS Walkinside, gDAP, Project Server Web Administration Tool, and various SIMATIC WinCC and TIA components—as affected. Siemens has issued new versions for many of these products and recommends customers update immediately; for products without a current fix, the vendor advises temporarily disabling Brotli compression/decompression if it is not essential. The advisory stresses that the vulnerability is remote‑unattended and could impact critical manufacturing, food and agriculture, and energy sectors worldwide.

### Original Overview

View CSAF Summary On October 21, 2026, the Node.js project released security updates addressing a critical vulnerability in the Brotli decoder bundled with Node.js, commonly referred to as "Node2Shell" (tracked as CVE-2026-111497). The vulnerability is an out-of-bounds write that could allow a remote attacker to cause memory corruption and potentially execute arbitrary code. This advisory covers the status of impact of various Siemens products. Siemens has released new versions for several affected products and recommends to update to the latest versions. Siemens is preparing further fixes and recommends specific mitigations for products where fixes are not or not yet available. The following versions of Siemens Industrial Automation Software Products are affected: COMOS Walkinside...
