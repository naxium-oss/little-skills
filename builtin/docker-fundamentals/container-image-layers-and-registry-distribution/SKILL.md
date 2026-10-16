---
name: container-image-layers-and-registry-distribution
description: "Use when \"container image layers and registry distribution\" is the work. trusting a mutable tag (:latest, :1.4) as a stable reference in a deploy pipeline without pinning to a."
---

# Container Image Layers and Registry Distribution

trusting a mutable tag (:latest.

1. Do not: trusting a mutable tag (:latest, :1.4) as a stable reference in a deploy pipeline.
2. Do not: assuming layer caching guarantees reproducibility across different builder machines/architectures without verifying digests match.

Example:
```bash
docker history my-app:1.4.0
```

Check: Do not: trusting a.
