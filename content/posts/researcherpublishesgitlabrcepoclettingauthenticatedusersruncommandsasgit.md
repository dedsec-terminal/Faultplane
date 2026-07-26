---
title: "Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git"
date: 2026-07-25T10:14:26+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A security researcher from depthfirst has published a proof-of-concept (PoC) exploit for a GitLab vulnerability that allows authenticated users to run commands as the "git" user on self-managed GitLab servers. The exploit takes advantage of two memory corruption bugs in the Oj JSON parser, which is used by GitLab's notebook renderer. By committing a crafted Jupyter notebook and opening its commit diff, an attacker can leak a heap pointer and eventually execute arbitrary code.

The vulnerability affects all tiers of GitLab, including Community Edition (CE) and Enterprise Edition (EE), and can be exploited by any authenticated user who can push to a project. The exploit does not require administrator rights, CI/CD access, or victim interaction. GitLab patched the vulnerability on June 10, but did not classify it as a security fix, and therefore did not assign a CVE or CVSS score. As a result, operators who only reviewed the security table may not have treated the update as urgent.

To mitigate the vulnerability, users are advised to upgrade to GitLab version 18.10.8, 18.11.5, or 19.0.2. There is no workaround for users who cannot upgrade. The public exploit is specific to GitLab 18.11.3 on x86-64, but the Oj bugs are general and can be ported to other versions with some effort. Depthfirst has reported that they are not aware of any in-the-wild exploitation, and GitLab has reproduced the vulnerability independently. The researcher has also identified nine additional CVE advisories in the Oj library, but none of them are related to this specific exploit chain.

---

> *The only real failure in life is not to be true to the best one knows.
Author: Buddha*

Source: [Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git](https://thehackernews.com/2026/07/researcher-publishes-gitlab-rce-poc.html)
