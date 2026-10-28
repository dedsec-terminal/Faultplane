---
title: "Scalable Vector Grief"
description: "PortSwigger researchers tested eight SVG sanitizers, successfully bypassing six. They demonstrated that a malicious response header can execute JavaSc..."
source: "PortSwigger Research"
source_url: "https://portswigger.net/research/scalable-vector-grief"
published: "2026-10-27T14:29:26+00:00"
ingested_at: "2026-10-28T03:48:01.141435+00:00"
date: "2026-10-28T03:48:01.141435+00:00"
category: "research"
tags:
  - "SVG"
  - "sanitizer"
  - "bypass"
  - "Firefox"
  - "response-header"
  - "XSS"
  - "web-security"
slug: "2026-10-28-scalable-vector-grief"
quote: "He that never changes his opinions, never corrects his mistakes, and will never be wiser on the morrow than he is today."
quote_author: "Tryon Edwards"
---

### Executive Summary
PortSwigger researchers tested eight SVG sanitizers, successfully bypassing six. They demonstrated that a malicious response header can execute JavaScript in Firefox even when the response body is benign XML, highlighting a new vector for XSS attacks via SVG content.

---
**Intelligence Metadata**
- **Source Publisher:** PortSwigger Research
- **Published Date:** 2026-10-27T14:29:26+00:00
- **Category:** research

**Original Description:**
I tested eight popular SVG sanitizers and bypassed six of them. In this post, I'll show you how a response header can run JavaScript in Firefox even when the response body is completely harmless XML.
