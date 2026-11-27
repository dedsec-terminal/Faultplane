---
title: Microsoft pushes emergency hotpatch to fix Windows Server crashes
description: Microsoft released an emergency out‑of‑band hotpatch (KB5138318) to address
  stop errors (0x139) that caused Windows Server 2025 to crash when IPv6 Rou...
source: Bleeping Computer
source_url: https://www.bleepingcomputer.com/news/microsoft/new-out-of-band-oob-emergency-hotpatch-fixes-windows-server-2025-crashes/
published: '2026-11-27T09:08:16+00:00'
ingested_at: '2026-11-27T19:47:03.167902+00:00'
date: '2026-11-27T19:47:03.167902+00:00'
category: vulnerabilities
tags:
- hotpatch
- Windows Server 2025
- IPv6
- Router Advertisement
- Windows 11
- Forcepoint DLP
slug: 2026-11-27-microsoft-pushes-emergency-hotpatch-to-fix-windows-server-cr
quote: Using the power of decision gives you the capacity to get past any excuse to
  change any and every part of your life in an instant.
quote_author: Tony Robbins
---

### Executive Summary

Microsoft released an emergency out‑of‑band hotpatch (KB5138318) to address stop errors (0x139) that caused Windows Server 2025 to crash when IPv6 Router Advertisement routes expire after the November 2026 security hotpatch (KB5131077). The update is automatically downloaded and installed via Windows Update for servers enrolled in hotpatch, and no restart is required. The same November hotpatch also caused installation, launch, and printing problems on Windows 11 systems, including Office, third‑party apps, and Forcepoint DLP Endpoint Agent, which Microsoft has acknowledged and is working to resolve. Administrators should ensure their devices are enrolled in hotpatch and monitor for the KB5138318 rollout, while Microsoft advises users to keep Windows Update enabled to receive the fix.

### Original Overview

Microsoft has released an emergency hotpatch update to address Windows Server 2025 crashes triggered after installing this month's security hotpatch update ( KB5131077 ). According to Microsoft, the KB5138318 out-of-band update should address stop errors with 0x139 codes triggered on affected servers when IPv6 routes expire. "Microsoft has released a new Windows out-of-band (OOB) update today, November 25, 2026, to address an issue affecting a limited number of Windows Servers with Router Advertisement (RA) enabled that receive time-bound IPv6 routes," it said in a message center update. "Affected devices might stop unexpectedly with stop error 0x139 (KERNEL_SECURITY_CHECK_FAILURE) when a route timer expires. This issue affects some Windows Server 2025 devices after installing the...
