---
title: "New Ted Backdoor Hides Inside Victims' Own HAProxy Builds to Intercept Web Traffic"
description: "A previously undocumented Linux toolkit was found compiled into trojanized HAProxy load balancers at two South Korean organizations. The implant, name..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/09/new-ted-backdoor-hides-inside-victims.html"
published: "2026-09-04T14:51:13+00:00"
ingested_at: "2026-09-05T02:43:56.043353+00:00"
date: "2026-09-05T02:43:56.043353+00:00"
category: "threat-intel"
tags:
  - "backdoor"
  - "HAProxy"
  - "Linux"
  - "web traffic interception"
  - "trojan"
slug: "2026-09-05-new-ted-backdoor-hides-inside-victims-own-haproxy-builds-to"
quote: "We should all be thankful for those people who rekindle the inner spirit."
quote_author: "Albert Schweitzer"
---

### Executive Summary
A previously undocumented Linux toolkit was found compiled into trojanized HAProxy load balancers at two South Korean organizations. The implant, named "ted", intercepts web traffic and serves altered pages to selected visitors. It requires host code execution and is not a HAProxy vulnerability.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-09-04T14:51:13+00:00
- **Category:** threat-intel

**Original Description:**
A previously undocumented Linux toolkit has been found compiled directly into the trojanized HAProxy load balancers of two South Korean organizations, where it intercepted web traffic and served altered pages to selected visitors. The attackers named the implant ted in debug strings left in the binary. It is not a HAProxy vulnerability, and installing it requires code execution on the host and
