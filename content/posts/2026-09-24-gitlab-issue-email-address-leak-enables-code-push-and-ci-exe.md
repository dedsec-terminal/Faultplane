---
title: "GitLab Issue Email Address Leak Enables Code Push and CI Execution"
description: "GitLab provides a private email address for each user to file issues via email. This address is effectively a credential. If exposed, an attacker can ..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/09/a-leaked-gitlab-issue-email-address.html"
published: "2026-09-23T16:53:10+00:00"
ingested_at: "2026-09-24T02:56:36.910763+00:00"
date: "2026-09-24T02:56:36.910763+00:00"
category: "threat-intel"
tags:
  - "GitLab"
  - "email credential"
  - "CI/CD"
  - "code injection"
  - "issue tracking"
slug: "2026-09-24-gitlab-issue-email-address-leak-enables-code-push-and-ci-exe"
quote: "He that never changes his opinions, never corrects his mistakes, and will never be wiser on the morrow than he is today."
quote_author: "Tryon Edwards"
---

### Executive Summary
GitLab provides a private email address for each user to file issues via email. This address is effectively a credential. If exposed, an attacker can send a patch to that address, which GitLab will commit in the sender's name to any branch the user can push to, including main. The attacker can also trigger CI/CD jobs that run with the user's permissions. The address is displayed behind the 'Email work item to this project' button.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-09-23T16:53:10+00:00
- **Category:** threat-intel

**Original Description:**
The private email address GitLab gives you for filing issues by email is a credential. Anyone who gets it can email a patch that GitLab commits in your name, to any branch you can push to, including main, and can start CI/CD jobs that run as you. GitLab shows each user this address behind a button labeled "Email work item to this project." Mail sent to it opens an issue in that project, authored
