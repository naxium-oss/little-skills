---
name: bash-functions-local-variables
description: "Use when \"bash functions local variables\" is the work. Bash functions share the shell environment unless variables are local."
---

# Bash Functions & Local Variables

Bash functions share the shell environment unless variables are local.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```bash
value="global"
helper() { local value="local"; printf "%s\n" "$value"; }
helper # local
```

Check: Do not edit the assert to match a surprising result.
