---
title: Introducing HTTP Anomaly Rank
description: If you've ever used Burp Intruder or Turbo Intruder, you'll be familiar
  with the ritual of manually digging through thousands of responses by repeated...
source: PortSwigger Research
source_url: https://portswigger.net/research/introducing-http-anomaly-rank
published: '2025-11-11T14:41:53+00:00'
ingested_at: '2026-11-27T19:39:14.666005+00:00'
date: '2026-11-27T19:39:14.666005+00:00'
category: research
tags:
- research
slug: 2026-11-27-introducing-http-anomaly-rank
quote: We could never learn to be brave and patient if there were only joy in the
  world.
quote_author: Helen Keller
---

### Executive Summary

If you've ever used Burp Intruder or Turbo Intruder, you'll be familiar with the ritual of manually digging through thousands of responses by repeatedly sorting the table via length, status code, etc. I've developed an algorithm called HTTP Anomaly Rank which can efficiently pick out the most interesting responses for you. HTTP Anomaly Rank is now integrated into Turbo Intruder and automatically places the most anomalous findings at the top of the results table without you needing to lift a finger. We've also integrated this algorithm into Burp Suite's API in release 2025.10, so you can...
