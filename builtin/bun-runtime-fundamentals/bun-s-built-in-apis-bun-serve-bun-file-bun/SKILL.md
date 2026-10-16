---
name: bun-s-built-in-apis-bun-serve-bun-file-bun
description: "Use when \"bun s built in apis bun serve bun file bun\" is the work. porting Express middleware directly assuming identical request/response objects."
---

# Bun's Built-in APIs: Bun.serve, Bun.file, Bun.$

porting Express middleware directly assuming identical request/response objects.

1. Do not: porting Express middleware directly assuming identical request/response objects.
2. Do not: using Bun.$ shell templating with unsanitized user input, risking injection just like any shell.

Example:
```javascript
const server = Bun.serve({
```

Check: Do not: porting Express middleware directly assuming identical request/response objects.
