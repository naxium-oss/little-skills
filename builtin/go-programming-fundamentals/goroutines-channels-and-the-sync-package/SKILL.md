---
name: goroutines-channels-and-the-sync-package
description: "Use when \"goroutines channels and the sync package\" is the work. capturing a loop variable incorrectly in a goroutine closure (fixed by-value per iteration since Go 1.22, but still."
---

# Goroutines, Channels, and the sync Package

capturing a loop variable incorrectly.

1. Do not: capturing a loop variable incorrectly in a goroutine closure (fixed by-value per iteration since.
2. Do not: forgetting to close channels or wg.Wait(), leaking goroutines that block forever.

Example:
```go
func fetchAll(urls []string) []string {
```

Check: Do not: capturing a loop variable incorrectly in a.
