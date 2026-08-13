---
title: "A stranger has been reading Salesforce and ServiceNow portals worldwide for 17 months"
date: 2026-08-12T13:51:02+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here is a summary of the article in three concise paragraphs:

A security researcher at Reco has been tracking a campaign called City-Forum, where an unknown individual has been accessing Salesforce and ServiceNow portals worldwide for 17 months. The attacker has been using a generic rented server from a German hosting provider to pull records from these portals, targeting telecom operators, banks, financial services firms, and public-sector portals. Notably, no software was exploited, and no credentials were needed, as the attacker simply visited public customer portals as an anonymous visitor and requested their contents.

The issue lies in the fact that both Salesforce and ServiceNow have a guest user account that is enabled by default, which allows unauthenticated visitors to access certain information. The attacker has been exploiting this feature by building their own tools to extract data from these portals. The researcher notes that the core issue is that what is public and what should be public are two different things, and the attacker has been exploiting this gap. The campaign is notable for its use of custom-built tools that target previously unexploited areas of the platforms, including Salesforce's newer site framework and a ServiceNow portal search endpoint.

The researcher provides guidance on how to detect and remediate this issue, including checking for specific patterns in logs and tightening guest sharing rules. The most common misconfiguration is guest/anonymous over-permission, and the highest-impact fix is to review and restrict sharing rules. The researcher emphasizes that this is a finite job that requires careful review of portal configurations and permissions. If an organization detects this pattern, they should confirm it and then remediate by tightening guest permissions and reviewing knowledge base access criteria. Ultimately, the goal is to prevent unauthorized access to sensitive information and to ensure that only authorized users can access certain data.

---

> *Our intention creates our reality.
Author: Wayne Dyer*

Source: [A stranger has been reading Salesforce and ServiceNow portals worldwide for 17 months](https://www.helpnetsecurity.com/2026/08/12/salesforce-servicenow-guest-user-exposure/)
