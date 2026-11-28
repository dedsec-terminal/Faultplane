---
title: 'Shadow Repeater: AI-Enhanced Manual Testing'
description: PortSwigger has released Shadow Repeater, an extension for Burp Suite
  that augments manual testing by automatically generating payload variations usin...
source: PortSwigger Research
source_url: https://portswigger.net/research/shadow-repeater-ai-enhanced-manual-testing
published: '2025-02-20T13:20:19+00:00'
ingested_at: '2026-11-28T06:05:31.043979+00:00'
date: '2026-11-28T06:05:31.043979+00:00'
category: research
tags:
- Burp Suite
- AI
- manual testing
- vulnerability discovery
- XSS
- path traversal
slug: 2026-11-28-shadow-repeater-ai-enhanced-manual-testing
quote: Intuition will tell the thinking mind where to look next.
quote_author: Jonas Salk
---

### Executive Summary

PortSwigger has released Shadow Repeater, an extension for Burp Suite that augments manual testing by automatically generating payload variations using an AI model. The tool monitors Repeater requests, extracts changing parameters, and sends them to the AI to produce variants, which are then sent to the target and analyzed via response diffing to detect new code paths. Shadow Repeater claims to uncover unconventional XSS vectors, path traversal attempts, and novel vulnerabilities such as email splitting attacks, while integrating seamlessly into existing workflows. The source code is available on GitHub and the extension can be installed from the BApp store. No specific defensive guidance is provided beyond normal Burp Suite usage.

### Original Overview

Have you ever wondered how many vulnerabilities you've missed by a hair's breadth, due to a single flawed choice? We've just released Shadow Repeater, which enhances your manual testing with AI-powered, fully automatic variation testing. Simply use Burp Repeater as you normally would, and behind the scenes Shadow Repeater will monitor your attacks, try permutations, and report any discoveries via Organizer. Shadow Repeater aids deep, targeted testing by analysing your payloads so when you have a near miss due to sending the wrong syntax, incorrect encoding, file path, or simply a typo, it can find the bug for you. It's fully automatic, and doesn't require any changes to your normal manual testing workflow. Shadow Repeater monitors your Repeater requests and identifies which parameters...
