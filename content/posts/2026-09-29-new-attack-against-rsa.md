---
title: "New Attack Against RSA"
description: "ArsTechnica reports on a new implementation of a 2007 RSA forgery attack that bypasses factoring. The attack allows forging digital signatures on unpa..."
source: "Schneier on Security"
source_url: "https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html"
published: "2026-09-28T11:02:58+00:00"
ingested_at: "2026-09-29T03:59:28.512917+00:00"
date: "2026-09-29T03:59:28.512917+00:00"
category: "threat-intel"
tags:
  - "RSA"
  - "digital signatures"
  - "forgery"
  - "subexponential"
  - "cryptanalysis"
slug: "2026-09-29-new-attack-against-rsa"
quote: "Our kindness may be the most persuasive argument for that which we believe."
quote_author: "Gordon Hinckley"
---

### Executive Summary
ArsTechnica reports on a new implementation of a 2007 RSA forgery attack that bypasses factoring. The attack allows forging digital signatures on unpadded RSA keys, does not recover private keys, and operates in subexponential time—faster than factoring. The authors forged 1024‑bit RSA signatures using 1380 CPU core‑years over five months. The technique only applies to pure signatures and is not typical in practice.

---
**Intelligence Metadata**
- **Source Publisher:** Schneier on Security
- **Published Date:** 2026-09-28T11:02:58+00:00
- **Category:** threat-intel

**Original Description:**
ArsTechnica is reporting on a &#8220;new&#8221; attack against RSA, one that bypasses factoring. First, this attack isn&#8217;t new. The original research is from 2007. What is new is the implementation. Second, it is a forgery attack. It allows an attacker to forge digital signatures. It does not recover the private key from the public key. Third, the attack only works against pure signatures. That is, signatures without any formatting or padding. This is not generally how we use RSA in prac...
