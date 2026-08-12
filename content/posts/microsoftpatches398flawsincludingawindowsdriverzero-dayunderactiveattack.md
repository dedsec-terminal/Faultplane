---
title: "Microsoft Patches 398 Flaws Including a Windows Driver Zero-Day Under Active Attack"
date: 2026-08-11T20:10:55+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

Microsoft has released its monthly security updates, patching 398 flaws, including a Windows driver zero-day vulnerability (CVE-2026-68820) that is under active attack. This bug, which has a CVSS score of 7.0, allows an attacker with code already running on a machine to escalate to SYSTEM level privileges. The vulnerability is a use-after-free flaw in the Ancillary Function Driver for WinSock and is being exploited by the Lazarus group as part of its Operation Dream Job campaign.

In addition to the zero-day vulnerability, Microsoft has also patched four other flaws that can be exploited remotely without any user interaction or authentication. These flaws, which have CVSS scores of 9.8, affect Windows DNS Server, Windows Deployment Services, Microsoft's implementation of the QUIC transport protocol, and High Performance Computing (HPC) Pack. While these flaws have higher CVSS scores than the zero-day vulnerability, they have not been flagged as actively exploited. However, they can still be used to gain code execution on a server without any user interaction.

The updates also include a fix for a SharePoint vulnerability that was partially patched in July. The vulnerability, which consists of an authentication bypass (CVE-2026-55040) and a remote code execution (RCE) flaw (CVE-2026-63520), can be used to gain unauthenticated RCE access to on-premises SharePoint farms. While the authentication bypass was patched in July, the RCE component has been patched in the latest update. Microsoft recommends prioritizing the patching of the zero-day vulnerability, followed by the four unauthenticated RCE flaws, and then confirming that on-premises SharePoint farms have both the July and August updates installed.

---

> *The best cure for the body is a quiet mind.
Author: Napoleon Bonaparte*

Source: [Microsoft Patches 398 Flaws Including a Windows Driver Zero-Day Under Active Attack](https://thehackernews.com/2026/08/microsoft-patches-398-flaws-including.html)
