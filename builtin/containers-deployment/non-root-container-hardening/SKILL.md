---
name: non-root-container-hardening
description: "Use when \"non root container hardening\" is the work. Set an appropriate user and minimal capabilities; test writable paths and runtime permissions."
---

# Non-Root Container Hardening

Set an appropriate user and minimal capabilities; test writable paths and runtime permissions.

1. Pin image digests and verify target platform compatibility.
2. Render deployment configuration and inspect privileges, probes, and limits.
3. Stage a rollout with observable acceptance gates and a tested rollback.

Example:
```text
Pin image digests and verify target platform compatibility.
```

Check: Exercise resource pressure, termination, rollout failure, and rollback; retain rendered manifests and image provenance.
