---
name: custom-properties-css-variables-and-theming
description: "Use when \"custom properties css variables and theming\" is the work. assuming custom properties are statically inlined like preprocessor variables, missing their live-updating cascade behavior."
---

# Custom Properties (CSS Variables) and Theming

assuming custom properties are statically inlined like.

1. Do not: assuming custom properties are statically inlined like preprocessor variables, missing their live-updating cascade behavior.
2. Do not: forgetting a fallback value (var(--x, default)) causes the property to be invalid, not just.

Example:
```bash
grep -rn "!important" --include=*.css . | wc -l
```

Check: Do not: assuming custom properties are statically inlined.
