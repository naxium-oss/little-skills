---
name: go-version-modules-and-toolchain-grounding
description: "Use when \"go version modules and toolchain grounding\" is the work. assuming generics syntax works on a go.mod declaring go 1.16."
---

# Go Version, Modules, and Toolchain Grounding

assuming generics syntax works on a go.mod declaring go 1.16.

1. Do not: assuming generics syntax works on a go.mod declaring go 1.16.
2. Do not: ignoring go mod tidy drift, where go.mod lists dependencies no longer imported or missing.

Example:
```bash
go build ./...
go test -race ./...
```

Check: Do not: assuming generics syntax works on a go.mod declaring go 1.16.
