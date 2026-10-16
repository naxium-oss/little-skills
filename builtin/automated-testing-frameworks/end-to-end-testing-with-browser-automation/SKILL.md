---
name: end-to-end-testing-with-browser-automation
description: "Use when \"end to end testing with browser automation\" is the work."
---

# End-to-End Testing with Browser Automation

using fixed sleep(2000) waits.

1. Do not: using fixed sleep(2000) waits instead of condition-based waiting (waitFor, auto-retrying assertions), causing flaky failures.
2. Do not: selecting elements by brittle CSS class names that change with every styling refactor instead.

Example:
```bash
read the runner config and the test script in the manifest
```

Check: Do not: using fixed.
