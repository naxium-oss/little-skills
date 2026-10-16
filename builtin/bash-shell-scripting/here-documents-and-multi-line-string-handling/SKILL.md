---
name: here-documents-and-multi-line-string-handling
description: "Use when \"here documents and multi line string handling\" is the work. expecting <<-EOF to strip leading spaces (it only strips tabs)."
---

# Here-Documents and Multi-Line String Handling

expecting <<-EOF to strip leading spaces (it only strips tabs).

1. Do not: expecting <<-EOF to strip leading spaces (it only strips tabs).
2. Do not: forgetting to quote the delimiter when literal $ or backticks must not be interpreted.

Example:
```bash
cat <<EOF > config.yaml
host: ${DB_HOST}
```

Check: Do not: expecting <<-EOF to strip leading spaces (it only strips tabs).
