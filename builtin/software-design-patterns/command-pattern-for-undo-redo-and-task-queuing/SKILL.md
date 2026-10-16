---
name: command-pattern-for-undo-redo-and-task-queuing
description: "Use when \"command pattern for undo redo and task queuing\" is the work. implementing undo() based on assumed inverse logic that doesnt account for state changes made by other commands in."
---

# Command Pattern for Undo/Redo and Task

implementing undo() based on assumed.

1. Do not: implementing undo() based on assumed inverse logic that doesn't account for state changes made.
2. Do not: storing commands with references to mutable external state that changes independently of the command.

Example:
```bash
map the callers and the concrete types actually constructed
```

Check: Do not: implementing undo() based on assumed inverse logic.
