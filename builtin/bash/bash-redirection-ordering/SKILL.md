---
name: bash-redirection-ordering
description: "Use when \"bash redirection ordering\" is the work. Descriptor duplication copies the descriptor’s current destination."
---

# Bash Redirection Ordering

Descriptor duplication copies the descriptor’s current destination.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```bash
{ printf "out\n"; printf "err\n" >&2; } >combined.txt 2>&1
{ printf "out\n"; printf "err\n" >&2; } 2>&1 >stdout.txt
```

Check: Do not edit the assert to match a surprising result.
