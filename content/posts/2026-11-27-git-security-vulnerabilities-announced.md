---
title: Git security vulnerabilities announced
description: 'Editor’s note (November 17, 2026): This post has been updated with additional
  CVE information and updated guidance for GitHub Enterprise Server users...'
source: GitHub Security Blog
source_url: https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/
published: '2026-11-10T18:00:00+00:00'
ingested_at: '2026-11-27T19:39:14.672005+00:00'
date: '2026-11-27T19:39:14.672005+00:00'
category: research
tags:
- research
slug: 2026-11-27-git-security-vulnerabilities-announced
quote: What lies behind us and what lies before us are tiny matters compared to what
  lies within us.
quote_author: Walt Emerson
---

### Executive Summary

Editor’s note (November 17, 2026): This post has been updated with additional CVE information and updated guidance for GitHub Enterprise Server users . Please see the release information below for the versions that include the fixes. Today, the Git project is releasing new versions to address six security vulnerabilities. These include arbitrary code execution when cloning a malicious repository, writes to unintended files, and memory corruption when processing merges or binary patches. The fixes are included in Git 2.56.1 , with backports to Git 2.55.1, 2.54.1, 2.53.1, 2.52.1, 2.51.3, and 2.50.2. We recommend updating to Git 2.56.1 or the patched release for your maintenance series, and updating any applications that bundle Git. Vulnerabilities in Git CVE-2026-111760: Code execution...
