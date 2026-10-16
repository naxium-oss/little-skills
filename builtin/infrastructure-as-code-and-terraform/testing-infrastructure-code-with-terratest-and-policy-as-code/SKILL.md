---
name: testing-infrastructure-code-with-terratest-and-policy-as-code
description: "Use when \"testing infrastructure code with terratest and policy as code\" is the work."
---

# Testing Infrastructure Code with Terratest and

running policy-as-code checks in report-only.

1. Do not: running policy-as-code checks in report-only mode indefinitely instead of promoting them to a blocking.
2. Do not: writing infrastructure integration tests that provision real cloud resources without guaranteed cleanup on failure.

Example:
```rego
package terraform.security
```

Check: Do not: running policy-as-code.
