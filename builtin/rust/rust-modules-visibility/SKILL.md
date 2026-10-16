---
name: rust-modules-visibility
description: "Use when \"rust modules visibility\" is the work. Items are private by default."
---

# Rust Modules & Visibility

Items are private by default.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```rust
mod domain {
pub struct User { name: String }
impl User {
```

Check: Do not edit the assert to match a surprising result.
