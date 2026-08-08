---
title: "ClickFix Attacks Deliver macOS Stealer That Can Drain Crypto Wallets"
date: 2026-08-07T18:29:08+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A new type of malware attack, known as ClickFix, has been discovered, which targets macOS users and can steal cryptocurrency assets, browser-stored passwords, Apple iCloud Keychain data, and cached credentials. The attack begins with a user pasting a ClickFix command into the Terminal app, which triggers the execution of a Bash profiler/loader that collects system details and retrieves a Mach-O payload compatible with the computer's CPU architecture. This payload is a Go-based stealer that can capture sensitive information and transmit it to a remote server.

The malware has a notable "DRAIN" routine that checks if a cryptocurrency wallet holds funds and redirects a portion or all of it to an attacker-controlled wallet. This feature is particularly concerning, as it allows the malware to slowly deplete cryptocurrency accounts without being detected. The malware targets various cryptocurrencies, including Bitcoin, Litecoin, Dogecoin, Monero, Ethereum, and Ripple's XRP. The attackers use infrastructure belonging to Aeza Group, a Russian bulletproof hosting provider that has been sanctioned by several countries for facilitating malicious activities.

The discovery of this ClickFix attack comes amid a surge in similar attacks, including campaigns distributing MacSync and Atomic Stealer malware, as well as variants that use legitimate Windows binaries and WebAssembly modules to evade detection. Additionally, two other stealer campaigns have been discovered, one delivering Lumma Stealer via fake movie releases and another using cracked software and pirated game lures to drop Remus, a 64-bit variant of Lumma Stealer. These findings highlight the increasing threat of malware attacks targeting macOS users and the importance of being cautious when interacting with unknown commands or links.

---

> *I am of the opinion that my life belongs to the community, and as long as I live it is my privilege to do for it whatever I can.
Author: Bernard Shaw*

Source: [ClickFix Attacks Deliver macOS Stealer That Can Drain Crypto Wallets](https://thehackernews.com/2026/08/clickfix-attacks-deliver-macos-stealer.html)
