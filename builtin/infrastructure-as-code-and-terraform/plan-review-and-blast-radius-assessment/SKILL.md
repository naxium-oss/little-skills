---
name: plan-review-and-blast-radius-assessment
description: "Use when \"plan review and blast radius assessment\" is the work. applying a plan without reading the full diff, missing an unexpected forces replacement on a stateful resource like."
---

# Plan Review and Blast Radius Assessment

applying a plan without reading the full diff, missing an.

1. Do not: applying a plan without reading the full diff, missing an unexpected forces replacement on.
2. Do not: not setting prevent_destroy on critical resources, allowing an accidental terraform destroy or config typo.

Example:
```bash
terraform plan -out=tfplan
```

Check: Do not: applying a plan without reading the full diff, missing an unexpected forces replacement on a stateful.
