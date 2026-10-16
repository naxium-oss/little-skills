---
name: built-in-test-runner-and-module-system
description: "Use when \"built in test runner and module system\" is the work. assuming built-in test runner mocking (t.mock) matches Jest/Sinon APIs."
---

# Built-in Test Runner and Module System

assuming built-in test runner.

1. Do not: assuming built-in test runner mocking (t.mock) matches Jest/Sinon APIs.
2. Do not: running --test against files that don't match the default .test.js glob and getting zero.

Example:
```javascript
import { test } from "node:test";
```

Check: Do not: assuming built-in test.
