---
title: "Microsoft Copilot for Word Can Copy Hidden Prompts Into New Documents"
date: 2026-07-30T11:54:49+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A security researcher, Håkon Måløy, has disclosed a vulnerability in Microsoft 365 Copilot for Word that allows hidden instructions in a document to be copied into new documents. This can lead to unintended changes, such as rewriting figures in a report, without the user's knowledge. The vulnerability was reported to Microsoft 144 days prior to its disclosure, and despite the company's efforts to mitigate the issue, the vulnerability remains exploitable.

The attack requires a malicious document to be used as a source for a Copilot drafting or editing operation, and the instructions are hidden in the document using white-on-white text. When Copilot reads the source file, it can mistake the instructions for part of the user's request and copy them into the output. The vulnerability can be used to manipulate documents without the user's knowledge, and the changes can be difficult to trace. Måløy recommends treating external documents as untrusted and reviewing attached documents before starting a generation or edit.

Microsoft has confirmed the reported behavior and has deployed two mitigations, including blocking the original prompt wording and upgrading the underlying model to GPT-5.5. However, Måløy has found that the vulnerability can still be exploited using modified instructions. The company has also emphasized the importance of controlling memory access and isolation through deterministic systems rather than model instructions. As of now, there is no customer-side remediation that fully addresses the issue, and users are advised to exercise caution when working with external documents and Copilot-generated files.

---

> *Take rest; a field that has rested gives a bountiful crop.
Author: Ovid*

Source: [Microsoft Copilot for Word Can Copy Hidden Prompts Into New Documents](https://thehackernews.com/2026/07/microsoft-copilot-for-word-can-copy.html)
