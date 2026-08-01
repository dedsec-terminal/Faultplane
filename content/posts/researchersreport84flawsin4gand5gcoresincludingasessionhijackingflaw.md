---
title: "Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw"
date: 2026-07-31T11:55:00+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Researchers from Singapore's Nanyang Technological University have discovered 84 security vulnerabilities in 4G and 5G core networks, including a session hijacking flaw. The vulnerabilities, which can trigger denial-of-service (DoS) attacks and session hijacking, are caused by implicit trust between core network functions. The researchers found that the transition to cloud-native deployments has made the trust model "fragile" and expanded the attack surface, allowing adversaries to potentially reach previously internal interfaces.

The study, which analyzed seven open-source LTE/5G core network implementations, used a large language model (LLM)-assisted multi-agent system to detect and categorize the vulnerabilities. The system, dubbed iFinder, identified a pattern of blind trust among core network components, which can be exploited by an external actor for conducting malicious activities. The researchers found that some of the identified weaknesses relate to a lack of due diligence in validating message format, message semantics, and resource availability. The vulnerabilities have been codenamed implicit trust errors (iTrue).

The researchers demonstrated a hypothetical DoS attack scenario against Open5GS LTE and a session hijacking attack scenario, where an attacker can send crafted PFCP or GTP-C messages to trigger the vulnerability. The session hijacking vulnerability has been discovered on two real-world commercial 5G core networks, with one vendor addressing the defect and the other still in the remediation process. The researchers emphasize that the continually increasing number of vulnerabilities demonstrates a broader and ongoing security problem that requires urgent attention from vendors and network operators.

---

> *Remember that sometimes not getting what you want is a wonderful stroke of luck.
Author: Dalai Lama*

Source: [Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw](https://thehackernews.com/2026/07/researchers-report-84-flaws-in-4g-and.html)
