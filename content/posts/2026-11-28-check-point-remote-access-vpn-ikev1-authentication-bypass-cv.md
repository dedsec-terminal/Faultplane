---
title: Check Point Remote Access VPN IKEv1 Authentication Bypass CVE-2026-50751
description: Check Point released hotfixes on 8 June 2026 for a critical authentication
  bypass (CVE‑2026‑50751) in the deprecated IKEv1 VPN code of its Mobile Acce...
source: watchTowr Labs
source_url: https://labs.watchtowr.com/marking-your-own-homework-check-point-remote-access-vpn-ikev1-authentication-bypass-cve-2026-50751/
published: '2026-06-12T05:17:20+00:00'
ingested_at: '2026-11-28T06:05:31.046979+00:00'
date: '2026-11-28T06:05:31.046979+00:00'
category: vulnerabilities
tags:
- Check Point
- CVE-2026-50751
- VPN
- Authentication Bypass
- Qilin ransomware
slug: 2026-11-28-check-point-remote-access-vpn-ikev1-authentication-bypass-cv
quote: Every day may not be good, but there's something good in every day.
quote_author: Unknown
---

### Executive Summary

Check Point released hotfixes on 8 June 2026 for a critical authentication bypass (CVE‑2026‑50751) in the deprecated IKEv1 VPN code of its Mobile Access/SSL VPN and Spark Firewall products. The flaw, a logic error in certificate validation during the IKEv1 key exchange, has been exploited in the wild since 7 May 2026, with a handful of targeted organizations and at least one incident linked to a Qilin ransomware affiliate. Affected Gaia versions include R80.20.X, R80.40, R81, R81.10, R81.10.X, R81.20, R82, R82.00.X, and R82.10; end‑of‑support releases receive no patch. Defenders are advised to apply the published hotfixes, disable legacy IKEv1 support, enforce machine‑certificate authentication, and consider migrating to IKEv2 only.

### Original Overview

It is yet another day in this parallel universe of security, where the devices we bolt onto the edge of our networks to keep the bad people out are, with remarkable consistency, the exact thing that let the bad people in. While we’ve seemingly had a breather from traditional SSL VPN exploitation season (you know, the one where every edge appliance vendor takes it in turns to have a very bad week ), it’s now time to pull up a chair and welcome ourselves back to another group therapy session. Welcome back to another watchTowr Labs blog post. On the 8th of June 2026, Check Point released hotfixes for a pair of vulnerabilities in their Mobile Access/SSL VPN, Remote Access VPN, and Spark Firewall products, specifically within the "deprecated" IKEv1 VPN code. The headline act was...
