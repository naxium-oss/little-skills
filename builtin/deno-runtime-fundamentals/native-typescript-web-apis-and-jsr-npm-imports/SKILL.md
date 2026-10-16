---
name: native-typescript-web-apis-and-jsr-npm-imports
description: "Use when \"native typescript web apis and jsr npm imports\" is the work. mixing unpinned URL imports across a team, causing works on my machine drift."
---

# Native TypeScript, Web APIs, and JSR/npm

mixing unpinned URL imports across a.

1. Do not: mixing unpinned URL imports across a team, causing "works on my machine" drift.
2. Do not: assuming every npm package works flawlessly under Deno's Node compatibility layer without testing.

Example:
```typescript
import { serve } from "jsr:@std/http/file-server";
```

Check: Do not: mixing unpinned URL imports across.
