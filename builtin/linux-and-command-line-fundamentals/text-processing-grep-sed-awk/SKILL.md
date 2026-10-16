---
name: text-processing-grep-sed-awk
description: "Use when \"text processing grep sed awk\" is the work. using basic regex grep syntax and expecting +/?"
---

# Text Processing: grep, sed, awk

using basic regex grep syntax and expecting +/?

1. Do not: using basic regex grep syntax and expecting +/? to work without -E.
2. Do not: assuming sed -i behaves identically on macOS (BSD sed requires an explicit backup suffix.

Example:
```bash
grep -E "ERROR|WARN" app.log | awk -F'|' '{print $1, $3}'
```

Check: Do not: using basic regex grep syntax and expecting +/?
