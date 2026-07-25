---
title: "ChatGPT AgentForger Flaw Could Deploy Rogue Workspace Agents via a Phishing Link"
date: 2026-07-24T11:53:55+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here is a summary of the article in three concise paragraphs:

Cybersecurity researchers at Zenity Labs have discovered a critical vulnerability in OpenAI's ChatGPT Workspace Agents, codenamed AgentForger. The flaw allows a single phishing link to create, authorize, and deploy a rogue AI agent within a victim's organization, giving the attacker control over the agent's actions. The vulnerability exploits a cross-site request forgery (CSRF) issue, allowing an attacker to forge an autonomous AI agent with a real employee's access and approvals switched off.

The attack occurs when an unsuspecting employee clicks on a benign-looking ChatGPT link, which spawns a new AI agent within the company's trust boundary. The Agent Builder tool, a visual canvas for building multi-step agent workflows, accepts initialization states through URL parameters, allowing an attacker to embed malicious prompts. If a logged-in user clicks on the link, ChatGPT opens the Builder in the victim's authenticated session and automatically submits the prompt, creating a rogue agent that can pull data from workspace applications and execute tasks without user approval.

The forged agent can conduct reconnaissance, harvest sensitive documents, and steal passwords, essentially becoming a persistent, autonomous insider. It can also impersonate the victim to send phishing links on Teams, redirecting recipients to a fake login page to siphon their credentials. The vulnerability has been addressed by OpenAI as of June 8, 2026, following responsible disclosure. The findings highlight the importance of securing AI infrastructure and agent frameworks, as exposed and misconfigured systems can be exploited by attackers to conduct malicious activities.

---

> *He who knows others is wise. He who knows himself is enlightened.
Author: Lao Tzu*

Source: [ChatGPT AgentForger Flaw Could Deploy Rogue Workspace Agents via a Phishing Link](https://thehackernews.com/2026/07/chatgpt-agentforger-flaw-could-deploy.html)
