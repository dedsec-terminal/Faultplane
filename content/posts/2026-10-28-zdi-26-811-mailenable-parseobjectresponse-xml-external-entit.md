---
title: "ZDI-26-811: MailEnable parseObjectResponse XML External Entity Processing Information Disclosure Vulnerability"
description: "A remote information disclosure vulnerability exists in MailEnable's parseObjectResponse function, allowing authenticated attackers to read sensitive ..."
source: "Zero Day Initiative"
source_url: "http://www.zerodayinitiative.com/advisories/ZDI-26-811/"
published: "2026-10-27T05:00:00+00:00"
ingested_at: "2026-10-28T03:48:09.720380+00:00"
date: "2026-10-28T03:48:09.720380+00:00"
category: "cves"
tags:
  - "MailEnable"
  - "XML External Entity"
  - "Information Disclosure"
  - "CVE-2026-114552"
slug: "2026-10-28-zdi-26-811-mailenable-parseobjectresponse-xml-external-entit"
quote: "It is one of the blessings of old friends that you can afford to be stupid with them."
quote_author: "Ralph Emerson"
---

### Executive Summary
A remote information disclosure vulnerability exists in MailEnable's parseObjectResponse function, allowing authenticated attackers to read sensitive data via XML External Entity processing. The flaw, identified as CVE-2026-114552, carries a CVSS score of 6.5 and was disclosed by Zero Day Initiative (ZDI-26-811).

---
**Intelligence Metadata**
- **Source Publisher:** Zero Day Initiative
- **Published Date:** 2026-10-27T05:00:00+00:00
- **Category:** cves

**Original Description:**
This vulnerability allows remote attackers to disclose sensitive information on affected installations of MailEnable. Authentication is required to exploit this vulnerability. The ZDI has assigned a CVSS rating of 6.5. The following CVEs are assigned: CVE-2026-114552.
