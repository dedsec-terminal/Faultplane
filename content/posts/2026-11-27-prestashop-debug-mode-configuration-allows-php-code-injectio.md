---
title: PrestaShop Debug Mode Configuration Allows PHP Code Injection
description: PrestaShop’s back‑office Performance > Debug mode configuration is vulnerable
  to PHP code injection. An authenticated user with permission to edit deb...
source: CERT/CC Vulnerability Notes
source_url: https://kb.cert.org/vuls/id/385711
published: '2026-11-09T14:53:28+00:00'
ingested_at: '2026-11-27T19:47:03.207902+00:00'
date: '2026-11-27T19:47:03.207902+00:00'
category: vulnerabilities
tags:
- PrestaShop
- PHP
- code injection
- arbitrary code execution
- debug mode
slug: 2026-11-27-prestashop-debug-mode-configuration-allows-php-code-injectio
quote: Spring is a time for rebirth and the fulfilment of new life.
quote_author: Byron Pulsifer
---

### Executive Summary

PrestaShop’s back‑office Performance > Debug mode configuration is vulnerable to PHP code injection. An authenticated user with permission to edit debug‑mode settings can submit crafted cookie values that are written into config/defines.inc.php or config/defines_custom.inc.php, causing arbitrary PHP code to execute with the privileges of the PHP process. The flaw does not grant root access, but it can expose application secrets, modify or delete files and database contents, and disrupt store operations. Administrators are advised to upgrade to PrestaShop 9.2.1 or later, limit who can change debug‑mode settings, restrict back‑office network access, and, where possible, prevent the PHP process from writing to the configuration files.

### Original Overview

Overview PrestaShop's back-office Performance > Debug mode functionality contains a PHP code injection vulnerability. An authenticated attacker with permission to modify debug-mode configuration can submit crafted cookie configuration values that are written into an executable PHP configuration file. Successful exploitation could allow arbitrary code execution with the privileges of the PHP process. Description PrestaShop is an open-source e-commerce platform for creating and managing online stores. Its back-office Performance configuration includes a Debug mode for developers, which is enabled based on a specified cookie name and value. PrestaShop's debug-mode configuration code inserts the user-controlled values debug_cookie_name and debug_cookie_value into a PHP expression without...
