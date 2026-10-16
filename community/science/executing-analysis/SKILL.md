---
name: executing-analysis
description: "Use when \"run the analysis\", \"execute the plan\" is the work. Run the frozen plan in order, one step at a time, and let each steps output decide whether."
---

# Execute the plan

Run the frozen plan in order, one step at a time, and let each step's output decide whether the next one runs.

1. Work the todo_write rows in order.
2. Before each run, print the shape of the input: rows, columns, dtypes, missing counts, and the.

Example:
```text
Work the todo_write rows in order.
```

Check: A quality gate fails (implausible values, a shifted distribution, a join that changes the row count): stop and.
