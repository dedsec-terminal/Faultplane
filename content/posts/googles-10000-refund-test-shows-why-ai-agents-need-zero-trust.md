---
title: "Google’s $10,000 refund test shows why AI agents need zero trust"
date: 2026-08-18T11:49:54+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Google’s $10,000 refund test shows why AI agents need zero trust
Google’s open-source autonomous Customer Support & Returns Agent, built using the Agent Development Kit (ADK) and Gemini, demonstrates how developers can apply zero-trust security principles to AI agents that interact with sensitive systems and take real-world actions.
The project tests an approach that assumes an AI agent could be manipulated or compromised and puts security controls around it to limit what the agent can do.
The architecture uses safeguards outside the model to verify actions, restrict AI-generated code, and block potentially dangerous requests.
Source: Google
The customer support agent shows why those controls matter. During normal operation, it reads a customer’s return request, generates a Python script to calculate prorated restocking deductions, records an approved refund in a database ledger, and provides a confirmation.
Google demonstrates an attack in which a customer with a $149 order instructs 

---

> *Sometimes by losing a battle you find a new way to win the war.
Author: Donald Trump*

Source: [Google’s $10,000 refund test shows why AI agents need zero trust](https://www.helpnetsecurity.com/2026/08/18/google-zero-trust-ai-agents/)
