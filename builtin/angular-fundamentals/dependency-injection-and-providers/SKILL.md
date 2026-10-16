---
name: dependency-injection-and-providers
description: "Use when \"dependency injection and providers\" is the work. re-providing a service meant to be a singleton at the component level, creating unintended separate instances with disconnected."
---

# Dependency Injection and Providers

re-providing a service meant to be a singleton at.

1. Do not: re-providing a service meant to be a singleton at the component level, creating unintended.
2. Do not: injecting via constructor parameter without the @Injectable decorator on the target class, causing a.

Example:
```typescript
@Injectable({ providedIn: "root" })
```

Check: Do not: re-providing a service meant to be a singleton at the component level, creating unintended separate instances.
