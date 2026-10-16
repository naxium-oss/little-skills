---
name: views-materialized-views-and-query-abstraction
description: "Use when \"views materialized views and query abstraction\" is the work. querying a materialized view assuming real-time freshness when its last refresh was hours ago."
---

# Views, Materialized Views, and Query Abstraction

querying a materialized view assuming real-time freshness.

1. Do not: querying a materialized view assuming real-time freshness when its last refresh was hours ago.
2. Do not: adding an unindexed materialized view refreshed non-concurrently, causing readers to be blocked during refresh.

Example:
```sql
CREATE MATERIALIZED VIEW daily_sales AS
```

Check: Do not: querying a materialized view assuming real-time freshness when its last refresh was hours ago.
