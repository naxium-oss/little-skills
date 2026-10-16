---
name: third-party-action-pinning-and-provenance-checks
description: "Use when \"third party action pinning and provenance checks\" is the work. Pin immutable action commits and verify their upstream provenance and update process."
---

# Third-Party Action Pinning and Provenance Checks

Pin immutable action commits and verify their upstream provenance and update process.

1. Verify workflow syntax and event semantics against current official documentation.
2. Pin third-party actions to reviewed commit identifiers.
3. Isolate untrusted inputs and grant only necessary token permissions.

Example:
```text
Verify workflow syntax and event semantics against current official documentation.
```

Check: Review cache keys, artifact integrity, secret exposure, OIDC audience and subject conditions, required checks, and local reproduction.
