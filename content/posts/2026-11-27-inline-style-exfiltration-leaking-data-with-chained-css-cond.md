---
title: 'Inline Style Exfiltration: leaking data with chained CSS conditionals'
description: PortSwigger researchers demonstrated a CSS‑based exfiltration technique
  that uses inline style attributes, the attr() function, and CSS if‑statements...
source: PortSwigger Research
source_url: https://portswigger.net/research/inline-style-exfiltration
published: '2025-08-26T12:54:03+00:00'
ingested_at: '2026-11-27T19:47:03.182902+00:00'
date: '2026-11-27T19:47:03.182902+00:00'
category: research
tags:
- css
- exfiltration
- inline styles
slug: 2026-11-27-inline-style-exfiltration-leaking-data-with-chained-css-cond
quote: Some people are always grumbling because roses have thorns; I am thankful that
  thorns have roses.
quote_author: Alphonse Karr
---

### Executive Summary

PortSwigger researchers demonstrated a CSS‑based exfiltration technique that uses inline style attributes, the attr() function, and CSS if‑statements to send background requests and retrieve attribute values such as data‑uid or data‑username. The method relies on chained conditionals to brute‑force numeric ranges and works only in Chromium‑based browsers, as shown in a Burp Suite Custom Action video. The article presents the technique as a proof‑of‑concept; no real‑world incidents or widespread exploitation have been reported. No specific defensive guidance is provided beyond noting the browser limitation, but the technique highlights the risk of CSS injection via style attributes.

### Original Overview

I discovered how to use CSS to steal attribute data without selectors and stylesheet imports! This means you can now exploit CSS injection via style attributes! Learn how below: Someone asked if you could steal data using inline styles. I initially dismissed the idea but then I was reminded of Slonser's excellent technique of using the attr() and image-set() functions to steal data from the attribute. This method can steal an entire attribute provided you import a style sheet from your chosen domain. But this left me pondering what about without importing a stylesheet? Can you steal data just using inline styles? CSS introduced if statements , that's right this (not a) programming language now has conditionals. I was sure I could use this as a way to check the attribute value and make...
