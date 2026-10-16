---
name: ci-secret-and-oidc-configuration
description: "Use when \"ci secret and oidc configuration\" is the work. Validate secret scope and OIDC issuer, audience, subject, trust policy, and protected environments."
---

# CI Secret and OIDC Configuration

Validate secret scope and OIDC issuer, audience, subject, trust policy, and protected environments.

1. Verify workflow syntax and event semantics against current official documentation.
2. Pin third-party actions to reviewed commit identifiers.
3. Isolate untrusted inputs and grant only necessary token permissions.

Example:
```text
Verify workflow syntax and event semantics against current official documentation.
```

Check: Review cache keys, artifact integrity, secret exposure, OIDC audience and subject conditions, required checks, and local reproduction.
