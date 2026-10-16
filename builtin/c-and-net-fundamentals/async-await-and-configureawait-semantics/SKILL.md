---
name: async-await-and-configureawait-semantics
description: "Use when \"async await and configureawait semantics\" is the work. blocking on async code with .Result/.Wait() in a UI or ASP.NET (Framework) context, causing a deadlock from context-capturing."
---

# async/await and ConfigureAwait Semantics

blocking on async code.

1. Do not: blocking on async code with .Result/.Wait() in a UI or ASP.NET (Framework) context, causing.
2. Do not: forgetting ConfigureAwait(false) consistently in library code, adding needless context-marshaling overhead in hot paths.

Example:
```bash
dotnet --info
```

Check: Do not: blocking on async code with .Result/.Wait() in.
