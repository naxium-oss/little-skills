---
name: ci-matrix-design
description: "Use when \"ci matrix design\" is the work. Choose axes from actual support policy and avoid redundant combinations that inflate cost."
---

# CI Matrix Design

Choose axes from actual support policy and avoid redundant combinations that inflate cost.

1. Verify workflow syntax and event semantics against current official documentation.
2. Pin third-party actions to reviewed commit identifiers.
3. Isolate untrusted inputs and grant only necessary token permissions.

Example:
```text
Verify workflow syntax and event semantics against current official documentation.
```

Check: Review cache keys, artifact integrity, secret exposure, OIDC audience and subject conditions, required checks, and local reproduction.
