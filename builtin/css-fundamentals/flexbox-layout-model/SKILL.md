---
name: flexbox-layout-model
description: "Use when \"flexbox layout model\" is the work. confusing justify-content (main axis) with align-items (cross axis) after changing flex-direction."
---

# Flexbox Layout Model

confusing justify-content (main axis) with.

1. Do not: confusing justify-content (main axis) with align-items (cross axis) after changing flex-direction.
2. Do not: using flex: 1 on children expecting equal width without accounting for differing flex-basis/content sizes.

Example:
```bash
grep -rn "!important" --include=*.css . | wc -l
```

Check: Do not: confusing justify-content (main axis).
