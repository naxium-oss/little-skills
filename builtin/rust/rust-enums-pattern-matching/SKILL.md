---
name: rust-enums-pattern-matching
description: "Use when \"rust enums pattern matching\" is the work. Prefer exhaustive matching over sentinel values."
---

# Rust Enums & Pattern Matching

Prefer exhaustive matching over sentinel values.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```rust
enum Status { Pending, Ready(u32) }
fn value(status: Status) -> Option<u32> {
match status {
```

Check: Do not edit the assert to match a surprising result.
