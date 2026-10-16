---
name: kubernetes-api-version-compatibility-checking
description: "Use when \"kubernetes api version compatibility checking\" is the work. Match manifests and controllers to the actual cluster version and removed API availability."
---

# Kubernetes API Version Compatibility Checking

Match manifests and controllers to the actual cluster version and removed API availability.

1. Pin image digests and verify target platform compatibility.
2. Render deployment configuration and inspect privileges, probes, and limits.
3. Stage a rollout with observable acceptance gates and a tested rollback.

Example:
```text
Pin image digests and verify target platform compatibility.
```

Check: Exercise resource pressure, termination, rollout failure, and rollback; retain rendered manifests and image provenance.
