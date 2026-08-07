---
title: "ChainDrop: Inside a Self-Propagating npm Worm"
date: 2026-08-06T22:26:39+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the ChainDrop npm worm:

The ChainDrop npm worm is a self-propagating malware that infected over 400 packages, including widely used ones like keyv and cacheable-request, which are downloaded hundreds of millions of times each week. The worm steals sensitive developer data, including cloud credentials, npm and GitHub tokens, SSH keys, and other credentials, and can also extract temporary credentials from GitHub Actions runner memory. It can use stolen npm publishing tokens to infect and republish additional packages while preserving their legitimate functionality.

The worm's attack chain involves a subtle modification to an infected package's package.json file, which points to a dropper that downloads and executes a JavaScript payload. The payload spawns a detached background process that harvests credentials from the environment, including cloud credentials, developer tooling, AI tools, and other sensitive information. The worm also establishes persistence mechanisms, including cross-linked persistence through VS Code and Claude Code, and a latent capability for OS-level persistence.

To mitigate the ChainDrop worm, Unit 42 recommends identifying and removing affected package versions, investigating developer workstations and CI runners for signs of compromise, and reviewing unexpected npm publishing and GitHub repository activity. Additionally, revoking and rotating potentially exposed credentials, removing identified persistence mechanisms, and blocking exfiltration channels can help prevent further compromise. Palo Alto Networks customers can use various tools, including Koi Agentic Endpoint Security and Cortex XDR, to help identify and control malicious packages and detect and respond to ChainDrop activity.

---

> *Reason and free inquiry are the only effectual agents against error.
Author: Thomas Jefferson*

Source: [ChainDrop: Inside a Self-Propagating npm Worm](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)
