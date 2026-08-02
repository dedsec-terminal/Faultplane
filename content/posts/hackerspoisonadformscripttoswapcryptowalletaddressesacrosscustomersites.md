---
title: "Hackers Poison Adform Script to Swap Crypto Wallet Addresses Across Customer Sites"
date: 2026-08-01T09:03:07+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Here is a summary of the incident in 3 concise paragraphs:

Adform, an advertising technology company, detected a malicious modification to one of its JavaScript files on July 27, 2026. The altered file, served from s2.adform.net, was designed to rewrite cryptocurrency wallet addresses on websites that used the script. As a result, visitors who copied a Bitcoin, Ethereum, or Tron address from an affected site may have pasted a different address inserted by the malicious code.

The compromised script, known as trackpoint-async.js, was able to rewrite addresses entered directly into form fields, not just those copied from the clipboard. The malicious code operated only while an affected page remained open and did not install any software or establish persistence. Adform has advised users to clear their browser cache to remove the altered file and to verify any wallet addresses before sending funds. The company has also notified affected clients and reported the incident to authorities.

The full scope of the incident is still unclear, including the number of websites that carried the malicious script, the number of visitors exposed, and whether any funds were diverted. Independent security researcher Kevin Beaumont reported seeing malicious activity via Adform over the past week, which suggests that the incident may have occurred over a longer period than Adform's reported affected date of July 27. Adform has not publicly identified the attacker or provided indicators of compromise, and the company's investigation is ongoing.

---

> *Difficulties increase the nearer we get to the goal.
Author: Johann Wolfgang von Goethe*

Source: [Hackers Poison Adform Script to Swap Crypto Wallet Addresses Across Customer Sites](https://thehackernews.com/2026/08/hackers-poison-adform-script-to-swap.html)
