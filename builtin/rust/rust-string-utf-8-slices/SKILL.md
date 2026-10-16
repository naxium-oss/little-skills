---
name: rust-string-utf-8-slices
description: "Use when \"rust string utf 8 slices\" is the work. String byte indexing is not character indexing."
---

# Rust String & UTF-8 Slices

String byte indexing is not character indexing.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```rust
let text = "éa";
assert_eq!(text.len(), 3);
assert_eq!(text.chars().count(), 2);
```

Check: Do not edit the assert to match a surprising result.
