---
title: 'VU#410595: Google BoringSSL Name Constraints bypass in SAN validation logic'
description: Five separate name‑constraint findings were identified in BoringSSL’s
  SAN validation logic (VUs 410595.8–12). Two issues (wildcard DNS and trailing‑do...
source: CERT/CC Vulnerability Notes
source_url: https://kb.cert.org/vuls/id/410595
published: '2026-10-14T15:11:33+00:00'
ingested_at: '2026-11-28T06:05:31.063979+00:00'
date: '2026-11-28T06:05:31.063979+00:00'
category: vulnerabilities
tags:
- BoringSSL
- Name Constraints
- Certificate Validation
- SAN
- Security Update
slug: 2026-11-28-vu-410595-google-boringssl-name-constraints-bypass-in-san-va
quote: On every thorn, delightful wisdom grows, In every rill a sweet instruction
  flows.
quote_author: Edward Young
---

### Executive Summary

Five separate name‑constraint findings were identified in BoringSSL’s SAN validation logic (VUs 410595.8–12). Two issues (wildcard DNS and trailing‑dot DNS handling) were fixed on 2026‑03‑04, one was accepted for remediation, one was disputed, and one was declined as below the security threshold. The vulnerabilities only affect scenarios where name constraints are enforced, a trusted signature is obtained over attacker‑chosen SAN fields, and the accepted name is used for authorization. Operators should verify whether their deployments use the affected validation paths, apply the available updates, and ensure SANs are well‑formed; no evidence indicates that Chrome, Android, or other products are impacted solely by the presence of BoringSSL.

### Original Overview

Overview Five Name Constraints findings in BoringSSL (VU#410595.8–.12) describe cases where certificate names may not be constrained as intended. Records .8, .9, .10 and .12 concern the legacy crypto/x509 path; .11 concerns the newer pki path. Two have been fixed, one is accepted, one is disputed, and one was declined. Description Name Constraints limit the names a subordinate certificate authority may issue. The reports concern how BoringSSL applies those limits to certain SAN (Subject Alternative Name) forms. The records do not share one status, and they do not all affect the same validation path. VU#410595.8 ( Fixed 2026-03-04 ): A wildcard DNS name may not be treated as covering a specifically excluded host. VU#410595.9 ( Accepted ): A URI with a colon before @ may cause the wrong...
