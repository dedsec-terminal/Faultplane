---
title: "Bing Images Flaws Let Crafted SVGs Run Commands as SYSTEM on Microsoft's Servers"
date: 2026-07-24T11:45:17+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here is a summary of the article in three concise paragraphs:

A security vulnerability was discovered in Bing's image search feature, allowing crafted SVG files to run commands as SYSTEM on Microsoft's production image-processing workers. The vulnerability was found by autonomous offensive security startup XBOW, which reported it privately to Microsoft. The issue was caused by the application treating an image as a command, allowing an attacker to execute arbitrary commands on the server. Microsoft issued two critical CVEs (CVE-2026-32194 and CVE-2026-32191) and rated them 9.8 on the CVSS scale.

The vulnerability was exploited by submitting a crafted SVG file to Bing's image search, which would run a command on the worker and curl the output back to a collector controlled by the attacker. The payload was a one-pixel SVG whose reference ran a command on the worker, allowing the attacker to gain SYSTEM-level access to the server. The vulnerability did not require authentication, cookies, session state, or a click, and could be exploited by hosting the SVG file anywhere and providing its URL to the search through the imgurl parameter.

To prevent similar vulnerabilities, XBOW recommends denying delegates in ImageMagick's policy.xml file, cutting the formats accepted by the application, reviewing and disabling unnecessary delegates, running conversion sandboxed and with reduced privileges, and blocking outbound network access from the worker. The company also emphasizes the importance of testing after any policy change and treating image helpers as part of the attack surface. By following these recommendations, applications can reduce the risk of similar vulnerabilities and prevent attackers from exploiting image-processing workers to gain unauthorized access to sensitive systems.

---

> *Love is the only force capable of transforming an enemy into friend.
Author: Martin Luther King, Jr.*

Source: [Bing Images Flaws Let Crafted SVGs Run Commands as SYSTEM on Microsoft's Servers](https://thehackernews.com/2026/07/bing-images-flaws-let-crafted-svgs-run.html)
