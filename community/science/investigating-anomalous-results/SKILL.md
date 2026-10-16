---
name: investigating-anomalous-results
description: "Use when \"numbers look wrong\", \"investigate the anomaly\" is the work. The tempting move is to drop the odd rows."
---

# Investigate the anomaly

The tempting move is to drop the odd rows.

1. Write down the observation exactly as the output showed it: the number, the group, the filter.
2. Check the four usual causes in order: a join or merge that duplicated rows, a filter.
3. Trace one concrete case.

Example:
```text
Write down the observation exactly as the output showed it: the number, the group.
```

Check: The cause is a logging or collection gap: report it as a data-quality finding in the deliverable.
