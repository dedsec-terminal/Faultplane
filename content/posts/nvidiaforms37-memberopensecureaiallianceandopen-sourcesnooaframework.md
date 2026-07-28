---
title: "NVIDIA Forms 37-Member Open Secure AI Alliance and Open-Sources NOOA Framework"
date: 2026-07-27T18:10:05+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the formation of the Open Secure AI Alliance and the open-sourcing of the NOOA framework:

NVIDIA has formed the Open Secure AI Alliance, a 37-member group consisting of cloud, security, enterprise software, and AI companies, including Microsoft, Cisco, and IBM. The alliance aims to develop and share open technologies, techniques, and tools for securing software and artificial intelligence (AI) agents. The group's scope covers the full agent stack, including identity, permissions, isolation, and secure coding workflows. The alliance's goal is to provide cyber defenders with AI models that can be read, changed, and run on their own hardware, rather than relying on closed systems accessed through a vendor's API.

The alliance's first technical contribution is the NVIDIA-labs OO Agents (NOOA) framework, an Apache 2.0 research framework designed to make agent behavior easier to test, trace, audit, and govern. NOOA represents the software layer around a model as a Python class, allowing developers to use familiar testing, tracing, and refactoring workflows. However, the framework comes with a warning, as it can be configured to execute large language model (LLM)-generated Python code, which may pose security risks. To mitigate these risks, NVIDIA recommends running NOOA behind operating system-level isolation, such as a container or virtual machine.

The formation of the Open Secure AI Alliance and the release of NOOA follow a recent incident at Hugging Face, where an autonomous agent system compromised parts of the company's production infrastructure. The incident highlights the need for locally controlled defensive models that can be run on a company's own infrastructure. While the alliance's goals and NOOA framework show promise, the group's governance, joint roadmap, and first multi-member deliverable remain undisclosed. The Linux Foundation has described itself as an inaugural partner, but the alliance's governance and joint participation remain unclear, with some notable companies, such as OpenAI and Google, absent from the

---

> *Ability is what you're capable of doing. Motivation determines what you do.Attitude determines how well you do it.
Author: Lou Holtz*

Source: [NVIDIA Forms 37-Member Open Secure AI Alliance and Open-Sources NOOA Framework](https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html)
