---
name: trace-the-call
description: "Use when \"who calls\", \"call path\", or \"trace the call\". Not when explain the product."
---

# Trace the call

Follow callers and callees, not a guess of the architecture.

1. Search for the symbol.
2. Open the caller and one callee.
3. Write the path as file to file.

Example:
```text
checkout() in cart.ts calls pay() in pay.ts.
```

Check: A box diagram you did not trace is not the path.
