---
title: "Greatness PhaaS Adds Device Code Phishing to Bypass MFA and Steal Tokens"
date: 2026-08-04T17:27:39+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

The Greatness PhaaS (Phishing-as-a-Service) toolkit has added device code phishing to its capabilities, allowing cybercriminals to bypass Multi-Factor Authentication (MFA) and steal tokens. This commercial crimeware solution provides a range of features, including AiTM (adversary-in-the-middle) credential and token theft, device code phishing, and OAuth consent abuse, all accessible through a single operator panel. The platform supports multiple target platforms, including iCloud, Yahoo, and Google Workspace, and has been used to target Microsoft 365 business users since at least mid-2022.

The Greatness PhaaS kit is available through a subscription model, with prices starting at $289 per month, and provides users with a range of tools and templates to conduct phishing campaigns. The platform includes a dashboard with campaign statistics, domain configuration, and CAPTCHA selection, as well as over 11 downloadable lure templates. The kit also includes anti-analysis protections, User-Agent fingerprinting, and a CAPTCHA gate to evade detection. The device code phishing branch is a new addition to the platform, allowing cybercriminals to silently obtain tokens without user interaction by leveraging the OAuth device authorization grant flow.

The use of Greatness and other PhaaS kits has led to a significant increase in phishing attacks, with device code phishing being a particularly effective tactic. Recent campaigns have used spoofed RingCentral voicemail lures to bypass email gateways and exploit the trust configuration of legitimate RingCentral customers. To prevent device code phishing attacks, it is recommended to block the authentication method at a global level in Conditional Access Policies and move to phishing-resistant MFA methods. Additionally, employees should be taught to distrust unexpected codes, and the permitted usage of the device code flow should be continuously audited and revoked as soon as it's no longer necessary.

---

> *It is better to take many small steps in the right direction than to make a great leap forward only to stumble backward.*

Source: [Greatness PhaaS Adds Device Code Phishing to Bypass MFA and Steal Tokens](https://thehackernews.com/2026/08/greatness-phaas-adds-device-code.html)
