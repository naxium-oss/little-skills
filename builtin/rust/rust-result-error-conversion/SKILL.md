---
name: rust-result-error-conversion
description: "Use when \"rust result error conversion\" is the work. The question-mark operator returns early on an error and may convert it through From."
---

# Rust Result & Error Conversion

The question-mark operator returns early on an error and may convert it through From.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```rust
fn add(a: &str, b: &str) -> Result<i32, std::num::ParseIntError> {
```

Check: Do not edit the assert to match a surprising result.
