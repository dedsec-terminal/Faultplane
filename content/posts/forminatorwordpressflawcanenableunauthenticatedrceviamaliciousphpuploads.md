---
title: "Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads"
date: 2026-08-17T18:22:09+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A critical security flaw has been disclosed in Forminator Forms, a WordPress plugin with more than 600,000 active installations, that could be exploited to achieve arbitrary code execution on susceptible sites.
The vulnerability, tracked as CVE-2026-15748, is rated 9.8 out of 10.0 on the CVSS scoring system. It was discovered and reported by a security researcher who goes by the online alias "daroo."
"This vulnerability makes it possible for unauthenticated attackers to upload arbitrary files, including executable PHP files, to a vulnerable site, which can lead to remote code execution and complete site compromise," Wordfence said in a report published today.
That said, a key prerequisite for successful exploitation is that the sites must have a form containing both a File Upload field and a Select field. The vulnerability impacts all versions of the plugin before and including 1.56.1. It has been addressed in version 1.56.2 released on July 31, 2026.
Per the WordPress security company

---

> *Sooner or later, those who win are those who think they can.
Author: Richard Bach*

Source: [Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads](https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html)
