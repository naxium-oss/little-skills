---
name: angular-universal-server-side-rendering
description: "Use when \"angular universal server side rendering\" is the work. calling window/document/localStorage unconditionally in a service or component constructor, crashing server-side rendering entirely."
---

# Angular Universal Server-Side Rendering

calling window/document/localStorage unconditionally in a service.

1. Do not: calling window/document/localStorage unconditionally in a service or component constructor, crashing server-side rendering entirely.
2. Do not: never testing the actual SSR build output, missing hydration mismatches that only manifest outside.

Example:
```typescript
import { isPlatformBrowser } from "@angular/common";
```

Check: Do not: calling window/document/localStorage unconditionally in a.
