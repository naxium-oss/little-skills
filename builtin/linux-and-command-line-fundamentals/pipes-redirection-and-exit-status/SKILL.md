---
name: pipes-redirection-and-exit-status
description: "Use when \"pipes redirection and exit status\" is the work. forgetting set -o pipefail in scripts, masking a failing grep/curl upstream of a successful wc -l."
---

# Pipes, Redirection, and Exit Status

forgetting set -o pipefail in scripts, masking a.

1. Do not: forgetting set -o pipefail in scripts, masking a failing grep/curl upstream of a successful.
2. Do not: redirecting 2>&1 in the wrong order, which merges streams incorrectly if placed before the.

Example:
```bash
grep -c "ERROR" app.log > error_count.txt 2> grep_errors.log
```

Check: Do not: forgetting set.
