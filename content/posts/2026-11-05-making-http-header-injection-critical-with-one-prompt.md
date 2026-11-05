---
title: "Making HTTP header injection critical with one prompt"
description: "PortSwigger researchers demonstrate how a single prompt can transform a basic HTTP header injection into a CRLF\u2011powered desynchronization attack, enab..."
source: "PortSwigger Research"
source_url: "https://portswigger.net/research/making-http-header-injection-critical-with-one-prompt"
published: "2026-11-04T15:12:29+00:00"
ingested_at: "2026-11-05T04:55:50.236266+00:00"
date: "2026-11-05T04:55:50.236266+00:00"
category: "research"
tags:
  - "HTTP header injection"
  - "CRLF desync"
  - "web exploitation"
  - "PortSwigger"
slug: "2026-11-05-making-http-header-injection-critical-with-one-prompt"
quote: "Yesterday is history. Tomorrow is a mystery. And today? Today is a gift that's why they call it the present."
quote_author: "Unknown"
---

### Executive Summary
PortSwigger researchers demonstrate how a single prompt can transform a basic HTTP header injection into a CRLF‑powered desynchronization attack, enabling attackers to redirect arbitrary users to malicious sites. The new scan check identifies this vulnerability, highlighting the risk of prompt‑based exploitation in web applications.

---
**Intelligence Metadata**
- **Source Publisher:** PortSwigger Research
- **Published Date:** 2026-11-04T15:12:29+00:00
- **Category:** research

**Original Description:**
You can now escalate HTTP header injection to a CRLF-Powered Desync and exploit it to serve random users a redirect to your collaborator, in a single prompt. We’ve just introduced a new scan check for
