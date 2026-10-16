---
name: least-privilege-workflow-permission-design
description: "Use when \"least privilege workflow permission design\" is the work. Start from minimal permissions and justify every additional token capability per job."
---

# Least-Privilege Workflow Permission Design

Start from minimal permissions and justify every additional token capability per job.

1. Verify workflow syntax and event semantics against current official documentation.
2. Pin third-party actions to reviewed commit identifiers.
3. Isolate untrusted inputs and grant only necessary token permissions.

Example:
```text
Verify workflow syntax and event semantics against current official documentation.
```

Check: Review cache keys, artifact integrity, secret exposure, OIDC audience and subject conditions, required checks, and local reproduction.
