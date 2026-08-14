---
title: "153GB of stolen credentials surface after LiteLLM supply chain attack"
date: 2026-08-13T10:32:51+00:00
draft: false
categories:
  - data-breaches
author: "DedSec-Terminal"
---

A massive 153GB archive of stolen credentials has surfaced following a supply chain attack on LiteLLM, an open-source proxy gateway used by developers to route requests to different AI models. The archive, which contains 433,909 files, exposes sensitive data linked to thousands of corporate domains, including AWS, Samsung, Cisco, and Salesforce. According to Hudson Rock, a cybersecurity firm that obtained and analyzed the archive, the stolen data includes credentials and other sensitive information that could be used to compromise the security of affected organizations.

The breach is attributed to a cybercriminal group called TeamPCP, which used stolen credentials to publish a compromised version of Trivy, a popular open-source vulnerability scanner. The compromised Trivy scanner was then used to steal PyPI publishing tokens, which were used to publish two malicious LiteLLM releases. The stolen data includes information linked to organizations such as NVIDIA, Volkswagen, Microsoft, and Epic Games, and includes sensitive information such as AWS secret access keys, Salesforce client secrets, and Azure environment variables. The breach highlights the evolving nature of supply chain attacks, which can affect thousands of companies simultaneously.

Hudson Rock is urging organizations to take immediate action to audit their environments and rotate any secrets that may have been exposed. The firm is working to disclose the breach to affected organizations and is providing guidance on how to respond to the incident. However, some organizations appear to be treating the exposure with less urgency than warranted, and security researchers are warning that the breach has the potential to be highly damaging if not addressed promptly. The incident highlights the need for organizations to prioritize DevOps security and to be proactive in responding to supply chain breaches.

---

> *To fly, we have to have resistance.
Author: Maya Lin*

Source: [153GB of stolen credentials surface after LiteLLM supply chain attack](https://www.helpnetsecurity.com/2026/08/13/litellm-breach-stolen-credentials-leak/)
