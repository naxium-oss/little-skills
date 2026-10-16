---
name: progressive-rollout-and-canary-verification
description: "Use when \"progressive rollout and canary verification\" is the work. Define canary cohorts, observation windows, measurable gates, and automatic stop conditions."
---

# Progressive Rollout and Canary Verification

Define canary cohorts, observation windows, measurable gates, and automatic stop conditions.

1. Pin image digests and verify target platform compatibility.
2. Render deployment configuration and inspect privileges, probes, and limits.
3. Stage a rollout with observable acceptance gates and a tested rollback.

Example:
```text
Pin image digests and verify target platform compatibility.
```

Check: Exercise resource pressure, termination, rollout failure, and rollback; retain rendered manifests and image provenance.
