---
title: "A few notes on AWS Nitro Enclaves: KMS integration"
description: "The post explains how AWS Nitro Enclaves can integrate with AWS Key Management Service (KMS) to offload key management. It details KMS key types (CMK,..."
source: "Trail of Bits"
source_url: "https://blog.trailofbits.com/2026/08/05/a-few-notes-on-aws-nitro-enclaves-kms-integration/"
date: "2026-08-05T11:00:00+00:00"
category: "research"
tags:
  - "AWS Nitro Enclaves"
  - "KMS"
  - "key management"
  - "enclave security"
  - "cloud security"
slug: "2026-08-05-a-few-notes-on-aws-nitro-enclaves-kms-integration"
quote: "It is only with the heart that one can see rightly, what is essential is invisible to the eye."
quote_author: "Antoine de Saint-Exupery"
---

The post explains how AWS Nitro Enclaves can integrate with AWS Key Management Service (KMS) to offload key management. It details KMS key types (CMK, data keys, key pairs), how data keys are used for envelope encryption, and how KMS policies can restrict CMK access to specific enclaves via PCR values or encrypt responses to enclave public keys. The article catalogs passive and active attack classes on the enclave‑KMS channel and discusses operational risks even when cryptography is correct.
