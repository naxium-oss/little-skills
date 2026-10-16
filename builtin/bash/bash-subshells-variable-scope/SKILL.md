---
name: bash-subshells-variable-scope
description: "Use when \"bash subshells variable scope\" is the work. Parentheses create a subshell environment; braces execute in the current shell."
---

# Bash Subshells & Variable Scope

Parentheses create a subshell environment; braces execute in the current shell.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```bash
value=1
( value=2 )
[[ $value == 1 ]]
```

Check: Do not edit the assert to match a surprising result.
