---
title: Microsoft removes WSUS server role in Windows Server 2028
description: Microsoft announced that the Windows Server Update Services (WSUS) server
  role will be removed in Windows Server 2028, following its official deprecat...
source: Bleeping Computer
source_url: https://www.bleepingcomputer.com/news/microsoft/microsoft-removes-wsus-server-role-in-windows-server-2028/
published: '2026-11-27T11:18:36+00:00'
ingested_at: '2026-11-27T19:47:03.164902+00:00'
date: '2026-11-27T19:47:03.164902+00:00'
category: research
tags:
- WSUS
- Windows Server 2028
- update management
- cloud-based solutions
- Microsoft Intune
slug: 2026-11-27-microsoft-removes-wsus-server-role-in-windows-server-2028
quote: Better to have loved and lost, than to have never loved at all.
quote_author: St. Augustine
---

### Executive Summary

Microsoft announced that the Windows Server Update Services (WSUS) server role will be removed in Windows Server 2028, following its official deprecation in September 2024. WSUS will remain available and supported in earlier releases such as Windows Server 2025 for the duration of their support lifecycle, allowing organizations to continue managing updates for Windows client and server releases, including Windows Server 2028. The change primarily impacts enterprise environments that rely on WSUS for centralized update distribution; home users and those using Microsoft Configuration Manager are not affected. Microsoft recommends that affected organizations transition to cloud‑based update solutions—Windows Autopatch, Microsoft Intune for client updates, and Azure Update Manager for server updates—to maintain endpoint security. The new release also removes legacy components such as VBScript, the WMIC utility, and WINS to reduce attack surface and improve overall security posture.

### Original Overview

Microsoft will remove the WSUS server role from Windows Server 2028, the next major release of its server operating system. Introduced in 2005 as Software Update Services (SUS), WSUS (Windows Server Update Services) lets IT administrators manage and distribute updates for Microsoft products across corporate networks with many Windows devices. It gives admins centralized control over the updates, rather than having each device download them individually from Microsoft's servers. Microsoft has officially deprecated WSUS in September 2024 , but said that it still plans to maintain functionality and continue publishing updates through the channel. The change affects enterprise environments that rely on WSUS to manage updates delivered to many devices but does not impact home users or...
