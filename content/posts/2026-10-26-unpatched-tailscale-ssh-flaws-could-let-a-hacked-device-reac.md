---
title: "Unpatched Tailscale SSH Flaws Could Let a Hacked Device Reach Root on Other Servers"
description: "A security researcher discovered that if Tailscale SSH is configured to allow port forwarding, a compromised device on the network can be used to gain..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/10/unpatched-tailscale-ssh-flaws-could-let.html"
published: "2026-10-25T17:44:09+00:00"
ingested_at: "2026-10-26T02:59:05.416287+00:00"
date: "2026-10-26T02:59:05.416287+00:00"
category: "threat-intel"
tags:
  - "Tailscale"
  - "SSH"
  - "root access"
  - "port forwarding"
  - "network security"
slug: "2026-10-26-unpatched-tailscale-ssh-flaws-could-let-a-hacked-device-reac"
quote: "I'm a great believer in luck and I find the harder I work, the more I have of it."
quote_author: "Thomas Jefferson"
---

### Executive Summary
A security researcher discovered that if Tailscale SSH is configured to allow port forwarding, a compromised device on the network can be used to gain root access to other servers it can reach. The attack requires an attacker who already controls a device permitted by the network’s access rules. The flaw highlights the need to patch Tailscale and restrict SSH port forwarding.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-10-25T17:44:09+00:00
- **Category:** threat-intel

**Original Description:**
A single hacked device on a Tailscale network can be used to gain root access to other servers it can reach, according to a security researcher who published the findings this week. The attack requires two things: Tailscale SSH set up to allow port forwarding, and an attacker who already controls one device that the network's access rules permit to connect to the target. The findings were
