---
title: "AWS Certificate Manager sets 2027 end date for email-validated certificate renewals"
date: 2026-08-14T08:25:31+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are 3 concise paragraphs summarizing the information:

AWS Certificate Manager (ACM) will phase out email validation for public certificates throughout 2027, ahead of the Certification Authority/Browser (CA/B) Forum's deadline of March 15, 2028. The CA/B Forum sets standards for publicly trusted certificates, and from March 15, 2028, public certificate authorities will no longer be able to use email-based domain validation to issue or renew publicly trusted certificates. Certificates issued before that date will remain valid until they expire.

AWS will begin phasing out email validation on January 1, 2027, and will stop offering the method in new AWS Regions. Email validation will no longer be available for new certificate requests in any AWS Region from March 31, 2027, and ACM will stop renewing existing email-validated certificates on September 30, 2027. AWS recommends migrating affected certificates to DNS validation before that date. Customers can check if their public certificates use email validation through the AWS Management Console or the AWS Command Line Interface (AWS CLI).

To assist with the migration, ACM is updating the UpdateCertificateOptions API to allow customers to switch a certificate's validation method from email to DNS in place, without changing the certificate's Amazon Resource Name (ARN). After initiating the switch, ACM provides a CNAME record that must be added to the domain's DNS configuration within 72 hours. Once DNS validation is completed, ACM will renew the certificate automatically before it expires, provided the required DNS validation record remains in place. Alternatively, HTTP validation will be supported for certificates used with Amazon CloudFront, but DNS validation is recommended for most use cases.

---

> *Fears are nothing more than a state of mind.
Author: Napoleon Hill*

Source: [AWS Certificate Manager sets 2027 end date for email-validated certificate renewals](https://www.helpnetsecurity.com/2026/08/14/aws-certificate-manager-email-validation/)
