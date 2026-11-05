---
title: "Debian and Ubuntu APT Flaw Lets MitM Attackers Swap Verified Packages and Run Code as Root"
description: "A flaw in Debian and Ubuntu's APT package manager allows an attacker who can modify package downloads to replace a verified package with malicious cod..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/11/debian-and-ubuntu-apt-flaw-lets-mitm.html"
published: "2026-11-04T17:00:46+00:00"
ingested_at: "2026-11-05T04:55:06.067715+00:00"
date: "2026-11-05T04:55:06.067715+00:00"
category: "vulnerabilities"
tags:
  - "APT"
  - "Debian"
  - "Ubuntu"
  - "MitM"
  - "root"
slug: "2026-11-05-debian-and-ubuntu-apt-flaw-lets-mitm-attackers-swap-verified"
quote: "When you arise in the morning, think of what a precious privilege it is to be alive \ufffd to breathe, to think, to enjoy, to love."
quote_author: "Marcus Aurelius"
---

### Executive Summary
A flaw in Debian and Ubuntu's APT package manager allows an attacker who can modify package downloads to replace a verified package with malicious code. The malicious package runs as root when APT retries failed downloads, which it does by default from Debian 12. The vulnerability was disclosed by Debian, Ubuntu, and APT developers on Nov 4.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-11-04T17:00:46+00:00
- **Category:** vulnerabilities

**Original Description:**
A flaw in APT, the package manager for Debian and Ubuntu, allows an attacker who can modify package downloads to swap a checked package for their own. The attacker's code then runs as root, according to advisories that&nbsp;Debian,&nbsp;Ubuntu, and&nbsp;APT's developers&nbsp;published on November 4. The attack needs APT to retry failed downloads, which it does by default from Debian 12 and
