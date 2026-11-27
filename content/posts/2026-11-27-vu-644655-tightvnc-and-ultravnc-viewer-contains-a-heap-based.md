---
title: 'VU#644655: TightVNC and UltraVNC Viewer contains a heap-based buffer overflow'
description: Overview A heap-based buffer overflow exists in the Tight JPEG decoding
  component of the TightVNC Windows Viewer version 1.3.10 and affected UltraVNC...
source: CERT/CC Vulnerability Notes
source_url: https://kb.cert.org/vuls/id/644655
published: '2026-11-13T00:08:48+00:00'
ingested_at: '2026-11-27T19:39:14.688005+00:00'
date: '2026-11-27T19:39:14.688005+00:00'
category: vulnerabilities
tags:
- vulnerabilities
slug: 2026-11-27-vu-644655-tightvnc-and-ultravnc-viewer-contains-a-heap-based
quote: These days people seek knowledge, not wisdom. Knowledge is of the past, wisdom
  is of the future.
quote_author: Vernon Cooper
---

### Executive Summary

Overview A heap-based buffer overflow exists in the Tight JPEG decoding component of the TightVNC Windows Viewer version 1.3.10 and affected UltraVNC Windows Viewers. An attacker controlling a malicious VNC server can trigger memory corruption by sending a specially crafted screen update. Successful exploitation can crash the viewer and may allow arbitrary code execution, although only denial of service conditions were demonstrated during testing. Description TightVNC and UltraVNC provide remote desktop access using the Remote Framebuffer (RFB) protocol. Their viewer applications connect to VNC servers and decode screen updates for local display. Tight encoding supports JPEG compression of image data within these updates. The Windows viewer function DecompressJpegRect() allocates a...
