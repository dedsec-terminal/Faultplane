---
title: "Pre-auth RCE in enterprise Java hits Bonita and OFBiz servers"
date: 2026-08-05T18:45:14+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

Vulnerability researchers at Novee have discovered pre-auth remote code execution (RCE) vulnerabilities in enterprise Java platforms, specifically in Bonita and OFBiz servers. The vulnerabilities allow an attacker to send a single web request to gain access to an internal API, which can then be used to run code on the host. This is particularly concerning as Bonita BPM handles sensitive processes such as loan approvals, insurance claims, and employee onboarding for banks, insurers, and government agencies.

The researchers found that the vulnerabilities are caused by a combination of weak spots in the internal routing and authentication mechanisms of the platforms. For example, in Bonita, a single web address can bypass three separate checks and gain access to the internal API, which uses the XStream library to turn XML into live Java objects. In OFBiz, a default signing key is used to authorize single sign-on tokens, which can be exploited to gain admin rights and execute code. The researchers have rated the vulnerabilities as critical and have assigned them a CVE number.

The researchers have reported the vulnerabilities to the affected projects and have worked with them to release new versions that address the issues. Novee has also provided guidance on how to defend against similar vulnerabilities in other enterprise Java platforms. The company recommends hardening internal routing, removing unsafe execution primitives, and being cautious of denylists and preference flags that can gate dangerous code. The researchers have also highlighted the importance of auditing and testing internal APIs and authentication mechanisms to prevent similar vulnerabilities from being exploited.

---

> *Our greatest glory is not in never failing but rising everytime we fall.*

Source: [Pre-auth RCE in enterprise Java hits Bonita and OFBiz servers](https://www.helpnetsecurity.com/2026/08/05/pre-auth-rce-java-bonita-ofbiz-cve-2026-31986/)
