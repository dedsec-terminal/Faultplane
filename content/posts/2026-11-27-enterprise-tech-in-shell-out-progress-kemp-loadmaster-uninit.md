---
title: Enterprise Tech In, Shell Out (Progress Kemp LoadMaster Uninitialized Heap
  to Pre-Auth RCE CVE-2026-8037)
description: Progress released an advisory on June 4 2026 for a pre‑authentication
  remote code execution flaw (CVE‑2026‑8037) in its Kemp LoadMaster load balancer....
source: watchTowr Labs
source_url: https://labs.watchtowr.com/enterprise-tech-in-shell-out-progress-kemp-loadmaster-uninitialized-heap-to-pre-auth-rce-cve-2026-8037/
published: '2026-06-29T19:24:54+00:00'
ingested_at: '2026-11-27T19:47:03.195902+00:00'
date: '2026-11-27T19:47:03.195902+00:00'
category: research
tags:
- CVE-2026-8037
- remote code execution
- load balancer
slug: 2026-11-27-enterprise-tech-in-shell-out-progress-kemp-loadmaster-uninit
quote: Difficulties are things that show a person what they are.
quote_author: Epictetus
---

### Executive Summary

Progress released an advisory on June 4 2026 for a pre‑authentication remote code execution flaw (CVE‑2026‑8037) in its Kemp LoadMaster load balancer. The vulnerability, affecting GA v7.2.63.1 and older and LTSF v7.2.54.17 and older, allows any user who can reach the device’s API to inject shell commands via an improperly escaped single‑quote handling routine. WatchTowr Labs’ research confirms the flaw’s root cause and demonstrates how the escape_quotes function fails to sanitize input, enabling command injection. Defensive guidance includes applying the vendor’s patch, disabling the API if not needed, and leveraging WatchTowr’s Preemptive Exposure Management to detect and mitigate exposure early.

### Original Overview

Welcome back to another watchTowr Labs blog post. This time, we're looking at Progress Kemp LoadMaster, a load balancer that sits at the edge of a lot of enterprise networks. Edge appliances have a habit of becoming the way in rather than the thing keeping people out, and CVE-2026-8037 keeps that streak alive: a pre-authentication Remote Code Execution vulnerability accessible to anyone who can access the API. So, in probably a predictable turn of events, we're back doing what we do best. As always, watchTowr clients gain industry-first access to our research days before publication to validate their exposure, accompanied by Active Defense capabilities to autonomously mitigate exposure. This research is a glimpse into the capabilities that power our Preemptive Exposure Management...
