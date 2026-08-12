---
title: "Solidity Pro VS Code Extensions Steal Crypto Wallets, API Keys, and Credentials"
date: 2026-08-10T07:38:23+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Cybersecurity researchers have discovered a malicious Microsoft Visual Studio Code (VS Code) extension named Solidity Pro that steals sensitive information, including crypto wallets, API keys, and credentials. The extension, which was available under the names "helper-beeps.solidity-pro" and "web3devtoolsx.solidity-pro", has been removed from the Open VSX registry, but its GitHub repository remains accessible. The extension's early versions beamed data to Cloudflare Workers endpoints, while later versions became full-blown information stealers, exfiltrating data via a Telegram bot upload.

The stolen data includes a wide range of sensitive information, such as GitHub and GitLab tokens, AWS keys, Cloudflare tokens, OpenAI keys, Telegram bot tokens, and crypto wallet vaults. The malware is heavily obfuscated, making it difficult to detect, and uses techniques such as delayed activation and randomized code execution to evade detection. The extension's behavior is similar to that of the WhiteCobra threat cluster, which was detected in September 2025. The researchers warn that users who have installed the extension should remove it immediately and take steps to inspect their dependency graphs and block known command-and-control domains.

The discovery of the Solidity Pro extension is not an isolated incident, as Yeeth Security has previously flagged other malicious VS Code extensions, including one that impersonated a Solidity language-support tool and harbored a delayed-activation clipboard stealer. The researchers also found other rogue VS Code extensions and npm packages that deliver malicious code, including a package that embeds malicious code in a dependency and a set of extensions that deliver Windows-based droppers. Users are advised to be cautious when installing extensions and to monitor their systems for suspicious activity, such as the use of cscript, mshta, cmd, curl, and powershell commands.

---

> *I care not so much what I am to others as what I am to myself. I will be rich by myself, and not by borrowing.
Author: Michel de Montaigne*

Source: [Solidity Pro VS Code Extensions Steal Crypto Wallets, API Keys, and Credentials](https://thehackernews.com/2026/08/solidity-pro-vs-code-extensions-steal.html)
