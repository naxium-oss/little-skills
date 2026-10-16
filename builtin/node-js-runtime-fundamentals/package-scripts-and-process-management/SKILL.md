---
name: package-scripts-and-process-management
description: "Use when \"package scripts and process management\" is the work. relying on npm start restarting automatically on crash with no supervisor configured."
---

# Package Scripts and Process Management

relying on npm start restarting automatically on crash with no supervisor configured.

1. Do not: relying on npm start restarting automatically on crash with no supervisor configured.
2. Do not: ignoring SIGTERM and having the orchestrator hard-kill (SIGKILL) mid-request.

Example:
```json
{
"scripts": {
"dev": "node --watch src/server.js",
```

Check: Do not: relying on npm start restarting automatically on crash with no supervisor configured.
