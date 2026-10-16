---
name: security-patch-minimal-diff-application
description: "Use when \"security patch minimal diff application\" is the work. Apply the smallest supported fix and separate remediation from unrelated dependency upgrades."
---

# Security Patch Minimal-Diff Application

Apply the smallest supported fix and separate remediation from unrelated dependency upgrades.

1. Cross-check vendor advisories and independent databases with retrieval dates.
2. Map affected ranges to the deployed artifact including backports.
3. Assess configuration and reachability before applying the smallest supported remediation.

Example:
```text
Cross-check vendor advisories and independent databases with retrieval dates.
```

Check: Reproduce only in an authorized isolated environment; validate patch effectiveness and compatibility; track exceptions with owners and expiry.
