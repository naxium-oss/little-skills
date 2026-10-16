---
name: smart-pointers-box-rc-arc-and-refcell
description: "Use when \"smart pointers box rc arc and refcell\" is the work."
---

# Smart Pointers: Box, Rc, Arc, and

using Rc<RefCell<T>> reflexively for.

1. Do not: using Rc<RefCell<T>> reflexively for shared mutable state without considering whether ownership could instead be.
2. Do not: forgetting RefCell::borrow_mut() panics (not compile-errors) on an already-active borrow, turning a class of bugs.

Example:
```rust
use std::sync::{Arc, Mutex};
```

Check: Do not: using Rc<RefCell<T>>.
