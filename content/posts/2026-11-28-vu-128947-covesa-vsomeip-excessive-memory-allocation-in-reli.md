---
title: 'VU#128947: COVESA vsomeip excessive memory allocation in reliable (TCP) endpoint
  buffer handling'
description: 'COVESA’s open‑source vsomeip 3.7.3 and earlier contain a memory‑allocation
  flaw in reliable (TCP) endpoints: the receive buffer is enlarged to the len...'
source: CERT/CC Vulnerability Notes
source_url: https://kb.cert.org/vuls/id/128947
published: '2026-10-26T19:07:02+00:00'
ingested_at: '2026-11-28T06:05:31.060979+00:00'
date: '2026-11-28T06:05:31.060979+00:00'
category: vulnerabilities
tags:
- CVE-2026-91141
- vsomeip
- memory-allocation
- denial-of-service
- automotive
- COVESA
slug: 2026-11-28-vu-128947-covesa-vsomeip-excessive-memory-allocation-in-reli
quote: It is only with the heart that one can see rightly, what is essential is invisible
  to the eye.
quote_author: Antoine de Saint-Exupery
---

### Executive Summary

COVESA’s open‑source vsomeip 3.7.3 and earlier contain a memory‑allocation flaw in reliable (TCP) endpoints: the receive buffer is enlarged to the length declared in a message header before the payload is fully received. A remote, unauthenticated peer can send a single short message with an attacker‑chosen size of up to ~4 GB, causing the host to allocate that amount of memory. In practice, a service limited to 1.5 GB was OOM‑killed by a 3 GB payload, and on larger hosts repeated or persistent connections can exhaust memory and deny service. The issue is fixed in vsomeip 3.7.4 (released 2026‑07‑06), which imposes a default maximum message size of 10 MiB and rejects oversized lengths. Until an upgrade is possible, deployments should configure a per‑endpoint or per‑service max‑payload‑size‑reliable limit and restrict reliable endpoints to trusted, isolated networks to mitigate exposure.

### Original Overview

Overview vsomeip, COVESA's open source implementation of the SOME/IP automotive communication middleware, contained a memory allocation vulnerability present in versions 3.7.3 and below. A vsomeip reliable (TCP) SOME/IP endpoint grows its receive buffer to an attacker-declared message size before validating that the declared bytes have actually been received, allowing a remote, unauthenticated peer to exhaust host memory and deny service. The issue was reported publicly as COVESA/vsomeip issue #1009 and fixed in release 3.7.4 (2026-07-06). Description CVE-2026-91141 vsomeip is a middleware implementation of the Scalable service-Oriented MiddlewarE over IP (SOME/IP) protocol, widely used for service-oriented communication between electronic control units (ECUs) in automotive and other...
