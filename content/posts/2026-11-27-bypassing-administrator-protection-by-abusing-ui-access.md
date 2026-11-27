---
title: Bypassing Administrator Protection by Abusing UI Access
description: In my last blog post I introduced the new Windows feature, Administrator
  Protection and how it aimed to create a secure boundary for UAC where one did...
source: Google Project Zero
source_url: https://projectzero.google/2026/02/windows-administrator-protection.html
published: '2026-02-12T08:00:00+00:00'
ingested_at: '2026-11-27T19:39:14.662005+00:00'
date: '2026-11-27T19:39:14.662005+00:00'
category: research
tags:
- research
slug: 2026-11-27-bypassing-administrator-protection-by-abusing-ui-access
quote: Learn wisdom from the ways of a seedling. A seedling which is never hardened
  off through stressful situations will never become a strong productive plant.
quote_author: Stephen Sigmund
---

### Executive Summary

In my last blog post I introduced the new Windows feature, Administrator Protection and how it aimed to create a secure boundary for UAC where one didn’t exist. I described one of the ways I was able to bypass the feature before it was released. In total I found 9 bypasses during my research that have now all been fixed. In this blog post I wanted to describe the root cause of 5 of those 9 issues, specifically the implementation of UI Access, how this has been a long standing problem with UAC that’s been under-appreciated, and how it’s being fixed now. A Question of Accessibility Prior to Windows Vista any process running on a user’s desktop could control any window created by another, such as by sending window messages . This behavior could be abused if a privileged user, such as...
