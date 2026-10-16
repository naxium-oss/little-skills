---
name: rust-interior-mutability-patterns
description: "Use when \"rust interior mutability patterns\" is the work. RefCell enforces exclusive mutable borrowing dynamically."
---

# Rust Interior Mutability Patterns

RefCell enforces exclusive mutable borrowing dynamically.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```rust
use std::cell::RefCell;
let value = RefCell::new(1);
*value.borrow_mut() += 1;
```

Check: Do not edit the assert to match a surprising result.
