---
title: "Google Deletes 3 ADK AI Workflows After Malicious GitHub Issue Could Trigger Privileged Agent"
date: 2026-08-04T11:16:23+00:00
draft: false
categories:
  - data-breaches
author: "DedSec-Terminal"
---

Google has deleted three AI agent workflows from its Agent Development Kit (ADK) Python repository after a security vulnerability was discovered. The issue, reported by Pillar Security, allowed a public GitHub issue to manipulate a triage agent into triggering a privileged code-fixing agent. This could lead to arbitrary code execution on the continuous integration (CI) runner and exfiltration of the bot's personal access token (PAT), as well as exposure of a Google API key and Google Cloud service-account credential.

The vulnerability was found in the repository automation, specifically in the `issue-analyze.yml` and `issue-fix.yml` workflows. The `issue-analyze.yml` workflow ran automatically when an issue was opened, and the `issue-fix.yml` workflow listened for specific comments and restricted execution to owners, members, or collaborators. However, the gate checked who posted the command, not whether an outsider had manipulated the trusted account behind it. This allowed an attacker to inject malicious code and execute it on the CI runner.

Pillar Security recommends that similar repositories use separate bot identities, narrower token and tool scopes, and an authorization signal that untrusted text cannot generate. Google has removed the vulnerable workflows, and Pillar has verified that they are no longer present in the repository. The company has also confirmed that the issue has been fixed. The incident highlights the importance of securing repository automation and ensuring that workflows are designed with security in mind to prevent similar vulnerabilities in the future.

---

> *The longer we dwell on our misfortunes, the greater is their power to harm us.
Author: Voltaire*

Source: [Google Deletes 3 ADK AI Workflows After Malicious GitHub Issue Could Trigger Privileged Agent](https://thehackernews.com/2026/08/google-deletes-3-adk-ai-workflows-after.html)
