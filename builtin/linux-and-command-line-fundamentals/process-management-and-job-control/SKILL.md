---
name: process-management-and-job-control
description: "Use when \"process management and job control\" is the work. using kill -9 (SIGKILL) as a first resort, preventing graceful cleanup (open file handles, DB transactions)."
---

# Process Management and Job Control

using kill -9 (SIGKILL) as a first resort.

1. Do not: using kill -9 (SIGKILL) as a first resort, preventing graceful cleanup (open file handles.
2. Do not: forgetting background jobs die when the parent shell exits unless disown/nohup is used.

Example:
```bash
long_running_task.sh &        # background
```

Check: Do not: using kill -9 (SIGKILL) as a first.
