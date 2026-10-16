# REST API Design Fundamentals

## HTTP Semantics and Resource Modeling
REST APIs model state as resources addressed by URLs, manipulated via HTTP methods with defined semantics (GET safe/idempotent, PUT idempotent, POST not idempotent, DELETE idempotent); verify actual method usage matches these guarantees, since clients and intermediaries (caches, retries) rely on them.
```
GET    /orders/42          -> 200 with representation, safe, cacheable
POST   /orders             -> 201 Created, Location: /orders/43
PUT    /orders/42          -> 200/204, full replace, idempotent
PATCH  /orders/42          -> 200/204, partial update
DELETE /orders/42          -> 204, idempotent (repeat calls are safe)
```
Verify idempotency claims with an actual repeated-request test, a `PUT` handler that increments a counter instead of replacing state violates the idempotency contract silently.
**Pitfalls:** using `POST` for operations that are actually idempotent updates, breaking safe-retry assumptions in clients/proxies; returning `200` for a resource-creation endpoint instead of `201` with a `Location` header.

## Status Codes and Error Response Design
HTTP status codes communicate outcome categories (2xx success, 4xx client error, 5xx server error); verify the exact code chosen matches the actual condition rather than defaulting to `200`/`500` for everything, since clients branch logic on these codes.
```json
// 422 Unprocessable Entity
{
  "error": { "code": "VALIDATION_FAILED", "message": "Invalid request body",
    "details": [{ "field": "email", "issue": "must be a valid email address" }] }
}
```
Adopt a consistent error schema (e.g., RFC 9457 Problem Details) across all endpoints so clients can parse errors uniformly, and verify actual responses match the documented schema with contract tests.
**Pitfalls:** returning `200 OK` with an `{"error": ...}` body instead of a proper 4xx/5xx status, breaking HTTP-level error handling in clients and monitoring; conflating `401 Unauthorized` (missing/invalid credentials) with `403 Forbidden` (authenticated but not permitted).

## Pagination, Filtering, and Sorting Conventions
Large collections require pagination (offset-based, cursor-based, or keyset) to avoid unbounded response sizes; verify which strategy an API uses, since offset pagination degrades in performance and correctness (skipped/duplicated items on concurrent writes) at scale compared to cursor-based approaches.
```
GET /orders?status=completed&sort=-created_at&limit=25&cursor=eyJpZCI6NDJ9
```
```json
{ "data": [...], "page_info": { "next_cursor": "eyJpZCI6Njd9", "has_more": true } }
```
Verify sort-stability: sorting only by a non-unique field (like `created_at` with duplicate timestamps) can produce inconsistent pagination, confirm a tie-breaker (like `id`) is included.
**Pitfalls:** using offset pagination on a frequently-mutated table, causing items to be skipped or duplicated across pages; sorting without a unique tie-breaker field, producing nondeterministic page boundaries.

## API Versioning and Backward Compatibility
Breaking changes require a versioning strategy (URL path `/v2/`, header-based, or content negotiation); verify what "breaking" means for the specific API contract, removing a field, changing a type, or altering validation rules are all breaking even if additive-seeming.
```
GET /v1/users/42     -> legacy shape
GET /v2/users/42     -> new shape, deployed alongside v1 during migration window
Accept: application/vnd.myapi.v2+json   -- alternative: content negotiation
```
Verify consumer impact before shipping a change by checking actual traffic/logs for which API version and fields are in active use, rather than assuming a field is unused because it's undocumented.
**Pitfalls:** treating "adding a required field" as non-breaking because it's additive; deprecating and removing an old version without confirming via traffic logs that no clients still depend on it.

# GraphQL Fundamentals

## Schema Design and Type System Grounding
A GraphQL schema defines types, queries, mutations, and subscriptions as a contract clients rely on; verify the schema actually deployed matches what documentation/clients assume by introspecting the live endpoint rather than trusting a stale schema file.
```graphql
type Order {
  id: ID!
  status: OrderStatus!
  items: [OrderItem!]!
  customer: Customer
}
type Query {
  order(id: ID!): Order
  orders(status: OrderStatus, first: Int = 20, after: String): OrderConnection!
}
```
```bash
curl -s -X POST $ENDPOINT -d '{"query":"{ __schema { types { name } } }"}' | jq
```
Verify nullability (`!`) matches actual runtime guarantees, marking a field non-null when the resolver can return null causes a runtime error that nulls out entire parent objects up the tree.
**Pitfalls:** marking a field non-nullable when the underlying data source can legitimately be absent, causing cascading null propagation errors; exposing internal database field names directly in the schema, coupling the API contract to implementation details.

## Resolvers and the N+1 Query Problem
Each field can have its own resolver function; naively resolving nested relations (e.g., each order's customer) triggers one database query per item, the classic N+1 problem. Verify actual query counts with database query logging during a GraphQL request, not just assumed efficiency from the schema shape.
```javascript
const customerLoader = new DataLoader(async (ids) => {
  const customers = await db.customers.findByIds(ids);
  return ids.map((id) => customers.find((c) => c.id === id));
});
// resolver: return customerLoader.load(order.customerId);
```
Confirm a batching solution (DataLoader or equivalent) is actually wired into the resolver, since simply importing DataLoader without per-request instantiation can leak cached data across unrelated requests.
**Pitfalls:** instantiating a DataLoader instance globally instead of per-request, leaking stale or cross-user cached data; resolving nested lists without batching and only noticing the N+1 cost under production-scale data, not small dev fixtures.

## Query Complexity, Depth Limiting, and Rate Limiting
Unlike REST, a single GraphQL query can request arbitrarily deep/nested data, creating a DoS vector if unbounded; verify actual complexity-limiting or depth-limiting middleware is configured and tested against a deliberately expensive query.
```javascript
const depthLimit = require("graphql-depth-limit");
const server = new ApolloServer({
  schema,
  validationRules: [depthLimit(6)],
});
```
Test with a deliberately malicious deeply-nested or circularly-aliased query in a staging environment to confirm limits actually reject it with a clear error rather than timing out the server.
**Pitfalls:** deploying a GraphQL API with no query cost analysis, allowing a single client request to fan out into thousands of database calls; rate-limiting only by request count, missing that GraphQL requests vary enormously in actual server cost.

## Caching and Persisted Queries
GraphQL's flexible queries make traditional HTTP caching (URL-based) ineffective; solutions include persisted queries (client sends a hash, server maps it to a stored query), normalized client-side caching (Apollo Client, Relay), and field-level server caching. Verify the actual caching strategy in use before assuming responses are fresh or optimally cached.
```javascript
// Client sends: { "extensions": { "persistedQuery": { "sha256Hash": "abc123..." } } }
// Server resolves hash to stored query text, reducing payload size and enabling allow-listing
```
Verify cache invalidation triggers correctly on mutations by checking that normalized cache entries update (or are evicted) after a mutation response, since stale nested object caches are a common GraphQL client bug.
**Pitfalls:** assuming a CDN caches GraphQL POST responses like REST GETs without explicit persisted-query + GET-based configuration; forgetting cache normalization requires consistent `id`/`__typename` fields across queries to merge correctly.

# REST API Design Fundamentals

## Content Negotiation and Media Type Versioning
HTTP content negotiation (`Accept`, `Content-Type` headers) lets clients and servers agree on representation format and version without changing the URL; verify a server actually implements negotiation correctly by requesting an unsupported `Accept` type and confirming a proper `406 Not Acceptable` response rather than a silent default fallback that masks client bugs.
```http
GET /orders/42 HTTP/1.1
Accept: application/vnd.myapi.v2+json
```
```javascript
app.get("/orders/:id", (req, res) => {
  if (req.accepts("application/vnd.myapi.v2+json")) return res.json(toV2Shape(order));
  if (req.accepts("application/vnd.myapi.v1+json")) return res.json(toV1Shape(order));
  res.status(406).json({ error: "unsupported media type" });
});
```
Verify caching layers (CDNs, browser caches) are configured with `Vary: Accept` when content negotiation is used, since otherwise a cached response for one requested format can be incorrectly served to a client requesting a different one.
**Pitfalls:** silently defaulting to one format when an unsupported `Accept` header is sent instead of returning `406`, hiding client integration bugs; forgetting `Vary: Accept` on cached negotiated responses, causing cross-format cache poisoning.

## HATEOAS and Discoverable API Design
Hypermedia As The Engine Of Application State (HATEOAS) embeds actionable links in API responses so clients can navigate available actions/resources dynamically rather than hardcoding URL structures; verify whether a given API actually implements this maturity level (most "REST" APIs in practice don't) before assuming clients can rely on discoverability instead of out-of-band documentation.
```json
{
  "id": 42, "status": "pending",
  "_links": {
    "self": { "href": "/orders/42" },
    "cancel": { "href": "/orders/42/cancel", "method": "POST" }
  }
}
```
Verify client code doesn't hardcode URLs that hypermedia links are meant to provide dynamically, since doing so defeats the purpose and creates the exact tight coupling HATEOAS aims to avoid.
**Pitfalls:** claiming an API is "RESTful" (in the full Richardson Maturity Model sense) while providing no hypermedia links at all, causing confusion when consumers expect discoverability; implementing links but having client SDKs hardcode URLs anyway, gaining none of the intended decoupling benefit.

## Rate Limiting Strategies and Client Communication
Rate limiting (fixed window, sliding window, token bucket) protects APIs from abuse and overload; verify the actual algorithm in use, since fixed-window counters allow bursts at window boundaries that a token bucket would smooth out, and confirm limits are clearly communicated via standard headers so well-behaved clients can self-throttle.
```http
HTTP/1.1 429 Too Many Requests
Retry-After: 30
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1718000000
```
Verify a distributed rate limiter (Redis-backed token bucket, for instance) works correctly across multiple API server instances, since an in-memory-only rate limiter silently fails to enforce a shared limit once traffic is load-balanced across more than one process.
**Pitfalls:** implementing rate limiting with in-process memory state behind a load balancer, allowing the effective limit to multiply by the number of server instances; omitting `Retry-After`/`X-RateLimit-*` headers, forcing clients to guess at backoff timing and often retry too aggressively.

## API Documentation as a Contract Testing Source
OpenAPI/Swagger specifications should be treated as an enforceable contract, not just documentation, verify the spec is validated against actual request/response behavior with contract testing tools rather than allowing it to drift silently out of sync with the real implementation over time.
```bash
npx @stoplight/spectral-cli lint openapi.yaml
npx dredd openapi.yaml http://localhost:3000 --hookfiles=hooks.js
```
Regenerate client SDKs from the OpenAPI spec periodically and run them against a live staging environment to catch drift between documented and actual behavior before it reaches consumers relying on generated clients.
**Pitfalls:** hand-writing an OpenAPI spec once and never validating it against the running API again, letting it silently drift out of date as the implementation evolves; generating client SDKs from a stale spec, shipping clients that don't match actual server behavior.

# GraphQL Fundamentals

## Fragments and Query Reusability
GraphQL fragments define reusable selection sets shared across multiple queries/mutations, keeping field lists (especially deeply nested ones) consistent and reducing duplication; verify fragment colocation with the components/functions that actually use the data (a common pattern in Relay/Apollo) so a UI change and its data requirements stay in sync.
```graphql
fragment OrderSummary on Order {
  id
  status
  total
  customer { name email }
}
query GetOrder($id: ID!) {
  order(id: $id) { ...OrderSummary }
}
```
Verify fragment field selections don't silently diverge across multiple copies of "the same" fragment defined ad hoc in different files, which reintroduces the duplication problem fragments are meant to solve.
**Pitfalls:** defining near-identical fragments in multiple places instead of sharing one canonical fragment, causing inconsistent field selections across the app; over-fragmenting trivial single-use selections, adding indirection without meaningful reuse benefit.

## Mutations, Optimistic Updates, and Cache Consistency
GraphQL mutations modify server state and typically return the updated object so client caches (Apollo, Relay, urql) can normalize and merge the result automatically; verify a mutation's response shape includes enough fields for the cache to update every affected query, and confirm optimistic UI updates are rolled back correctly on mutation failure.
```graphql
mutation UpdateOrderStatus($id: ID!, $status: OrderStatus!) {
  updateOrderStatus(id: $id, status: $status) {
    order { id status }
  }
}
```
```javascript
const [updateStatus] = useMutation(UPDATE_ORDER_STATUS, {
  optimisticResponse: { updateOrderStatus: { order: { id, status: "SHIPPED", __typename: "Order" } } },
});
```
Verify `__typename` and `id` are present in every mutation response used for cache normalization, since missing either field prevents the cache from correctly identifying which normalized object to update.
**Pitfalls:** returning a mutation response missing fields other active queries depend on, leaving those queries' cached data stale until a manual refetch; configuring optimistic updates without proper rollback handling, leaving the UI in an inconsistent state after a failed mutation.

## Subscriptions and Real-Time Data over WebSockets
GraphQL subscriptions deliver real-time updates over a persistent connection (typically WebSockets via `graphql-ws` or the older, largely deprecated `subscriptions-transport-ws` protocol); verify which subprotocol both client and server actually implement, since the two are incompatible and mismatched protocol versions fail silently or with unhelpful connection errors.
```graphql
subscription OnOrderUpdated($orderId: ID!) {
  orderUpdated(orderId: $orderId) { id status }
}
```
Verify connection resilience (automatic reconnect, missed-message handling during a disconnect) is actually implemented, since a naive subscription client silently misses events during any connection drop without a reconnect-and-resync strategy.
**Pitfalls:** mismatching the WebSocket subprotocol between client and server libraries, causing connections to fail with unhelpful generic errors; assuming a subscription client automatically catches up on missed events after a reconnect without an explicit resync/refetch strategy.

## Schema Stitching, Federation, and Distributed Graphs
Large organizations often compose one logical GraphQL schema from multiple underlying services via Apollo Federation or schema stitching rather than one monolithic resolver set; verify the exact federation version/spec (`@key`, `@external`, `@requires` directives differ between Federation 1 and 2) and confirm the gateway's query planning actually resolves cross-service entity references correctly under real network latency, not just in a local all-services-on-one-host test.
```graphql
type Order @key(fields: "id") {
  id: ID!
  customerId: ID!
  customer: Customer @external
}
```
Verify gateway-level error handling and partial-failure behavior (one subgraph down) matches expectations by deliberately taking a subgraph offline in staging and observing the actual client-facing response.
**Pitfalls:** assuming Federation 1 directive syntax works unchanged under a Federation 2 gateway, hitting schema composition errors; not testing partial subgraph outages, discovering only in production that one failing service silently breaks unrelated parts of the composed graph.
