---
name: drift-detection-and-state-reconciliation
description: "Use when \"drift detection and state reconciliation\" is the work. running terraform apply to fix drift without understanding why it occurred, potentially reverting an intentional emergency fix made."
---

# Drift Detection and State Reconciliation

running terraform apply to "fix".

1. Do not: running terraform apply to "fix" drift without understanding why it occurred, potentially reverting an.
2. Do not: never running drift detection at all, letting Terraform state silently diverge from reality until.

Example:
```bash
terraform plan -refresh-only          # shows drift without proposing to "fix" it back yet
```

Check: Do not: running terraform apply to "fix" drift without.
