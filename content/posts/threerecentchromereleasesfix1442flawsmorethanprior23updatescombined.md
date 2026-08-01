---
title: "Three Recent Chrome Releases Fix 1,442 Flaws, More Than Prior 23 Updates Combined"
date: 2026-07-31T12:51:52+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Google has released three recent Chrome updates, versions 149, 150, and 151, which have fixed a total of 1,442 security flaws. This is a significant increase from the total number of flaws fixed in the previous 23 updates combined. The majority of the vulnerabilities were reported by Google itself, with seven of them marked as critical in severity. The updates come amid a surge in vulnerability discovery, largely driven by the use of large language models (LLMs) that have accelerated the process of identifying new bugs.

The vulnerabilities fixed in the recent updates include a critical sandbox escape in the Navigation component, which could have been exploited to trick the browser into reading local files from the user's system. This particular flaw had gone undetected in the Chrome codebase for over 13 years. Google has attributed the discovery of this vulnerability to its Gemini models, which leverage AI-powered agents to identify security issues. The company is now piloting a shift to two security releases per week to keep pace with the increasing number of vulnerabilities being discovered.

To improve browser security, Google is taking several steps, including automating the process of generating release notes and CVE descriptions, dynamically applying patches without requiring a restart, and eliminating entire classes of security issues from Chrome. The company is also transitioning to memory-safe languages like Rust and implementing the browser's top-level user interface using HTML, CSS, and TypeScript to reduce dependencies on traditional C++ frameworks. Additionally, Google is moving all Chrome third-party dependencies onto automated update pipelines to ensure they are up-to-date, with the goal of creating a browser that is continuously protected without disrupting the user.

---

> *Pick battles big enough to matter, small enough to win.
Author: Jonathan Kozol*

Source: [Three Recent Chrome Releases Fix 1,442 Flaws, More Than Prior 23 Updates Combined](https://thehackernews.com/2026/07/three-recent-chrome-releases-fix-1442.html)
