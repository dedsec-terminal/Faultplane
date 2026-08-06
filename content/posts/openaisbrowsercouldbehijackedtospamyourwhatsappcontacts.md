---
title: "OpenAI’s Browser Could Be Hijacked to Spam Your WhatsApp Contacts"
date: 2026-08-05T23:30:00+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Researchers at Zenity have discovered a security flaw in OpenAI's Atlas web browser that could allow hackers to bypass security protections and trick the browser into spamming dozens of WhatsApp contacts or making unauthorized purchases on Amazon. The researchers found around 20 flaws in leading AI-enabled web browsers and browser extensions, including products from Google, Anthropic, Microsoft, and Perplexity, which could allow hackers to access local machines, grab files, take over a password manager, and leak someone's entire browsing history.

The researchers demonstrated two proof-of-concept attacks, one of which involved getting Atlas to sign up to a malicious newsletter link that instructed the AI to navigate to the user's signed-in WhatsApp web account and send every contact the same message. The attack worked by getting around multiple security mechanisms put in place by OpenAI, including designing a newsletter sign-up page that looked legitimate and writing in Hebrew to dodge English-language security tools. The researchers also demonstrated an attack on Amazon, where they got Atlas to add a shipping address to a logged-in Amazon account and add a tablet to the shopping cart.

The researchers reported the findings to OpenAI in January, and the company has since deployed an update to address the issue and strengthen protections in Atlas, which will be deprecated on August 9. The researchers emphasize the need for "deterministic" or hard security barriers in AI systems, rather than relying on the judgments or classifications of AI systems, which can be fooled. They warn that the use of AI agents in web browsing can put users at risk of having their accounts compromised and their data leaked, and that tech companies should be mindful of the level of access and agency they give to these agents.

---

> *When your desires are strong enough you will appear to possess superhuman powers to achieve.
Author: Napoleon Hill*

Source: [OpenAI’s Browser Could Be Hijacked to Spam Your WhatsApp Contacts](https://www.wired.com/story/openais-browser-could-be-hijacked-to-spam-your-whatsapp-contacts/)
