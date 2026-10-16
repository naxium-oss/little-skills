---
name: bash-parameter-expansion-patterns
description: "Use when \"bash parameter expansion patterns\" is the work. Distinguish unset variables from empty values when choosing default operators."
---

# Bash Parameter Expansion Patterns

Distinguish unset variables from empty values when choosing default operators.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```bash
path="archive/report.csv"
printf "%s\n" "${path##*/}" # report.csv
printf "%s\n" "${path%.*}" # archive/report
```

Check: Do not edit the assert to match a surprising result.
