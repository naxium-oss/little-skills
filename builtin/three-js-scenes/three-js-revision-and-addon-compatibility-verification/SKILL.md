---
name: three-js-revision-and-addon-compatibility-verification
description: "Use when \"three js revision and addon compatibility verification\" is the work. Ensure core and addon imports come from compatible revisions and inspect migration notes."
---

# Three.js Revision and Addon Compatibility Verification

Ensure core and addon imports come from compatible revisions and inspect migration notes.

1. Pin the Three.js revision and matching addons.
2. Validate coordinate spaces, asset units, color pipeline, and renderer capabilities.

Example:
```text
Pin the Three.js revision and matching addons.
```

Check: Test asset-load failures, resize, context loss, frustum behavior, GPU limits, and repeated mount/unmount memory use.
