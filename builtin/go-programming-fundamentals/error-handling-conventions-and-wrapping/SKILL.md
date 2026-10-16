---
name: error-handling-conventions-and-wrapping
description: "Use when \"error handling conventions and wrapping\" is the work. discarding an error with _ out of convenience, silently swallowing failures."
---

# Error Handling Conventions and Wrapping

discarding an error with _ out of convenience, silently swallowing failures.

1. Do not: discarding an error with _ out of convenience, silently swallowing failures.
2. Do not: comparing wrapped errors with == instead of errors.Is, missing matches because wrapping changes the.

Example:
```go
func loadUser(id string) (*User, error) {
row, err := db.QueryRow("SELECT ...", id)
```

Check: Do not: discarding an error with _ out of convenience, silently swallowing failures.
