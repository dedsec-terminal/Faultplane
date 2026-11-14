---
title: "New Mior and Skyfall Attacks Let Rogue Cloud Hosts Steal Secrets From AMD SEV-SNP VMs"
description: "Researchers revealed two attacks\u2014Mior and Skyfall\u2014that enable a malicious hypervisor to read and, in Mior\u2019s case, modify memory inside AMD SEV\u2011SNP vir..."
source: "The Hacker News"
source_url: "https://thehackernews.com/2026/11/new-mior-and-skyfall-attacks-let-rogue.html"
published: "2026-11-13T15:27:05+00:00"
ingested_at: "2026-11-14T04:45:08.591244+00:00"
date: "2026-11-14T04:45:08.591244+00:00"
category: "threat-intel"
tags:
  - "AMD SEV-SNP"
  - "Mior"
  - "Skyfall"
  - "hypervisor"
  - "cloud-host"
slug: "2026-11-14-new-mior-and-skyfall-attacks-let-rogue-cloud-hosts-steal-sec"
quote: "This is the final test of a gentleman: his respect for those who can be of no possible value to him."
quote_author: "William Lyon Phelps"
---

### Executive Summary
Researchers revealed two attacks—Mior and Skyfall—that enable a malicious hypervisor to read and, in Mior’s case, modify memory inside AMD SEV‑SNP virtual machines. The exploits require control of the hypervisor, and Mior also needs BIOS access, allowing rogue cloud hosts to bypass the VM’s isolation and steal sensitive data.

---
**Intelligence Metadata**
- **Source Publisher:** The Hacker News
- **Published Date:** 2026-11-13T15:27:05+00:00
- **Category:** threat-intel

**Original Description:**
Two attacks made public this week allow a malicious host to read data inside AMD SEV-SNP-protected virtual machines (VMs), which are built to keep the server's operator out. One of them, Mior, can also modify a VM's memory and fake the signed report confirming which software it runs. Both need control of the server's hypervisor, and Mior also needs control of the server's BIOS. Researchers
