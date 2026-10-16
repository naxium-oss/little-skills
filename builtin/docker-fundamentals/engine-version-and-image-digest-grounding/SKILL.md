---
name: engine-version-and-image-digest-grounding
description: "Use when \"engine version and image digest grounding\" is the work. pinning only a mutable tag (node:22) and being surprised a rebuild months later pulls a different underlying image."
---

# Engine Version and Image Digest Grounding

pinning only a mutable.

1. Do not: pinning only a mutable tag (node:22) and being surprised a rebuild months later pulls.
2. Do not: assuming BuildKit features work on a legacy builder without checking docker buildx version.

Example:
```bash
docker image inspect <image> --format "{{.Id}}"
```

Check: Do not: pinning only a mutable tag (node:22) and.
