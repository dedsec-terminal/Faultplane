---
title: "Obfuscating IP Addresses as Hostnames"
description: "The article discusses how hostnames can replace IP addresses, noting that many applications accept hostnames where IPs are expected. It references rec..."
source: "SANS Internet Storm Center"
source_url: "https://isc.sans.edu/diary/rss/33280"
published: "2026-08-25T15:03:33+00:00"
ingested_at: "2026-08-26T01:05:44.334147+00:00"
date: "2026-08-26T01:05:44.334147+00:00"
category: "threat-intel"
tags:
  - "SSRF"
  - "cloud metadata"
  - "IP obfuscation"
  - "hostnames"
  - "blocklist"
  - "SANS"
  - "Internet Storm Center"
slug: "2026-08-26-obfuscating-ip-addresses-as-hostnames"
quote: "I never think of the future. It comes soon enough."
quote_author: "Albert Einstein"
---

### Executive Summary
The article discusses how hostnames can replace IP addresses, noting that many applications accept hostnames where IPs are expected. It references recent scans targeting the cloud metadata service at 169.254.169.254 for SSRF vulnerabilities. To mitigate such attacks, the author suggests filtering requests containing the IP string or adding it to a blocklist of disallowed URLs.

---
**Intelligence Metadata**
- **Source Publisher:** SANS Internet Storm Center
- **Published Date:** 2026-08-25T15:03:33+00:00
- **Category:** threat-intel

**Original Description:**
It is pretty obvious that hostnames can replace IP addresses. Pretty much any software accepting an IP address will also accept a hostname as an argument. Last week, I wrote about scans for the cloud metadata service listening at 169.254.169.254. These scans attempted to exploit Server Side Request Forgery (SSRF) vulnerability. One way to prevent these types of exploits is to filter requests that contain the string "169.254.169.254" or to add this IP to a blocklist of URLs that should not be ...
