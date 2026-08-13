---
title: "737 Chrome VPN Extensions Caught Routing Traffic Through Proxies. Check If You Have One"
date: 2026-08-12T14:09:50+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are 3 concise paragraphs summarizing the article:

A massive set of 737 free VPN and proxy extensions on the Chrome Web Store have been found to be routing user traffic through proxies, mainly targeting Russian-speaking users. These extensions, which have been installed 75,486 times, impersonate established VPN and privacy brands, including Proton VPN, NordVPN, and ExpressVPN. The extensions route user traffic through a single provider's SOCKS5 proxies, allowing the threat actor to observe browser destinations, source IP addresses, and request bodies sent over plain HTTP.

The majority of the extensions have been found to set a fixed SOCKS5 server on port 1082, placing the threat actor in an adversary-in-the-middle position. The extensions also come with a bypass list that only includes loopback addresses, funnelling all other browser requests through the SOCKS5 relay. As many as 221 browser add-ons have been removed from the Chrome Web Store, while the remaining 516 extensions are still active. The threat actor is believed to be running a subscription VPN business in Russia, and has been found to be using tactics such as DNS-over-HTTPS blocklist evasion and fake connection animations to evade detection.

The discovery of these malicious extensions highlights the risks of using free VPN and proxy services, particularly those that impersonate established brands. Users are advised to be cautious when installing extensions and to check for red flags such as fake premium tiers, non-existent servers, and attempts to evade Chrome Web Store policies. The incident also highlights the need for greater vigilance in monitoring extension updates, as a previously removed extension was found to have resurfaced with a new monetization scheme, opening affiliate links in browser tabs and suppressing redirects to other services.

---

> *All perceiving is also thinking, all reasoning is also intuition, all observation is also invention.
Author: Rudolf Arnheim*

Source: [737 Chrome VPN Extensions Caught Routing Traffic Through Proxies. Check If You Have One](https://thehackernews.com/2026/08/737-chrome-vpn-extensions-caught.html)
