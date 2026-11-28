---
title: 'SAML roulette: the hacker always wins'
description: Researchers discovered a round‑trip XML mutation vulnerability in the
  ruby‑saml library that could allow an attacker to forge SAML assertions and gain...
source: PortSwigger Research
source_url: https://portswigger.net/research/saml-roulette-the-hacker-always-wins
published: '2025-03-18T14:55:43+00:00'
ingested_at: '2026-11-28T06:05:31.042979+00:00'
date: '2026-11-28T06:05:31.042979+00:00'
category: research
tags:
- SAML
- ruby-saml
- GitLab
- unauthenticated access
- XML round‑trip
slug: 2026-11-28-saml-roulette-the-hacker-always-wins
quote: The truth is always exciting. Speak it, then. Life is dull without it.
quote_author: Pearl Buck
---

### Executive Summary

Researchers discovered a round‑trip XML mutation vulnerability in the ruby‑saml library that could allow an attacker to forge SAML assertions and gain unauthenticated administrator access to GitLab Enterprise. The flaw arises from inconsistent parsing between REXML and Nokogiri, enabling namespace confusion and signature bypass. GitHub independently identified and patched related issues, but the researchers argue that publishing full technical details will help defenders detect and mitigate similar attacks. They recommend reviewing SAML parsing logic, ensuring consistent serialization, and applying the latest ruby‑saml patches.

### Original Overview

In this post, we’ll show precisely how to chain round-trip attacks and namespace confusion to achieve unauthenticated admin access on GitLab Enterprise by exploiting the ruby-saml library. While researching this, GitHub independently discovered and patched our vulnerabilities. However, their disclosure omits key technical details, including the specific mutation and how to exploit it without authentication. https://github.blog/security/sign-in-as-anyone-bypassing-saml-sso-authentication-with-parser-differentials/ We believe sharing the full details on how these attacks work is crucial for improving security by empowering everyone with the knowledge needed to identify, mitigate, and defend against such threats effectively. This research began after we came across a fascinating post by...
