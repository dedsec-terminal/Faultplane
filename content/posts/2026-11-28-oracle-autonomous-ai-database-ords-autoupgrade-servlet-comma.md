---
title: Oracle Autonomous AI Database ORDS AutoUpgrade Servlet Command Injection Vulnerability
description: A flaw in the AutoUpgrade servlet of Oracle REST Data Services (ORDS)
  allows remote attackers to execute arbitrary code on Oracle Autonomous AI Databa...
source: Zero Day Initiative
source_url: http://www.zerodayinitiative.com/advisories/ZDI-26-1149/
published: '2026-11-24T06:00:00+00:00'
ingested_at: '2026-11-28T06:05:31.052979+00:00'
date: '2026-11-28T06:05:31.052979+00:00'
category: vulnerabilities
tags:
- Oracle
- Command Injection
- Remote Code Execution
- AutoUpgrade
- REST Data Services
slug: 2026-11-28-oracle-autonomous-ai-database-ords-autoupgrade-servlet-comma
quote: When fate hands us a lemon, lets try to make lemonade.
quote_author: Dale Carnegie
---

### Executive Summary

A flaw in the AutoUpgrade servlet of Oracle REST Data Services (ORDS) allows remote attackers to execute arbitrary code on Oracle Autonomous AI Database installations. The vulnerability requires authentication, but the existing authentication mechanism can be bypassed, and the lack of proper validation of a configuration property permits OS command injection. Attackers can combine this flaw with other vulnerabilities to run code in the context of the oracle service account. Oracle has released an update to remediate the issue. Users are advised to apply the vendor patch immediately to mitigate the risk.

### Original Overview

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle Autonomous AI Database. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the AutoUpgrade servlet in Oracle REST Data Services. The issue results from the lack of proper validation of a configuration property before using it to construct an OS command. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the oracle service account. Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cspunov2026.html 2026-10-26 - Vulnerability reported to vendor...
