---
title: 'VU#701544: Retraction of mpc-lib Hardened Derivation Vulnerability'
description: Fireblocks’ mpc-lib library was reported to contain a fail‑open flaw
  in its BIP32 hardened derivation that could allow an attacker with a compromised...
source: CERT/CC Vulnerability Notes
source_url: https://kb.cert.org/vuls/id/701544
published: '2026-10-26T22:45:54+00:00'
ingested_at: '2026-11-27T19:47:03.210902+00:00'
date: '2026-11-27T19:47:03.210902+00:00'
category: vulnerabilities
tags:
- cryptography
- BIP32
- MPC
- Fireblocks
slug: 2026-11-27-vu-701544-retraction-of-mpc-lib-hardened-derivation-vulnerab
quote: Fortune befriends the bold.
quote_author: John Dryden
---

### Executive Summary

Fireblocks’ mpc-lib library was reported to contain a fail‑open flaw in its BIP32 hardened derivation that could allow an attacker with a compromised lower‑level MPC share to recover ancestor shares. Fireblocks clarified that their signing protocols use only non‑hardened derivation and treat hardened indices as non‑hardened, meaning that effective exploitation would require privileged access that already includes the master share, rendering the issue moot. The reported impact—loss of post‑compromise ancestor isolation and degradation of threshold security—was therefore deemed invalid. Defensive guidance includes treating chain codes as secret, avoiding reliance on hardened derivation for isolation, and auditing derivation paths for hardened segments, though no vendor fix is available.

### Original Overview

Overview Fireblocks' mpc-lib library contains a cryptographic fail-open vulnerability in its BIP32 hardened derivation implementation in the case of a missing private parent key. This breaks the ancestor isolation property of hardened derivation, allowing an attacker with a compromised lower-level signer share to recover the higher-level share it was derived from. After reviewing the feedback from Fireblocks and further analysis of the case, we have determined that this does not constitute a valid vulnerability. Fireblocks clarified that mpc-lib's signing protocols use only non-hardened BIP32 derivation and that a hardened index is handled as a non-hardened one. Effective exploitation would require privileged access, at which point the attacker would already hold the master share,...
