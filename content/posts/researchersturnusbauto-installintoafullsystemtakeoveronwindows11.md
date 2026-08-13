---
title: "Researchers Turn USB Auto-Install Into a Full SYSTEM Takeover on Windows 11"
date: 2026-08-11T10:48:26+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Here is a 3-paragraph summary of the research:

Security researchers Alejandro Hernando and Borja Martinez have discovered a vulnerability in Windows 11 that allows an attacker to gain full system access by exploiting the Windows Plug and Play (PnP) auto-install feature. The researchers found that they can emulate a USB device, triggering the PnP installation path, which can lead to the execution of privileged installation components. This can be done by an unprivileged user, and the researchers demonstrated the technique on a fully updated Windows 11 machine.

The researchers used a combination of emulated USB devices, including a Sierra Wireless device and a Sony FeliCa reader, to exploit vulnerabilities in signed vendor software. They were able to redirect DNS, place a DLL in the System32 directory, and ultimately gain SYSTEM access. The researchers also demonstrated a remote variant of the attack, which uses synthetic USB traffic over Remote Desktop Protocol (RDP) to exploit the vulnerability. This remote attack requires specific configuration settings to be enabled, including supported Plug and Play and low-level USB redirection.

Microsoft has noted that the remote attack is not a default exposure, as Remote Desktop Services does not allow supported Plug and Play and RemoteFX USB redirection by default. Administrators can mitigate the vulnerability by disabling the feature or using device-installation restrictions to block devices by hardware or compatible ID. The researchers' findings highlight the importance of securing the Windows PnP auto-install feature and the need for vendors to ensure the security of their signed software packages. The research demonstrates the potential for abuse of legitimate privileged installation paths combined with weaknesses in signed third-party packages.

---

> *How many cares one loses when one decides not to be something but to be someone.
Author: Coco Chanel*

Source: [Researchers Turn USB Auto-Install Into a Full SYSTEM Takeover on Windows 11](https://thehackernews.com/2026/08/researchers-turn-usb-auto-install-into.html)
