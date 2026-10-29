---
title: "Inside KeyDrift: Analyzing historical UAT-11473 activity on Cisco SD-WAN"
description: "Talos identified the UAT-11473 APT, which exploited CVE-2026-20127, an authentication bypass vulnerability in Cisco SD\u2011WAN Catalyst Controller instanc..."
source: "Cisco Talos"
source_url: "https://blog.talosintelligence.com/uat-11473-keydrift/"
published: "2026-10-28T21:32:02+00:00"
ingested_at: "2026-10-29T04:10:38.926131+00:00"
date: "2026-10-29T04:10:38.926131+00:00"
category: "research"
tags:
  - "APT"
  - "Cisco SD-WAN"
  - "CVE-2026-20127"
  - "KeyDrift"
  - "authentication bypass"
  - "Talos"
slug: "2026-10-29-inside-keydrift-analyzing-historical-uat-11473-activity-on-c"
quote: "The heart has eyes which the brain knows nothing of."
quote_author: "Charles Perkhurst"
---

### Executive Summary
Talos identified the UAT-11473 APT, which exploited CVE-2026-20127, an authentication bypass vulnerability in Cisco SD‑WAN Catalyst Controller instances. The exploit allowed attackers to bypass authentication, gain unauthorized access, and deploy the KeyDrift malware. The analysis covers historical activity and attack techniques.

---
**Intelligence Metadata**
- **Source Publisher:** Cisco Talos
- **Published Date:** 2026-10-28T21:32:02+00:00
- **Category:** research

**Original Description:**
Talos has identified UAT-11473, a highly sophisticated APT, who exploited CVE-2026-20127, an authentication bypass vulnerability in Cisco SD-WAN Catalyst Controller instances to bypass authentication and gain unauthorized access to affected systems to deploy KeyDrift.
