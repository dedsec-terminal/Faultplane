---
title: "DOUBLECUP Uses ClickFix and Cached PNGs to Deliver CountLoader and DeviceManager RAT"
date: 2026-08-04T09:03:23+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

A new Russian loader-as-a-service (LaaS) called DOUBLECUP has been discovered, which uses ClickFix lures to deliver malware-laced PNG images to victims' browser caches. The malware then executes a second stage, which decrypts the final payload in memory using a custom SHA-256 stream cipher and bitwise XOR. The payloads delivered via DOUBLECUP include CountLoader, a malware that establishes persistence and connects to a command-and-control (C2) server, and DeviceManager, a previously undocumented remote access trojan (RAT) that uses EtherHiding to resolve its C2 infrastructure.

DOUBLECUP is a highly sophisticated service that provides operators with licenses and a client agent to create campaigns and load payloads. The service uses a Go-based Windows GUI client that allows operators to update configurations, update software, and issue commands directly via a Broadcast Pane. The client also features a Payload Builder Pane that enables threat actors to set up commands triggered by a ClickFix decoy. The attack requires operators to inject frontend code onto their ClickFix site to trigger the malicious code, which involves fetching configuration data, prefetching steganographic images, and evaluating browser User-Agent strings.

The DOUBLECUP infrastructure has been used to deliver CountLoader and DeviceManager to victims via bogus sites impersonating CRM login pages. CountLoader has been updated with new capabilities, including establishing persistence using scheduled tasks and profiling hosts to check for Signal's desktop app. DeviceManager, on the other hand, uses EtherHiding to resolve its C2 server details and communicates with the server using DNS or HTTP. The malware collects extensive device information and can run PowerShell and Python scripts. DOUBLECUP highlights the expanding reach of ClickFix campaigns, providing threat actors with a reliable payload delivery pipeline that leverages steganography and environmental keying to bypass defenses.

---

> *The universe is full of magical things, patiently waiting for our wits to grow sharper.
Author: Eden Phillpotts*

Source: [DOUBLECUP Uses ClickFix and Cached PNGs to Deliver CountLoader and DeviceManager RAT](https://thehackernews.com/2026/08/doublecup-uses-clickfix-and-cached-pngs.html)
