---
name: base-image-version-and-digest-selection
description: "Use when \"base image version and digest selection\" is the work. Select a maintained target-compatible base and pin its content digest, not only a mutable tag."
---

# Base Image Version and Digest Selection

Select a maintained target-compatible base and pin its content digest, not only a mutable tag.

1. Pin image digests and verify target platform compatibility.
2. Render deployment configuration and inspect privileges, probes, and limits.

Example:
```text
Pin image digests and verify target platform compatibility.
```

Check: Exercise resource pressure, termination, rollout failure, and rollback; retain rendered manifests and image provenance.
