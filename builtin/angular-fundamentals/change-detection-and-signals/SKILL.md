---
name: change-detection-and-signals
description: "Use when \"change detection and signals\" is the work. mutating an @Input() object in place under OnPush, expecting a re-render since the object changed, reference equality is."
---

# Change Detection and Signals

mutating an @Input() object in.

1. Do not: mutating an @Input() object in place under OnPush, expecting a re-render since the object.
2. Do not: mixing signals and Zone.js-triggered detection without understanding which schedules the actual re-render.

Example:
```typescript
@Component({ changeDetection: ChangeDetectionStrategy.OnPush })
```

Check: Do not: mutating an @Input() object in place under.
