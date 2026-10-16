---
name: debug-shell
description: "Use when \"shell Exit code lost\", \"Exit code lost\". Not when explaining working shell code."
---

# Debug shell

Reproduce the shell failure with the project command, then change one thing.

1. Exit code lost: `$?` is consumed by the next command; capture it immediately, and `set -e`.
2. Quoting bugs: Unquoted variables split on IFS and glob-expand; quote `"$var"` and `"$@"`, check paths with.
3. Variable set in a subshell lost: Pipelines and `( ... )` run in subshells; changes don't.

Example:
```text
bash -x script.sh
```

Check: The same command that failed has to pass.
