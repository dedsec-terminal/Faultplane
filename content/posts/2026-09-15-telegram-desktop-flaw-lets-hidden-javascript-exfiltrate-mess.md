---
title: "Telegram Desktop Flaw Lets Hidden JavaScript Exfiltrate Messages From HTML Exports"
description: "Security researchers discovered that a flaw in Telegram Desktop allows a malicious bot to embed hidden JavaScript in chat messages. When users export ..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/09/telegram-desktop-flaw-lets-hidden.html"
published: "2026-09-14T17:58:16+00:00"
ingested_at: "2026-09-15T03:10:49.710171+00:00"
date: "2026-09-15T03:10:49.710171+00:00"
category: "threat-intel"
tags:
  - "Telegram"
  - "Desktop"
  - "JavaScript"
  - "HTML export"
  - "exfiltration"
slug: "2026-09-15-telegram-desktop-flaw-lets-hidden-javascript-exfiltrate-mess"
quote: "A life spent making mistakes is not only more honourable but more useful than a life spent in doing nothing."
quote_author: "Bernard Shaw"
---

### Executive Summary
Security researchers discovered that a flaw in Telegram Desktop allows a malicious bot to embed hidden JavaScript in chat messages. When users export chats to HTML and open the file in a browser, the script runs and copies all messages from the file, exfiltrating them to the attacker. The vulnerability was reported on September 12 by ExPatch.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-09-14T17:58:16+00:00
- **Category:** threat-intel

**Original Description:**
A flaw in Telegram Desktop let a bot's message plant hidden JavaScript inside chats that users exported to HTML files, security researchers at ExPatch said in a&nbsp;writeup&nbsp;published on September 12. In Telegram, the message looked ordinary, with a link button, and the script ran only when someone opened the export file in a web browser. It could then copy every message in that file to
