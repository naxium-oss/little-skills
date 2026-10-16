---
name: image-representation-and-color-space-grounding
description: "Use when \"image representation and color space grounding\" is the work. feeding a BGR image directly into a model/visualization expecting RGB, causing subtly wrong-colored (but not obviously broken) results."
---

# Image Representation and Color Space Grounding

feeding a BGR image.

1. Do not: feeding a BGR image directly into a model/visualization expecting RGB, causing subtly wrong-colored (but.
2. Do not: mixing uint8 and normalized float32 images without explicit rescaling, causing values to clip or.

Example:
```bash
confirm channel order, value range, and resolution at each stage
```

Check: Do not: feeding a BGR image directly into a.
