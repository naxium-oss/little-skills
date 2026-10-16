# Next.js Fundamentals

## Version, Router, and Rendering Mode Grounding
Next.js 13+ introduced the App Router (React Server Components, `app/` directory) alongside the legacy Pages Router (`pages/`); behavior around data fetching, caching, and layouts differs fundamentally between them. Verify which router a project uses and the exact Next.js version before applying any guidance.
```bash
npm ls next                        # next@15.1.2
cat next.config.js | head -5
ls app 2>/dev/null || ls pages 2>/dev/null
```
**Pitfalls:** applying App Router `fetch` caching guidance to a Pages Router project using `getServerSideProps`; assuming a Next.js 12 tutorial's `getStaticProps` incremental revalidation numbers still match a 14+ App Router `revalidate` config.

## Server Components, Client Components, and the Boundary
In the App Router, components are Server Components by default (render on the server, zero client JS, cannot use hooks/browser APIs); adding `"use client"` opts a subtree into client-side interactivity. Verify which side a component actually renders on rather than assuming from its file location alone.
```tsx
// app/dashboard/page.tsx: Server Component by default
import { UserChart } from "./user-chart";

export default async function DashboardPage() {
  const data = await fetch("https://api.example.com/stats", { cache: "no-store" }).then((r) => r.json());
  return <UserChart data={data} />;
}
```
```tsx
"use client";
export function UserChart({ data }: { data: Stat[] }) { /* useState, chart lib, etc. */ }
```
Confirm props passed from Server to Client components are serializable (no functions, class instances, or Dates without conversion), since the boundary crosses a network-like serialization layer.
**Pitfalls:** adding `"use client"` to an entire page just because one leaf component needs interactivity, ballooning client bundle size unnecessarily; passing non-serializable props (functions, Symbols) across the server/client boundary and hitting a cryptic runtime error.

## Data Fetching, Caching, and Revalidation
The App Router extends `fetch` with caching semantics (`force-cache` default, `no-store`, `next: { revalidate: N }`, `next: { tags: [...] }`); verify the actual cache behavior with response headers and repeated requests rather than assuming from the code alone, since Next.js caching layers (Data Cache, Full Route Cache) changed across versions (notably v15 defaults).
```tsx
const res = await fetch(`${API}/products/${id}`, {
  next: { revalidate: 60, tags: [`product-${id}`] },
});
```
```tsx
import { revalidateTag } from "next/cache";
export async function POST() {
  await updateProduct();
  revalidateTag(`product-${id}`);
  return Response.json({ ok: true });
}
```
Verify the currently installed major version's default caching behavior explicitly (Next 15 made `fetch` uncached by default, a reversal from Next 14), since assuming the wrong default silently serves stale or unexpectedly fresh data.
**Pitfalls:** assuming Next 14 caching defaults apply unchanged to a Next 15 project; forgetting to call `revalidateTag`/`revalidatePath` after a mutation, serving stale cached data indefinitely.

## Route Handlers, Middleware, and Edge Runtime
Route Handlers (`app/api/*/route.ts`) replace the Pages Router's `pages/api`; Middleware runs before a request completes and can run in the Edge runtime with a restricted API surface (no native Node APIs like `fs`). Verify which runtime a given file targets before using Node-specific modules.
```typescript
// app/api/users/route.ts
export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const page = Number(searchParams.get("page") ?? "1");
  return Response.json({ page, users: await fetchUsers(page) });
}
```
```typescript
export const config = { matcher: "/dashboard/:path*" };
export function middleware(request: NextRequest) {
  if (!request.cookies.get("session")) {
    return NextResponse.redirect(new URL("/login", request.url));
  }
}
```
Confirm `export const runtime = "nodejs" | "edge"` matches the actual APIs used in a route handler, since importing an unsupported Node builtin under the Edge runtime fails at build or request time.
**Pitfalls:** using `fs`, `crypto` (Node variant), or large native dependencies inside Edge middleware and hitting a build error; assuming middleware runs after route handlers rather than before, missing its actual request-interception order.

# SQL & Relational Database Fundamentals

## Engine and Dialect Version Grounding
SQL is not one language, window function support, `RETURNING`, upsert syntax (`ON CONFLICT` vs `ON DUPLICATE KEY`), and JSON functions differ by engine and version. Verify the exact database product and version before writing or debugging a query.
```sql
SELECT version();                          -- PostgreSQL
SELECT @@version;                          -- MySQL/SQL Server variants differ
```
Confirm which SQL standard features (CTEs, `LATERAL`, `MERGE`) are supported in the specific version pinned in production, since even the same engine gains/removes syntax across major releases.
**Pitfalls:** writing PostgreSQL-specific syntax (`ILIKE`, `RETURNING`) against a MySQL connection and getting a syntax error; assuming a feature available in the latest docs is present in an older pinned production version.

## Joins and Cardinality Reasoning
`INNER JOIN` returns only matching rows, `LEFT JOIN` preserves unmatched left-side rows with NULLs on the right, and a join that fans out on a one-to-many relationship silently multiplies rows in subsequent aggregations. Verify actual row counts before and after a join rather than assuming cardinality.
```sql
SELECT o.id, o.total, COUNT(oi.id) AS item_count
FROM orders o
LEFT JOIN order_items oi ON oi.order_id = o.id
GROUP BY o.id, o.total;
```
Check for accidental row duplication by comparing `COUNT(*)` before and after adding a join, especially before computing `SUM`/`AVG` on a joined table, which silently double-counts.
**Pitfalls:** joining to a one-to-many table and then summing a column from the "one" side, inflating totals by the fan-out factor; using `INNER JOIN` where `LEFT JOIN` was intended, silently dropping rows with no match.

## NULL Semantics and Three-Valued Logic
SQL uses three-valued logic (`TRUE`, `FALSE`, `UNKNOWN`); any comparison with `NULL` (including `NULL = NULL`) evaluates to `UNKNOWN`, which is filtered out by `WHERE`/`JOIN` conditions. Verify NULL-handling explicitly with `IS NULL`/`IS NOT NULL` or `COALESCE` rather than `=`/`!=`.
```sql
SELECT * FROM users WHERE deleted_at IS NULL;         -- correct
SELECT * FROM users WHERE deleted_at != '2024-01-01'; -- silently excludes NULL deleted_at rows too
SELECT COALESCE(nickname, first_name) AS display_name FROM users;
```
Confirm aggregate functions' NULL behavior (`COUNT(*)` counts all rows, `COUNT(col)` skips NULLs, `AVG` ignores NULLs rather than treating them as zero) by testing with a small NULL-containing dataset.
**Pitfalls:** using `NOT IN (SELECT ...)` against a subquery that can return NULL, causing the entire `NOT IN` to evaluate to no rows unexpectedly; assuming `AVG` treats NULL as 0 instead of excluding it from the divisor.

## Transactions and Isolation Levels
Transactions group statements atomically (`BEGIN`/`COMMIT`/`ROLLBACK`); isolation levels (`READ COMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`) trade consistency guarantees for concurrency, and the *default* isolation level differs by engine (PostgreSQL defaults to `READ COMMITTED`, unlike some other systems). Verify the active isolation level rather than assuming.
```sql
BEGIN;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;   -- row lock to prevent lost update
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```
```sql
SHOW TRANSACTION ISOLATION LEVEL;   -- verify, don't assume, on the actual connection
```
Reproduce suspected anomalies (dirty read, non-repeatable read, phantom read) with two concurrent sessions in a test environment before concluding an isolation level is the cause of a bug.
**Pitfalls:** assuming `SERIALIZABLE` prevents all race conditions without handling serialization-failure retries; forgetting `FOR UPDATE` row locking when implementing a read-then-write balance update, causing lost-update races.

# Next.js Fundamentals

## Static Generation, ISR, and Dynamic Rendering Selection
Next.js can render pages fully statically at build time, incrementally revalidate them (ISR) on a timer or on-demand, or render dynamically per request; verify which mode a given route actually uses by checking the build output summary (`○ Static`, `● SSG`, `λ Dynamic`) rather than assuming from the code alone, since a single dynamic API call (like reading cookies) can silently force an entire route to dynamic rendering.
```bash
npm run build
# Route (app)                    Size     First Load JS
# ○ /                            5 kB     92 kB
# λ /dashboard                   3 kB     90 kB   <- forced dynamic
```
Verify the actual reason a route became dynamic (reading `cookies()`, `headers()`, or an uncached `fetch`) by checking the build's route segment config, since an accidental dynamic API call in a shared layout can force many otherwise-static pages dynamic.
**Pitfalls:** assuming a page is statically generated because no obvious dynamic code is visible, missing that a shared layout or imported utility calls `cookies()`/`headers()`; setting an aggressive ISR `revalidate` interval without confirming the underlying data source's actual update frequency.

## Image and Font Optimization Components
`next/image` and `next/font` provide automatic optimization (responsive sizing, lazy loading, format conversion for images; self-hosted, layout-shift-free loading for fonts) but require correct configuration (`remotePatterns` for external image domains, explicit `width`/`height` or `fill`) to work as intended. Verify actual served image formats/sizes in the Network tab rather than assuming optimization is automatically comprehensive for every source.
```tsx
import Image from "next/image";
<Image src="/hero.jpg" alt="Product hero" width={1200} height={630} priority />
```
```javascript
// next.config.js
module.exports = { images: { remotePatterns: [{ protocol: "https", hostname: "cdn.example.com" }] } };
```
Verify `priority` is set only on true above-the-fold LCP images, since overusing it defeats lazy-loading benefits for images further down the page.
**Pitfalls:** forgetting to add an external image domain to `remotePatterns`, causing a build/runtime error when using `next/image` with that source; marking every image `priority`, eliminating the lazy-loading performance benefit entirely.

## Metadata API and Dynamic SEO Tags
The App Router's Metadata API (`export const metadata` or `generateMetadata`) replaces manually managing `<head>` tags, supporting both static and dynamically computed (per-route-param) metadata; verify dynamically generated metadata actually resolves correctly by inspecting rendered page source, not just the function's return value in isolation, since streaming and caching can affect when metadata is actually attached.
```tsx
export async function generateMetadata({ params }): Promise<Metadata> {
  const product = await getProduct(params.id);
  return { title: product.name, description: product.description, openGraph: { images: [product.image] } };
}
```
Confirm metadata inheritance/override behavior between nested layouts and pages matches intent by checking the final rendered `<head>`, since child route metadata merges with (and can override) parent layout metadata in specific, version-dependent ways.
**Pitfalls:** assuming `generateMetadata` runs independently of the page's own data fetching, duplicating an expensive fetch call instead of leveraging Next.js's automatic request memoization; not verifying final merged metadata in nested layouts, shipping incomplete or unexpectedly overridden SEO tags.

## Environment Variables and Client/Server Exposure Boundaries
Next.js only exposes environment variables prefixed `NEXT_PUBLIC_` to client-side bundles; all others remain server-only, and this distinction is enforced at build time by string replacement, not runtime filtering. Verify no secret accidentally uses the `NEXT_PUBLIC_` prefix, and confirm server-only variables are actually unavailable client-side by inspecting the built client bundle.
```bash
# .env.local
DATABASE_URL=postgres://...          # server-only, never bundled to the client
NEXT_PUBLIC_API_BASE_URL=https://api.example.com   # bundled into client JS, publicly visible
```
Grep the production client bundle for a secret's literal value to confirm it wasn't accidentally inlined, rather than trusting the naming convention alone during a code review.
**Pitfalls:** prefixing a secret (API key, DB credential) with `NEXT_PUBLIC_` out of habit or copy-paste, baking it into the publicly downloadable client bundle; assuming a non-prefixed variable is safe to reference in client component code, when it will simply be `undefined` at runtime rather than erroring loudly.

# SQL & Relational Database Fundamentals

## Normalization and Denormalization Tradeoffs
Normalization (organizing data to eliminate redundancy via 1NF/2NF/3NF) reduces update anomalies but increases the number of joins needed for reads; denormalization trades some redundancy for read performance. Verify the actual read/write ratio and query patterns of the specific workload before choosing a normalization level, rather than applying a fixed rule universally.
```sql
-- Normalized: avoids storing customer name redundantly on every order
CREATE TABLE customers (id SERIAL PRIMARY KEY, name TEXT);
CREATE TABLE orders (id SERIAL PRIMARY KEY, customer_id INT REFERENCES customers(id), total NUMERIC);

-- Denormalized: duplicates customer_name for read-heavy reporting, avoiding a join
CREATE TABLE order_reports (order_id INT, customer_name TEXT, total NUMERIC);
```
Verify denormalized copies have a defined synchronization strategy (triggers, application-level writes, or periodic ETL) and confirm staleness tolerance matches business requirements before introducing them.
**Pitfalls:** over-normalizing a read-heavy analytics workload, forcing expensive multi-way joins on every dashboard query; denormalizing without a clear update strategy, letting duplicated data silently drift out of sync.

## Constraints and Referential Integrity
Primary keys, foreign keys, unique constraints, and check constraints enforce data validity at the database level, catching bugs that application-level validation alone would miss (e.g., a race condition between two application instances); verify constraints actually exist in the schema (not just assumed from application code) with a direct schema inspection.
```sql
ALTER TABLE orders ADD CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers(id);
ALTER TABLE orders ADD CONSTRAINT chk_positive_total CHECK (total >= 0);
\d+ orders    -- psql: inspect actual constraints on the table
```
Verify the specific `ON DELETE`/`ON UPDATE` behavior (`CASCADE`, `RESTRICT`, `SET NULL`) matches business intent before applying a foreign key, since the default varies by engine and an unexpected cascade delete can silently remove far more data than intended.
**Pitfalls:** relying solely on application-level validation for uniqueness/referential integrity, allowing a race condition to insert duplicate or orphaned rows; adding a foreign key with `ON DELETE CASCADE` without realizing it will silently delete large amounts of dependent data.

## Common Table Expressions and Recursive Queries
CTEs (`WITH` clauses) improve query readability by naming intermediate result sets, and recursive CTEs traverse hierarchical/graph-like data (org charts, category trees) that a single flat query cannot express; verify a recursive CTE terminates correctly by testing against data containing cycles, which without a cycle guard causes infinite recursion.
```sql
WITH RECURSIVE org_chart AS (
  SELECT id, name, manager_id, 1 AS depth FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id, oc.depth + 1
  FROM employees e JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT * FROM org_chart ORDER BY depth;
```
Verify a maximum recursion depth or cycle-detection column is included for data that could contain a cycle (a manager accidentally set as their own report's report), since most engines will hit an internal recursion limit and error rather than hang indefinitely.
**Pitfalls:** writing a recursive CTE without a termination/cycle guard on data that could contain a cycle, triggering a runtime recursion-limit error in production; using a CTE purely for readability on a query planner that doesn't inline it, unexpectedly materializing large intermediate results and hurting performance.

## Views, Materialized Views, and Query Abstraction
Views encapsulate a query behind a virtual table interface for reuse and abstraction, while materialized views precompute and physically store results for performance at the cost of staleness until refreshed; verify whether a given view is materialized (and its actual refresh schedule/trigger) before assuming its data is always current.
```sql
CREATE MATERIALIZED VIEW daily_sales AS
  SELECT date_trunc('day', created_at) AS day, SUM(total) AS revenue FROM orders GROUP BY 1;
REFRESH MATERIALIZED VIEW CONCURRENTLY daily_sales;
```
Verify `CONCURRENTLY` refresh requires a unique index on the materialized view and test actual refresh duration under production data volume, since a slow refresh can block or seriously lag behind source-table changes if scheduled too infrequently.
**Pitfalls:** querying a materialized view assuming real-time freshness when its last refresh was hours ago; adding an unindexed materialized view refreshed non-concurrently, causing readers to be blocked during refresh.
