---
title: "ZDI-26-564: NVIDIA Transformers4Rec load_model_trainer_states_from_checkpoint Deserialization of Untrusted Data Remote Code Execution Vulnerability"
date: 2026-08-13T05:00:00+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

NVIDIA Transformers4Rec load_model_trainer_states_from_checkpoint Deserialization of Untrusted Data Remote Code Execution Vulnerability
Vulnerability Details
This vulnerability allows remote attackers to execute arbitrary code on affected installations of NVIDIA Transformers4Rec. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file.
The specific flaw exists within the load_model_trainer_states_from_checkpoint function. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current process.
Additional Details
NVIDIA has issued an update to correct this vulnerability. More details can be found at:
                            
                            https://nvidia.custhelp.com/app/answers/detail/a_id/5869
                            
                  

---

> *If you must tell me your opinions, tell me what you believe in. I have plenty of douts of my own.
Author: Johann Wolfgang von Goethe*

Source: [ZDI-26-564: NVIDIA Transformers4Rec load_model_trainer_states_from_checkpoint Deserialization of Untrusted Data Remote Code Execution Vulnerability](http://www.zerodayinitiative.com/advisories/ZDI-26-564/)
