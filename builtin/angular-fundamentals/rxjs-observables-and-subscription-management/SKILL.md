---
name: rxjs-observables-and-subscription-management
description: "Use when \"rxjs observables and subscription management\" is the work. subscribing manually in ngOnInit without any teardown logic, leaking subscriptions on every component destroy/recreate cycle."
---

# RxJS Observables and Subscription Management

subscribing manually in ngOnInit without any teardown.

1. Do not: subscribing manually in ngOnInit without any teardown logic, leaking subscriptions on every component destroy/recreate.
2. Do not: nesting subscriptions (subscribe inside subscribe) instead of composing with operators like switchMap, causing race.

Example:
```typescript
export class UserListComponent implements OnDestroy {
```

Check: Do not: subscribing manually in ngOnInit without any teardown logic, leaking subscriptions on every component destroy/recreate cycle.
