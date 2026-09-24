---
title: "Attackers Use Malicious Terraform Providers to Deliver Go Malware via HashiCorp Registry"
description: "Cybersecurity researchers uncovered Go-based malware distributed through two Go modules and two Terraform providers hosted on the HashiCorp Registry, ..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/09/attackers-use-malicious-terraform.html"
published: "2026-09-23T18:06:30+00:00"
ingested_at: "2026-09-24T02:56:34.821689+00:00"
date: "2026-09-24T02:56:34.821689+00:00"
category: "threat-intel"
tags:
  - "malware"
  - "terraform"
  - "hashicorp"
  - "go"
  - "distribution vector"
slug: "2026-09-24-attackers-use-malicious-terraform-providers-to-deliver-go-ma"
quote: "You, yourself, as much as anybody in the entire universe, deserve your love and affection."
quote_author: "Buddha"
---

### Executive Summary
Cybersecurity researchers uncovered Go-based malware distributed through two Go modules and two Terraform providers hosted on the HashiCorp Registry, marking the first use of this centralized repository as a malicious distribution vector. The identified providers include gocommunity-io/dockerd and kreuzwenker/, illustrating a novel threat channel for attackers.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-09-23T18:06:30+00:00
- **Category:** threat-intel

**Original Description:**
Cybersecurity researchers have disclosed Go-based malware distributed via two Go Modules and two Terraform providers, marking the first time threat actors are using the centralized repository hosted by HashiCorp as a distribution vector for malicious payloads. According to Aikido, the list of Terraform providers and Go modules is below - gocommunity-io/dockerd (222 downloads) kreuzwenker/
