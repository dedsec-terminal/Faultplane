---
title: "Cheap Android TV Boxes Pose as Phones and Turn Owners’ Broadband Into Proxies"
date: 2026-07-31T14:45:01+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are 3 concise paragraphs summarizing the article:

Researchers at Bitsight have discovered a malicious operation, dubbed Fuyao, where cheap Android TV boxes are being used to commit ad fraud and turn owners' broadband into proxies. The TV boxes, which are often shipped with apps that mimic Samsung, Huawei, Xiaomi, or Vivo phones, are used to click ads on websites run by the same operators. When an HDMI signal is detected, the box relays other people's traffic through the owner's broadband line as a SOCKS5 exit node, and when the signal is off, it waits for ad-fraud tasks.

The operation is attributed to Zhejiang Fengwo IoT Technology Co., Ltd., a mainland China company founded in 2019. The company has advertised over 120,000 "AI digital humans," but it is unclear what this term refers to. Bitsight found that the operation uses machine vision and automation to locate ads, and the command-and-control server pushes complete phone profiles to each device, deleting chipset properties that would expose the true hardware. The operation is estimated to generate around $1.25 per device per day, or $47,500 daily if 38,000 devices are active.

Google has stated that the off-brand devices used in the operation are not Play Protect certified Android devices, which means they have not undergone extensive testing to ensure quality and user safety. The FBI has advised owners to assess connected devices, disconnect suspicious ones, and keep firmware current. Bitsight has provided some information on the operation, but a complete list of affected packages, firmware builds, and network indicators is still lacking. The company has promised to release further technical details, but as of now, Fuyao-specific identification guidance remains incomplete.

---

> *Think for yourselves and let others enjoy the privilege to do so too.
Author: Voltaire*

Source: [Cheap Android TV Boxes Pose as Phones and Turn Owners’ Broadband Into Proxies](https://thehackernews.com/2026/07/cheap-android-tv-boxes-pose-as-phones.html)
