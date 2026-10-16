---
name: image-and-font-optimization-components
description: "Use when \"image and font optimization components\" is the work. forgetting to add an external image domain to remotePatterns, causing a build/runtime error when using next/image with that."
---

# Image and Font Optimization Components

forgetting to add an.

1. Do not: forgetting to add an external image domain to remotePatterns, causing a build/runtime error when.
2. Do not: marking every image priority, eliminating the lazy-loading performance benefit entirely.

Example:
```tsx
import Image from "next/image";
```

Check: Do not: forgetting to add an external image domain to remotePatterns, causing a build/runtime error when using next/image.
