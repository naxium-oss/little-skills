---
name: rust-iterator-adapters-collection
description: "Use when \"rust iterator adapters collection\" is the work. Iterator adapters are lazy until consumed."
---

# Rust Iterator Adapters & Collection

Iterator adapters are lazy until consumed.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```rust
let values = vec![1, 2, 3, 4];
let even: Vec<_> = values.iter().copied()
.filter(|x| x % 2 == 0).map(|x| x * 10).collect();
```

Check: Do not edit the assert to match a surprising result.
