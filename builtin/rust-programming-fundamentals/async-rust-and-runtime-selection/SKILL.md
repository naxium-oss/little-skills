---
name: async-rust-and-runtime-selection
description: "Use when \"async rust and runtime selection\" is the work. mixing Tokio-specific async I/O primitives with an async-std-based executor in the same binary, hitting confusing runtime panics about."
---

# Async Rust and Runtime Selection

mixing Tokio-specific async I/O primitives.

1. Do not: mixing Tokio-specific async I/O primitives with an async-std-based executor in the same binary, hitting.
2. Do not: publishing a library that hardcodes a specific async runtime, forcing every downstream consumer onto.

Example:
```rust
async fn main() {
```

Check: Do not: mixing Tokio-specific async I/O primitives with an.
