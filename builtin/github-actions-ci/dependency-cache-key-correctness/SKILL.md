---
name: dependency-cache-key-correctness
description: "Use when \"dependency cache key correctness\" is the work. Include dependency locks, platform, toolchain, and relevant build inputs in cache identity."
---

# Dependency Cache Key Correctness

Include dependency locks, platform, toolchain, and relevant build inputs in cache identity.

1. Verify workflow syntax and event semantics against current official documentation.
2. Pin third-party actions to reviewed commit identifiers.
3. Isolate untrusted inputs and grant only necessary token permissions.

Example:
```text
Verify workflow syntax and event semantics against current official documentation.
```

Check: Review cache keys, artifact integrity, secret exposure, OIDC audience and subject conditions, required checks, and local reproduction.
