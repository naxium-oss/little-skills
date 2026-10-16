---
name: bash-pattern-matching-globbing
description: "Use when \"bash pattern matching globbing\" is the work. Globs expand against filenames and can remain literal when no match exists."
---

# Bash Pattern Matching & Globbing

Globs expand against filenames and can remain literal when no match exists.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```bash
shopt -s nullglob
files=(./*.unlikely_extension)
printf "matches: %s\n" "${#files[@]}"
```

Check: Do not edit the assert to match a surprising result.
