---
name: designing-the-analysis
description: "Use when \"how should we analyse\", \"design the analysis\" is the work."
---

# Design the analysis

The plan is the memory for the rest of the work.

1. One row per step: step number, what it produces, the exact input (file path and version).
2. Separate loading, cleaning, quality control, the primary analysis, robustness checks, and the figure or table each.

Example:
```text
One row per step: step number, what it produces, the exact input (file path.
```

Check: A step cannot be specified without seeing the data (for example, which columns exist): insert an exploration step.
