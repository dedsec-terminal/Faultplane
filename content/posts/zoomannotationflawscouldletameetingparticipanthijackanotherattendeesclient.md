---
title: "Zoom Annotation Flaws Could Let a Meeting Participant Hijack Another Attendee's Client"
date: 2026-08-11T19:08:47+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A security flaw was discovered in Zoom's annotation tool, which allows participants to draw and type on a shared screen. This vulnerability could have allowed an attacker to take control of another participant's computer, including the presenter's, without requiring any interaction from the victim. The flaw was found in the way the annotation tool handles structured objects, which can be manipulated to overflow a buffer and execute malicious code.

The vulnerability was discovered by an Israeli-founded startup called "A Security," which claims to have developed a working exploit in under a day using publicly available AI models. The firm rates the bugs as highly severe, with CVSS scores of 9.0, while Zoom rates them lower, with scores of 8.3, 6.5, and 8.3. The patches for the flaws were released in June and July, and no exploitation has been reported. The affected versions of Zoom include Zoom Workplace, Zoom Workplace VDI Client for Windows, and Zoom Rooms and Zoom Meeting SDK.

The discovery of this flaw highlights the potential risks of using AI models in security research. The startup claims that it was able to develop the exploit using models that are publicly available, which raises concerns about the ease of developing similar exploits in the future. The disclosure also comes as OpenAI has restricted access to its more advanced AI models, citing concerns about their potential use in malicious activities. The vulnerability has been assigned three CVE identifiers, and Zoom has published advisories with patches and workarounds to mitigate the flaws.

---

> *He that respects himself is safe from others; he wears a coat of mail that none can pierce.
Author: Henry Longfellow*

Source: [Zoom Annotation Flaws Could Let a Meeting Participant Hijack Another Attendee's Client](https://thehackernews.com/2026/08/zoom-annotation-flaws-could-let-meeting.html)
