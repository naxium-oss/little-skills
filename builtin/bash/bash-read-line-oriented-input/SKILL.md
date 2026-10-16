---
name: bash-read-line-oriented-input
description: "Use when \"bash read line oriented input\" is the work. Use IFS= and read -r for literal lines."
---

# Bash read & Line-Oriented Input

Use IFS= and read -r for literal lines.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```bash
while IFS= read -r line || [[ -n $line ]]; do
printf "<%s>\n" "$line"
done < fixture.txt
```

Check: Do not edit the assert to match a surprising result.
