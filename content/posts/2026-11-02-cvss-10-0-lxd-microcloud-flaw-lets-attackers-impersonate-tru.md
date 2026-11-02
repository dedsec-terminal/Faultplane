---
title: "CVSS 10.0 LXD, MicroCloud Flaw Lets Attackers Impersonate Trusted Clients Without a Private Key"
description: "Canonical\u2019s LXD and MicroCloud containers have a critical authentication flaw (CVSS 10.0). An attacker who can reach the HTTPS API and knows a trusted..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/11/critical-lxd-and-microcloud-flaw-cvss.html"
published: "2026-11-01T08:51:31+00:00"
ingested_at: "2026-11-02T04:08:15.870995+00:00"
date: "2026-11-02T04:08:15.870995+00:00"
category: "vulnerabilities"
tags:
  - "LXD"
  - "MicroCloud"
  - "Canonical"
  - "authentication-bypass"
  - "impersonation"
  - "public-key"
  - "HTTPS API"
slug: "2026-11-02-cvss-10-0-lxd-microcloud-flaw-lets-attackers-impersonate-tru"
quote: "The possession of knowledge does not kill the sense of wonder and mystery. There is always more mystery."
quote_author: "Anais Nin"
---

### Executive Summary
Canonical’s LXD and MicroCloud containers have a critical authentication flaw (CVSS 10.0). An attacker who can reach the HTTPS API and knows a trusted client’s public certificate can impersonate that client without possessing its private key. The attacker then gains full cluster and VM access, effectively bypassing authentication.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-11-01T08:51:31+00:00
- **Category:** vulnerabilities

**Original Description:**
A critical flaw in Canonical's LXD and MicroCloud let an attacker log in as a trusted client without holding that client's private key. To do it, the attacker had to reach their HTTPS API over the network and have the trusted client's public certificate. Once in, the attacker would act as that client, with access to the cluster and its virtual machines. If the impersonated account is
