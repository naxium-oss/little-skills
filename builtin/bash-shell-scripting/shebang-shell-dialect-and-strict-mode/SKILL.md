---
name: shebang-shell-dialect-and-strict-mode
description: "Use when \"shebang shell dialect and strict mode\" is the work. using array syntax (arr=(a b c)) in a #!/bin/sh script that runs under dash in production, causing a."
---

# Shebang, Shell Dialect, and Strict Mode

using array syntax (arr=(a b.

1. Do not: using array syntax (arr=(a b c)) in a #!/bin/sh script that runs under dash.
2. Do not: relying on set -e to catch errors inside if conditions or && chains, where.

Example:
```bash
#!/usr/bin/env bash
```

Check: Do not: using array.
