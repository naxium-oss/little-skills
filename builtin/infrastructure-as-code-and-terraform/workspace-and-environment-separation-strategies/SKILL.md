---
name: workspace-and-environment-separation-strategies
description: "Use when \"workspace and environment separation strategies\" is the work. using Terraform workspaces for environments with fundamentally different resource configurations (not just variable values), fighting the tools design."
---

# Workspace and Environment Separation Strategies

using Terraform workspaces for environments with fundamentally different resource configurations (not.

1. Do not: using Terraform workspaces for environments with fundamentally different resource configurations (not just variable values).
2. Do not: forgetting to switch workspace before an apply, applying a plan intended for one environment.

Example:
```bash
terraform workspace list
```

Check: Do not: using Terraform workspaces for environments with fundamentally different resource configurations (not just variable values), fighting the.
