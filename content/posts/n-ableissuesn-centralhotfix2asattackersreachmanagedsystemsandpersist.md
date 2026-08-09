---
title: "N-able Issues N-central Hotfix 2 as Attackers Reach Managed Systems and Persist"
date: 2026-08-08T06:57:43+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

N-able has released a new hotfix for its N-central Remote Monitoring and Management (RMM) product to address an ongoing exploitation of a security flaw. The company detected unusual activity on July 31, 2026, which led to the discovery of unknown threat actors exploiting a zero-day flaw (CVE-2026-18577) in the N-central server. This vulnerability allows authentication bypass and account takeover, and has been flagged as actively exploited by the US Cybersecurity and Infrastructure Security Agency (CISA).

The attackers were able to obtain administrative access remotely and leverage the Take Control feature to connect to systems within the N-central managed environment. They then registered a new service for a Cloudflare Tunnel, enabling persistence even after access to the N-central server was revoked. N-able has confirmed that a limited number of customers have been affected by the exploitation activity. The company has advised customers running an on-premise version to update their instances to 026.3.1.10 immediately.

N-able has also shared a list of IP addresses as indicators of compromise (IoCs) and released a custom service template to help customers check for known IoCs against Windows device endpoints in N-central. The company has warned that a clean result should not be interpreted as a guarantee that the environment has not been impacted, and recommends a thorough review of environment, logs, and account activity. The investigation is ongoing, and additional indicators may be identified over time. Customers are advised to apply the new hotfix, even if they have already applied the previous hotfix, as it supersedes the earlier fix with additional hardening measures.

---

> *A rolling stone gathers no moss.
Author: Publilius Syrus*

Source: [N-able Issues N-central Hotfix 2 as Attackers Reach Managed Systems and Persist](https://thehackernews.com/2026/08/n-central-attackers-reach-managed.html)
