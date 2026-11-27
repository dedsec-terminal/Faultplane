---
title: 'Repeater Strike: AI-Powered Burp Suite Extension for Automated IDOR Detection'
description: PortSwigger Research introduced Repeater Strike, an AI‑powered Burp Suite
  extension that automates the hunt for IDOR and similar vulnerabilities by ge...
source: PortSwigger Research
source_url: https://portswigger.net/research/repeater-strike-manual-testing-amplified
published: '2025-07-15T13:46:37+00:00'
ingested_at: '2026-11-27T19:47:03.185902+00:00'
date: '2026-11-27T19:47:03.185902+00:00'
category: research
tags:
- Burp Suite
- AI
- IDOR
- vulnerability testing
- automation
slug: 2026-11-27-repeater-strike-ai-powered-burp-suite-extension-for-automate
quote: Though no one can go back and make a brand new start, anyone can start from
  now and make a brand new ending.
quote_author: Unknown
---

### Executive Summary

PortSwigger Research introduced Repeater Strike, an AI‑powered Burp Suite extension that automates the hunt for IDOR and similar vulnerabilities by generating regular expressions from Repeater traffic and scanning proxy history. The tool uses AI to identify potential weaknesses, produce a JSON description, mutate probes, and create Strike Rules that can be applied across past requests with minimal token usage. Users can also edit generated rules manually and trigger dynamic rule creation for each Repeater request. The article discusses challenges such as handling large responses, inconsistent AI output, and the difficulty of creating site‑agnostic regex patterns, and invites the community to help refine the approach. No direct security impact is claimed; the extension is intended to aid security testers in discovering and expanding vulnerability findings more efficiently.

### Original Overview

Manual testing doesn't have to be repetitive. In this post, we're introducing Repeater Strike - a new AI-powered Burp Suite extension designed to automate the hunt for IDOR and similar vulnerabilities. By analyzing your Repeater traffic, Repeater Strike generates smart regular expressions based on the requests and responses you're testing. It then applies these regexes across your proxy history to uncover related issues, letting you turn a single vulnerability into a broader set of actionable findings with minimal effort. At PortSwigger research we're experimenting with AI to produce semi-automated tools that help enhance your security testing. One of the ideas I had was to use AI to find variations and so I built Shadow Repeater . This turned out to be quite cool and it fit nicely...
