---
name: debug-php
description: "Use when \"php White screen\", \"White screen\". Not when explaining working php code."
---

# Debug php

Reproduce the php failure with the project command, then change one thing.

1. White screen: Enable error display or read the server log; parse errors and uncaught exceptions are.
2. Wrong values from loose types: PHP type juggling (`'1abc' == 1`, null coalescing vs `isset`); use.
3. Composer autoload not finding class: PSR-4 namespace vs directory mismatch; run `composer dump-autoload` after moving files.

Example:
```text
composer test
```

Check: The same command that failed has to pass.
