---
title: "Ghostscript Sandbox Escape RCE via Crafted File Uploads in Popular Apps"
description: "Security firm pwn.ai demonstrated that a now-patched vulnerability in Ghostscript allows crafted files to escape its sandbox and execute arbitrary com..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/11/researchers-demonstrate-ghostscript.html"
published: "2026-11-22T05:03:41+00:00"
ingested_at: "2026-11-23T05:31:49.683873+00:00"
date: "2026-11-23T05:31:49.683873+00:00"
category: "threat-intel"
tags:
  - "Ghostscript"
  - "sandbox escape"
  - "RCE"
  - "file upload"
  - "Linux"
slug: "2026-11-23-ghostscript-sandbox-escape-rce-via-crafted-file-uploads-in-p"
quote: "I'm a great believer in luck and I find the harder I work, the more I have of it."
quote_author: "Thomas Jefferson"
---

### Executive Summary
Security firm pwn.ai demonstrated that a now-patched vulnerability in Ghostscript allows crafted files to escape its sandbox and execute arbitrary commands on servers processing PDFs, PostScript, or images. The flaw, exploited through ordinary file uploads in popular Linux applications, could enable remote code execution on affected systems. The issue has been patched, but the demonstration highlights the risk of using Ghostscript for file conversion.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-11-22T05:03:41+00:00
- **Category:** threat-intel

**Original Description:**
A now-patched flaw in Ghostscript allows a crafted file to escape the program's security sandbox and run commands on the server that processes it. Ghostscript is the interpreter that many Linux servers use to convert uploaded PDFs, PostScript files, and images into other formats, often without the application calling it directly. Security firm pwn.ai showed this week that ordinary upload,
