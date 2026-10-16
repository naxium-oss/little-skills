---
name: component-communication-props-emits-and-provide-inject
description: "Use when \"component communication props emits and provide inject\" is the work. mutating a prop directly inside a child component, violating one-way data flow and producing a runtime warning."
---

# Component Communication: Props, Emits, and Provide/Inject

mutating a prop directly inside a child component.

1. Do not: mutating a prop directly inside a child component, violating one-way data flow and producing.
2. Do not: overusing provide/inject for data that would be clearer as explicit props.

Example:
```vue
<script setup>
```

Check: Do not: mutating a prop directly inside a child.
