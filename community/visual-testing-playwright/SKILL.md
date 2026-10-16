---
name: visual-testing-playwright
description: "Use when \"visual test\", \"playwright screenshot\", \"visual testing with playwright\" is the work. Verify what the user actually sees: screenshots prove layout, and DOM assertions prove behavior."
---

# Visual testing with Playwright

Verify what the user actually sees: screenshots prove layout, and DOM assertions prove behavior.

1. Setup.
2. Snapshot strategy.
3. Flake control.

Example:
```ts
import { test, expect } from "@playwright/test";
test("home renders without layout shift", async ({ page }) => {
await page.goto("/");
```

Check: Say not run when the check did not run.
