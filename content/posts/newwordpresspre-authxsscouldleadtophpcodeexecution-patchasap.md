---
title: "New WordPress Pre-Auth XSS Could Lead to PHP Code Execution - Patch ASAP"
date: 2026-08-07T12:56:23+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here is a 3-paragraph summary of the article:

A high-severity vulnerability has been discovered in WordPress, affecting all versions of the content management system. The pre-authentication reflected cross-site scripting (XSS) flaw, tracked as CVE-2026-64638, can be exploited to execute PHP code on the server when a logged-in administrator interacts with an attacker-controlled page. The vulnerability requires no attacker privileges and can be triggered by a crafted username on the login page, which executes JavaScript in the visitor's browser without further interaction.

The vulnerability was discovered by pwn.ai, which demonstrated how the flaw can be chained into PHP code execution on the server. The attack, dubbed "XSS2Shell," involves a series of steps, including exploiting the XSS vulnerability, invoking a WordPress REST request, and using a permitted JSONP property chain to invoke a method in another browser window. The researchers found that the vulnerability can be exploited to install a plugin, upload an arbitrary ZIP file, and execute PHP code on the server, potentially exposing sensitive data and allowing an attacker to take control of the site.

WordPress has released a security update, version 7.0.3, which patches the vulnerability and includes fixes backported to version 4.7. The update is available for all versions of WordPress, and users are advised to update immediately to prevent exploitation. The researchers emphasize that known WordPress hardening measures are not sufficient to mitigate the underlying XSS vulnerability, and that applying the security update is the only way to ensure protection. As of August 7, there have been no reported instances of in-the-wild exploitation, but users are urged to update their sites as soon as possible to prevent potential attacks.

---

> *The only limit to your impact is your imagination and commitment.
Author: Tony Robbins*

Source: [New WordPress Pre-Auth XSS Could Lead to PHP Code Execution - Patch ASAP](https://thehackernews.com/2026/08/new-wordpress-pre-auth-xss-could-lead.html)
