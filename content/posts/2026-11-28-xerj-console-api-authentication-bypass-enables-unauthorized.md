---
title: Xerj Console API Authentication Bypass Enables Unauthorized Credential Minting
description: An authentication bypass in the Xerj Console API (CVE‑2026‑97406) allows
  an attacker who already possesses a valid API token to create new, persistent...
source: CERT/CC Vulnerability Notes
source_url: https://kb.cert.org/vuls/id/645818
published: '2026-10-20T18:09:44+00:00'
ingested_at: '2026-11-28T06:05:31.062979+00:00'
date: '2026-11-28T06:05:31.062979+00:00'
category: vulnerabilities
tags:
- authentication bypass
- token issuance
- Xerj
slug: 2026-11-28-xerj-console-api-authentication-bypass-enables-unauthorized
quote: Do not be embarrassed by your mistakes. Nothing can teach us better than our
  understanding of them. This is one of the best ways of self-education.
quote_author: Thomas Carlyle
---

### Executive Summary

An authentication bypass in the Xerj Console API (CVE‑2026‑97406) allows an attacker who already possesses a valid API token to create new, persistent successor tokens without passkey authentication. The flaw stems from the system treating browser and bearer‑token sessions as the same generic AuthSession, bypassing passkey checks during token issuance. Because Xerj lacks hierarchical revocation, revoking the original token does not invalidate the newly minted tokens, enabling persistent unauthorized access and potential privilege escalation to administrative levels. Users are advised to monitor the Xerj GitHub repository for updates and install the latest patched version once available, as no vendor patch has yet been released.

### Original Overview

Overview An authentication bypass vulnerability in the Xerj Console API allows sessions to bypass passkey-backed requirements during token issuance. By exploiting this flaw, an attacker with an existing valid token can create independent, persistent successor credentials directly through the console API. This allows the attacker to maintain access and potentially escalate privileges within the Xerj ecosystem, even if the initial token is revoked. Description Xerj is an open-source search and indexing engine tailored specifically for AI agents utilizing the Elasticsearch API, allowing AI models to query a structured index. The vulnerability, CVE-2026-97406 , stems from a flaw in how session states are authenticated and handled within the Xerj system architecture. According to the...
