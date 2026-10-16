---
name: rust-newtype-conversion-patterns
description: "Use when \"rust newtype conversion patterns\" is the work. A newtype is a distinct type."
---

# Rust Newtype & Conversion Patterns

A newtype is a distinct type.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```rust
struct Percent(u8);
impl TryFrom<u8> for Percent {
type Error = &'static str;
```

Check: Do not edit the assert to match a surprising result.
