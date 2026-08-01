---
title: "Suspected Chinese-Speaking Hackers Target Central Asian Governments With OctLurk and SilkLurk"
date: 2026-07-31T18:52:04+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A Chinese-speaking threat actor is suspected to be behind a series of cyber attacks targeting government organizations in Central Asia, including Afghanistan, Kyrgyzstan, Tajikistan, Uzbekistan, Kazakhstan, and the Syrian Arab Republic, since January 2025. The attacks have targeted various sectors, such as healthcare, research, and government offices, and have been characterized by the use of two new obfuscated backdoors, OctLurk and SilkLurk, as well as a specialized utility called LurkProxy.

The backdoors, OctLurk and SilkLurk, are capable of downloading and injecting additional plugins to perform malicious actions, including launching command shells, credential dumping, keylogging, and remote access. The initial access vector used in these attacks is currently unknown, but Kaspersky analysis has found that OctLurk is injected into memory and deployed by means of a loader. The attackers also use LurkProxy to proxy network traffic and establish contact with a remote server for command-and-control (C2).

The threat actors have been found to leverage the backdoors to perform various malicious activities, including fingerprinting the host, harvesting extensive data, dropping and executing a keylogger, and establishing remote access to the victim machine. The attacks have also been linked to a prior set of attacks involving a C++-based implant codenamed SilentRaid, with infrastructure overlaps suggesting shared infrastructure across multiple OS-targeting campaigns. The emergence of the OctLurk and SilkLurk malware framework highlights the threat actors' ability to refine their tactics to evade detection and maintain control over compromised networks.

---

> *It is the greatest of all mistakes to do nothing because you can only do little � do what you can.
Author: Sydney Smith*

Source: [Suspected Chinese-Speaking Hackers Target Central Asian Governments With OctLurk and SilkLurk](https://thehackernews.com/2026/08/suspected-chinese-speaking-hackers.html)
