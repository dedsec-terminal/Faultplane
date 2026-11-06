---
title: "OpenSSH Issues Emergency Fix for Flaw Letting Long Passwords Bypass SSH Auth on Alpine Linux"
description: "OpenSSH released version 10.6p2 to fix a critical flaw that allowed attackers to bypass SSH authentication on Alpine Linux servers by using passwords ..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/11/openssh-issues-emergency-fix-for-flaw.html"
published: "2026-11-05T16:42:46+00:00"
ingested_at: "2026-11-06T04:54:14.097867+00:00"
date: "2026-11-06T04:54:14.097867+00:00"
category: "vulnerabilities"
tags:
  - "OpenSSH"
  - "Alpine Linux"
  - "SSH"
  - "authentication bypass"
  - "critical vulnerability"
slug: "2026-11-06-openssh-issues-emergency-fix-for-flaw-letting-long-passwords"
quote: "Nature takes away any faculty that is not used."
quote_author: "William R. Inge"
---

### Executive Summary
OpenSSH released version 10.6p2 to fix a critical flaw that allowed attackers to bypass SSH authentication on Alpine Linux servers by using passwords between 257 and 1,024 bytes. The vulnerability could let attackers log into accounts with no password, such as key‑only accounts, if they had network access, an account name, and a long password. Alpine Linux has published fixed packages for all affected releases.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-11-05T16:42:46+00:00
- **Category:** vulnerabilities

**Original Description:**
Attackers can log in to accounts that have no password, such as SSH key-only accounts, on some Alpine Linux servers running the standard openssh-server package. They need network access to the server, an account name, and a password between 257 and 1,024 bytes long. OpenSSH, which rates the flaw critical, released version 10.6p2 today to block it. Alpine has published fixed packages for every
