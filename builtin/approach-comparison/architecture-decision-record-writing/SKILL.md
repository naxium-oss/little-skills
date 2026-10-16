---
name: architecture-decision-record-writing
description: "Use when \"architecture decision record writing\" is the work. Write context, considered alternatives, evidence, decision, consequences, owner, and reconsideration triggers."
---

# Architecture Decision Record Writing

Write context, considered alternatives, evidence, decision, consequences, owner, and reconsideration triggers.

1. Extract hard constraints and weighted criteria before comparing alternatives.
2. Compute bounds for memory, latency, and cost with units.
3. Use a representative spike to test the most uncertain assumptions.

Example:
```text
Extract hard constraints and weighted criteria before comparing alternatives.
```

Check: Perform sensitivity analysis; reject incompatible alternatives before ranking; separate measured values from estimates.
