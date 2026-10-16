---
name: quoting-and-word-splitting
description: "Use when \"quoting and word splitting\" is the work. iterating for f in $(ls .txt) instead of a glob (for f in .txt), breaking on filenames with."
---

# Quoting and Word Splitting

iterating for f in $(ls.

1. Do not: iterating for f in $(ls .txt) instead of a glob (for f in .txt).
2. Do not: omitting -- and having a filename like -rf misinterpreted as an option.

Example:
```bash
files=("my file.txt" "other.txt")
```

Check: Do not: iterating for f in $(ls .txt) instead.
