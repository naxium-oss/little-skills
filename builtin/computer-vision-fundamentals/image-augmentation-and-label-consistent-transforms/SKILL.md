---
name: image-augmentation-and-label-consistent-transforms
description: "Use when \"image augmentation and label consistent transforms\" is the work. applying a geometric augmentation to images without correspondingly transforming bounding box/mask labels, silently corrupting supervision."
---

# Image Augmentation and Label-Consistent Transforms

applying a geometric augmentation to images without.

1. Do not: applying a geometric augmentation to images without correspondingly transforming bounding box/mask labels, silently corrupting.
2. Do not: mixing up bounding box formats (xyxy vs xywh, normalized vs. absolute pixels) between augmentation.

Example:
```bash
confirm channel order, value range, and resolution at each stage
```

Check: Do not: applying a geometric augmentation to images.
