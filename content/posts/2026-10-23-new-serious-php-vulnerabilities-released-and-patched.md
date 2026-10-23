---
title: "New Serious PHP Vulnerabilities Released and Patched"
description: "PHP maintainers released patches for two critical vulnerabilities affecting PHP 8.5.12, 8.4.27, 8.3.36, and 8.2.35. The flaws allow unauthenticated re..."
source: "Schneier on Security"
source_url: "https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html"
published: "2026-10-22T13:26:51+00:00"
ingested_at: "2026-10-23T03:10:51.943299+00:00"
date: "2026-10-23T03:10:51.943299+00:00"
category: "vulnerabilities"
tags:
  - "php"
  - "remote-code-execution"
  - "vulnerability"
  - "web-server"
slug: "2026-10-23-new-serious-php-vulnerabilities-released-and-patched"
quote: "There is nothing so useless as doing efficiently that which should not be done at all."
quote_author: "Peter Drucker"
---

### Executive Summary
PHP maintainers released patches for two critical vulnerabilities affecting PHP 8.5.12, 8.4.27, 8.3.36, and 8.2.35. The flaws allow unauthenticated remote code execution before application code runs, targeting PHP-FPM, Apache mod_php, php-cgi, FrankenPHP, and LiteSpeed. All PHP users are urged to update immediately.

---
**Intelligence Metadata**
- **Source Publisher:** Schneier on Security
- **Published Date:** 2026-10-22T13:26:51+00:00
- **Category:** vulnerabilities

**Original Description:**
PHP maintainers have released fixes for two critical vulnerabilities: PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 fix two critical vulnerabilities that can allow unauthenticated remote code execution. All PHP users are strongly encouraged to update immediately. Who is at risk: all PHP installations serving web requests, including PHP-FPM, Apache with mod_php, php-cgi, FrankenPHP and LiteSpeed. We consider the risk highest for mod_php, with a demonstrated exploit where an unauthenticated request can...
