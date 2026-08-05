---
title: "New cPanel Critical Flaw Could Let Hosting Customers Run SQL as Database Root"
date: 2026-08-04T10:36:27+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the critical flaw in cPanel:

A critical flaw has been discovered in cPanel, a popular web hosting control panel, which allows an authenticated hosting customer to execute SQL commands with full administrative privileges. The flaw, tracked as CVE-2026-58048, affects all supported versions of cPanel & WHM and can be exploited by a valid cPanel account holder with access to the MySQL/MariaDB feature. This vulnerability can lead to operating-system-level compromise, depending on the configuration of the database engine and operating system.

The flaw is caused by a failure in cPanel's database-renaming process, which allows SQL to run in the database administrative context, bypassing normal database-level privileges. cPanel has patched the vulnerability in several builds, including 11.110.0.137, 11.118.0.71, and 11.126.0.78. Servers that cannot update immediately can temporarily revoke the MySQL feature from cPanel users to prevent exploitation. The US Cybersecurity and Infrastructure Security Agency (CISA) has rated the flaw as having a total technical impact, but notes that there is currently no known exploitation.

In addition to the critical database flaw, cPanel has also patched two other vulnerabilities: an HTTP request-smuggling issue (CVE-2026-58047) and a local privilege escalation vulnerability in Exim (GCVE-25-2026-07-45-3). The request-smuggling issue can be exploited by an unauthenticated remote attacker to manipulate responses delivered to other users on the same server, while the Exim vulnerability can be triggered by a local user's .forward file to execute arbitrary code. cPanel has provided workarounds and patches for these vulnerabilities, and users are advised to update their systems as soon as possible to prevent exploitation.

---

> *Think for yourselves and let others enjoy the privilege to do so too.
Author: Voltaire*

Source: [New cPanel Critical Flaw Could Let Hosting Customers Run SQL as Database Root](https://thehackernews.com/2026/08/new-cpanel-critical-flaw-could-let.html)
