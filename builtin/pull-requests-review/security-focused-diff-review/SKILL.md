---
name: security-focused-diff-review
description: "Use when \"security focused diff review\" is the work. Review trust boundaries, authorization, injection risks, secrets, and newly reachable attack surfaces."
---

# Security-Focused Diff Review

Review trust boundaries, authorization, injection risks, secrets, and newly reachable attack surfaces.

1. Map requirements to changed code and tests.
2. Review correctness, security, compatibility, and operational risks independently.
3. Write actionable comments with file locations and reproduce material findings.

Example:
```text
Map requirements to changed code and tests.
```

Check: Resolve every blocking finding with evidence; distinguish reviewed code from uninspected areas and report residual release risk.
