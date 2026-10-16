# Message Queues & Event Streaming

## Broker Selection and Delivery Semantics Grounding
Message brokers (Kafka, RabbitMQ, SQS, Redis Streams) differ fundamentally in delivery guarantees (at-most-once, at-least-once, exactly-once-within-scope), ordering guarantees, and retention model; verify the specific broker's documented guarantees for the exact version deployed before designing consumer logic around an assumed guarantee.
```bash
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic orders
rabbitmqctl list_queues name messages consumers
```
Confirm whether "exactly-once" claims apply end-to-end or only within a specific scope (e.g., Kafka's exactly-once semantics apply within Kafka-to-Kafka pipelines via transactions, not automatically to external side effects like a database write).
**Pitfalls:** assuming a broker's "exactly-once" marketing claim eliminates the need for idempotent consumer logic entirely; assuming FIFO ordering across partitions/queues when ordering is only guaranteed within a single partition/queue.

## Producer Acknowledgment and Durability Tradeoffs
Producer acknowledgment settings (Kafka's `acks=0/1/all`, RabbitMQ publisher confirms) trade latency for durability guarantees; verify the actual configured setting in code/config rather than assuming a "safe" default, since some client library defaults prioritize throughput over durability.
```python
producer = KafkaProducer(
    bootstrap_servers="broker:9092",
    acks="all",              # wait for all in-sync replicas before ack
    enable_idempotence=True, # prevents duplicate writes on producer retries
)
```
Test actual message durability under a simulated broker failure (kill the leader broker mid-publish in a staging environment) to confirm the configured acknowledgment level behaves as documented, rather than trusting configuration alone.
**Pitfalls:** using `acks=1` (leader-only acknowledgment) for critical financial events, risking data loss on leader failure before replication; leaving producer retries enabled without `enable_idempotence`, risking duplicate message delivery on retry.

## Consumer Idempotency and Deduplication
At-least-once delivery (the common practical default) means consumers must handle duplicate message delivery; verify consumer logic is actually idempotent (applying the same message twice produces the same end state) via deduplication keys or upsert-style writes, rather than assuming duplicates "won't happen in practice."
```python
def handle_payment_event(event):
    with db.transaction():
        if db.payments.exists(event["idempotency_key"]):
            return  # already processed, safe no-op
        db.payments.insert(event["idempotency_key"], event["amount"])
```
Test idempotency explicitly by replaying the same message twice in a staging consumer and verifying the end state (database row count, side effects) is identical to processing it once.
**Pitfalls:** writing consumer logic that assumes each message arrives exactly once, causing duplicate charges/emails/side-effects on redelivery after a consumer crash-and-restart; storing deduplication state only in memory, losing it on consumer restart and allowing duplicates through after a redeploy.

## Consumer Group Rebalancing and Partition Assignment
Consumer groups (Kafka) or competing consumers (RabbitMQ, SQS) distribute work across multiple consumer instances, but rebalancing (triggered by scaling, crashes, or deploys) can cause temporary processing pauses or, if not handled carefully, duplicate/out-of-order processing during the transition. Verify actual rebalance behavior and duration under a real scaling event in staging, not just from documentation.
```python
consumer = KafkaConsumer(
    "orders", group_id="order-processor",
    enable_auto_commit=False,   # manual commit after successful processing, not before
)
for msg in consumer:
    process(msg)
    consumer.commit()            # commit offset only after confirmed processing
```
Confirm offset-commit timing (before vs. after processing) matches the intended delivery guarantee, committing before processing risks message loss on crash, while committing after (with idempotent handling) favors at-least-once safety.
**Pitfalls:** using auto-commit with a short interval, acknowledging messages before processing actually completes and risking loss on crash; not testing rebalance behavior under real scaling/deploy events, discovering processing gaps only in production incidents.

# Web Servers & Reverse Proxies

## Reverse Proxy Version and Module Grounding
Nginx, Caddy, HAProxy, and Envoy differ significantly in configuration syntax, module availability, and default behaviors (buffering, timeout defaults, HTTP/2-3 support); verify the exact installed version and compiled-in modules before applying a configuration snippet found online.
```bash
nginx -v
nginx -V 2>&1 | tr ' ' '\n' | grep -i module   # compiled-in modules
nginx -t                                        # validate config syntax before reload
```
Always run a config syntax test (`nginx -t`, `caddy validate`) before reloading in production, and verify the actual running config matches the file on disk with `nginx -T` (which dumps the fully resolved, included configuration).
**Pitfalls:** applying an Nginx directive that requires a module not compiled into the installed binary, causing a silent no-op or startup failure; reloading a syntactically valid but logically wrong config without testing it against a staging replica first.

## Reverse Proxy Header Forwarding and Client IP Trust
A reverse proxy sits between clients and the application, and headers like `X-Forwarded-For`, `X-Forwarded-Proto`, and `Host` must be explicitly forwarded and trusted correctly, or the application will see the proxy's IP/protocol instead of the client's, breaking rate limiting, logging, and redirect logic.
```nginx
location / {
    proxy_pass http://backend;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```
Verify the application only trusts `X-Forwarded-For` from a known, controlled set of proxy IPs (configuring trusted proxy ranges), since an internet-facing app blindly trusting client-supplied `X-Forwarded-For` allows IP spoofing for rate-limit/geo-block bypass.
**Pitfalls:** forgetting to forward `X-Forwarded-Proto`, causing the app to think all requests are HTTP even behind an HTTPS-terminating proxy, breaking secure-cookie logic; trusting `X-Forwarded-For` from any source without restricting to known proxy IPs, enabling trivial IP spoofing.

## Timeout, Buffering, and Connection Limits
Reverse proxies impose their own timeouts (connect, read, send) and buffering behavior independent of the backend application's own timeouts; a slow backend response can be prematurely cut off by a shorter proxy timeout, producing a confusing 504 that looks like a backend bug. Verify actual configured timeout values on every layer (client, proxy, backend, load balancer) rather than debugging only the application.
```nginx
proxy_connect_timeout 5s;
proxy_read_timeout 60s;
proxy_buffering on;
proxy_buffer_size 8k;
client_max_body_size 20m;
```
Confirm `client_max_body_size`/equivalent upload limits are consistent across every layer (CDN, load balancer, reverse proxy, application framework) since the most restrictive layer silently determines the actual effective limit.
**Pitfalls:** setting a generous application-level upload limit while a stricter reverse-proxy or CDN default silently rejects large requests first; assuming a single component's timeout setting controls end-to-end behavior when multiple layered timeouts exist.

## TLS Termination and Certificate Configuration
Reverse proxies commonly terminate TLS, forwarding plaintext (or re-encrypted) traffic to backends; verify the actual certificate chain served (not just the leaf certificate) and confirm renewal automation actually updates the files the running proxy process reads, requiring a reload/restart to pick up new certificates.
```bash
openssl s_client -connect example.com:443 -showcerts </dev/null 2>/dev/null | grep -c "BEGIN CERTIFICATE"  # verify full chain, not just leaf
nginx -s reload   # reload config/certs without dropping existing connections
```
Confirm the renewal automation's post-renewal hook actually triggers a proxy reload (`nginx -s reload`, not a full restart that drops connections) by checking real logs from the last successful automated renewal.
**Pitfalls:** serving only the leaf certificate without the intermediate chain, causing some clients/validators to fail trust verification while browsers with cached intermediates appear fine; renewing a certificate file on disk without reloading the proxy process, continuing to serve the expired certificate from memory.

# Message Queues & Event Streaming

## Dead Letter Queues and Poison Message Handling
A "poison message" repeatedly fails processing (malformed payload, a bug triggered only by specific content) and can block an entire queue/partition if retried indefinitely without a limit; verify a dead-letter queue (DLQ) is actually configured with a bounded retry count, and confirm DLQ messages are actively monitored/alerted on rather than silently accumulating unnoticed.
```python
consumer_config = {
    "max_retries": 3,
    "dlq_topic": "orders.dlq",
}
def handle_message(msg):
    try:
        process(msg)
    except Exception as e:
        if msg.retry_count >= consumer_config["max_retries"]:
            publish_to_dlq(consumer_config["dlq_topic"], msg, error=str(e))
        else:
            requeue_with_backoff(msg)
```
Verify an actual alert fires when messages land in the DLQ (not just a dashboard nobody watches), and confirm a documented process exists for inspecting and reprocessing DLQ messages after the underlying bug is fixed.
**Pitfalls:** retrying a poison message indefinitely without a DLQ, causing it to block a partition/queue and stall all subsequent messages behind it; routing messages to a DLQ with no monitoring or alerting, letting critical failed events silently pile up unnoticed for weeks.

## Schema Evolution and Message Versioning
As producers and consumers evolve independently, message schemas change over time; verify a schema registry (Confluent Schema Registry, AWS Glue Schema Registry) or explicit versioning convention enforces backward/forward compatibility rules (adding optional fields is usually safe, removing or retyping existing fields usually isn't) before deploying a producer change that could break running consumers.
```json
{ "type": "record", "name": "OrderEvent", "fields": [
  { "name": "orderId", "type": "string" },
  { "name": "total", "type": "double" },
  { "name": "currency", "type": ["null", "string"], "default": null }
]}
```
Verify a schema registry's compatibility mode (`BACKWARD`, `FORWARD`, `FULL`) is actually configured and enforced at publish time, rejecting incompatible schema changes automatically, rather than relying on manual review alone to catch breaking changes.
**Pitfalls:** removing or changing the type of an existing required field without a coordinated multi-phase rollout, breaking consumers still expecting the old schema; deploying schema changes without a registry's automated compatibility check, discovering the break only when a consumer crashes in production.

## Exactly-Once Processing Patterns Beyond Broker Guarantees
True end-to-end exactly-once processing (including side effects like external API calls or non-transactional database writes) generally cannot be guaranteed by the broker alone, verify the actual pattern used (idempotency keys, transactional outbox, two-phase commit where supported) to achieve effectively-exactly-once behavior at the application level, since broker-level exactly-once semantics typically only cover broker-to-broker or broker-to-database-within-a-supported-connector scope.
```python
def process_order_event(event):
    with db.transaction():
        if db.processed_events.exists(event.id):
            return  # already handled, safe no-op, achieves effective exactly-once at the app level
        db.processed_events.insert(event.id)
        apply_business_logic(event)
```
Verify the idempotency check and the business logic mutation happen within the same atomic transaction, since performing them as separate non-atomic steps reintroduces a race window where a crash between them causes exactly the duplicate-processing bug the pattern was meant to prevent.
**Pitfalls:** assuming a broker's "exactly-once" configuration eliminates the need for any application-level idempotency handling for external side effects (email sends, third-party API calls) it doesn't cover; checking for a duplicate and performing the actual side effect as two separate non-transactional steps, reintroducing a race condition on crash.

## Event Sourcing and CQRS Fundamentals
Event sourcing persists state changes as an immutable, ordered sequence of events (rather than just current state), enabling full audit history and state reconstruction by replay; Command Query Responsibility Segregation (CQRS) separates write models (handling commands, producing events) from read models (optimized query projections built from those events). Verify a proposed event-sourced design actually needs the audit/replay benefits before adopting the added complexity of maintaining projections and handling eventual consistency between write and read sides.
```python
events = [
    {"type": "OrderCreated", "orderId": "o1", "total": 100},
    {"type": "OrderShipped", "orderId": "o1", "trackingId": "t123"},
]
def rebuild_order_state(events):
    state = {}
    for e in events:
        if e["type"] == "OrderCreated": state = {"id": e["orderId"], "total": e["total"], "status": "created"}
        elif e["type"] == "OrderShipped": state["status"] = "shipped"
    return state
```
Verify read-model projections are rebuildable from scratch by replaying the event log (a key operational safety net), and confirm the team has a plan for handling eventual consistency lag between a write and its corresponding read-model update becoming visible.
**Pitfalls:** adopting event sourcing for a simple CRUD domain that doesn't actually need audit history or temporal queries, absorbing significant complexity for no real benefit; failing to verify read-model projections can be fully rebuilt from the event log, discovering this only when a projection bug requires exactly that recovery path.

# Web Servers & Reverse Proxies

## HTTP Caching Headers and Validation
Correct use of `Cache-Control`, `ETag`, and `Last-Modified` headers determines whether browsers/CDNs/proxies can safely cache and reuse a response without re-fetching from origin; verify actual cache behavior with real repeated requests and header inspection rather than assuming a `Cache-Control` value takes effect uniformly across every caching layer between origin and client.
```http
Cache-Control: public, max-age=3600, stale-while-revalidate=86400
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d"
```
```bash
curl -sI https://example.com/style.css | grep -i "cache-control\|etag"
curl -sI -H 'If-None-Match: "33a64df551..."' https://example.com/style.css   # verify 304 Not Modified
```
Verify a conditional request (`If-None-Match`/`If-Modified-Since`) actually returns `304 Not Modified` when content hasn't changed, confirming validation-based caching is functioning rather than always re-serving full response bodies.
**Pitfalls:** setting `Cache-Control: no-cache` (which actually permits caching with revalidation) when `no-store` (which prevents caching entirely) was intended, or vice versa, based on a misunderstanding of the directive names; never testing conditional requests, missing that a misconfigured `ETag` generator causes every request to be treated as changed.

## Static Asset Serving and Compression
Reverse proxies/web servers can serve static assets far more efficiently than application servers, using techniques like gzip/Brotli compression, byte-range requests for media seeking, and long-lived cache headers with content-hashed filenames for cache-busting; verify compression is actually negotiated correctly (`Accept-Encoding` matched against `Content-Encoding`) and that byte-range requests work for large media files.
```nginx
location /static/ {
    gzip_static on;
    brotli_static on;
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```
Verify content-hashed filenames (`app.a1b2c3.js`) are actually used for aggressively-cached assets so a deploy invalidates the cache automatically via a new filename, rather than relying on a short cache duration that still risks serving stale assets between deploys.
**Pitfalls:** setting a long `max-age` on assets without content-hashed filenames, causing users to be stuck with stale cached JS/CSS after a deploy until the cache naturally expires; not verifying byte-range request support for video/audio files, breaking seeking functionality for media players.

## Web Application Firewall and Request Filtering
A Web Application Firewall (WAF), often deployed at the reverse-proxy/CDN layer, filters malicious requests (SQL injection patterns, known bad user agents, excessive request rates) before they reach the application; verify WAF rules are tuned against actual legitimate traffic patterns to avoid false positives blocking real users, and confirm the WAF is actually in blocking mode (not just logging/monitoring mode) if protection is assumed to be active.
```bash
curl -s https://example.com/?id=1%27%20OR%20%271%27=%271 -o /dev/null -w "%{http_code}\n"  # verify WAF blocks an injection-pattern test request
```
Verify WAF logs are reviewed periodically for both blocked-attack patterns (confirming it's working) and false-positive blocks of legitimate traffic (confirming it's not overly aggressive), rather than deploying it once and assuming indefinite correct behavior.
**Pitfalls:** deploying a WAF in monitoring-only mode and assuming it's actively blocking attacks, when it's merely logging them; tuning WAF rules so aggressively that legitimate traffic patterns (valid but unusual user input) get falsely blocked, degrading real user experience.

## HTTP/2 Server Push and Resource Hints Deprecation Awareness
HTTP/2 Server Push (proactively sending resources before the client requests them) was deprecated and removed from major browsers due to caching inefficiencies and complexity, replaced by resource hints (`<link rel="preload">`, `103 Early Hints`); verify current browser support status for any push/hint mechanism before building a performance strategy around it, since guidance from a few years ago may reference a now-removed feature.
```http
HTTP/1.1 103 Early Hints
Link: </styles.css>; rel=preload; as=style
Link: </app.js>; rel=preload; as=script
```
Verify actual client-observed loading behavior with real browser testing (WebPageTest, Lighthouse) rather than assuming a preload/hint directive improves performance uniformly, since misused preload hints can actually hurt performance by wasting early bandwidth on non-critical resources.
**Pitfalls:** implementing HTTP/2 Server Push based on outdated tutorials, building infrastructure around a feature browsers no longer support; overusing `<link rel="preload">` for non-critical resources, competing for early bandwidth with genuinely critical resources and delaying actual page render.
