---
name: provider-version-and-state-backend-grounding
description: "Use when \"provider version and state backend grounding\" is the work. running terraform apply from two different machines/CI jobs without state locking configured, corrupting shared state."
---

# Provider Version and State Backend Grounding

running terraform apply from two different machines/CI.

1. Do not: running terraform apply from two different machines/CI jobs without state locking configured, corrupting shared.
2. Do not: upgrading a provider version without reading its changelog, triggering unexpected resource replacement on the.

Example:
```bash
terraform plan -out <file> and read the diff
```

Check: Do not: running terraform apply from two different.
