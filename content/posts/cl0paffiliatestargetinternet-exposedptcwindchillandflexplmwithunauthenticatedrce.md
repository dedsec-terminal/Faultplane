---
title: "Cl0p Affiliates Target Internet-Exposed PTC Windchill and FlexPLM with Unauthenticated RCE"
date: 2026-07-25T10:14:03+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

The Cl0p ransomware group is targeting internet-exposed PTC Windchill and FlexPLM deployments with a new data extortion campaign. The attackers are exploiting a critical security flaw, CVE-2026-12569, which has a CVSS score of 9.3 and was recently added to the US Cybersecurity and Infrastructure Security Agency's (CISA) Known Exploited Vulnerabilities catalog. This vulnerability allows for unauthenticated remote code execution and deployment of JSP web shells, enabling the attackers to gain an initial foothold.

Upon gaining access, the attackers conduct file system enumeration, stage engineering and design data, and carry out double extortion data theft. The targets of this campaign include manufacturing, automotive, aerospace, and retail sectors. The attackers are also exploiting a pre-authentication information disclosure in the FlexPLM WSDL endpoint, which has a CVSS score of 7.5, to enable unauthenticated exploitation. The extortion emails appear to originate from previously compromised accounts and are sent to hundreds of users within an impacted organization.

Ransom-ISAC has shared four IP addresses as indicators of compromise (IoCs), and PTC has warned customers of heightened threat activity. The Cl0p gang has a history of exploiting security flaws in widely-used enterprise products to break into target organizations for data theft and extortion attacks. Previous campaigns have targeted file transfer appliances and vulnerabilities in Oracle E-Business Suite. The actor behind these attacks remains unconfirmed, but the observed tradecraft shares characteristics with previous Cl0p campaigns. Organizations are advised to take immediate action to protect themselves from this threat.

---

> *There is no way to prosperity, prosperity is the way.
Author: Wayne Dyer*

Source: [Cl0p Affiliates Target Internet-Exposed PTC Windchill and FlexPLM with Unauthenticated RCE](https://thehackernews.com/2026/07/cl0p-affiliates-target-internet-exposed.html)
