---
name: context-propagation-for-cancellation-and-deadlines
description: "Use when \"context propagation for cancellation and deadlines\" is the work. creating a derived context with WithTimeout/WithCancel and forgetting to call the returned cancel function, leaking the associated timer/goroutine."
---

# Context Propagation for Cancellation and Deadlines

creating a derived context.

1. Do not: creating a derived context with WithTimeout/WithCancel and forgetting to call the returned cancel function.
2. Do not: passing context.Background() deep into a call chain instead of the actual request-scoped context, silently.

Example:
```go
func fetchWithTimeout(ctx context.Context, url string) ([]byte, error) {
```

Check: Do not: creating a.
