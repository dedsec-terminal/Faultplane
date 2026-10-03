---
title: "SequenceHash: multihashing for the rest of us"
description: "Trail of Bits introduces SequenceHash and SequenceMAC, flexible multihashing constructions that work with any secure hash function (e.g., SHA\u2011256/384/..."
source: "Trail of Bits"
source_url: "https://blog.trailofbits.com/2026/10/02/sequencehash-multihashing-for-the-rest-of-us/"
published: "2026-10-02T11:00:00+00:00"
ingested_at: "2026-10-03T03:36:27.794269+00:00"
date: "2026-10-03T03:36:27.794269+00:00"
category: "research"
tags:
  - "multihashing"
  - "hash functions"
  - "cryptography"
  - "SequenceHash"
  - "SequenceMAC"
  - "Trail of Bits"
  - "C2SP"
slug: "2026-10-03-sequencehash-multihashing-for-the-rest-of-us"
quote: "Though no one can go back and make a brand new start, anyone can start from now and make a brand new ending."
quote_author: "Unknown"
---

### Executive Summary
Trail of Bits introduces SequenceHash and SequenceMAC, flexible multihashing constructions that work with any secure hash function (e.g., SHA‑256/384/512, BLAKE, RIPEMD). They aim to prevent ambiguous input‑encoding attacks and simplify multihashing compared to NIST’s TupleHash. The open‑source spec is part of the Community Cryptography Specification Project (C2SP) and includes Rust, Go, and Python implementations plus test vectors.

---
**Intelligence Metadata**
- **Source Publisher:** Trail of Bits
- **Published Date:** 2026-10-02T11:00:00+00:00
- **Category:** research

**Original Description:**
Multihashing is one of those cryptographic tasks that’s easy not to think about too much. This is unfortunate, because multihashing is a common stumbling point when cryptographers try to use hashes. As part of our goal to “fix software, not bugs,” Trail of Bits is introducing SequenceHash and its sister function SequenceMAC, a pair of related hash constructions that bring secure multihashing to developers using hash functions other than Keccak. We hope SequenceHash and SequenceMAC will help c...
