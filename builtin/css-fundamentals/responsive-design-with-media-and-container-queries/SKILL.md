---
name: responsive-design-with-media-and-container-queries
description: "Use when \"responsive design with media and container queries\" is the work. relying only on min-width media query breakpoints without testing intermediate widths, missing awkward layout states."
---

# Responsive Design with Media and Container

relying only on min-width media query breakpoints.

1. Do not: relying only on min-width media query breakpoints without testing intermediate widths, missing awkward layout.
2. Do not: assuming container queries are supported without checking the minimum target browser version.

Example:
```bash
grep -rn "!important" --include=*.css . | wc -l
```

Check: Do not: relying only on min-width media query.
