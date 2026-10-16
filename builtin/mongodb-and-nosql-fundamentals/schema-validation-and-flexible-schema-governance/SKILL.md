---
name: schema-validation-and-flexible-schema-governance
description: "Use when \"schema validation and flexible schema governance\" is the work. assuming schema-less means no governance is needed, leading to years of inconsistent document shapes that break downstream code."
---

# Schema Validation and Flexible Schema Governance

assuming schema-less means no.

1. Do not: assuming schema-less means no governance is needed, leading to years of inconsistent document shapes.
2. Do not: setting validation to "moderate" and assuming it retroactively fixes historical documents, when it does.

Example:
```javascript
db.createCollection("orders", {
```

Check: Do not: assuming schema-less means no governance is needed.
