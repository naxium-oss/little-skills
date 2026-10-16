---
name: container-resource-limit-validation
description: "Use when \"container resource limit validation\" is the work. Test CPU throttling, memory pressure, OOM handling, and termination under declared resource limits."
---

# Container Resource Limit Validation

Test CPU throttling, memory pressure, OOM handling, and termination under declared resource limits.

1. Pin image digests and verify target platform compatibility.
2. Render deployment configuration and inspect privileges, probes, and limits.
3. Stage a rollout with observable acceptance gates and a tested rollback.

Example:
```text
Pin image digests and verify target platform compatibility.
```

Check: Exercise resource pressure, termination, rollout failure, and rollback; retain rendered manifests and image provenance.
