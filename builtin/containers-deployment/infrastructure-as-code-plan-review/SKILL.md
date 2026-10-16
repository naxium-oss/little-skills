---
name: infrastructure-as-code-plan-review
description: "Use when \"infrastructure as code plan review\" is the work. Inspect replacement, deletion, privilege, network, and drift consequences before applying the plan."
---

# Infrastructure-as-Code Plan Review

Inspect replacement, deletion, privilege, network, and drift consequences before applying the plan.

1. Pin image digests and verify target platform compatibility.
2. Render deployment configuration and inspect privileges, probes, and limits.
3. Stage a rollout with observable acceptance gates and a tested rollback.

Example:
```text
Pin image digests and verify target platform compatibility.
```

Check: Exercise resource pressure, termination, rollout failure, and rollback; retain rendered manifests and image provenance.
