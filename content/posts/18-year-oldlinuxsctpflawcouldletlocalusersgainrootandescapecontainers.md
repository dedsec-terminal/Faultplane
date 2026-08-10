---
title: "18-Year-Old Linux SCTP Flaw Could Let Local Users Gain Root and Escape Containers"
date: 2026-08-07T11:10:33+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A 18-year-old flaw in Linux's SCTP (Stream Control Transmission Protocol) networking code has been discovered, allowing local users to gain root access and potentially escape containers. The bug, tracked as CVE-2026-64564 and named SCTPhantom, is a use-after-free vulnerability that can be exploited to gain full root access on a host. The flaw has existed since 2008 and affects all Linux kernels released since then.

The vulnerability can be exploited when SCTP is reachable on the target system, and it requires a specific sequence of events to occur. Tencent researchers, who discovered the flaw, claim to have used it to escape a container and reach the underlying machine. However, their claim has not been independently verified, and the severity of the vulnerability is still being debated. The fix for the flaw has already been released in stable kernels 7.1.6, 6.18.42, 6.12.101, and 6.6.148.

Users are advised to update their kernels to the latest version to patch the vulnerability. It's also possible to block the SCTP module to remove the attack surface altogether, if SCTP is not needed. The discovery of the SCTPhantom flaw highlights the importance of continuous kernel testing and vulnerability detection, and it's the latest in a series of long-dormant kernel flaws to be surfaced with the help of machine learning-based research tools.

---

> *I have just three things to teach: simplicity, patience, compassion. These three are your greatest treasures.
Author: Lao Tzu*

Source: [18-Year-Old Linux SCTP Flaw Could Let Local Users Gain Root and Escape Containers](https://thehackernews.com/2026/08/18-year-old-linux-sctp-flaw-could-let.html)
