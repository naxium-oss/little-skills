---
name: toolchain-edition-and-crate-version-grounding
description: "Use when \"toolchain edition and crate version grounding\" is the work. assuming a nightly-only feature (behind a #![feature(...)] flag) is available on stable Rust."
---

# Toolchain, Edition, and Crate Version Grounding

assuming a nightly-only feature (behind a.

1. Do not: assuming a nightly-only feature (behind a #![feature(...)] flag) is available on stable Rust.
2. Do not: using edition-2021 idioms in a crate still declared as edition 2018 without updating Cargo.toml.

Example:
```bash
cargo check
```

Check: Do not: assuming a nightly-only feature (behind.
