---
title: BaseChat – Audio Dating App Android 9.8.1 Vulnerabilities (VU#124705)
description: 'The advisory confirms three vulnerabilities in BaseChat – Audio Dating
  App version 9.8.1: (1) the app accepts any self‑signed TLS certificate, (2) it...'
source: CERT/CC Vulnerability Notes
source_url: https://kb.cert.org/vuls/id/124705
published: '2026-11-03T15:42:35+00:00'
ingested_at: '2026-11-27T19:47:03.208902+00:00'
date: '2026-11-27T19:47:03.208902+00:00'
category: vulnerabilities
tags:
- Android
- TLS
- Privacy
- RevenueCat
- Logging
- Vulnerability
slug: 2026-11-27-basechat-audio-dating-app-android-9-8-1-vulnerabilities-vu-1
quote: A rolling stone gathers no moss.
quote_author: Publilius Syrus
---

### Executive Summary

The advisory confirms three vulnerabilities in BaseChat – Audio Dating App version 9.8.1: (1) the app accepts any self‑signed TLS certificate, (2) it exposes users’ phone numbers via a public RevenueCat SDK key, and (3) it logs personally identifiable information (PII) to Android system logs during voice calls. These weaknesses could allow a network attacker to intercept API traffic and potentially take over accounts, enable an attacker to query user metadata from RevenueCat, and reveal anonymous users’ phone numbers from local logs. No vendor‑provided mitigation guidance was available, as the owner, Mobile Trading GmbH, could not be reached to coordinate the issue.

### Original Overview

Overview Multiple vulnerabilities have been identified in the Android application, BaseChat – Audio Dating App, version 9.8.1, which ultimately compromise the privacy of users’ personal data and activity. Description BaseChat is an online dating platform built in Flutter and targeted toward users over 18. It facilitates anonymous, voice-first interaction between users. Three distinct vulnerabilities have been identified within the shipped Android application. VU#124705.1: The application fails open when validating TLS server certificates for connections to its backend API host. The application allows any self-signed certificate to bypass standard TLS security checks. VU#124705.2: Paid user accounts are mapped to a third-party RevenueCat subscriber database using raw MSISDNs (phone...
