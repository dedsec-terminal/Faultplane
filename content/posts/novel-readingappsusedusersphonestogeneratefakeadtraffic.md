---
title: "Novel-reading apps used users’ phones to generate fake ad traffic"
date: 2026-08-06T14:07:15+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A new mobile ad fraud scheme, dubbed Papyrus, has been discovered using a cluster of novel-reading apps to generate hidden browser traffic. While users read chapters of a story, the app quietly loads websites in a hidden browser window, clicks on them, and scrolls through them on its own. This is made possible by an orchestration layer called BootNova, which controls the hidden browser activity and receives instructions from a remote command-and-control infrastructure.

The Papyrus scheme uses a combination of built-in JavaScript and server-delivered code to automate the hidden browsing activity. It can track user interactions, replay synthetic touches, clicks, and scrolls, and even mute media elements and automatically click page elements. The scheme also uses "click and scroll modules" that pass user taps into hidden webviews, registering clicks in the background. The automation is designed to vary and not repeat in a fixed pattern, making it harder to detect.

The scale of the operation is significant, with IAS linking Papyrus to over 800 domains and nearly 8,000 unique hostnames. The scheme is estimated to have brought in close to $1 million a month at its peak, with a click success rate nearly 25 times higher than non-Papyrus traffic. The fraudulent traffic appears more valuable than legitimate traffic, which can lead to misinformed campaign optimization strategies and wasted ad spend. The scheme's ability to distort performance reporting and attention-based evaluation can also cause advertisers to put more budget behind the exact traffic that's defrauding them.

---

> *You are always free to change your mind and choose a different future, or a different past.
Author: Richard Bach*

Source: [Novel-reading apps used users’ phones to generate fake ad traffic](https://www.helpnetsecurity.com/2026/08/06/papyrus-mobile-ad-fraud-scheme/)
