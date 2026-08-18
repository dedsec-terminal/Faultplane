---
title: "Snowflake GitHub Actions Flaw Lets Crafted Issues Trigger Command Injection"
date: 2026-08-17T18:44:17+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Cybersecurity researchers at Wiz have disclosed a new GitHub Actions workflow injection vulnerability in Snowflake's public snowflakedb/snowflake-connector-net repository that it said could be exploited through a crafted GitHub issue to execute commands in a workflow containing internal Jira credentials.
The issue was present in .github/workflows/jira_issue.yml, which ran when a public issue was opened and exposed JIRA_BASE_URL, JIRA_USER_EMAIL, and JIRA_API_TOKEN to the same workflow step. The weakness was confined to the repository's CI/CD automation, with no affected Snowflake Connector for .NET release identified.
The workflow inserted attacker-controlled issue title and body values directly into a shell run: block. It also checked github.event.pull_request.user.login even though the event was an issue, meaning the referenced pull request property did not exist.
GitHub says, "If you attempt to dereference a nonexistent property, it will evaluate to an empty string." In this case, t

---

> *When I dare to be powerful, to use my strength in the service of my vision, then it becomes less and less important whether I am afraid.
Author: Audre Lorde*

Source: [Snowflake GitHub Actions Flaw Lets Crafted Issues Trigger Command Injection](https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets_0330881554.html)
