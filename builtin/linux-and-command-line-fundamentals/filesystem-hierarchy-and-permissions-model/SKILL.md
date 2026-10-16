---
name: filesystem-hierarchy-and-permissions-model
description: "Use when \"filesystem hierarchy and permissions model\" is the work. using chmod 777 as a quick fix instead of diagnosing the real ownership/group issue."
---

# Filesystem Hierarchy and Permissions Model

using chmod 777 as a quick fix.

1. Do not: using chmod 777 as a quick fix instead of diagnosing the real ownership/group issue.
2. Do not: forgetting a directory needs execute (x) permission to be traversed even if files inside.

Example:
```bash
ls -l file.sh                      # -rwxr-xr-- 1 user group ...
```

Check: Do not: using chmod 777 as a quick fix instead of diagnosing the real ownership/group issue.
