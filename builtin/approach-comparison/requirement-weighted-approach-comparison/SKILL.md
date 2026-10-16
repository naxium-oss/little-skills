---
name: requirement-weighted-approach-comparison
description: "Use when \"requirement weighted approach comparison\" is the work. Separate hard constraints from weighted preferences and expose weights before scoring candidates."
---

# Requirement-Weighted Approach Comparison

Separate hard constraints from weighted preferences and expose weights before scoring candidates.

1. Extract hard constraints and weighted criteria before comparing alternatives.
2. Compute bounds for memory, latency, and cost with units.
3. Use a representative spike to test the most uncertain assumptions.

Example:
```text
Extract hard constraints and weighted criteria before comparing alternatives.
```

Check: Perform sensitivity analysis; reject incompatible alternatives before ranking; separate measured values from estimates.
