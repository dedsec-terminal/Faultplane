---
title: "Package managers have an integrity problem"
description: "Trail of Bits tested 25 popular package managers for integrity checks against malicious repositories. Fewer than half use lockfiles that automatically..."
source: "Trail of Bits"
source_url: "https://blog.trailofbits.com/2026/10/14/package-managers-have-an-integrity-problem/"
published: "2026-10-14T11:00:00+00:00"
ingested_at: "2026-10-15T03:00:51.300733+00:00"
date: "2026-10-15T03:00:51.300733+00:00"
category: "research"
tags:
  - "package managers"
  - "cryptographic hashes"
  - "lockfiles"
  - "supply chain attacks"
  - "integrity verification"
  - "Trail of Bits"
slug: "2026-10-15-package-managers-have-an-integrity-problem"
quote: "Yesterday is history. Tomorrow is a mystery. And today? Today is a gift that's why they call it the present."
quote_author: "Unknown"
---

### Executive Summary
Trail of Bits tested 25 popular package managers for integrity checks against malicious repositories. Fewer than half use lockfiles that automatically verify tampering, and only two verify every downloaded package. Most rely on cryptographic hashes or signatures, but many implementations require extra configuration, use insecure hashes, or lack signatures entirely. The study highlights a wide variance in supply‑chain security across ecosystems.

---
**Intelligence Metadata**
- **Source Publisher:** Trail of Bits
- **Published Date:** 2026-10-14T11:00:00+00:00
- **Category:** research

**Original Description:**
I tested 25 of the most popular package managers to check whether they detect a compromised package repository injecting malicious code into legitimate packages. This code integrity problem could be solved using cryptographic hashes or signatures, but many package managers are still vulnerable to this threat. Of the 25 package managers reviewed1, fewer than half used lockfiles that checked for tampering by default, and only two verified the integrity of every package they downloaded. Supply-c...
