---
title: "Tengu Botnet Reboots Compromised Linux Devices When Defenders Kill Its Process"
date: 2026-07-28T15:01:33+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

A new Mirai-derived botnet called Tengu has been discovered, which can reboot compromised Linux devices when its main process is killed by defenders. This is achieved through the device's hardware watchdog, allowing Tengu's other persistence mechanisms to relaunch it. The botnet supports 25 distributed denial-of-service (DDoS) methods, can run a SOCKS5 proxy, execute shell commands, and collect system and network data.

Tengu's persistence and self-defense code make it stand out among Mirai-derived samples. It uses a detached guardian to check the principal malware process every 60 seconds and relaunches the installed binary if it stops. The botnet can also create a fake systemd service, add init and RC scripts, alter shell startup files, and mark its installed binary immutable. Additionally, Tengu carries a hardcoded list of reboot and shutdown utilities, which it overwrites to interfere with defenders' attempts to restart or safely power down a compromised device.

To defend against Tengu, Nozomi Networks Labs recommends removing internet exposure for Telnet and other unnecessary administrative services, replacing default credentials, updating firmware, segmenting IoT networks, and reviewing systemd services, init scripts, shell startup files, and cron-related paths. The full extent of Tengu's spread and impact is currently unknown, as Nozomi's report only provides information on the botnet's capabilities and not its real-world victims or infection count. Further analysis and investigation are needed to determine the scope of the threat.

---

> *Life a culmination of the past, an awareness of the present, an indication of the future beyond knowledge, the quality that gives a touch of divinity to matter.
Author: Charles A. Lindbergh*

Source: [Tengu Botnet Reboots Compromised Linux Devices When Defenders Kill Its Process](https://thehackernews.com/2026/07/tengu-botnet-reboots-compromised-linux.html)
