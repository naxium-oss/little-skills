---
name: debugging-with-set-x-and-shellcheck
description: "Use when \"debugging with set x and shellcheck\" is the work. debugging by adding scattered echo statements instead of set -x, missing the actual expanded command and word-splitting behavior."
---

# Debugging with set -x and Shellcheck

debugging by adding scattered.

1. Do not: debugging by adding scattered echo statements instead of set -x, missing the actual expanded.
2. Do not: ignoring shellcheck warnings as "style only" when many flag genuine correctness bugs.

Example:
```bash
bash -x deploy.sh 2> trace.log
```

Check: Do not: debugging by adding scattered echo statements instead of set -x, missing the actual expanded command and.
