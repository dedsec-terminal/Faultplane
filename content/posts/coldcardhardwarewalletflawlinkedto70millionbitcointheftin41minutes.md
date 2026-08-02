---
title: "Coldcard Hardware Wallet Flaw Linked to $70 Million Bitcoin Theft in 41 Minutes"
date: 2026-08-01T17:17:22+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A significant flaw in the Coldcard hardware wallet, made by Coinkite, has been linked to the theft of approximately $70 million in Bitcoin. The vulnerability, which was discovered by Galaxy Research, allowed an attacker to drain 1,196 Bitcoin addresses in just 41 minutes on July 30. The flaw was caused by a firmware integration error in March 2021, which routed seed generation to a deterministic software pseudorandom number generator (PRNG) instead of the hardware random number generator (RNG).

The error made it possible for an attacker to reproduce candidate output streams offline without accessing the device, by determining or constraining the device UID, timer state, and prior RNG-call history. Coinkite has since shipped emergency firmware to address the issue, but installing it does not repair an existing seed. Owners with exposed seeds are advised to generate a new one on patched firmware and move their coins to a new wallet. The company estimates that the effective entropy of the affected seeds is roughly 40-72 bits, compared to the 128 bits of a standard 12-word BIP-39 seed.

The vulnerability affects various models of the Coldcard wallet, including the Mk2, Mk3, Mk4, Mk5, and Q, with specific firmware versions being impacted. Coinkite recommends that users who created their seeds with fewer than 50 fair, independent, private dice rolls migrate to a new seed. Additionally, using a strong, unique BIP-39 passphrase can create a separate wallet that is not vulnerable to this bug. The incident highlights the importance of robust security measures in cryptocurrency wallets and the need for users to stay vigilant and take proactive steps to protect their assets.

---

> *Time is the most valuable thing a man can spend.
Author: Theophrastus*

Source: [Coldcard Hardware Wallet Flaw Linked to $70 Million Bitcoin Theft in 41 Minutes](https://thehackernews.com/2026/08/coldcard-hardware-wallet-flaw-linked-to.html)
