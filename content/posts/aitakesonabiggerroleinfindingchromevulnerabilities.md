---
title: "AI takes on a bigger role in finding Chrome vulnerabilities"
date: 2026-07-30T17:01:33+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Google has expanded its use of Artificial Intelligence (AI) in Chrome's security workflow to find vulnerabilities, triage bug reports, generate patches, and review code. The AI-powered system, which includes a Gemini-based vulnerability discovery tool, has been used to identify flaws in the Chrome codebase, including a sandbox escape vulnerability that had gone undetected for over 13 years. The AI system has also been trained on Chrome's Git history and previously disclosed Common Vulnerabilities and Exposures (CVEs) to improve its accuracy.

The AI system is also being used to assist with remediation, generating candidate patches, reviewing proposed fixes, and writing tests before engineers review the changes. This has led to a significant increase in the number of security bugs fixed, with Chrome 149 and Chrome 150 including fixes for 1,072 security bugs. Google notes that the higher number of reported vulnerabilities reflects improved detection rather than a decline in Chrome's security. The company is also working to reduce the "patch gap" between publishing a security fix and users installing the update, by piloting two security releases a week and developing dynamic patching.

Google is also making longer-term security improvements, including expanding a memory-safety tool called MiraclePtr and migrating new components to the memory-safe language Rust. The company is also using AI models to scan code changes before they are merged, catching potential vulnerabilities. Additionally, Google is contributing $12.5 million to the Alpha-Omega project, which supports open-source maintainers, and is moving third-party components to pipelines that update them automatically. The company believes that by combining rapid deployment mechanisms with deep structural defenses, it can ensure that the advantage remains with defenders and make Chrome and the broader web safer with every update.

---

> *Silence is the true friend that never betrays.
Author: Confucius*

Source: [AI takes on a bigger role in finding Chrome vulnerabilities](https://www.helpnetsecurity.com/2026/07/30/google-chrome-ai-security-workflow/)
