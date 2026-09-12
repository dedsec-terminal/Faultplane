---
title: "GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure"
description: "GitLab patched a critical CVE-2026-85706 (CVSS 10.0) path\u2011traversal flaw in its repository commits API that lets unauthenticated users read arbitrary ..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html"
published: "2026-09-11T16:30:18+00:00"
ingested_at: "2026-09-12T02:55:26.860374+00:00"
date: "2026-09-12T02:55:26.860374+00:00"
category: "cves"
tags:
  - "GitLab"
  - "CVE-2026-85706"
  - "CVSS 10"
  - "path traversal"
  - "unauthenticated"
  - "file read"
  - "in-the-wild probes"
slug: "2026-09-12-gitlab-cvss-10-file-read-flaw-draws-in-the-wild-probes-after"
quote: "To accomplish great things, we must not only act, but also dream; not only plan, but also believe."
quote_author: "Anatole France"
---

### Executive Summary
GitLab patched a critical CVE-2026-85706 (CVSS 10.0) path‑traversal flaw in its repository commits API that lets unauthenticated users read arbitrary server files. The vulnerability triggered in‑the‑wild probing within hours of public disclosure.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-09-11T16:30:18+00:00
- **Category:** cves

**Original Description:**
GitLab has released patches to address multiple flaws, including a maximum-severity security vulnerability that has witnessed in-the-wild probes within hours of public disclosure. The vulnerability in question is CVE-2026-85706 (CVSS score: 10.0), a path traversal issue in the repository commits API that could allow an unauthenticated user to read arbitrary files from the GitLab server under
