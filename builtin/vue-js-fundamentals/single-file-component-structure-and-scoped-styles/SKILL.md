---
name: single-file-component-structure-and-scoped-styles
description: "Use when \"single file component structure and scoped styles\" is the work. expecting a scoped style to affect a child components internal markup without :deep(), silently having no effect."
---

# Single-File Component Structure and Scoped Styles

expecting a scoped style to affect a child.

1. Do not: expecting a scoped style to affect a child component's internal markup without :deep(), silently.
2. Do not: relying on global <style> blocks for component-specific styling, reintroducing the leakage scoped styles were.

Example:
```vue
<template><button class="btn">Save</button></template>
```

Check: Do not: expecting a.
