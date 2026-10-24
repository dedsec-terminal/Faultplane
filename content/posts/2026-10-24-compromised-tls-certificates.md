---
title: "Compromised TLS Certificates"
description: "Indian CA eMudhra Limited issued eight TLS certificates with severely weak private keys, ranging from 3 to 8 bits of entropy, far below the expected 3..."
source: "Schneier on Security"
source_url: "https://www.schneier.com/blog/archives/2026/10/compromised-tls-certificates.html"
published: "2026-10-23T11:04:22+00:00"
ingested_at: "2026-10-24T03:05:46.295644+00:00"
date: "2026-10-24T03:05:46.295644+00:00"
category: "threat-intel"
tags:
  - "TLS"
  - "certificate"
  - "eMudhra"
  - "weak-keys"
  - "cryptography"
  - "CA"
slug: "2026-10-24-compromised-tls-certificates"
quote: "Who looks outside, dreams; who looks inside, awakes."
quote_author: "Carl Jung"
---

### Executive Summary
Indian CA eMudhra Limited issued eight TLS certificates with severely weak private keys, ranging from 3 to 8 bits of entropy, far below the expected 384 bits for NIST P‑384 EC keys. The flaw exposes the certificates to compromise and undermines trust in the CA's cryptographic practices.

---
**Intelligence Metadata**
- **Source Publisher:** Schneier on Security
- **Published Date:** 2026-10-23T11:04:22+00:00
- **Category:** threat-intel

**Original Description:**
The Indian CA eMudhra Limited has eight TLS certificates with laughably weak private keys: The compromised eMudhra keys were defective at a level that’s challenging the imagination of many of the engineers studying the incident. A normal size for a NIST P-384 elliptic curve cryptography private key contains roughly 384 bits of entropy, a size allowing almost 2384, or a number with 116 digits, different possibilities. The private key sizes of the compromised keys ranged from 3 to 8 bits. Aston...
