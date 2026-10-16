---
name: cloudformation-and-infrastructure-drift
description: "Use when \"cloudformation and infrastructure drift\" is the work. manually editing a CloudFormation-managed resource in the console for a quick fix, causing drift that silently breaks the."
---

# CloudFormation and Infrastructure Drift

manually editing a CloudFormation-managed resource.

1. Do not: manually editing a CloudFormation-managed resource in the console for a quick fix, causing drift.
2. Do not: executing a change set without reviewing it first, missing an unexpected resource replacement that.

Example:
```bash
aws cloudformation detect-stack-drift --stack-name my-stack
```

Check: Do not: manually editing a CloudFormation-managed resource in the console for a quick fix, causing drift that silently.
