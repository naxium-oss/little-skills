---
name: rust-traits-generic-bounds
description: "Use when \"rust traits generic bounds\" is the work. A trait bound states which operations generic code may use."
---

# Rust Traits & Generic Bounds

A trait bound states which operations generic code may use.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```rust
trait Area { fn area(&self) -> u32; }
struct Square(u32);
impl Area for Square {
```

Check: Do not edit the assert to match a surprising result.
