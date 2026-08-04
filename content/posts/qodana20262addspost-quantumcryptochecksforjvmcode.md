---
title: "Qodana 2026.2 adds post-quantum crypto checks for JVM code"
date: 2026-08-03T11:21:33+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Qodana 2026.2 has been released with new security features, including post-quantum cryptography checks for JVM code. The update also includes new security inspections, benchmark results, and coverage reporting enhancements. The security inspections are integrated into the .NET linter and run by default, tracking untrusted data across files in C#, JavaScript, and TypeScript to detect vulnerabilities such as SQL injection and cross-site scripting.

The analysis is split into two parts: pattern rules that catch bad code at a single spot, and a taint engine that follows the data. This allows teams to add their own custom rules in the OpenGrep format. The benchmark results are publicly available, with SABER (Static Analysis Benchmark Evaluation Runner) running Qodana against public security benchmarks and comparing its findings with expected results. The results are hosted on a TeamCity server with guest login open, providing a transparent comparison of Qodana's performance.

The post-quantum cryptography checks come in five levels, following NIST's recommendations, and flag cryptography that would be vulnerable to quantum computer attacks. The checks are designed to help teams prepare for the potential risks of quantum computing, where an attacker could harvest encrypted data now and decrypt it later when the necessary hardware becomes available. Other features in the update include license gates, Laravel checks, and enhanced coverage reporting that no longer requires manual configuration. Future releases will extend these features to Kotlin and Java code.

---

> *Everyone has been made for some particular work, and the desire for that work has been put in every heart.
Author: Rumi*

Source: [Qodana 2026.2 adds post-quantum crypto checks for JVM code](https://www.helpnetsecurity.com/2026/08/03/qodana-2026-2-static-analysis-benchmarks/)
