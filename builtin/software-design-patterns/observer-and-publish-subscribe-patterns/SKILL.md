---
name: observer-and-publish-subscribe-patterns
description: "Use when \"observer and publish subscribe patterns\" is the work. subscribing to an event bus/observable in a component without capturing and calling the returned unsubscribe function on teardown."
---

# Observer and Publish-Subscribe Patterns

subscribing to an event bus/observable.

1. Do not: subscribing to an event bus/observable in a component without capturing and calling the returned.
2. Do not: broadcasting synchronously to observers that themselves mutate the observer list during iteration, causing skipped.

Example:
```bash
map the callers and the concrete types actually constructed
```

Check: Do not: subscribing to an event bus/observable in a component without capturing and calling the returned unsubscribe function.
