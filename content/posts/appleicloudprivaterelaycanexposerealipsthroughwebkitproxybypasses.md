---
title: "Apple iCloud Private Relay Can Expose Real IPs Through WebKit Proxy Bypasses"
date: 2026-08-06T11:33:08+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Cybersecurity researchers have discovered a security issue with Apple's iCloud Private Relay tool, which can expose a user's real IP address. Introduced with iOS 15, iCloud Private Relay is designed to ensure users' privacy by routing their Safari web traffic through two relays, making it impossible for any single third-party to determine the request's origin and destination. However, researchers found that three features in Apple's WebKit - DNS prefetching, WebAuthn Related Origin Requests, and WebTransport - can bypass the configured proxy and send traffic directly from the device, exposing the user's real network.

The issue affects not only Safari but also other WebKit-based browsers on iOS, iPadOS, and macOS, including Google Chrome, Microsoft Edge, and Mozilla Firefox. The vulnerabilities allow websites to view a user's real IP address even if iCloud Private Relay is enabled. Specifically, WebAuthn, which allows users to log in with passkeys, can be exploited by websites to reveal the browser's real IP address. A proof-of-concept website has been created to demonstrate the issue, showing how the device's real IP address can leak out of the configured proxy path.

Apple has been informed of the issue and is investigating the researchers' report. This is not the first time security issues have been discovered in iCloud Private Relay, with a previous vulnerability discovered in 2021 that leaked a client's real IP address through a WebRTC-based mechanism. The disclosure comes after another vulnerability was addressed in Apple's Hide My Email service, which enabled users' real email addresses to be unmasked under certain conditions. The latest issue highlights the ongoing challenges in ensuring the privacy and security of online browsing, even with features like iCloud Private Relay in place.

---

> *Knowledge is a process of piling up facts; wisdom lies in their simplification.
Author: Martin Fischer*

Source: [Apple iCloud Private Relay Can Expose Real IPs Through WebKit Proxy Bypasses](https://thehackernews.com/2026/08/webkit-proxy-bypasses-can-expose-real.html)
