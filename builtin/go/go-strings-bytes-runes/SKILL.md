---
name: go-strings-bytes-runes
description: "Use when \"go strings bytes runes\" is the work. len(string) counts bytes."
---

# Go Strings, Bytes & Runes

len(string) counts bytes.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```go
text := "éa"
fmt.Println(len(text)) // 3
fmt.Println(len([]rune(text))) // 2
```

Check: Do not edit the assert to match a surprising result.
