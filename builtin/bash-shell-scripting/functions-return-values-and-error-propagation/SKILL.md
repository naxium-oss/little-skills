---
name: functions-return-values-and-error-propagation
description: "Use when \"functions return values and error propagation\" is the work. forgetting local, causing a functions temp variable to clobber a global one used elsewhere."
---

# Functions, Return Values, and Error Propagation

forgetting local, causing a function's temp variable to clobber a global one used elsewhere.

1. Do not: forgetting local, causing a function's temp variable to clobber a global one used elsewhere.
2. Do not: assuming a non-empty stdout implies success without checking $?.

Example:
```bash
fetch_status() {
local url="$1"
local code
```

Check: Do not: forgetting local, causing a function's temp variable to clobber a global one used elsewhere.
