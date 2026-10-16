---
name: traits-generics-and-zero-cost-abstraction
description: "Use when \"traits generics and zero cost abstraction\" is the work. defaulting to dyn Trait everywhere out of unfamiliarity with generics, paying unnecessary vtable dispatch overhead in hot paths."
---

# Traits, Generics, and Zero-Cost Abstraction

defaulting to dyn Trait everywhere out of unfamiliarity with.

1. Do not: defaulting to dyn Trait everywhere out of unfamiliarity with generics, paying unnecessary vtable dispatch.
2. Do not: over-using generics in ways that cause combinatorial monomorphization bloat and slow compile times.

Example:
```rust
trait Shape {
```

Check: Do not: defaulting to dyn Trait everywhere out of unfamiliarity with generics, paying unnecessary vtable dispatch overhead in.
