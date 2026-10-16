---
name: box-model-and-sizing
description: "Use when \"box model and sizing\" is the work. forgetting border-box reset and being surprised padding/border inflate the total size beyond the declared width."
---

# Box Model and Sizing

forgetting border-box reset and being surprised padding/border.

1. Do not: forgetting border-box reset and being surprised padding/border inflate the total size beyond the declared.
2. Do not: not accounting for vertical margin collapse between siblings or parent/child blocks.

Example:
```bash
grep -rn "!important" --include=*.css . | wc -l
```

Check: Do not: forgetting border-box reset and being surprised.
