---
title: "Tengu botnet reboots Linux devices to survive removal"
date: 2026-07-29T13:52:33+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here is a summary of the article in 3 concise paragraphs:

A new IoT botnet called Tengu has been discovered by Nozomi Networks Labs, which can force infected Linux devices to reboot once its main process is killed, allowing its persistence mechanisms to relaunch it. Tengu is a Mirai-derived botnet that was found to have a range of capabilities, including an encrypted channel for issuing commands, traffic relaying, payload delivery, and denial-of-service functions. The malware also has multiple persistence and self-defense mechanisms designed to keep it running on compromised devices and make recovery more difficult.

Tengu has several features that distinguish it from other Mirai variants, including a SOCKS5 proxy, shell command execution, system and network reconnaissance, and the ability to download ELF binaries or Android APKs. The malware also includes 25 DDoS methods and targets poorly secured Android TV boxes and similar Android-based devices. To survive removal, Tengu uses various techniques, including abusing the Linux hardware watchdog, overwriting reboot and shutdown binaries, and terminating competing botnets. The malware also has anti-debugging and anti-emulation capabilities to reduce the chance of detection.

To defend against Tengu, Nozomi Networks recommends applying security updates, replacing default credentials, segmenting networks, and monitoring Linux-based and IoT devices for unusual activity. The company has published indicators of compromise (IoCs), including the malware's C2 address and sample hashes for six processor architectures, along with a MITRE ATT&CK mapping of Tengu's tactics and techniques. By taking these steps, defenders can reduce the risk of infection and improve their ability to detect and respond to Tengu and other similar threats.

---

> *As you think, so shall you become.
Author: Bruce Lee*

Source: [Tengu botnet reboots Linux devices to survive removal](https://www.helpnetsecurity.com/2026/07/29/tengu-mirai-iot-botnet-linux/)
