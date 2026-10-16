---
name: bash-command-substitution-semantics
description: "Use when \"bash command substitution semantics\" is the work. Command substitution strips trailing newlines and runs in a subshell environment."
---

# Bash Command Substitution Semantics

Command substitution strips trailing newlines and runs in a subshell environment.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```bash
value=$(printf "a\n\n")
[[ $value == a ]]
printf "<%s>\n" "$value"
```

Check: Do not edit the assert to match a surprising result.
