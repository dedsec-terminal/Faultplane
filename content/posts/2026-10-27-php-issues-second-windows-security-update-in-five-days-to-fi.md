---
title: "PHP Issues Second Windows Security Update in Five Days to Fix Brotli Code Execution Flaw"
description: "PHP released a second Windows security update within five days to address CVE-2026-111497, a flaw in the Brotli compression library that could corrupt..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/10/php-issues-second-windows-security.html"
published: "2026-10-26T17:45:57+00:00"
ingested_at: "2026-10-27T03:31:32.257279+00:00"
date: "2026-10-27T03:31:32.257279+00:00"
category: "cves"
tags:
  - "PHP"
  - "Brotli"
  - "CVE-2026-111497"
  - "cURL"
  - "Windows"
slug: "2026-10-27-php-issues-second-windows-security-update-in-five-days-to-fi"
quote: "These days people seek knowledge, not wisdom. Knowledge is of the past, wisdom is of the future."
quote_author: "Vernon Cooper"
---

### Executive Summary
PHP released a second Windows security update within five days to address CVE-2026-111497, a flaw in the Brotli compression library that could corrupt memory and enable code execution. The vulnerability is triggered via the cURL extension when it automatically decompresses HTTP responses. Official Windows packages for PHP 8.2‑8.5 were rebuilt to mitigate the issue.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-10-26T17:45:57+00:00
- **Category:** cves

**Original Description:**
PHP has rebuilt its official Windows packages for PHP 8.2 through 8.5 to fix CVE-2026-111497, a flaw in the Brotli compression library that the packages include. The flaw can let an attacker corrupt memory and potentially run code. PHP says the flaw can be reached through the cURL extension when the extension decompresses HTTP responses automatically. cURL leaves that off by default, but
