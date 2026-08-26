---
title: "State divergence enables unauthorized access"
description: "Trail of Bits discovered a bug in Provenance Blockchain (Cosmos SDK) that lets any user grant themselves admin control over marker accounts without ho..."
source: "Trail of Bits"
source_url: "https://blog.trailofbits.com/2026/08/25/state-divergence-enables-unauthorized-access/"
published: "2026-08-25T11:00:00+00:00"
ingested_at: "2026-08-26T01:07:25.745913+00:00"
date: "2026-08-26T01:07:25.745913+00:00"
category: "vulnerabilities"
tags:
  - "provenance"
  - "cosmos-sdk"
  - "marker"
  - "access-control"
  - "bug"
slug: "2026-08-26-state-divergence-enables-unauthorized-access"
quote: "All truths are easy to understand once they are discovered; the point is to discover them."
quote_author: "Galileo Galilei"
---

### Executive Summary
Trail of Bits discovered a bug in Provenance Blockchain (Cosmos SDK) that lets any user grant themselves admin control over marker accounts without holding tokens. The flaw, present in versions <1.28.0, allows bypassing access checks by exploiting a state divergence in the accountControlsAllSupply function, which compares the caller’s balance to the marker’s stored supply. The issue affected 82 live markers on mainnet and was reported on April 1 2026, patched in v1.28.0 (May 1) and fully fixed in v1.29.0 (June 8).

---
**Intelligence Metadata**
- **Source Publisher:** Trail of Bits
- **Published Date:** 2026-08-25T11:00:00+00:00
- **Category:** vulnerabilities

**Original Description:**
We found and reported a bug in Provenance Blockchain, a public proof-of-stake chain built on Cosmos SDK, that lets any user grant themselves admin control over marker accounts without holding a single token. Provenance covers a range of financial services, including on-chain tokenized loans, private equity tokens, bridged assets, and asset registries. Our bug affected 82 markers representing live financial assets on mainnet. We found the bug, which affects versions before 1.28.0, in March 202...
