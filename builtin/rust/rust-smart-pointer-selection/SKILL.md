---
name: rust-smart-pointer-selection
description: "Use when \"rust smart pointer selection\" is the work. Box gives heap ownership; Rc shares ownership within a thread; Arc shares ownership across threads when contained types."
---

# Rust Smart Pointer Selection

Box gives heap ownership; Rc shares ownership within a thread; Arc shares ownership across threads when contained types permit it.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```rust
use std::rc::Rc;
let original = Rc::new(String::from("shared"));
```

Check: Do not edit the assert to match a surprising result.
