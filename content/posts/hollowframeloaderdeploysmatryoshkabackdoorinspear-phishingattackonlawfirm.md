---
title: "HollowFrame Loader Deploys Matryoshka Backdoor in Spear-Phishing Attack on Law Firm"
date: 2026-07-31T16:39:31+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Cybersecurity researchers have discovered a previously undocumented loader framework called HollowFrame and a malware family known as Matryoshka. The attack begins with a spear-phishing message containing a link to an encrypted archive, which holds a Windows Shortcut (LNK) file. When executed, the file triggers a multi-stage chain that involves privilege escalation, weakening Microsoft Defender protections, and downloading additional payloads.

The HollowFrame loader is launched via a DLL side-loading pair, comprising a legitimate Python binary and a rogue DLL. It operates as a modular loader and persistence framework, supporting various methods to load auxiliary components while performing anti-analysis checks to avoid running within sandboxed environments. The loader is embedded with an encrypted container that is unpacked to launch a second side-loading chain to deploy Matryoshka, a Rust-based backdoor that communicates with its command-and-control (C2) server over HTTP.

The Matryoshka backdoor comes in two variants, one that uses HTTP-based communication and another that uses a private GitHub repository for command-and-control. The GitHub variant allows the operator to manage tasking and results for individual endpoints, leaving a versioned history of repository changes. The attack targeted a law firm, giving the actor a persistent foothold for remote command execution, Active Directory reconnaissance, file transfer, and deployment of follow-on tooling. The identity of the actor behind the activity is currently unknown, and the separation of malicious behavior across multiple stages complicates attribution and detection.

---

> *Our intention creates our reality.
Author: Wayne Dyer*

Source: [HollowFrame Loader Deploys Matryoshka Backdoor in Spear-Phishing Attack on Law Firm](https://thehackernews.com/2026/07/hollowframe-loader-deploys-matryoshka.html)
