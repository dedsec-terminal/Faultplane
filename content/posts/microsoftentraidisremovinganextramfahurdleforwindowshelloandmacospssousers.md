---
title: "Microsoft Entra ID is removing an extra MFA hurdle for Windows Hello and macOS PSSO users"
date: 2026-08-10T13:19:07+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Microsoft Entra ID is making a significant change to its Multi-Factor Authentication (MFA) process for users who sign in with Windows Hello for Business (WHfB) or macOS Platform Single Sign-On (PSSO). The change, set to roll out worldwide and to GCC tenants starting in early October 2026, aims to simplify the MFA process for these users. By removing an extra MFA hurdle, Microsoft hopes to encourage the use of phishing-resistant authentication methods and reduce reliance on weaker ones.

The update will allow WHfB and macOS PSSO to satisfy MFA requirements without requiring users to register an additional passkey. This means that users who rely on these methods as their only registered MFA method will be considered MFA-capable, and Entra ID will stop prompting them to register another MFA method. However, there is a potential issue to note: since WHfB and macOS PSSO credentials are bound to a device, users may be unable to complete an MFA challenge from another device where the credential is unavailable.

To mitigate this issue, Microsoft recommends that users register a portable MFA method, such as a synced passkey or a passkey stored in Microsoft Authenticator. Fortunately, no configuration changes are required for the rollout, making it a relatively seamless process for admins. Nevertheless, organizations are advised to review their onboarding and MFA registration processes, as well as Authentication Strength policies, before the deployment to ensure a smooth transition.

---

> *The important thing is this: to be able at any moment to sacrifice what we are for what we could become.
Author: Charles Dubois*

Source: [Microsoft Entra ID is removing an extra MFA hurdle for Windows Hello and macOS PSSO users](https://www.helpnetsecurity.com/2026/08/10/entra-id-windows-hello-macos-psso-standalone-mfa/)
