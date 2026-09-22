---
title: "SAML: A Fractal of Bad Design"
description: "SAML, an XML\u2011based authentication protocol created in 2002 by OASIS, grew from academic and corporate needs for single sign\u2011on (SSO). Its design emerg..."
source: "Trail of Bits"
source_url: "https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/"
published: "2026-09-21T11:00:00+00:00"
ingested_at: "2026-09-22T03:05:58.902238+00:00"
date: "2026-09-22T03:05:58.902238+00:00"
category: "research"
tags:
  - "SAML"
  - "SSO"
  - "OpenID Connect"
  - "XML signature"
  - "protocol design"
slug: "2026-09-22-saml-a-fractal-of-bad-design"
quote: "If you have knowledge, let others light their candles in it."
quote_author: "Margaret Fuller"
---

### Executive Summary
SAML, an XML‑based authentication protocol created in 2002 by OASIS, grew from academic and corporate needs for single sign‑on (SSO). Its design emerged from a committee of subcommittees, resulting in a complex, fragile system that relies on XML signature validation—a notoriously difficult and error‑prone process. The protocol’s proliferation led to multiple overlapping XML‑based security standards, and its inherent complexity has made it difficult to implement securely. Recent research highlights widespread security weaknesses, the difficulty of maintaining robust XML signature validation, and the protocol’s unsuitability for modern SaaS environments. The article argues for deprecation in favor of lighter, JSON‑based alternatives such as OpenID Connect (OIDC).

---
**Intelligence Metadata**
- **Source Publisher:** Trail of Bits
- **Published Date:** 2026-09-21T11:00:00+00:00
- **Category:** research

**Original Description:**
Born out of academia and raised in corporate IT departments, the Security Assertion Markup Language (SAML) authentication protocol continues to be a staple in these organizations. However, it&rsquo;s time for it to retire. With the rise of software-as-a-service (SaaS) companies in the late aughts, IT departments needed a way for users to authenticate to many new web services. SAML and the burgeoning single sign-on (SSO) industry fulfilled this need. However, SAML is being crushed under the we...
