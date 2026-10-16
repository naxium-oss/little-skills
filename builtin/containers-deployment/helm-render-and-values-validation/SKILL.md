---
name: helm-render-and-values-validation
description: "Use when \"helm render and values validation\" is the work. Render exact values and chart dependencies, then validate schemas and inspect security-sensitive output."
---

# Helm Render and Values Validation

Render exact values and chart dependencies, then validate schemas and inspect security-sensitive output.

1. Pin image digests and verify target platform compatibility.
2. Render deployment configuration and inspect privileges, probes, and limits.
3. Stage a rollout with observable acceptance gates and a tested rollback.

Example:
```text
Pin image digests and verify target platform compatibility.
```

Check: Exercise resource pressure, termination, rollout failure, and rollback; retain rendered manifests and image provenance.
