---
name: browser-and-rendering-engine-version-verification
description: "Use when \"browser and rendering engine version verification\" is the work. Capture the browser build and engine independently; account for embedded webviews and automated-browser revisions."
---

# Browser and Rendering Engine Version Verification

Capture the browser build and engine independently; account for embedded webviews and automated-browser revisions.

1. Identify the actual executable or service endpoint used by the failing process.
2. Compare shell resolution with the application process.
3. Collect a machine-readable environment manifest.

Example:
```text
Identify the actual executable or service endpoint used by the failing process.
```

Check: Repeat the check in a clean shell and the real execution context; explain every mismatch.
