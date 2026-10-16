---
name: environment-variables-and-env-handling
description: "Use when \"environment variables and env handling\" is the work. keeping a dotenv import from a ported Node codebase that double-loads env vars with different precedence than Buns."
---

# Environment Variables and .env Handling

keeping a dotenv import from.

1. Do not: keeping a dotenv import from a ported Node codebase that double-loads env vars with.
2. Do not: Assuming Node parity for an API Bun only partially implements.

Example:
```javascript
console.log(Bun.env.API_KEY, process.env.API_KEY); // both populated
```

Check: Do not: keeping a dotenv import from a ported Node codebase that double-loads env vars with different precedence.
