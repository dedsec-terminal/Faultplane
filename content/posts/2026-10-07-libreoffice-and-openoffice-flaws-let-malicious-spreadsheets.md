---
title: "LibreOffice and OpenOffice Flaws Let Malicious Spreadsheets Run Code Without Macro Warnings"
description: "Security researchers demonstrated that a malicious spreadsheet can execute attacker code immediately upon opening in LibreOffice and Apache OpenOffice..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/10/libreoffice-and-openoffice-flaws-let.html"
published: "2026-10-06T11:57:00+00:00"
ingested_at: "2026-10-07T04:03:45.393260+00:00"
date: "2026-10-07T04:03:45.393260+00:00"
category: "threat-intel"
tags:
  - "LibreOffice"
  - "Apache OpenOffice"
  - "malicious spreadsheet"
  - "macro bypass"
  - "Java support"
  - "code execution"
slug: "2026-10-07-libreoffice-and-openoffice-flaws-let-malicious-spreadsheets"
quote: "Through pride we are ever deceiving ourselves. But deep down below the surface of the average conscience a still, small voice says to us, Something is out of tune."
quote_author: "Carl Jung"
---

### Executive Summary
Security researchers demonstrated that a malicious spreadsheet can execute attacker code immediately upon opening in LibreOffice and Apache OpenOffice when Java support is enabled, bypassing macro warnings. The proof‑of‑concept attack shows no real‑world reports yet.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-10-06T11:57:00+00:00
- **Category:** threat-intel

**Original Description:**
A malicious spreadsheet can make LibreOffice and Apache OpenOffice run an attacker's code as soon as the file is opened, security researchers have shown. There is no warning first, of the kind either program shows before it runs a macro. The attack works only when the program's Java support is enabled. So far, it has only been shown as a proof of concept, and there are no reports of its use in
