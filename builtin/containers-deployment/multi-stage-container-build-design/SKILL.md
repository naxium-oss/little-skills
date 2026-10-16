---
name: multi-stage-container-build-design
description: "Use when \"multi stage container build design\" is the work. Keep build tools and secrets out of the final image and verify copied runtime dependencies."
---

# Multi-Stage Container Build Design

Keep build tools and secrets out of the final image and verify copied runtime dependencies.

1. Pin image digests and verify target platform compatibility.
2. Render deployment configuration and inspect privileges, probes, and limits.
3. Stage a rollout with observable acceptance gates and a tested rollback.

Example:
```text
Pin image digests and verify target platform compatibility.
```

Check: Exercise resource pressure, termination, rollout failure, and rollback; retain rendered manifests and image provenance.
