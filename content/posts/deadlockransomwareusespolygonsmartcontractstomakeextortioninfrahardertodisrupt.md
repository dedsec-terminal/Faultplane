---
title: "DeadLock Ransomware Uses Polygon Smart Contracts to Make Extortion Infra Harder to Disrupt"
date: 2026-08-11T16:35:27+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

The DeadLock ransomware group has been observed using decentralized infrastructure to facilitate victim communications and data leak operations. This approach combines the Session messaging network with blockchain-backed services to store and deliver resources used throughout the extortion process. The group was first detected in July 2025 and has claimed 96 victims, mostly located in Italy, Spain, Poland, Türkiye, and the US.

The DeadLock ransomware employs a selective encryption model, excluding certain directories, file extensions, and file names from encryption. It uses a hybrid cryptographic design that combines Curve25519 elliptic-curve cryptography with the XChaCha20 stream cipher for file encryption. The ransom note instructs victims to download a decentralized messaging application to make a Bitcoin or Monero payment and provides a decrypted version of a locked file as proof. The note also claims to offer a "security report" detailing the steps taken to break into the network and promises security recommendations to prevent future attacks.

The most notable aspect of the DeadLock ransomware is its use of an HTML note that implements an end-to-end encrypted chat, a paginated data leak blog, and a file browser. This note uses JavaScript code to interact with Polygon smart contracts, allowing the operator to update the proxy URL without touching any victim-facing domains or registering new domains. This approach makes the infrastructure more resilient to takedown efforts, posing new challenges for disruption and allowing the DeadLock operators to maintain continuity for victims. The use of blockchain-based services and smart contracts represents a significant evolution in ransomware communication channels.

---

> *Keeping a little ahead of conditions is one of the secrets of business, the trailer seldom goes far.
Author: Charles Schwab*

Source: [DeadLock Ransomware Uses Polygon Smart Contracts to Make Extortion Infra Harder to Disrupt](https://thehackernews.com/2026/08/deadlock-ransomware-uses-polygon-smart.html)
