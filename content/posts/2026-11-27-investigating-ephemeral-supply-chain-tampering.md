---
title: Investigating Ephemeral Supply Chain Tampering
description: Google Threat Intelligence Group (GTIG) and Mandiant identified a supply‑chain
  compromise that targeted AOMEI Technology’s update infrastructure betwe...
source: Google Threat Intelligence
source_url: https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering/
published: '2026-10-15T11:00:00+00:00'
ingested_at: '2026-11-27T19:47:03.170902+00:00'
date: '2026-11-27T19:47:03.170902+00:00'
category: threat-intel
tags:
- supply chain
- software update
- AOMEI
- UNC7017
- CROSSROAD
- SHINYROAD
slug: 2026-11-27-investigating-ephemeral-supply-chain-tampering
quote: If we are facing in the right direction, all we have to do is keep on walking.
quote_author: Unknown
---

### Executive Summary

Google Threat Intelligence Group (GTIG) and Mandiant identified a supply‑chain compromise that targeted AOMEI Technology’s update infrastructure between April and July 2026. The threat actor, attributed to the UNC7017 cluster, performed brief configuration tampering windows of five to ten minutes, during which malicious configuration files were served to any client polling the update servers. Victims included organizations across IT services, telecommunications, higher education, and other sectors in Australia, Brazil, India, Pakistan, Portugal, Singapore, South Africa, Spain, Switzerland, Türkiye, and the United States, with the campaign likely affecting additional opportunistic targets. AOMEI responded by securing its distribution servers, and GTIG and METAL shared findings with affected customers; defenders are advised to monitor update traffic, validate configuration files, and block known malicious staging domains.

### Original Overview

Written by: Tyler McLellan Introduction Google Threat Intelligence Group (GTIG) and Mandiant investigated a software supply chain compromise campaign targeting the update infrastructure belonging to AOMEI Technology between April 2026 and July 2026. The threat actor conducted repeated, short-burst configuration tampering against AOMEI origin servers. Each tampering window remained active for only five to ten minutes before reverting to authentic versions. This is the first time that we have encountered a software supply chain compromise that was implemented with these very short windows, effectively evading traditional point-in-time triage and automated file scanning. The campaign delivered a multi-stage payload chain involving the newly tracked CROSSROAD downloader and SHINYROAD...
