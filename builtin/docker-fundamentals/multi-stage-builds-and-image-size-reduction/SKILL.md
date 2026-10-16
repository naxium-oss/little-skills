---
name: multi-stage-builds-and-image-size-reduction
description: "Use when \"multi stage builds and image size reduction\" is the work. forgetting --from=builder and accidentally including the full build toolchain in the final image."
---

# Multi-Stage Builds and Image Size Reduction

forgetting --from=builder and accidentally including the.

1. Do not: forgetting --from=builder and accidentally including the full build toolchain in the final image.
2. Do not: using a latest-tagged distroless/base image without pinning, causing unreproducible builds.

Example:
```dockerfile
FROM golang:1.23 AS builder
```

Check: Do not: forgetting --from=builder and accidentally including the full build toolchain in the final image.
