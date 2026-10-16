---
name: document-structure-and-parsing-verification
description: "Use when \"document structure and parsing verification\" is the work. omitting <!doctype html>, triggering quirks mode with different box-model/layout behavior."
---

# Document Structure and Parsing Verification

omitting <!doctype html>, triggering quirks mode with different box-model/layout behavior.

1. Do not: omitting <!doctype html>, triggering quirks mode with different box-model/layout behavior.
2. Do not: assuming invalid nesting (block inside inline) renders as authored across all browsers.

Example:
```html
<!doctype html>
<html lang="en">
```

Check: Do not: omitting <!doctype html>, triggering quirks mode with different box-model/layout behavior.
