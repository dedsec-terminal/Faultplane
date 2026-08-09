---
title: "Microsoft 365 AitM Phishing Hijacks Accounts to Collect Payroll and Finance Emails"
date: 2026-08-07T10:38:27+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the Microsoft 365 AitM phishing campaign:

Cybersecurity researchers have identified a widespread email-driven phishing campaign that uses adversary-in-the-middle (AitM) techniques to hijack Microsoft 365 accounts. The campaign targets key personnel involved in financial workflows, aiming to gather related emails and sensitive information. The attackers use residential proxies to disguise malicious sign-ins as ordinary consumer traffic, maintaining compromised sessions at approximately eight-hour intervals. This campaign is assessed to impact organizations across various sectors, including healthcare, education, and government, in the US, Canada, and Europe.

The phishing campaign employs voicemail-themed emails to lead victims to AitM decoy pages that capture their credentials and multi-factor authentication (MFA) codes. The attack chain involves a six-stage redirection process, using legitimate services like Google and Amazon S3 to sidestep reputation-driven filters. The phishing pages also use JavaScript to gather information about the visiting host, including browser, operating system, and geolocation data. This information is used to select geographically matched proxy infrastructure for subsequent logins, evading security controls and making it harder to detect the malicious activity.

Once initial access is obtained, the threat actors use the compromised sessions to collect emails from payroll and HR personnel involved in financial matters. They abuse the Microsoft Graph API to enumerate tenant users and access sensitive messages related to payroll, invoices, and banking. The attackers restrict their post-compromise actions to session maintenance, reconnaissance, and mailbox collection, avoiding common behaviors that could trigger early detection. By using rotating residential proxies and centralized automation, the threat actors can quietly maintain stolen sessions and collect relevant data, making the campaign harder to detect and connect to the original phishing event.

---

> *The heart has eyes which the brain knows nothing of.
Author: Charles Perkhurst*

Source: [Microsoft 365 AitM Phishing Hijacks Accounts to Collect Payroll and Finance Emails](https://thehackernews.com/2026/08/microsoft-365-aitm-phishing-hijacks.html)
