---
name: sequence-packing-and-boundary-correctness
description: "Use when \"sequence packing and boundary correctness\" is the work. Prevent cross-example attention or target leakage according to the selected packing semantics."
---

# Sequence Packing and Boundary Correctness

Prevent cross-example attention or target leakage according to the selected packing semantics.

1. Pin model, tokenizer, dataset, trainer, and dependency revisions.
2. Inspect tokenized examples and label masks.
3. Run an overfit-on-small-batch check before a budgeted full experiment.

Example:
```text
Pin model, tokenizer, dataset, trainer, and dependency revisions.
```

Check: Check optimizer groups, schedule units, effective batch size, RNG restoration, evaluation contamination, forgetting, and checkpoint compatibility.
