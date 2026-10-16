---
name: color-space-and-tone-mapping-configuration
description: "Use when \"color space and tone mapping configuration\" is the work. Trace texture encoding, working color space, output conversion, exposure, and tone mapping exactly once."
---

# Color Space and Tone Mapping Configuration

Trace texture encoding, working color space, output conversion, exposure, and tone mapping exactly once.

1. Pin the Three.js revision and matching addons.
2. Validate coordinate spaces, asset units, color pipeline, and renderer capabilities.

Example:
```text
Pin the Three.js revision and matching addons.
```

Check: Test asset-load failures, resize, context loss, frustum behavior, GPU limits, and repeated mount/unmount memory use.
