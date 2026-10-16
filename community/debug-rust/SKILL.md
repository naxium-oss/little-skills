---
name: debug-rust
description: "Use when \"rust Borrow checker rejection\", \"Borrow checker rejection\". Not when explaining working rust code."
---

# Debug rust

Reproduce the rust failure with the project command, then change one thing.

1. Borrow checker rejection: The borrow outlives the data or two borrows conflict; restructure ownership (clone, scope.
2. Panic: unwrap on None: Run with RUST_BACKTRACE=1 and read the frame in your crate; the invariant.
3. Release-only bug: Integer overflow and unchecked arithmetic behave differently in debug vs release; audit `wrapping_*` and.

Example:
```text
cargo build
```

Check: The same command that failed has to pass.
