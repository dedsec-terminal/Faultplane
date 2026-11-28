---
title: TLS Libraries Name Constraint Bypass Vulnerabilities
description: CERT/CC identified thirteen records (VU#948176.6, .8–.19) describing
  how several widely used TLS libraries—GnuTLS, pyca/cryptography, wolfSSL, Go, Ope...
source: CERT/CC Vulnerability Notes
source_url: https://kb.cert.org/vuls/id/948176
published: '2026-10-14T15:11:20+00:00'
ingested_at: '2026-11-28T06:05:31.064979+00:00'
date: '2026-11-28T06:05:31.064979+00:00'
category: vulnerabilities
tags:
- TLS
- Name Constraints
- Certificate Validation
- Library Vulnerabilities
slug: 2026-11-28-tls-libraries-name-constraint-bypass-vulnerabilities
quote: No one can make you feel inferior without your consent.
quote_author: Eleanor Roosevelt
---

### Executive Summary

CERT/CC identified thirteen records (VU#948176.6, .8–.19) describing how several widely used TLS libraries—GnuTLS, pyca/cryptography, wolfSSL, Go, OpenSSL, Apple Security.framework, Mozilla NSS, LibreSSL, AWS‑LC, and Mbed TLS—handled X.509 Name Constraints inconsistently. Issues ranged from case‑sensitive DNS matching, wildcard handling, IPv4‑mapped IPv6 mismatches, to non‑critical constraint enforcement. Some vulnerabilities were fixed (e.g., GnuTLS CVE‑2026‑3833, pyca/cryptography CVE‑2026‑34073, wolfSSL CVE‑2026‑3547, AWS‑LC wildcard‑CN fixes), while others remain under review or in triage. The impact is limited to scenarios where an attacker can obtain a trusted signature over chosen certificate fields and the application accepts the mis‑validated identity for authorization. Defensive guidance recommends updating to patched library versions and ensuring that Name Constraints are marked critical and enforced.

### Original Overview

Overview This note covers thirteen library-specific records (VU#948176.6, .8–.19) of how widely used TLS libraries apply X.509 Name Constraints. The records describe cases where a constrained name may be accepted by one library and rejected by another. Some are fixed, some remain under review, and some were not accepted as security issues. Description Name Constraints are meant to keep a subordinate CA inside an allowed namespace. The records cover several name forms and do not all have the same classification. VU#948176.7 does not exist. DNS case-sensitivity and wildcards. While RFC 5280 requires case-insensitive DNS matching, it does not explicitly define wildcard Subject Alternative Name (SAN) matching, leading to varied implementation behaviors. For instance, GnuTLS was found to...
