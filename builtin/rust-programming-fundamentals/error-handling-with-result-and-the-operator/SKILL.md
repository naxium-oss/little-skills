---
name: error-handling-with-result-and-the-operator
description: "Use when \"error handling with result and the operator\" is the work. using .unwrap()/.expect() widely in production code paths, causing panics on recoverable errors instead of graceful handling."
---

# Error Handling with Result and the

using .unwrap()/.expect() widely in production code paths, causing.

1. Do not: using .unwrap()/.expect() widely in production code paths, causing panics on recoverable errors instead of.
2. Do not: mixing custom error enums with Box<dyn Error> inconsistently across a codebase, complicating callers' error.

Example:
```rust
use std::fs;
```

Check: Do not: using .unwrap()/.expect().
