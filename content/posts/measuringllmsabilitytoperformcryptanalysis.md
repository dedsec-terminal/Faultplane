---
title: "Measuring LLMs’ Ability to Perform Cryptanalysis"
date: 2026-07-29T01:47:05+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Researchers have introduced a new benchmark called CryptanalysisBench to measure the ability of large language models (LLMs) to perform mathematical cryptanalysis. The benchmark consists of 191 tasks across six families of cryptographic primitives, including block ciphers and hash functions. The goal is to evaluate the ability of LLMs to discover new mathematical cryptanalytic attacks against these primitives.

The results show that five frontier models, including Claude Opus 4.8 and GPT-5.5, are able to break 65-86% of the schemes in the first tier of the benchmark, which includes primitives with known practical breaks. The models also produce novel cryptanalysis, such as a key-recovery attack that exploits a design flaw in the SpoC AEAD. Additionally, Anthropic used the benchmark to test its Mythos Preview model and found new vulnerabilities in Hawk and reduced-round AES.

The release of CryptanalysisBench is intended to help track the development of AI cryptanalysis and provide a tool for stress-testing candidate schemes before deployment. The benchmark is seen as an important step in evaluating the ability of LLMs to perform cryptanalysis, which has significant implications for digital security. As the field continues to evolve, it is likely that AI cryptanalysis will become a increasingly important factor in the development of secure cryptographic schemes.

---

> *Love doesn't make the world go round, love is what makes the ride worthwhile.
Author: Elizabeth Browning*

Source: [Measuring LLMs’ Ability to Perform Cryptanalysis](https://www.schneier.com/blog/archives/2026/07/measuring-llms-ability-to-perform-cryptanalysis.html)
