---
title: "phpAfterShell Explained: How Hackers Could Turn a PHP Session Flaw Into Code Execution"
description: "PHP\u2019s default file\u2011based session storage can be manipulated by truncating a session write, causing PHP to deserialize attacker\u2011chosen objects. When pa..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/11/phpaftershell-explained-how-hackers.html"
published: "2026-11-19T16:59:56+00:00"
ingested_at: "2026-11-20T05:32:12.978073+00:00"
date: "2026-11-20T05:32:12.978073+00:00"
category: "vulnerabilities"
tags:
  - "php"
  - "session"
  - "code execution"
  - "CVE-2026-126714"
  - "phpAfterShell"
slug: "2026-11-20-phpaftershell-explained-how-hackers-could-turn-a-php-session"
quote: "Setting an example is not the main means of influencing another, it is the only means."
quote_author: "Albert Einstein"
---

### Executive Summary
PHP’s default file‑based session storage can be manipulated by truncating a session write, causing PHP to deserialize attacker‑chosen objects. When paired with a suitable gadget chain in the application, these objects enable remote code execution on the server. The flaw, identified as CVE‑2026‑126714, is now fixed in current PHP releases.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-11-19T16:59:56+00:00
- **Category:** vulnerabilities

**Original Description:**
PHP's default file-based session storage can be made to return objects an attacker chose, by cutting off a session write at the right moment. When combined with a second weakness, such as a suitable gadget chain in the app, those objects can allow the attacker to run code on the server. Today's PHP releases fix the flaw, called phpAfterShell. The flaw is tracked as CVE-2026-126714 and rated
