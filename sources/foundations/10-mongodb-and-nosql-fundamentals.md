# MongoDB & NoSQL Fundamentals

## Server Version and Driver Compatibility Grounding
MongoDB server versions (4.4, 5.0, 6.0, 7.0, 8.0) and driver library versions must be compatible; transactions, time-series collections, and certain aggregation operators require specific minimums. Verify both server and driver versions before assuming a feature is available.
```bash
mongosh --eval "db.version()"
npm ls mongodb                     # mongodb driver package version
```
Check the official MongoDB driver compatibility matrix for the exact server/driver pair before debugging a "function not supported" error.
**Pitfalls:** assuming multi-document transactions work on a standalone (non-replica-set) deployment, they require a replica set or sharded cluster; using an aggregation operator introduced in a newer server version than what's deployed.

## Document Modeling and Embedding vs. Referencing
NoSQL document design should be driven by access patterns, not normalized relational habits; embedding suits data read together and bounded in size, while referencing suits large or independently-updated sub-entities. Verify the actual read/write pattern before choosing a shape.
```javascript
// Embedded: order + line items read/written together, bounded count
{ _id: 1, customer: "c1", items: [{ sku: "A1", qty: 2 }, { sku: "B2", qty: 1 }] }

// Referenced: comments grow unbounded and are queried independently
{ _id: 1, postId: 42, author: "u9", text: "..." }
```
Verify document size stays well under the 16MB BSON document limit for embedded designs with potentially unbounded arrays, and check actual query patterns with `explain()` rather than guessing.
**Pitfalls:** embedding an unbounded array (e.g., all comments ever made) that eventually hits the 16MB document limit; over-normalizing into many collections requiring `$lookup` joins for every simple read, hurting performance.

## Indexing and Query Plan Verification
MongoDB uses indexes (single-field, compound, multikey, text) to avoid full collection scans; verify actual query execution with `explain("executionStats")` rather than assuming an index is used just because it exists.
```javascript
db.orders.createIndex({ customerId: 1, createdAt: -1 });
db.orders.find({ customerId: "c1" }).sort({ createdAt: -1 }).explain("executionStats");
```
Confirm the `winningPlan` shows `IXSCAN` (index scan) rather than `COLLSCAN` (collection scan), and check `totalDocsExamined` versus `nReturned` for efficiency, a large gap indicates a poorly targeted index.
**Pitfalls:** creating an index whose field order doesn't match the query's equality-then-sort-then-range pattern (ESR rule), causing it to be ignored or only partially used; assuming an index exists in production because it exists in a local dev database without verifying with `getIndexes()`.

## Aggregation Pipeline Correctness
The aggregation framework processes documents through ordered stages (`$match`, `$group`, `$lookup`, `$project`); stage order affects both correctness and performance, filtering early with `$match` before expensive stages like `$lookup` or `$group` reduces work. Verify actual output shape at each stage while debugging.
```javascript
db.orders.aggregate([
  { $match: { status: "completed" } },
  { $lookup: { from: "customers", localField: "customerId", foreignField: "_id", as: "customer" } },
  { $unwind: "$customer" },
  { $group: { _id: "$customer.region", total: { $sum: "$amount" } } },
]);
```
Insert `{ $limit: 5 }` temporarily at each stage boundary while developing to inspect intermediate document shapes, since aggregation bugs are hard to spot from the final output alone.
**Pitfalls:** placing `$match` after an expensive `$lookup`/`$group` instead of before, processing far more documents than necessary; forgetting `$unwind` turns an array field into one document per element, multiplying downstream counts if not accounted for.

# Docker Fundamentals

## Engine Version and Image Digest Grounding
Docker behavior (BuildKit defaults, syntax features, multi-platform builds) depends on the installed Docker Engine/CLI version; image reproducibility depends on pinning by digest, not just tag, since tags are mutable pointers.
```bash
docker version                        # Client/Server versions
docker buildx version
docker pull node:22.11.0-bookworm-slim@sha256:abcd1234...
```
Verify `DOCKER_BUILDKIT=1` (default in modern Docker) is actually active before relying on BuildKit-only Dockerfile syntax like cache mounts.
**Pitfalls:** pinning only a mutable tag (`node:22`) and being surprised a rebuild months later pulls a different underlying image; assuming BuildKit features work on a legacy builder without checking `docker buildx version`.

## Dockerfile Layer Caching and Build Context
Each Dockerfile instruction creates a cached layer; reordering instructions so rarely-changing steps (dependency installs) come before frequently-changing steps (source code copy) maximizes cache reuse and build speed. Verify actual cache hits with `docker build --progress=plain`.
```dockerfile
FROM node:22.11.0-bookworm-slim AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev

FROM deps AS build
COPY . .
RUN npm run build
```
Check `.dockerignore` excludes `node_modules`, `.git`, and build artifacts from the build context, since an oversized context slows every build and can leak files into layers unintentionally.
**Pitfalls:** copying the entire source tree before installing dependencies, invalidating the dependency-install cache layer on every source change; missing a `.dockerignore`, bloating build context and accidentally baking in local secrets or `.env` files.

## Multi-Stage Builds and Image Size Reduction
Multi-stage builds compile/build in one stage and copy only final artifacts into a slim runtime stage, dramatically reducing final image size and attack surface by excluding build tools and dev dependencies. Verify the final image doesn't accidentally retain build-stage layers.
```dockerfile
FROM golang:1.23 AS builder
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o /app ./cmd/server

FROM gcr.io/distroless/static-debian12
COPY --from=builder /app /app
ENTRYPOINT ["/app"]
```
Compare `docker images` size before/after multi-stage refactor to confirm the expected reduction actually occurred, and scan the final image (not just the builder stage) for vulnerabilities.
**Pitfalls:** forgetting `--from=builder` and accidentally including the full build toolchain in the final image; using a `latest`-tagged distroless/base image without pinning, causing unreproducible builds.

## Networking, Volumes, and Container Lifecycle
Containers are ephemeral by default, data written inside a container's writable layer is lost on removal unless persisted via a volume or bind mount; container-to-container communication requires an explicit user-defined network for DNS-based service discovery. Verify actual network attachment and volume mounts with `docker inspect` rather than assuming from the Compose file alone.
```yaml
services:
  api:
    build: .
    networks: [backend]
    volumes:
      - api-data:/var/lib/api
    depends_on:
      db:
        condition: service_healthy
  db:
    image: postgres:16.4
    networks: [backend]
    volumes: [db-data:/var/lib/postgresql/data]
volumes: { api-data: {}, db-data: {} }
networks: { backend: {} }
```
Verify `depends_on` with `condition: service_healthy` actually waits for a real health check, since plain `depends_on` only waits for container start, not application readiness.
**Pitfalls:** relying on default bridge networking instead of a user-defined network, losing DNS-based service name resolution between containers; assuming `depends_on` (without a healthcheck condition) guarantees the dependency is ready to accept connections.

# MongoDB & NoSQL Fundamentals

## Schema Validation and Flexible Schema Governance
MongoDB's flexible schema doesn't mean "no schema" in practice, uncontrolled documents drift into inconsistent shapes over time; JSON Schema-based validation rules enforce structure at the database level while still allowing intentional flexibility. Verify actual validation rules are attached to a collection and set to the intended enforcement level (`strict` vs `moderate`) rather than assuming application-level validation alone is sufficient.
```javascript
db.createCollection("orders", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["customerId", "total"],
      properties: { total: { bsonType: "double", minimum: 0 } },
    },
  },
  validationLevel: "moderate",
});
```
Verify `validationLevel: "moderate"` (validates new/modified documents only) versus `"strict"` (validates all writes) matches intent, since moderate mode can leave old non-conforming documents silently untouched.
**Pitfalls:** assuming schema-less means no governance is needed, leading to years of inconsistent document shapes that break downstream code; setting validation to `"moderate"` and assuming it retroactively fixes historical documents, when it does not.

## Replica Sets and Read/Write Concern Tuning
MongoDB replica sets provide high availability through automatic failover; `writeConcern` (how many replicas must acknowledge a write) and `readConcern`/`readPreference` (consistency vs. staleness/latency tradeoffs for reads) must be tuned explicitly per operation's actual durability and freshness requirements, verify the configured defaults rather than assuming the driver's defaults match your durability needs.
```javascript
db.orders.insertOne(doc, { writeConcern: { w: "majority", wtimeout: 5000 } });
db.orders.find().readConcern("majority").readPref("secondaryPreferred");
```
Test actual failover behavior in a staging replica set (stepping down the primary) to confirm application code handles the resulting transient errors and retries correctly, rather than assuming the driver handles it invisibly.
**Pitfalls:** using `w: 1` (default in many client configs) for critical writes, risking data loss if the primary fails before replication completes; reading from secondaries without accounting for replication lag, serving stale data to users expecting immediate consistency.

## Change Streams for Real-Time Reactivity
Change Streams let applications subscribe to real-time data changes (inserts, updates, deletes) on a collection/database without polling, built on the replication oplog; verify the deployment is a replica set or sharded cluster (change streams require this) and that resume tokens are persisted so a consumer can recover its position after a restart without missing or reprocessing events.
```javascript
const changeStream = db.collection("orders").watch([{ $match: { operationType: "insert" } }]);
changeStream.on("change", (event) => {
  persistResumeToken(event._id);
  handleNewOrder(event.fullDocument);
});
```
Verify oplog retention window is long enough to cover expected consumer downtime, since a resume token older than the oplog's retention causes an unrecoverable "resume point not found" error requiring a full resync.
**Pitfalls:** running change streams against a standalone (non-replica-set) instance, which doesn't support them; not persisting resume tokens, causing every consumer restart to either miss events or require a full collection rescan.

## Sharding for Horizontal Scale
Sharding distributes data across multiple servers using a shard key, whose choice critically affects write distribution and query routing efficiency; verify a shard key provides high cardinality and even write distribution for the actual workload before committing to it, since changing a shard key on an already-sharded, populated collection is a costly operation (though newer MongoDB versions support online resharding with caveats).
```javascript
sh.shardCollection("app.orders", { customerId: "hashed" });
db.orders.find({ customerId: "c123" }).explain("executionStats");  // verify targeted (not scatter-gather) query
```
Verify queries filtering by the shard key are actually routed to a single shard ("targeted" query) rather than scanning all shards ("scatter-gather"), which defeats much of sharding's performance benefit, check with `explain()`.
**Pitfalls:** choosing a low-cardinality or monotonically increasing shard key (like a timestamp), causing uneven write distribution and hotspotting on one shard; querying without the shard key in the filter, forcing an expensive scatter-gather across every shard.

# Docker Fundamentals

## Container Image Layers and Registry Distribution
Docker images are composed of immutable, content-addressed layers that are cached and shared across images with common ancestry; pushing/pulling only transfers layers not already present in the target registry/daemon. Verify actual layer reuse and image provenance with `docker history` and digest inspection rather than assuming a rebuilt "same" image is byte-identical.
```bash
docker history my-app:1.4.0
docker inspect --format='{{.RepoDigests}}' my-app:1.4.0
docker manifest inspect my-app:1.4.0    # verify multi-platform manifest contents
```
Verify a specific tag hasn't been silently overwritten in a shared registry by comparing digests before and after a deploy, since tags are mutable and CI race conditions can push a different image under the same tag.
**Pitfalls:** trusting a mutable tag (`:latest`, `:1.4`) as a stable reference in a deploy pipeline without pinning to a digest, risking a different image being pulled than what was tested; assuming layer caching guarantees reproducibility across different builder machines/architectures without verifying digests match.

## Docker Compose for Local Multi-Service Development
Docker Compose orchestrates multiple related containers (app, database, cache) for local development and testing with a single declarative file; verify service startup ordering and readiness (not just container-start ordering) using health checks, and confirm environment parity between Compose and the actual production orchestrator (Kubernetes, ECS) to avoid "works in Compose, fails in prod" surprises.
```yaml
services:
  api:
    build: .
    environment:
      - DATABASE_URL=postgres://db:5432/app
    depends_on:
      db: { condition: service_healthy }
  db:
    image: postgres:16.4
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      retries: 5
```
Verify `docker compose config` output (the fully resolved, interpolated configuration) matches expectations when using multiple override files (`docker-compose.override.yml`), since merge behavior across files can silently change intended settings.
**Pitfalls:** assuming Compose's networking/volume behavior matches production Kubernetes exactly, missing environment-specific bugs only caught after deployment; layering multiple Compose override files without verifying the final merged config, causing unexpected setting overrides.

## Container Logging and Log Driver Configuration
Container stdout/stderr is captured by Docker's logging driver (`json-file` by default, or `journald`, `fluentd`, `awslogs` for centralized collection); verify the configured driver and its retention/rotation settings, since the default `json-file` driver has no size limit by default and can fill disk on long-running, chatty containers.
```bash
docker inspect --format='{{.HostConfig.LogConfig}}' my-container
docker run --log-driver=json-file --log-opt max-size=10m --log-opt max-file=3 my-app:1.4.0
```
Verify logs are actually reaching the intended centralized destination in a staging deploy before relying on it during a production incident, rather than assuming a logging driver configuration works purely from its presence in a compose file.
**Pitfalls:** leaving default unbounded `json-file` logging on a verbose long-running container, eventually filling host disk and causing unrelated container failures; configuring a remote log driver without verifying actual delivery, discovering the gap only during an incident when logs are needed most.

## Docker Security: Image Scanning and Least-Privilege Runtime
Container images can carry vulnerable OS packages or dependencies inherited from base images; verify images are scanned (Trivy, Grype, or registry-native scanning) as part of the build pipeline, and confirm containers run with the minimum necessary Linux capabilities and a read-only root filesystem where possible, rather than the permissive defaults.
```bash
trivy image my-app:1.4.0 --severity HIGH,CRITICAL
docker run --read-only --cap-drop=ALL --cap-add=NET_BIND_SERVICE --user 1000:1000 my-app:1.4.0
```
Verify a scan's severity threshold actually blocks CI on critical findings (not just reports them), and confirm dropped capabilities don't break legitimate application functionality by testing the hardened configuration in staging before production rollout.
**Pitfalls:** running vulnerability scans that only produce a report nobody reviews, without a CI gate that blocks builds on critical findings; running containers as root by default when the application never needs elevated privileges, unnecessarily widening the container breakout attack surface.
