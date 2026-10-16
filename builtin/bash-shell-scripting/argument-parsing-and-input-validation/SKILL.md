---
name: argument-parsing-and-input-validation
description: "Use when \"argument parsing and input validation\" is the work. assuming getopts supports --long-options natively."
---

# Argument Parsing and Input Validation

assuming getopts supports --long-options natively.

1. Do not: assuming getopts supports --long-options natively.
2. Do not: forgetting shift in manual arg-parsing loops, causing infinite loops or misread arguments.

Example:
```bash
#!/usr/bin/env bash
set -euo pipefail
usage() { echo "Usage: $0 -e <env> [-d]" >&2; exit 1; }
```

Check: Do not: assuming getopts supports --long-options natively.
