---
name: container-health-and-readiness-probe-design
description: "Use when \"container health and readiness probe design\" is the work. Separate startup, readiness, and liveness semantics and test dependency failure without restart storms."
---

# Container Health and Readiness Probe Design

Separate startup, readiness, and liveness semantics and test dependency failure without restart storms.

1. Pin image digests and verify target platform compatibility.
2. Render deployment configuration and inspect privileges, probes, and limits.
3. Stage a rollout with observable acceptance gates and a tested rollback.

Example:
```text
Pin image digests and verify target platform compatibility.
```

Check: Exercise resource pressure, termination, rollout failure, and rollback; retain rendered manifests and image provenance.
