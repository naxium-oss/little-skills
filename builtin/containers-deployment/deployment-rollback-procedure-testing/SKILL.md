---
name: deployment-rollback-procedure-testing
description: "Use when \"deployment rollback procedure testing\" is the work. Restore the previous artifact and compatible state in a rehearsal, including database considerations."
---

# Deployment Rollback Procedure Testing

Restore the previous artifact and compatible state in a rehearsal, including database considerations.

1. Pin image digests and verify target platform compatibility.
2. Render deployment configuration and inspect privileges, probes, and limits.
3. Stage a rollout with observable acceptance gates and a tested rollback.

Example:
```text
Pin image digests and verify target platform compatibility.
```

Check: Exercise resource pressure, termination, rollout failure, and rollback; retain rendered manifests and image provenance.
