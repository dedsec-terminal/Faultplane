---
title: "Orphaned VBA Projects Inside DWG Files YARA Rule"
description: "A YARA rule was published on the SANS Internet Storm Center to detect orphaned VBA projects embedded within DWG (AutoCAD) files. The rule helps securi..."
source: "SANS Internet Storm Center"
source_url: "https://isc.sans.edu/diary/rss/33434"
published: "2026-10-18T12:59:30+00:00"
ingested_at: "2026-10-19T03:03:08.501030+00:00"
date: "2026-10-19T03:03:08.501030+00:00"
category: "threat-intel"
tags:
  - "YARA"
  - "VBA"
  - "DWG"
  - "malware detection"
  - "file analysis"
slug: "2026-10-19-orphaned-vba-projects-inside-dwg-files-yara-rule"
quote: "Do, or do not. There is no try."
quote_author: "Yoda"
---

### Executive Summary
A YARA rule was published on the SANS Internet Storm Center to detect orphaned VBA projects embedded within DWG (AutoCAD) files. The rule helps security analysts identify potential malicious macros that are not linked to a parent project, which can be used for persistence or data exfiltration. The article includes the rule syntax and usage guidance.

---
**Intelligence Metadata**
- **Source Publisher:** SANS Internet Storm Center
- **Published Date:** 2026-10-18T12:59:30+00:00
- **Category:** threat-intel

**Original Description:**
Here is the YARA rule I used to detect "Orphaned VBA Projects Inside DWG Files".&#xd;
