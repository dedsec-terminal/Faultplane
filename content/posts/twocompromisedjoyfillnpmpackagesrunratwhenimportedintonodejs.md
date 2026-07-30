---
title: "Two Compromised joyfill npm Packages Run RAT When Imported Into Node.js"
date: 2026-07-29T04:20:57+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the compromised npm packages:

Two npm packages, `@joyfill/layouts` and `@joyfill/components`, have been compromised to deliver a remote access trojan (RAT) associated with the DEV#POPPER malware family. The affected packages, `@joyfill/layouts@0.1.2-2773.beta.0` and `@joyfill/components@4.0.0-rc24-2773-beta.4`, contain an import-time JavaScript implant that resolves encrypted code through Tron, Aptos, and BNB Smart Chain transactions. This implant runs when Node.js loads the CommonJS package entry point, unlike other malicious packages that are triggered via an npm lifecycle hook.

The implant consists of two parallel sequences of actions, leading to a recovered 77 KB JavaScript payload with similarities to the DEV#POPPER malware family. The payload is a JavaScript loader that employs a blockchain resolution method to retrieve a second-stage malware named "clientCode." The final "clientCode" payload is a heavily obfuscated Node.js RAT that can upload files, retrieve additional JavaScript, collect host details, send status check-in messages, and read clipboard data. The malware avoids execution on development, CI, or sandboxed machines with specific hostnames.

The compromised packages are linked to a threat cluster tracked as PolinRider, which is assessed to be related to Contagious Interview. The use of a multi-blockchain resolver structure has been linked to North Korean threat actors, and the malicious packages are connected to the same ongoing operation as the ViteVenom malware. Developers who have installed the affected versions are advised to remove them and take steps to secure their environments. The affected packages can lead to arbitrary code execution, and the final recovered code can collect host information, establish a remote-control channel, execute supplied JavaScript or shell commands, and modify files belonging to developer tools.

---

> *Success is determined by those whom prove the impossible, possible.
Author: James Pence*

Source: [Two Compromised joyfill npm Packages Run RAT When Imported Into Node.js](https://thehackernews.com/2026/07/two-compromised-joyfill-npm-packages.html)
