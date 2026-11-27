---
title: 'GitHub’s model for secret detection: Finding more secrets with less noise'
description: OUR PIPELINE VS. THE PREVIOUS LLM PIPELINE Smarter secret scanning, at
  a fraction of the cost 11.5% higher acceptance Owner-weighted alert precision 8...
source: GitHub Security Blog
source_url: https://github.blog/ai-and-ml/githubs-model-for-secret-detection-finding-more-secrets-with-less-noise/
published: '2026-10-13T17:56:33+00:00'
ingested_at: '2026-11-27T19:39:14.674005+00:00'
date: '2026-11-27T19:39:14.674005+00:00'
category: research
tags:
- research
slug: 2026-11-27-github-s-model-for-secret-detection-finding-more-secrets-wit
quote: When you arise in the morning, think of what a precious privilege it is to
  be alive — to breathe, to think, to enjoy, to love.
quote_author: Marcus Aurelius
---

### Executive Summary

OUR PIPELINE VS. THE PREVIOUS LLM PIPELINE Smarter secret scanning, at a fraction of the cost 11.5% higher acceptance Owner-weighted alert precision 86% lower median scan execution time Post-push scanning 98% lower serving cost Compact model vs. remote LLM calls Secret scanning works best when developers are confident in the findings. Catch too little, and real credentials can remain in a repository. Alert too often, and developers may spend time investigating strings that aren’t secrets. Generic secrets make that balance especially difficult. The same string could be a real credential or a documentation placeholder, so detecting it requires understanding the surrounding code and text. To address this challenge, we trained a secret classifier specifically for GitHub’s product needs:...
