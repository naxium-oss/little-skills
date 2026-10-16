---
name: pipeline-stage-design-and-fail-fast-ordering
description: "Use when \"pipeline stage design and fail fast ordering\" is the work. running a slow integration/E2E suite before a fast lint/unit stage, wasting compute and developer wait time on failures."
---

# Pipeline Stage Design and Fail-Fast Ordering

running a slow integration/E2E suite.

1. Do not: running a slow integration/E2E suite before a fast lint/unit stage, wasting compute and developer.
2. Do not: assuming stage order in a YAML file guarantees execution order without checking actual dependency.

Example:
```bash
read the workflow triggers, permissions, and runner labels
```

Check: Do not: running a.
