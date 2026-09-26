---
title: "Don't let TEEs break your MPC"
description: "Threshold signature schemes combine multi\u2011party computation (MPC) with trusted execution environments (TEEs) to enhance security. The article explains..."
source: "Trail of Bits"
source_url: "https://blog.trailofbits.com/2026/09/25/dont-let-tees-break-your-mpc/"
published: "2026-09-25T11:00:00+00:00"
ingested_at: "2026-09-26T03:17:57.889664+00:00"
date: "2026-09-26T03:17:57.889664+00:00"
category: "research"
tags:
  - "MPC"
  - "TEE"
  - "attestation"
  - "cryptography"
  - "security"
slug: "2026-09-26-don-t-let-tees-break-your-mpc"
quote: "You only lose what you cling to."
quote_author: "Buddha"
---

### Executive Summary
Threshold signature schemes combine multi‑party computation (MPC) with trusted execution environments (TEEs) to enhance security. The article explains how MPC’s security depends on participant behavior—semi‑honest vs malicious—and how TEE attestation can elevate a semi‑honest protocol to provide malicious‑security guarantees by ensuring correct implementation. It highlights pitfalls such as host rollback attacks that can cause nonce reuse and key leakage, and offers best practices: strong attestation, binding to party identities, and treating the TEE as defense‑in‑depth rather than a substitute for sound protocol design.

---
**Intelligence Metadata**
- **Source Publisher:** Trail of Bits
- **Published Date:** 2026-09-25T11:00:00+00:00
- **Category:** research

**Original Description:**
Threshold signature schemes, a form of multi-party computation (MPC) that lets a set of parties sign together without any one of them holding the key, are increasingly deployed inside trusted execution environments (TEEs). The combination is intended to amplify security for sensitive computations: MPC distributes trust across multiple independent parties, while TEEs root trust in the hardware manufacturer and its attestation infrastructure. But subtle issues can arise when running an MPC prot...
