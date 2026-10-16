---
name: cascade-specificity-and-source-order
description: "Use when \"cascade specificity and source order\" is the work. reaching for !important to force a win instead of fixing specificity/source order, which compounds into unmaintainable overrides."
---

# Cascade, Specificity, and Source Order

reaching for !important to force a win instead.

1. Do not: reaching for !important to force a win instead of fixing specificity/source order, which compounds.
2. Do not: assuming later-defined CSS files always win regardless of specificity.

Example:
```bash
grep -rn "!important" --include=*.css . | wc -l
```

Check: Do not: reaching for !important to force a win.
