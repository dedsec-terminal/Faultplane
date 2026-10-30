---
title: "ZDI-26-845: MLflow Statsmodels _load_model Deserialization Remote Code Execution Vulnerability"
description: "A remote code execution vulnerability (CVE-2024-37052) exists in MLflow's Statsmodels _load_model deserialization. Attackers can execute arbitrary cod..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-845/"
published: "2026-10-29T05:00:00+00:00"
ingested_at: "2026-10-30T04:12:02.594335+00:00"
date: "2026-10-30T04:12:02.594335+00:00"
category: "cves"
tags:
  - "MLflow"
  - "Statsmodels"
  - "deserialization"
  - "remote code execution"
  - "CVE-2024-37052"
slug: "2026-10-30-zdi-26-845-mlflow-statsmodels-load-model-deserialization-rem"
quote: "Every human being is the author of his own health or disease."
quote_author: "Buddha"
---

### Executive Summary
A remote code execution vulnerability (CVE-2024-37052) exists in MLflow's Statsmodels _load_model deserialization. Attackers can execute arbitrary code on affected installations when a user visits a malicious page or opens a malicious file. The vulnerability has a CVSS score of 7.8.

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-10-29T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to execute arbitrary code on affected installations of MLflow. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2024-37052.
