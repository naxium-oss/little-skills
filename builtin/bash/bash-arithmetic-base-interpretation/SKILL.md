---
name: bash-arithmetic-base-interpretation
description: "Use when \"bash arithmetic base interpretation\" is the work. Leading zeroes can request octal interpretation."
---

# Bash Arithmetic & Base Interpretation

Leading zeroes can request octal interpretation.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```bash
text="08"
[[ $text =~ ^[0-9]+$ ]] || exit 1
value=$((10#$text))
```

Check: Do not edit the assert to match a surprising result.
