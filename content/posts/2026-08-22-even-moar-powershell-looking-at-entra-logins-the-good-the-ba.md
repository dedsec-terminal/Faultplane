---
title: "Even MOAR Powershell, looking at Entra logins - the good, the bad and the password sprays"
description: "The article discusses how security teams can use PowerShell scripts to analyze Azure Entra login logs, highlighting best practices, common pitfalls, a..."
source: "SANS Internet Storm Center"
source_url: "https://isc.sans.edu/diary/rss/33268"
published: "2026-08-21T01:49:18+00:00"
ingested_at: "2026-08-22T01:00:51.400433+00:00"
date: "2026-08-22T01:00:51.400433+00:00"
category: "threat-intel"
tags:
  - "PowerShell"
  - "Entra"
  - "Password Spray"
  - "Cloud Security"
  - "Log Analysis"
slug: "2026-08-22-even-moar-powershell-looking-at-entra-logins-the-good-the-ba"
quote: "Sooner or later, those who win are those who think they can."
quote_author: "Richard Bach"
---

### Executive Summary
The article discusses how security teams can use PowerShell scripts to analyze Azure Entra login logs, highlighting best practices, common pitfalls, and detection of password spray attacks. It emphasizes the importance of reviewing logs after migrating to the cloud and provides actionable guidance for identifying suspicious login patterns.

---
**Intelligence Metadata**
- **Source Publisher:** SANS Internet Storm Center
- **Published Date:** 2026-08-21T01:49:18+00:00
- **Category:** threat-intel

**Original Description:**
One thing that folks never seem to do after "going to the CLOOOOUUUUD" is to look at their logs, logs that they would have checked daily when things were on premise.&#xd;
