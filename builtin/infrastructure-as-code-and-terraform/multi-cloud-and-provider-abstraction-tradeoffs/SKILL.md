---
name: multi-cloud-and-provider-abstraction-tradeoffs
description: "Use when \"multi cloud and provider abstraction tradeoffs\" is the work. investing heavily in cloud-agnostic abstractions for a hypothetical future multi-cloud migration that never materializes, paying ongoing complexity cost."
---

# Multi-Cloud and Provider Abstraction Tradeoffs

investing heavily in cloud-agnostic abstractions.

1. Do not: investing heavily in cloud-agnostic abstractions for a hypothetical future multi-cloud migration that never materializes.
2. Do not: building a multi-cloud abstraction that's only ever tested against one actual provider, silently accumulating.

Example:
```hcl
module "compute" {
```

Check: Do not: investing heavily in cloud-agnostic abstractions for a.
