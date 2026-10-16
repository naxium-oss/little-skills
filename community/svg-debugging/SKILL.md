---
name: svg-debugging
description: "Use when \"svg is blank\", \"svg debugging\", \"debugging svgs and common issues\" is the work. Get from a symptom to the cause in one pass."
---

# Debugging SVGs and common issues

Get from a symptom to the cause in one pass.

1. Inherited from the parent (fill is inherited; stroke is not).
2. A presentation attribute on the element (fill="#333").
3. A stylesheet rule (#icon path { fill: … }), which beats presentation attributes.

Example:
```text
Inherited from the parent (fill is inherited; stroke is not).
```

Check: Say not run when the check did not run.
