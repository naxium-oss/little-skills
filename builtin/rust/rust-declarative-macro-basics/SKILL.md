---
name: rust-declarative-macro-basics
description: "Use when \"rust declarative macro basics\" is the work. Match token fragments intentionally and avoid evaluating an expression multiple times."
---

# Rust Declarative Macro Basics

Match token fragments intentionally and avoid evaluating an expression multiple times.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```rust
macro_rules! pair {
($value:expr) => {{
let value = $value;
```

Check: Do not edit the assert to match a surprising result.
