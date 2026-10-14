---
title: "Docker Fixes Critical Two-Year-Old Hub Flaw That Let One User Push Images as Another"
description: "Docker discovered a flaw in Docker Hub that allowed a user to push, pull, or delete images as another user. The vulnerability existed for two years an..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/10/docker-fixes-critical-two-year-old-hub.html"
published: "2026-10-13T18:03:18+00:00"
ingested_at: "2026-10-14T03:21:10.362435+00:00"
date: "2026-10-14T03:21:10.362435+00:00"
category: "vulnerabilities"
tags:
  - "docker"
  - "hub"
  - "vulnerability"
  - "privilege-escalation"
  - "security-advisory"
slug: "2026-10-14-docker-fixes-critical-two-year-old-hub-flaw-that-let-one-use"
quote: "Every person, all the events of your life are there because you have drawn them there. What you choose to do with them is up to you."
quote_author: "Richard Bach"
---

### Executive Summary
Docker discovered a flaw in Docker Hub that allowed a user to push, pull, or delete images as another user. The vulnerability existed for two years and was fixed on September 30. Docker found no evidence of exploitation. The issue was in the account-to-organization conversion feature.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-10-13T18:03:18+00:00
- **Category:** vulnerabilities

**Original Description:**
A flaw in Docker Hub, the registry where container images are published and downloaded, let one user push, pull, or delete images as another user. Docker fixed the flaw on September 30 and says it found no evidence that anyone exploited it. The flaw was in the feature that&nbsp;converts a personal account&nbsp;into an organization, Docker said in a&nbsp;security advisory&nbsp;on October 12.
