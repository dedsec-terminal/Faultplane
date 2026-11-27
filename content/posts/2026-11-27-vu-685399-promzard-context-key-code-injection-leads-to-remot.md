---
title: 'VU#685399: PromZard context key code injection leads to remote code execution'
description: Overview The npm library promzard , versions 4.0.0 and earlier, is vulnerable
  to remote code execution due to direct string interpolation of context o...
source: CERT/CC Vulnerability Notes
source_url: https://kb.cert.org/vuls/id/685399
published: '2026-11-12T15:09:39+00:00'
ingested_at: '2026-11-27T19:39:14.690005+00:00'
date: '2026-11-27T19:39:14.690005+00:00'
category: vulnerabilities
tags:
- vulnerabilities
slug: 2026-11-27-vu-685399-promzard-context-key-code-injection-leads-to-remot
quote: Being right is highly overrated. Even a stopped clock is right twice a day.
quote_author: Unknown
---

### Executive Summary

Overview The npm library promzard , versions 4.0.0 and earlier, is vulnerable to remote code execution due to direct string interpolation of context object keys, which allows unsanitized JavaScript code injection. Description promzard is a Node.js library designed to automate configuration workflows by evaluating template modules and generating data objects via interactive prompting. The library allows users to provide a context object ctx to expose specific data to the template module. promzard builds an object by walking the template module for prompt() and asynchronous functions. The keys of ctx , however, are treated as raw JavaScript source code instead of inert data. The implementation performs direct string interpolation of ctx keys, without validation or sanitization, into the...
