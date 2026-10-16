---
name: visual-regression-baseline-management
description: "Use when \"visual regression baseline management\" is the work. Pin rendering conditions and review baseline changes with reasons instead of approving all differences."
---

# Visual Regression Baseline Management

Pin rendering conditions and review baseline changes with reasons instead of approving all differences.

1. Define representative journeys, viewports, browsers, and input methods.
2. Capture stable screenshots alongside console and network evidence.
3. Reproduce each defect with minimal steps and an expected-behavior statement.

Example:
```text
Define representative journeys, viewports, browsers, and input methods.
```

Check: Check touch and keyboard parity, missing assets, stacking contexts, localization, and baseline validity; do not approve unexplained visual.
