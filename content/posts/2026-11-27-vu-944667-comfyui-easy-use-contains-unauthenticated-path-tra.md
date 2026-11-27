---
title: 'VU#944667: ComfyUI-Easy-Use contains unauthenticated path traversal vulnerability'
description: Overview ComfyUI-Easy-Use version 1.4.1 and earlier contains a vulnerability
  in its save_preview() handler that allows an unauthenticated attacker to...
source: CERT/CC Vulnerability Notes
source_url: https://kb.cert.org/vuls/id/944667
published: '2026-11-12T14:48:14+00:00'
ingested_at: '2026-11-27T19:39:14.691005+00:00'
date: '2026-11-27T19:39:14.691005+00:00'
category: vulnerabilities
tags:
- vulnerabilities
slug: 2026-11-27-vu-944667-comfyui-easy-use-contains-unauthenticated-path-tra
quote: We all have problems. The way we solve them is what makes us different.
quote_author: Unknown
---

### Executive Summary

Overview ComfyUI-Easy-Use version 1.4.1 and earlier contains a vulnerability in its save_preview() handler that allows an unauthenticated attacker to overwrite an installed custom node’s Python file. An attacker who can reach the affected ComfyUI instance over the network can use the overwrite to execute arbitrary code when ComfyUI restarts. Description ComfyUI is a node-based interface for building generative AI workflows. ComfyUI-Easy-Use is an extension that adds custom nodes and workflow utilities. An attacker can upload a Python file to ComfyUI’s input directory then use save_preview() to copy that file over an installed custom node’s __init__.py . Upon restart, ComfyUI will import and execute the modified node. Remote exploitation requires a deployment that exposes the affected...
