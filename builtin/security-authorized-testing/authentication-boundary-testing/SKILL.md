---
name: authentication-boundary-testing
description: "Use when \"authentication boundary testing\" is the work. Test session creation, expiration, recovery, and identity transitions with controlled test accounts."
---

# Authentication Boundary Testing

Test session creation, expiration, recovery, and identity transitions with controlled test accounts.

1. Obtain written authorization, target scope, test limits, and stop conditions.
2. Map assets and trust boundaries.
3. Use non-destructive controlled fixtures to test defenses and document reproducible findings.

Example:
```text
Obtain written authorization, target scope, test limits, and stop conditions.
```

Check: Use synthetic data; avoid production disruption; verify remediation with both denied malicious cases and allowed legitimate workflows.
