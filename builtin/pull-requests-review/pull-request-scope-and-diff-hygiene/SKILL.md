---
name: pull-request-scope-and-diff-hygiene
description: "Use when \"pull request scope and diff hygiene\" is the work. Remove unrelated churn and separate mechanical changes from behavior changes where practical."
---

# Pull Request Scope and Diff Hygiene

Remove unrelated churn and separate mechanical changes from behavior changes where practical.

1. Map requirements to changed code and tests.
2. Review correctness, security, compatibility, and operational risks independently.
3. Write actionable comments with file locations and reproduce material findings.

Example:
```text
Map requirements to changed code and tests.
```

Check: Resolve every blocking finding with evidence; distinguish reviewed code from uninspected areas and report residual release risk.
