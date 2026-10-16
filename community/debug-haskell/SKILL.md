---
name: debug-haskell
description: "Use when \"haskell Type error that makes no sense\", \"Type error that makes no sense\". Not when explaining working haskell code."
---

# Debug haskell

Reproduce the haskell failure with the project command, then change one thing.

1. Type error that makes no sense: Read the constraint the compiler reports and the most specific.
2. Space leak: Lazy accumulation: `foldl` vs `foldl'`; check for unevaluated thunks in strict contexts.
3. head: Partial functions panic at runtime; replace with `case`/`maybe` and handle the empty case.

Example:
```text
cabal test
```

Check: The same command that failed has to pass.
