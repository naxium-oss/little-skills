---
name: data-validation-and-schema-enforcement-in-pipelines
description: "Use when \"data validation and schema enforcement in pipelines\" is the work. validating schema once during initial development and never re-running it as part of the ongoing production pipeline, missing."
---

# Data Validation and Schema Enforcement in

validating schema once during initial.

1. Do not: validating schema once during initial development and never re-running it as part of the.
2. Do not: catching schema validation errors and logging them without halting the pipeline, allowing corrupted data.

Example:
```bash
print df.dtypes, df.shape, and df.head() before transforming
```

Check: Do not: validating schema once during initial development and.
