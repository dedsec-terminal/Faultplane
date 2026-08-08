---
title: "ShieldFont fights AI scraping by handing crawlers the wrong words"
date: 2026-08-07T04:30:47+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

**Introduction to ShieldFont**
ShieldFont is a web font designed to combat AI scraping by displaying different words to humans and crawlers. Developed by Isaque Seneda and Gabriel Abrucio, it works by swapping words in the page's code before it loads, replacing them with similar words that are then drawn on the screen as the original words. This way, a person reading the content sees the intended text, while a scraper or AI model sees the swapped words.

**How ShieldFont Works**
The font uses typographic substitution rules to replace words with similar ones, making it difficult for scrapers to extract the original content. The swap happens on the writer's machine or server, and the font draws the swapped word to look like the original. This approach protects the content from scrapers, copy-paste, and language models that digest raw HTML. However, it may introduce some friction, such as requiring readers to solve a puzzle to unlock the real words, and may not be compatible with all screen readers or platforms.

**Goals and Implications**
The creators of ShieldFont aim to provide a tool for writers and artists to protect their work from unauthorized scraping, while also sparking a debate about the ethics of AI training. By making scraping more costly and riskier, ShieldFont hopes to give writers bargaining power against big tech and restore the incentive to share work online. The font is available for free on GitHub, and its developers plan to continue improving it, including adding features like dictionary rotation and per-deploy rotation to increase the cost for scrapers.

---

> *It is surprising what a man can do when he has to, and how little most men will do when they don't have to.
Author: Walter Linn*

Source: [ShieldFont fights AI scraping by handing crawlers the wrong words](https://www.helpnetsecurity.com/2026/08/07/shieldfont-ai-scraping-protection/)
