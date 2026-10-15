---
title: "Orphaned VBA Projects Inside DWG Files"
description: "The article revisits earlier diary entries that detail how Visual Basic for Applications (VBA) code can be embedded within AutoCAD drawing files (.dwg..."
source: "SANS Internet Storm Center"
source_url: "https://isc.sans.edu/diary/rss/33420"
published: "2026-10-14T06:49:46+00:00"
ingested_at: "2026-10-15T03:00:00.197991+00:00"
date: "2026-10-15T03:00:00.197991+00:00"
category: "threat-intel"
tags:
  - "VBA"
  - "AutoCAD"
  - "DWG"
  - "malware"
  - "persistence"
  - "file-based persistence"
slug: "2026-10-15-orphaned-vba-projects-inside-dwg-files"
quote: "You only lose what you cling to."
quote_author: "Buddha"
---

### Executive Summary
The article revisits earlier diary entries that detail how Visual Basic for Applications (VBA) code can be embedded within AutoCAD drawing files (.dwg). It explains that such VBA projects can become orphaned—detached from their original context—yet still execute when the drawing is opened. The piece highlights the persistence risk posed by these hidden scripts, noting that attackers can leverage them to run malicious payloads or exfiltrate data without triggering traditional antivirus detection.

---
**Intelligence Metadata**
- **Source Publisher:** SANS Internet Storm Center
- **Published Date:** 2026-10-14T06:49:46+00:00
- **Category:** threat-intel

**Original Description:**
Years ago I wrote diary entries about VBA code stored inside AutoCAD drawing files (.dwg).&#xd;
