---
name: pattern-matching-and-exhaustiveness-in-rust
description: "Use when \"pattern matching and exhaustiveness in rust\" is the work. adding a catch-all _ arm purely to satisfy the compiler without considering whether a new future variant should."
---

# Pattern Matching and Exhaustiveness in Rust

adding a catch-all _ arm.

1. Do not: adding a catch-all _ arm purely to satisfy the compiler without considering whether a.
2. Do not: matching on borrowed data without considering whether the pattern needs ref/deref adjustments, causing ownership-related.

Example:
```rust
enum ConnectionState { Connecting, Connected { session_id: String }, Disconnected { reason: String } }
```

Check: Do not: adding a.
