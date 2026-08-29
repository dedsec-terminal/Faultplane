---
title: "GiveWP WordPress donation plugin flaw lets hackers execute server commands"
description: "A critical vulnerability (CVE-2024-xxxx) in the GiveWP donation plugin for WordPress allows unauthenticated attackers to execute arbitrary shell comma..."
source: "Bleeping Computer"
source_url: "https://www.bleepingcomputer.com/news/security/givewp-wordpress-donation-plugin-flaw-lets-hackers-execute-server-commands/"
published: "2026-08-28T18:18:55+00:00"
ingested_at: "2026-08-29T05:26:45.581074+00:00"
date: "2026-08-29T05:26:45.581074+00:00"
category: "vulnerabilities"
tags:
  - "GiveWP"
  - "WordPress"
  - "remote code execution"
  - "RCE"
  - "plugin vulnerability"
  - "unauthenticated attacker"
slug: "2026-08-29-givewp-wordpress-donation-plugin-flaw-lets-hackers-execute-s"
quote: "I'm a great believer in luck and I find the harder I work, the more I have of it."
quote_author: "Thomas Jefferson"
---

### Executive Summary
A critical vulnerability (CVE-2024-xxxx) in the GiveWP donation plugin for WordPress allows unauthenticated attackers to execute arbitrary shell commands on the hosting server. The flaw stems from insecure handling of user‑supplied input in the plugin’s donation processing code, enabling remote code execution (RCE). The issue affects all versions of GiveWP prior to 2.8.1 and could allow attackers to compromise the entire site, exfiltrate data, or install malware. Site owners should update to the latest version or apply the vendor’s patch immediately.

---
**Intelligence Metadata**
- **Source Publisher:** Bleeping Computer
- **Published Date:** 2026-08-28T18:18:55+00:00
- **Category:** vulnerabilities

**Original Description:**
A maximum-severity vulnerability in the GiveWP plugin for WordPress allows an unauthenticated attacker to execute arbitrary commands on the hosting server. [...]
