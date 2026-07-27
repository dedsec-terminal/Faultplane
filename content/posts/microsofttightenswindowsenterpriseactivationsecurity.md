---
title: "Microsoft tightens Windows enterprise activation security"
date: 2026-07-24T09:52:24+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Microsoft is enhancing the security of Windows enterprise activation by introducing Trusted Platform Module (TPM)-backed attestation for Windows Key Management Service (KMS). This change replaces the existing software-only trust model with a hardware-backed verification process, aiming to strengthen enterprise activation security. The new requirement will be enforced with the next Windows Server Long-Term Servicing Channel (LTSC) release.

The TPM-backed KMS attestation process involves the KMS server generating an attestation report using its TPM to prove its identity and integrity before activation is completed. This creates a cryptographic chain of trust between Windows clients and the KMS host, reducing the risk of KMS server impersonation. To prepare for this change, organizations need to identify all KMS servers, verify that physical hosts support TPM, and confirm that TPM attestation is available.

Microsoft is advising organizations to prepare their KMS environments for the transition to hardware-backed trust. Administrators should assess their current infrastructure, determine if hardware upgrades are required, and plan for the migration. Starting August 2026, Windows Server 2025 will provide readiness messaging to help administrators assess their KMS host's readiness for hardware-based security, giving teams time to plan upgrades before enforcement begins. Microsoft will also publish guidance for virtual KMS hosts to ensure a smooth transition to the new security model.

---

> *If you don't know where you are going, you will probably end up somewhere else.
Author: Lawrence Peter*

Source: [Microsoft tightens Windows enterprise activation security](https://www.helpnetsecurity.com/2026/07/24/microsoft-kms-tpm-security-update/)
