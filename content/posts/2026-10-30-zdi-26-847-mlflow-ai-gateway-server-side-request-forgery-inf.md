---
title: "ZDI-26-847: MLflow AI Gateway Server-Side Request Forgery Information Disclosure Vulnerability"
description: "A server\u2011side request forgery (SSRF) vulnerability in MLflow\u2019s AI Gateway allows authenticated attackers to trigger arbitrary outbound requests, poten..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-847/"
published: "2026-10-29T05:00:00+00:00"
ingested_at: "2026-10-30T04:11:46.946320+00:00"
date: "2026-10-30T04:11:46.946320+00:00"
category: "cves"
tags:
  - "MLflow"
  - "Server-Side Request Forgery"
  - "Information Disclosure"
  - "CVE-2026-71211"
  - "ZDI-26-847"
  - "Zero Day Initiative"
slug: "2026-10-30-zdi-26-847-mlflow-ai-gateway-server-side-request-forgery-inf"
quote: "No act of kindness, no matter how small, is ever wasted."
quote_author: "Aesop"
---

### Executive Summary
A server‑side request forgery (SSRF) vulnerability in MLflow’s AI Gateway allows authenticated attackers to trigger arbitrary outbound requests, potentially exposing sensitive data. The flaw, identified as ZDI‑26‑847 and assigned CVE‑2026‑71211, carries a CVSS score of 7.7. Exploitation requires valid credentials, but once achieved it can lead to information disclosure.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-10-29T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to initiate arbitrary server-side requests on affected installations of MLflow. Authentication is required to exploit this vulnerability. The ZDI has assigned a CVSS rating of 7.7. The following CVEs are assigned: CVE-2026-71211.
