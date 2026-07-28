---
title: "Dysphoria IoT Botnet Adds Blockchain C2 and Victim Relays After JackSkid Disruption"
date: 2026-07-27T17:16:28+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

The Dysphoria IoT botnet has evolved to use blockchain-based name services and infected-device relays after a law-enforcement operation disrupted the JackSkid infrastructure in March. Researchers from CNCERT and XLab have been tracking the botnet, which is estimated to have over 200,000 bots, with 4,401 confirmed active devices in China and a single-day peak of 239,000 bots abroad. However, the exact numbers are not independently verified and should be treated with caution.

The botnet's design makes it harder to disrupt, as it uses a blockchain-based command-and-control (C2) system and relays traffic through infected devices. The C2 system uses Ethereum Name Service (ENS) and Solana Name Service (SNS) domains to resolve the addresses of distribution nodes, which are infected machines that relay traffic to the real controllers. The botnet also uses a relay-only variant that drops the DDoS modules and instead uses UPnP to map ports on the local gateway and shuttle traffic between an outside connection and a remote C2 service.

To defend against the Dysphoria botnet, researchers recommend patching exposed IoT gear, replacing devices that can no longer be updated, eliminating default and weak credentials, and disabling remote management and UPnP where they are not needed. The botnet spreads through Telnet and SSH weak-password guessing and known IoT remote-code-execution flaws, including a Linksys E1700 command-injection flaw. While the exact scale and impact of the botnet are not independently verified, it is clear that Dysphoria is a significant threat to internet-service and gaming targets, with the potential to launch large-scale DDoS attacks.

---

> *To avoid criticism, do nothing, say nothing, be nothing.
Author: Elbert Hubbard*

Source: [Dysphoria IoT Botnet Adds Blockchain C2 and Victim Relays After JackSkid Disruption](https://thehackernews.com/2026/07/dysphoria-iot-botnet-adds-blockchain-c2.html)
