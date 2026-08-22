---
title: "Microsoft Defender Driver Weaponized to Delete Security Software at Boot"
description: "Check Point Research revealed that Microsoft Defender\u2019s signed boot\u2011time remediation driver, BTR.sys, can be abused to perform arbitrary kernel\u2011level ..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/08/microsoft-defenders-own-driver-can-be.html"
published: "2026-08-21T15:52:10+00:00"
ingested_at: "2026-08-22T00:59:38.774511+00:00"
date: "2026-08-22T00:59:38.774511+00:00"
category: "threat-intel"
tags:
  - "Microsoft Defender"
  - "BTR.sys"
  - "boot-time driver"
  - "kernel-level"
  - "security software removal"
  - "Check Point Research"
slug: "2026-08-22-microsoft-defender-driver-weaponized-to-delete-security-soft"
quote: "If we are facing in the right direction, all we have to do is keep on walking."
quote_author: "Unknown"
---

### Executive Summary
Check Point Research revealed that Microsoft Defender’s signed boot‑time remediation driver, BTR.sys, can be abused to perform arbitrary kernel‑level file and registry operations, enabling the removal of security software during boot on Windows 7‑11 25H2. The technique requires no software flaw or external driver, relying solely on the legitimate driver.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-08-21T15:52:10+00:00
- **Category:** threat-intel

**Original Description:**
Check Point Research has disclosed a technique that uses Microsoft Defender's own legitimately signed boot-time remediation driver to perform arbitrary kernel-level file and registry operations on Windows systems ranging from Windows 7 through Windows 11 25H2, with no software flaw exploited and no driver imported from outside the machine. The driver, BTR.sys (Boot Time Removal Tool), is a
