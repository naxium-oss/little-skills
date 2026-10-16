---
name: ci-artifact-retention-and-integrity-checks
description: "Use when \"ci artifact retention and integrity checks\" is the work. Check artifact contents, retention settings, provenance, and verification before privileged consumption."
---

# CI Artifact Retention and Integrity Checks

Check artifact contents, retention settings, provenance, and verification before privileged consumption.

1. Verify workflow syntax and event semantics against current official documentation.
2. Pin third-party actions to reviewed commit identifiers.
3. Isolate untrusted inputs and grant only necessary token permissions.

Example:
```text
Verify workflow syntax and event semantics against current official documentation.
```

Check: Review cache keys, artifact integrity, secret exposure, OIDC audience and subject conditions, required checks, and local reproduction.
