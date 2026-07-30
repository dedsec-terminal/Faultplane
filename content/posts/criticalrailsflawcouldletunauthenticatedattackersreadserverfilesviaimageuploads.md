---
title: "Critical Rails Flaw Could Let Unauthenticated Attackers Read Server Files via Image Uploads"
date: 2026-07-29T18:10:00+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A critical vulnerability has been discovered in Ruby on Rails, specifically in the Active Storage component, which could allow unauthenticated attackers to read arbitrary files from application servers through crafted image uploads. The flaw, tracked as CVE-2026-66066 with a CVSS score of 9.5, can expose sensitive information such as secret keys, database passwords, and API tokens, potentially enabling remote code execution or lateral movement into connected systems.

The vulnerability affects Rails applications that use libvips for image processing and accept image uploads from untrusted users. The affected versions include Rails 7.0.0 through 7.2.3.1, Rails 8.0.0 through 8.0.5, and Rails 8.1.0 through 8.1.3, as well as Rails 6.0.0 through 6.1.7.10 when Active Storage is configured to use Vips. To fix the issue, operators should upgrade to Rails 7.2.3.2, 8.0.5.1, or 8.1.3.1 and rotate every secret readable by the application process.

The patch for the vulnerability involves calling `Vips.block_untrusted(true)` when Active Storage starts, which blocks untrusted operations in libvips. Applications that cannot immediately update Rails can set `VIPS_BLOCK_UNTRUSTED` when running libvips 8.13 or later, or call `Vips.block_untrusted(true)` with ruby-vips 2.2.1 or later. The researchers who discovered the vulnerability have not published a proof-of-concept exploit, and there is no evidence of in-the-wild exploitation at this time. However, operators are advised to take immediate action to patch the vulnerability and rotate sensitive credentials to prevent potential attacks.

---

> *Your work is to discover your world and then with all your heart give yourself to it.
Author: Buddha*

Source: [Critical Rails Flaw Could Let Unauthenticated Attackers Read Server Files via Image Uploads](https://thehackernews.com/2026/07/critical-rails-flaw-could-let.html)
