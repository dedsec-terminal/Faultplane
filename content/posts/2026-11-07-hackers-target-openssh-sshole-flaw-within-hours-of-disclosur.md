---
title: "Hackers Target OpenSSH SSHole Flaw Within Hours of Disclosure, Gain Root on Honeypot"
description: "Within hours of the public disclosure of CVE\u20112026\u2011123158 (codenamed SSHole), threat actors exploited a flaw in OpenSSH that allows password\u2011less sign\u2011..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/11/hackers-exploited-openssh-sshole-flaw.html"
published: "2026-11-06T15:21:49+00:00"
ingested_at: "2026-11-07T04:26:10.817133+00:00"
date: "2026-11-07T04:26:10.817133+00:00"
category: "threat-intel"
tags:
  - "OpenSSH"
  - "CVE-2026-123158"
  - "SSHole"
  - "musl"
  - "PAM"
  - "root"
  - "honeypot"
slug: "2026-11-07-hackers-target-openssh-sshole-flaw-within-hours-of-disclosur"
quote: "The important thing is this: to be able at any moment to sacrifice what we are for what we could become."
quote_author: "Charles Dubois"
---

### Executive Summary
Within hours of the public disclosure of CVE‑2026‑123158 (codenamed SSHole), threat actors exploited a flaw in OpenSSH that allows password‑less sign‑ins on Linux systems running OpenSSH on the musl C library with PAM disabled. The attackers achieved root access on a honeypot, demonstrating the vulnerability’s potential for privilege escalation.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-11-06T15:21:49+00:00
- **Category:** threat-intel

**Original Description:**
Threat actors are attempting to exploit a recently disclosed security flaw impacting OpenSSH that can enable sign-ins to accounts that have no password set, according to Previdian. The vulnerability, tracked as CVE-2026-123158 (CVSS score: 8.1) and codenamed SSHole (or *sshole), impacts Linux systems that run OpenSSH on the musl C library with Pluggable Authentication Modules (PAM) disabled,
