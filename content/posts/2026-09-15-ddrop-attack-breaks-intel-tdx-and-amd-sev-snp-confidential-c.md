---
title: "DDRop Attack Breaks Intel TDX and AMD SEV\u2011SNP Confidential Computing"
description: "Researchers disclosed DDRop, a hardware attack that subverts Intel TDX and AMD SEV\u2011SNP by silently dropping writes to memory, causing processors to re..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/09/new-ddrop-attack-breaks-intel-tdx-and.html"
published: "2026-09-14T18:02:13+00:00"
ingested_at: "2026-09-15T03:10:44.801413+00:00"
date: "2026-09-15T03:10:44.801413+00:00"
category: "threat-intel"
tags:
  - "hardware attack"
  - "confidential computing"
  - "Intel TDX"
  - "AMD SEV‑SNP"
  - "DDRop"
  - "memory protection"
slug: "2026-09-15-ddrop-attack-breaks-intel-tdx-and-amd-sev-snp-confidential-c"
quote: "Your work is to discover your world and then with all your heart give yourself to it."
quote_author: "Buddha"
---

### Executive Summary
Researchers disclosed DDRop, a hardware attack that subverts Intel TDX and AMD SEV‑SNP by silently dropping writes to memory, causing processors to read stale encrypted data. The attack requires software control and brief physical access to insert a small circuit.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-09-14T18:02:13+00:00
- **Category:** threat-intel

**Original Description:**
Researchers have disclosed a new hardware attack, called DDRop, that breaks the memory protection in Intel and AMD confidential computing by silently dropping writes to a server's memory, so the processor keeps reading old encrypted data as if it were current. The attack requires an attacker who already controls the server's software and can briefly access the machine to insert a small circuit
