---
name: debug-elixir
description: "Use when \"elixir GenServer crash\", \"GenServer crash\". Not when explaining working elixir code."
---

# Debug elixir

Reproduce the elixir failure with the project command, then change one thing.

1. GenServer crash: The crash report shows the failing call and stack; check state shape and message.
2. PatternMatchError in pipes: The pipe result doesn't match the next clause; log the intermediate value (`|>.
3. N+1 in Ecto: Check query preloads and the SQL log; `Repo.preload` or a join avoids per-row.

Example:
```text
mix test
```

Check: The same command that failed has to pass.
