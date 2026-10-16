---
name: ci-failure-reproduction-locally
description: "Use when \"ci failure reproduction locally\" is the work. Match runner image, shell, environment, services, and exact failing command locally."
---

# CI Failure Reproduction Locally

Match runner image, shell, environment, services, and exact failing command locally.

1. Verify workflow syntax and event semantics against current official documentation.
2. Pin third-party actions to reviewed commit identifiers.
3. Isolate untrusted inputs and grant only necessary token permissions.

Example:
```text
Verify workflow syntax and event semantics against current official documentation.
```

Check: Review cache keys, artifact integrity, secret exposure, OIDC audience and subject conditions, required checks, and local reproduction.
