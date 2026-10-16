---
name: modern-color-spaces-and-functions
description: "Use when \"modern color spaces and functions\" is the work. using oklch/lab without a fallback for browsers predating broad support."
---

# Modern Color Spaces and Functions

using oklch/lab without a fallback for browsers predating broad support.

1. Do not: using oklch/lab without a fallback for browsers predating broad support.
2. Do not: assuming color-mix() percentages behave linearly in all color spaces without checking the actual interpolation.

Example:
```bash
grep -rn "!important" --include=*.css . | wc -l
```

Check: Do not: using oklch/lab without a fallback for browsers predating broad support.
