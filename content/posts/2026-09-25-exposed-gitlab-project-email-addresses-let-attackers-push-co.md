---
title: "Exposed GitLab project email addresses let attackers push code"
description: "GitLab projects are leaking email addresses in public documentation, enabling attackers to send malicious code via the project's email integration. Th..."
source: "Bleeping Computer"
source_url: "https://www.bleepingcomputer.com/news/security/exposed-gitlab-project-email-addresses-let-attackers-push-code/"
published: "2026-09-24T17:47:44+00:00"
ingested_at: "2026-09-25T03:13:31.704011+00:00"
date: "2026-09-25T03:13:31.704011+00:00"
category: "threat-intel"
tags:
  - "GitLab"
  - "email exposure"
  - "code injection"
  - "bug bounty"
  - "misconfiguration"
slug: "2026-09-25-exposed-gitlab-project-email-addresses-let-attackers-push-co"
quote: "Limitations live only in our minds. But if we use our imaginations, our possibilities become limitless."
quote_author: "Jamie Paolinetti"
---

### Executive Summary
GitLab projects are leaking email addresses in public documentation, enabling attackers to send malicious code via the project's email integration. The exposed addresses allow unauthorized push of code, potentially compromising the repository. The issue arises from developers publishing support and bug‑reporting emails in READMEs and guides. Attackers can exploit this to inject malicious commits, bypassing code review. The vulnerability highlights the need to keep integration emails private and enforce proper access controls.

---
**Intelligence Metadata**
- **Source Publisher:** Bleeping Computer
- **Published Date:** 2026-09-24T17:47:44+00:00
- **Category:** threat-intel

**Original Description:**
Private GitLab email addresses that allow developers to push issues or tasks to a project are being deliberately exposed in READMEs, contributing guides, and support pages used to collect bug reports. [...]
