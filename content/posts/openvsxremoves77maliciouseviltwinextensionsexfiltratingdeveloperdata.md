---
title: "Open VSX Removes 77 Malicious Evil Twin Extensions Exfiltrating Developer Data"
date: 2026-08-05T09:23:03+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Here are 3 concise paragraphs summarizing the article:

A recent discovery has found 77 malicious "evil twin" extensions on the Open VSX marketplace, which impersonate legitimate developer tools while transmitting sensitive information about the systems and development environments they are installed on. These extensions were uploaded between July 26 and August 1, 2026, and have since been removed from the repository. The malicious extensions send data such as hostname, workspace folder name, and editor version to a domain called "mangorbit[.]com", which was registered on July 15, 2026.

The extensions can be categorized into two sets: lightweight tools that exfiltrate basic information and reconnaissance payloads that transmit more detailed data, including local hostname, operating system username, and editor version. The malicious code has contingency plans in place, including a retry mechanism and a fallback exfiltration URL, to ensure data transmission in case the primary domain is blocked. The extensions also inspect files in the workspace's .git directory, enumerate installed extension IDs, and extract CI markers and environment variables.

The discovery of these malicious extensions comes amidst a larger software supply chain attack, codenamed ChainDrop, which has compromised 450 unique npm packages and delivered an information stealer. The attack has been found to use a self-propagating credential-stealing worm and has established persistence by injecting configuration files into repositories. Security researchers are calling for a more granular security layer to prevent such attacks, including permission control over what packages can and can't do, and requiring permission before exfiltrating sensitive data.

---

> *Build a better mousetrap and the world will beat a path to your door.
Author: Ralph Emerson*

Source: [Open VSX Removes 77 Malicious Evil Twin Extensions Exfiltrating Developer Data](https://thehackernews.com/2026/08/open-vsx-removes-77-malicious-evil-twin.html)
