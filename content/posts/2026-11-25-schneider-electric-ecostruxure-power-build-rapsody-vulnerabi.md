---
title: "Schneider Electric EcoStruxure Power Build Rapsody Vulnerability CVE-2026-119055"
description: "Schneider Electric has disclosed a use\u2011after\u2011free vulnerability (CVE\u20112026\u2011119055) in its EcoStruxure Power Build Rapsody software (versions \u22642.9.1.0_F..."
source: "CISA Cyber Advisories"
source_url: "https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-02"
published: "2026-11-24T12:00:00+00:00"
ingested_at: "2026-11-25T06:49:08.525444+00:00"
date: "2026-11-25T06:49:08.525444+00:00"
category: "cves"
tags:
  - "CVE-2026-119055"
  - "use-after-free"
  - "memory-corruption"
  - "local-exploit"
  - "Schneider Electric"
  - "EcoStruxure Power Build Rapsody"
slug: "2026-11-25-schneider-electric-ecostruxure-power-build-rapsody-vulnerabi"
quote: "Life is 10% what happens to you and 90% how you react to it."
quote_author: "Charles Swindoll"
---

### Executive Summary
Schneider Electric has disclosed a use‑after‑free vulnerability (CVE‑2026‑119055) in its EcoStruxure Power Build Rapsody software (versions ≤2.9.1.0_FR, 2.9.12.0101_FR, ≤2.8.5.0301_ESP, 2.9.5.0000_ESP, ≤2.8.7.0101_PT, 2.9.7.0000_PT, ≤2.8.8.0201_BEL(FR), 2.9.8.0000_BELFR, ≤2.8.3.0201_BEL(EN), 2.9.3.0000_BELEN, ≤2.8.4.0401_INT(EN), 2.9.4.0000_INTEN, ≤2.8.6.0000_INT(FR), 2.9.6.0000_INTFR, ≤2.8.2.0000_NL, 2.9.6.0000_NL). The flaw can lead to memory corruption and arbitrary code execution by a local attacker who tricks a user into opening a malicious SSD file. Schneider has released fixed versions (e.g., 2.9.12.0101_FR, 2.9.5.0000_ESP, 2.9.7.0000_PT, 2.9.8.0000_BELFR, 2.9.3.0000_BELEN, 2.9.4.0000_INTEN, 2.9.6.0000_INTFR, 2.9.6.0000_NL).

---
**Intelligence Metadata**
- **Source Publisher:** CISA Cyber Advisories
- **Published Date:** 2026-11-24T12:00:00+00:00
- **Category:** cves

**Original Description:**
View CSAF Summary Schneider Electric is aware of a vulnerability in its EcoStruxure™ Power Build Rapsody product. The EcoStruxure™ Power Build Rapsody is used to enter or import the single line diagram, to get the extensive bill of material of your switchboard, including all devices, connection items, and mounting components. Failure to apply the remediations provided below may risk memory corruption, heap-based buffer overflow, and/or stack-based buffer overflow, which could result in local ...
