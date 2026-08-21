---
title: "Using Microsoft Graph and Powershell to Mine for Information - Stale Accounts and Licenses"
description: "The article explains how attackers can use Microsoft Graph API and PowerShell to enumerate stale user accounts and unused licenses in Microsoft 365 en..."
source: "SANS Internet Storm Center"
source_url: "https://isc.sans.edu/diary/rss/33264"
published: "2026-08-20T12:45:32+00:00"
ingested_at: "2026-08-21T01:05:01.792573+00:00"
date: "2026-08-21T01:05:01.792573+00:00"
category: "threat-intel"
tags:
  - "Microsoft Graph"
  - "PowerShell"
  - "M365"
  - "Entra"
  - "account mining"
  - "license management"
slug: "2026-08-21-using-microsoft-graph-and-powershell-to-mine-for-information"
quote: "Every human being is the author of his own health or disease."
quote_author: "Buddha"
---

### Executive Summary
The article explains how attackers can use Microsoft Graph API and PowerShell to enumerate stale user accounts and unused licenses in Microsoft 365 environments. It details the API endpoints, authentication, and scripts that retrieve user and license data, highlighting the risk of privileged data exposure and the need for proper monitoring.

---
**Intelligence Metadata**
- **Source Publisher:** SANS Internet Storm Center
- **Published Date:** 2026-08-20T12:45:32+00:00
- **Category:** threat-intel

**Original Description:**
Microsoft Graph is a newer API that is meant to replace several others.&&#x23&#x3b;x26&#x3b;&#x23&#x3b;xc2&#x3b;&&#x23&#x3b;x26&#x3b;&#x23&#x3b;xa0&#x3b; OK, it&&#x23&#x3b;x26&#x3b;&#x23&#x3b;39&#x3b;s at version 2.3.9, so it&&#x23&#x3b;x26&#x3b;&#x23&#x3b;39&#x3b;s not all that new, but it&&#x23&#x3b;x26&#x3b;&#x23&#x3b;39&#x3b;s new enough that lots of folks (and commercial tools) aren&&#x23&#x3b;x26&#x3b;&#x23&#x3b;39&#x3b;t using it yet.&&#x23&#x3b;x26&#x3b;&#x23&#x3b;xc2&#x3b;&&#x23&#x3b...
