---
name: lambda-execution-model-cold-starts-and-concurrency-limits
description: "Use when \"lambda execution model cold starts and concurrency limits\" is the work."
---

# Lambda Execution Model, Cold Starts, and

placing initialization-heavy code (large SDK.

1. Do not: placing initialization-heavy code (large SDK client setup, model loading) inside the handler instead of.
2. Do not: not setting reserved concurrency limits, allowing one runaway function to consume the account's entire.

Example:
```bash
aws lambda get-function-configuration --function-name my-function --query "{Runtime:Runtime,MemorySize:MemorySize,Timeout:Timeout}"
```

Check: Do not: placing initialization-heavy.
