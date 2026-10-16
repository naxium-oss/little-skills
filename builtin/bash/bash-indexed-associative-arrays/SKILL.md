---
name: bash-indexed-associative-arrays
description: "Use when \"bash indexed associative arrays\" is the work. Quoted array expansion preserves each element."
---

# Bash Indexed & Associative Arrays

Quoted array expansion preserves each element.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```bash
values=("hello world" "" "third")
printf "<%s>\n" "${values[@]}"
declare -A counts=([apple]=2 [pear]=3)
```

Check: Do not edit the assert to match a surprising result.
