---
name: git-bisect-for-failure-localization
description: "Use when \"git bisect for failure localization\" is the work. Choose known-good and known-bad commits and automate a reliable pass/fail/skip classifier."
---

# Git Bisect for Failure Localization

Choose known-good and known-bad commits and automate a reliable pass/fail/skip classifier.

1. Reproduce the symptom and preserve the earliest causal evidence.
2. Rank competing hypotheses and choose a discriminating observation.

Example:
```text
Reproduce the symptom and preserve the earliest causal evidence.
```

Check: Show a failing baseline, the causal mechanism, a passing regression, and a check that the fix did not.
