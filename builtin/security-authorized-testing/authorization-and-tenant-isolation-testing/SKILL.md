---
name: authorization-and-tenant-isolation-testing
description: "Use when \"authorization and tenant isolation testing\" is the work. Verify every object operation enforces identity and tenant ownership independently of client input."
---

# Authorization and Tenant Isolation Testing

Verify every object operation enforces identity and tenant ownership independently of client input.

1. Obtain written authorization, target scope, test limits, and stop conditions.
2. Map assets and trust boundaries.
3. Use non-destructive controlled fixtures to test defenses and document reproducible findings.

Example:
```text
Obtain written authorization, target scope, test limits, and stop conditions.
```

Check: Use synthetic data; avoid production disruption; verify remediation with both denied malicious cases and allowed legitimate workflows.
