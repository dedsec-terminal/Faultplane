---
title: "Fake LastPass Authenticator Installer Uses Microsoft-Signed Driver to Disable Antivirus and EDR"
description: "Researchers at LastPass and Delphos Labs uncovered a malicious installer on GitHub that installs a Windows kernel driver signed by Microsoft\u2019s hardwar..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/09/fake-lastpass-authenticator-installer.html"
published: "2026-09-21T17:31:01+00:00"
ingested_at: "2026-09-22T03:05:14.092320+00:00"
date: "2026-09-22T03:05:14.092320+00:00"
category: "threat-intel"
tags:
  - "LastPass"
  - "Microsoft-signed driver"
  - "antivirus bypass"
  - "EDR bypass"
  - "password stealer"
  - "GitHub"
  - "kernel driver"
slug: "2026-09-22-fake-lastpass-authenticator-installer-uses-microsoft-signed"
quote: "Make the most of yourself for that is all there is of you."
quote_author: "Ralph Emerson"
---

### Executive Summary
Researchers at LastPass and Delphos Labs uncovered a malicious installer on GitHub that installs a Windows kernel driver signed by Microsoft’s hardware‑compatibility program. The driver disables antivirus and EDR software before a password‑stealing payload runs, evading detection on VirusTotal. The attack demonstrates how legitimate signatures can be abused to bypass security controls.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-09-21T17:31:01+00:00
- **Category:** threat-intel

**Original Description:**
A fake LastPass Authenticator installer offered on GitHub installs a Windows kernel driver that shuts off antivirus and other security software before a password stealer runs if a victim downloads and runs it, researchers at LastPass and Delphos Labs said on September 17. Microsoft's own hardware-compatibility program signs the driver, scored zero detections on VirusTotal when researchers
