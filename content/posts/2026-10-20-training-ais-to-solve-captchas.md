---
title: "Training AIs to Solve CAPTCHAs"
description: "Vision\u2011language models can solve visual CAPTCHAs without task\u2011specific training, but each new instance costs full compute. A hybrid system pairs a fin..."
source: "Schneier on Security"
source_url: "https://www.schneier.com/blog/archives/2026/10/training-ais-to-solve-captchas.html"
published: "2026-10-19T11:07:43+00:00"
ingested_at: "2026-10-20T03:12:20.905365+00:00"
date: "2026-10-20T03:12:20.905365+00:00"
category: "research"
tags:
  - "AI"
  - "CAPTCHA"
  - "VLM"
  - "YOLO"
  - "adversarial"
slug: "2026-10-20-training-ais-to-solve-captchas"
quote: "Life is a learning experience, only if you learn."
quote_author: "Yogi Berra"
---

### Executive Summary
Vision‑language models can solve visual CAPTCHAs without task‑specific training, but each new instance costs full compute. A hybrid system pairs a fine‑tuned YOLOv8 detector with an open‑weight VLM behind a confidence router, achieving 85.4% accuracy across 16 classes. The VLM’s predictions serve as training labels, enabling the detector to learn new categories after one or two encounters and to self‑repair. Even when CAPTCHA operators deploy perturbations that drop the detector’s accuracy to 0%, the VLM remains unaffected and the detector recovers. Over a year‑long simulated arms race, the solver consistently recovers after each monthly update, demonstrating that adaptive solvers can quickly overcome visual CAPTCHA defenses that assume static failure.

---
**Intelligence Metadata**
- **Source Publisher:** Schneier on Security
- **Published Date:** 2026-10-19T11:07:43+00:00
- **Category:** research

**Original Description:**
Interesting research: Abstract: Vision-language models (VLMs) can solve visual CAPTCHAs without task-specific training, but the agents built on them approach every challenge from scratch. For such an agent, the hundredth instance of a familiar puzzle costs as much time and compute as the first. Specialized detectors invert the trade-off, answering in milliseconds but only for categories they were trained on. Neither improves with exposure. We study what changes when a solver improves with use...
