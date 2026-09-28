---
title: "Cloudflare fixes Containers cross-tenant flaw exposing customer data"
description: "Cloudflare patched a flaw in its Containers and Sandboxes service that let Workers Paid customers recover residual data from other customers\u2019 containe..."
source: "Bleeping Computer"
source_url: "https://www.bleepingcomputer.com/news/security/cloudflare-fixes-containers-cross-tenant-flaw-exposing-customer-data/"
published: "2026-09-27T14:13:31+00:00"
ingested_at: "2026-09-28T03:22:54.017586+00:00"
date: "2026-09-28T03:22:54.017586+00:00"
category: "vulnerabilities"
tags:
  - "cloudflare"
  - "containers"
  - "cross-tenant"
  - "data-exposure"
  - "workers"
slug: "2026-09-28-cloudflare-fixes-containers-cross-tenant-flaw-exposing-custo"
quote: "We could never learn to be brave and patient if there were only joy in the world."
quote_author: "Helen Keller"
---

### Executive Summary
Cloudflare patched a flaw in its Containers and Sandboxes service that let Workers Paid customers recover residual data from other customers’ containers on the same physical host. The vulnerability allowed cross‑tenant data leakage, potentially exposing sensitive information. The fix prevents unauthorized access to leftover data and mitigates the risk of data exposure across tenants.

---
**Intelligence Metadata**
- **Source Publisher:** Bleeping Computer
- **Published Date:** 2026-09-27T14:13:31+00:00
- **Category:** vulnerabilities

**Original Description:**
Cloudflare has fixed a vulnerability in Containers and Sandboxes that allowed customers with a Workers Paid account to recover residual data from other customers' containers on the same physical host. [...]
