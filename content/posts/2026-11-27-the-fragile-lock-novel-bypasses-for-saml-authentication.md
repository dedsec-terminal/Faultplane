---
title: 'The Fragile Lock: Novel Bypasses For SAML Authentication'
description: 'This post shows how to achieve a full authentication bypass in the Ruby
  and PHP SAML ecosystem by exploiting several parser-level inconsistencies: inc...'
source: PortSwigger Research
source_url: https://portswigger.net/research/the-fragile-lock
published: '2025-12-10T12:32:00+00:00'
ingested_at: '2026-11-27T19:39:14.665005+00:00'
date: '2026-11-27T19:39:14.665005+00:00'
category: research
tags:
- research
slug: 2026-11-27-the-fragile-lock-novel-bypasses-for-saml-authentication
quote: Most folks are about as happy as they make up their minds to be.
quote_author: Abraham Lincoln
---

### Executive Summary

This post shows how to achieve a full authentication bypass in the Ruby and PHP SAML ecosystem by exploiting several parser-level inconsistencies: including attribute pollution, namespace confusion, and a new class of Void Canonicalization attacks. These techniques allow an attacker to completely bypass XML Signature validation while still presenting a perfectly valid SAML document to the application. You can get this paper as a print/download friendly PDF. You can also grab the slides from Black Hat . Here’s a demo of the attack on a vulnerable GitLab EE 17.8.4 instance: Service...
