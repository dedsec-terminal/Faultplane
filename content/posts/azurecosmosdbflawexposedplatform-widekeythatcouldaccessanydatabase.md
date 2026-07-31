---
title: "Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database"
date: 2026-07-30T13:34:09+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A vulnerability in Azure Cosmos DB, discovered by Wiz, could have allowed an attacker to escape the service's Gremlin query sandbox and gain full read and write access to databases across customer tenants. The exploit chain, codenamed CosmosEscape, began with a crafted query against a Gremlin database controlled by the attacker, which led to code execution on a multi-tenant gateway. This exposed a platform-wide signing secret and a regional account directory, allowing the researchers to locate a target and retrieve its primary account key.

The vulnerability was reported to Microsoft in November 2025, and the company blocked the vulnerable Gremlin entry point within 48 hours. A longer-term fix was completed in July 2026, eliminating the platform-wide key. Microsoft has stated that it has fully addressed the issue and found no evidence of customer impact based on its investigations. The company also said that no customer data was accessed and no customer action is required. Wiz will present the complete exploit chain at a Black Hat USA briefing on August 6.

The exploit took advantage of a custom Gremlin engine that translates Gremlin queries into .NET code, which failed to account for .NET reflection. This allowed the researchers to build file-read and file-write primitives and eventually achieve arbitrary code execution. The vulnerability could have potentially exposed databases supporting Microsoft products such as Teams and Copilot, which store data in Cosmos DB. However, Wiz did not report accessing any sensitive data, and Microsoft's review found no unauthorized activity outside the researchers' testing. The duration of potential exposure remains unknown, but the known path has since been closed.

---

> *The thing always happens that you really believe in; and the belief in a thing makes it happen.
Author: Frank Wright*

Source: [Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database](https://thehackernews.com/2026/07/azure-cosmos-db-flaw-exposed-platform.html)
