---
title: "Signal’s new security feature checks if your encrypted chats were tampered with"
date: 2026-08-12T13:47:45+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here is a summary of the article in 3 concise paragraphs:

Signal has introduced a new security feature called automatic key verification, which allows users to confirm that their encrypted chats have not been tampered with. This feature provides an additional layer of security to Signal's end-to-end encryption, giving users assurance that there is no unexpected party intercepting their conversations. The feature works through a system of verifications performed by the user, their Signal connections, and third-party auditors, providing the same assurance as manually verifying safety numbers.

The automatic key verification feature is based on a cryptographic system known as key transparency. When a user registers or makes changes to their account, the changes are incorporated into Signal's key-transparency system, which is audited by two outside organizations, Cloudflare and Trail of Bits. This system helps ensure that a phone number or username remains associated with a consistent encryption key across Signal's network, guarding against scenarios where an attacker manipulates Signal's key directory. If verification succeeds, Signal displays a green checkmark alongside the message "Encryption verified".

The new feature addresses the risk of an attacker gaining control of Signal's key directory or a privileged insider abusing their access to swap in a different key for a target's account. While Signal frames this as an unlikely scenario, the company has been tightening security around its app lately, including adding new protections for users after Russian state-sponsored hackers targeted high-profile accounts. Users can enable or disable automatic key verification under Signal's Privacy > Advanced settings, and can still manually verify Safety Numbers when automatic verification is unavailable.

---

> *The only real valuable thing is intuition.
Author: Albert Einstein*

Source: [Signal’s new security feature checks if your encrypted chats were tampered with](https://www.helpnetsecurity.com/2026/08/12/signal-automatic-key-verification-feature/)
