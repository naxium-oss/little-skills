# Concurrency & Parallelism Fundamentals

## Concurrency versus Parallelism Distinction
Concurrency is about structuring a program to handle multiple logical tasks that can interleave (not necessarily simultaneously), while parallelism is about actually executing multiple tasks at the same physical instant on multiple cores; verify which one a given optimization actually needs before reaching for threads or async, since misapplying either wastes effort.
```python
import asyncio, multiprocessing

# Concurrency for I/O-bound waiting (network calls interleave while waiting)
async def fetch_many(urls): ...

# Parallelism for CPU-bound work (actual simultaneous computation across cores)
with multiprocessing.Pool(processes=4) as pool:
    results = pool.map(cpu_heavy_function, data_chunks)
```
Profile the actual bottleneck (I/O wait vs. CPU saturation) with real measurements before choosing a concurrency model, since applying `asyncio` to CPU-bound work or multiprocessing to I/O-bound work both underperform the correct choice.
**Pitfalls:** using threads for CPU-bound work in a language with a global interpreter lock, expecting parallel speedup that doesn't materialize; assuming `async`/`await` alone provides parallelism when it only provides concurrency on a single thread.

## Race Conditions and Critical Section Protection
A race condition occurs when the correctness of a result depends on the unpredictable timing/interleaving of concurrent operations on shared mutable state; verify shared state access is protected by a mutex/lock, atomic operation, or by eliminating sharing entirely (message passing), and reproduce races with a stress test under load, not just manual testing.
```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100_000):
        with lock:            # without this, concurrent increments lose updates
            counter += 1
```
Run the unsynchronized version under a thread sanitizer or repeated stress test to observe the actual lost-update count, confirming the race is real rather than theoretical before adding synchronization overhead.
**Pitfalls:** assuming a single Python/JS statement like `counter += 1` is atomic when it's actually a read-modify-write sequence; adding locks so broadly that they serialize everything, eliminating the concurrency benefit entirely.

## Deadlock Conditions and Prevention
Deadlock requires four simultaneous conditions (mutual exclusion, hold-and-wait, no preemption, circular wait); breaking any one prevents it, the most common practical fix is enforcing a consistent global lock-acquisition order across all code paths. Verify actual lock-acquisition order in code handling multiple locks, since it's easy to introduce inconsistent order across different call sites.
```python
# Consistent ordering prevents circular wait between threads locking A and B
def transfer(account_a, account_b, amount):
    first, second = sorted([account_a, account_b], key=lambda a: a.id)
    with first.lock:
        with second.lock:
            account_a.balance -= amount
            account_b.balance += amount
```
Reproduce a suspected deadlock deterministically in a test by forcing thread interleaving (barriers/sleeps) rather than relying on production timing, which may only trigger the deadlock rarely.
**Pitfalls:** acquiring locks in different orders in different functions operating on the same pair of resources, creating a circular-wait deadlock that only manifests under specific timing; using a single global lock as a blunt "fix," reintroducing serialization bottlenecks.

## Async Runtime Models and the Cost of Blocking
Async runtimes (Node's event loop, Python's asyncio, Rust's Tokio) execute cooperative tasks on one or few OS threads; a single blocking (synchronous, CPU-heavy) call inside an async task stalls the entire runtime for all concurrent tasks sharing that thread. Verify no synchronous blocking calls exist inside async code paths by profiling actual event-loop lag under load.
```python
import asyncio, time

async def bad():
    time.sleep(2)          # blocks the entire event loop, not just this task

async def good():
    await asyncio.sleep(2) # yields control back to the event loop
```
Use runtime-specific instrumentation (Node's `perf_hooks.monitorEventLoopDelay`, Python's `asyncio` debug mode) to detect blocking calls in production rather than assuming code review catches every instance.
**Pitfalls:** calling a synchronous, blocking library function (a non-async DB driver, `requests.get`) inside an async handler, silently serializing all concurrent requests; assuming `await`-ing a function makes it non-blocking regardless of what it does internally.

# Computer Networking Fundamentals

## OSI/TCP-IP Layers and Troubleshooting Scope
Network problems should be diagnosed layer by layer (physical/link, network/IP, transport/TCP-UDP, application/HTTP) rather than guessing; verify connectivity at each layer with the appropriate tool before assuming the failure is at the application layer.
```bash
ping 8.8.8.8                 # network layer reachability
traceroute example.com       # path/routing diagnosis
nc -zv example.com 443       # transport layer: is the port open?
curl -v https://example.com  # application layer: actual HTTP exchange
```
Confirm which layer actually fails before applying an application-level fix (e.g., a "timeout" error might be a firewall dropping packets at the network layer, not a slow application).
**Pitfalls:** debugging application code for a connectivity issue that's actually a firewall/security-group rule blocking the port; assuming DNS resolution succeeded without explicitly verifying with `dig`/`nslookup`.

## DNS Resolution and Propagation
DNS resolves names to IP addresses through a hierarchy (root → TLD → authoritative nameserver) with caching at multiple levels (OS resolver, recursive resolver, browser); verify actual current records with a direct query to an authoritative or well-known public resolver rather than trusting local/stale cached results.
```bash
dig +short example.com A
dig +short example.com A @8.8.8.8      # bypass local resolver cache
dig +trace example.com                  # follow the full resolution chain
```
Confirm TTL values before assuming a DNS change has propagated everywhere, a low TTL propagates faster, but caches beyond your control (ISP resolvers) may still serve stale records for their own configured duration.
**Pitfalls:** assuming a DNS record change is instantly visible everywhere, ignoring TTL-based caching delays; testing only against a local machine's resolver cache instead of querying an authoritative nameserver directly.

## TLS/HTTPS Handshake and Certificate Validation
TLS establishes an encrypted channel via a handshake negotiating protocol version, cipher suite, and certificate validation (chain of trust to a trusted root CA); verify actual certificate details (expiry, SAN entries, issuing CA) with a direct inspection tool rather than assuming "the padlock icon" tells the whole story.
```bash
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -dates -subject -issuer
curl -vI https://example.com 2>&1 | grep -i "SSL\|subject\|expire"
```
Confirm certificate expiry dates and renewal automation (ACME/Let's Encrypt renewal jobs) are actually working by checking logs, not just assuming a cron job configured months ago still runs successfully.
**Pitfalls:** letting a certificate auto-renewal job fail silently until the certificate expires and causes an outage; assuming TLS 1.2/1.3 support without verifying the actual negotiated protocol version in a handshake trace.

## Load Balancing and Connection Behavior
Load balancers distribute traffic across backend instances using strategies (round-robin, least-connections, IP hash) with implications for session affinity and connection draining during deploys; verify actual behavior under a real rolling deployment rather than assuming graceful connection handling.
```bash
kubectl exec -it loadtest -- hey -z 30s -c 50 https://api.example.com/health
```
Confirm health-check endpoints used by the load balancer reflect true application readiness (not just process liveness), and verify connection draining actually waits for in-flight requests during a deploy by observing real request logs during a rollout.
**Pitfalls:** using a shallow liveness check as the load balancer's health endpoint, routing traffic to instances that are alive but unable to serve requests (e.g., DB connection lost); assuming zero-downtime deploys work without testing actual in-flight request behavior during a real rollout.

# Concurrency & Parallelism Fundamentals

## Atomic Operations and Lock-Free Data Structures
Atomic operations (compare-and-swap, fetch-and-add) provide thread-safe updates without traditional locks by leveraging hardware-level indivisible instructions, forming the basis of lock-free data structures; verify a claimed "lock-free" implementation actually avoids blocking under contention (some "lock-free" code still has retry loops that can theoretically starve) rather than assuming the label guarantees uniform progress.
```python
import threading

counter = 0
lock = threading.Lock()
# Python's GIL makes simple += operations effectively atomic for CPython specifically,
# but this is an implementation detail, not a language guarantee, verify per-runtime.
def increment_safely():
    global counter
    with lock:
        counter += 1
```
Verify atomic/lock-free claims with a stress test under heavy contention (many threads hammering the same atomic variable) and confirm the specific language runtime's memory model actually guarantees the ordering assumed, since atomicity alone doesn't imply memory visibility ordering on all architectures without explicit fences.
**Pitfalls:** assuming a "lock-free" algorithm is also "wait-free" (guaranteed per-thread progress), when many lock-free designs can still starve individual threads under adversarial scheduling; relying on a language's incidental atomicity (like CPython's GIL) as a portable guarantee, when it doesn't hold on other runtimes or under free-threaded builds.

## Thread Pools and Work Queue Sizing
Thread/worker pools bound the number of concurrent execution contexts to avoid unbounded resource consumption from unlimited thread creation; verify pool size is tuned against actual measured workload characteristics (CPU-bound work benefits from a pool size near core count, I/O-bound work can benefit from a much larger pool) rather than a copied default, and confirm the work queue itself has a bound to prevent unbounded memory growth under sustained overload.
```python
from concurrent.futures import ThreadPoolExecutor
import os

pool = ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) * 4))
futures = [pool.submit(fetch_url, url) for url in urls]
```
Verify actual pool utilization and queue depth under realistic load with monitoring, adjusting size based on observed saturation rather than a one-time guess, since production traffic patterns often differ from initial assumptions.
**Pitfalls:** sizing a thread pool by copying a number from an unrelated project without profiling the actual workload's CPU/IO characteristics; using an unbounded work queue in front of a fixed-size pool, allowing memory to grow without limit during a sustained traffic spike instead of applying backpressure.

## Futures, Promises, and Cancellation Propagation
Futures/Promises represent eventual results of async work; verify cancellation actually propagates through a chain of dependent operations rather than assuming cancelling a top-level future automatically stops in-flight underlying work (in many runtimes, cancellation is cooperative and requires the underlying operation to check for and honor a cancellation signal).
```python
import asyncio

async def fetch_with_timeout(url, timeout=5):
    task = asyncio.create_task(fetch(url))
    try:
        return await asyncio.wait_for(task, timeout=timeout)
    except asyncio.TimeoutError:
        task.cancel()   # cancellation is cooperative; fetch() must handle CancelledError
        raise
```
Verify the underlying operation actually stops consuming resources after cancellation (network connection closed, not just the Python-level task marked cancelled) by checking with actual connection/resource monitoring, since a "cancelled" future can leave real work still running in the background.
**Pitfalls:** assuming cancelling a future/promise immediately halts all underlying work, when many implementations only stop awaiting the result while the operation continues running in the background; forgetting to catch and handle a cancellation exception in cleanup code, leaking resources on the cancelled path.

## Green Threads, Fibers, and M:N Scheduling
Some runtimes multiplex many lightweight logical threads (green threads, fibers, goroutines, virtual threads) onto a smaller number of OS threads (M:N scheduling), providing concurrency at far lower memory/context-switch cost than one-OS-thread-per-task; verify the specific runtime's scheduling model (cooperative vs. preemptive, work-stealing behavior) before assuming a lightweight-thread abstraction behaves identically to OS threads for CPU-bound or blocking-syscall-heavy work.
```go
func main() {
    var wg sync.WaitGroup
    for i := 0; i < 100_000; i++ {   // cheap: goroutines cost a few KB of stack, not full OS threads
        wg.Add(1)
        go func() { defer wg.Done(); doWork() }()
    }
    wg.Wait()
}
```
Verify a blocking syscall inside a green-thread/fiber model doesn't unexpectedly block the underlying OS thread it's scheduled on (some runtimes handle this transparently via async syscall integration, others don't), since this determines whether spawning many lightweight threads actually achieves the intended concurrency.
**Pitfalls:** assuming all lightweight-thread runtimes transparently handle blocking syscalls without stalling the underlying OS thread, when this varies significantly by language/runtime implementation; spawning an extremely large number of lightweight threads without verifying the scheduler's actual overhead characteristics at that scale.

# Computer Networking Fundamentals

## HTTP/1.1, HTTP/2, and HTTP/3 Protocol Differences
HTTP versions differ substantially in connection behavior: HTTP/1.1 uses one request per connection (or pipelining, rarely used) with typical browser connection-per-host limits, HTTP/2 multiplexes many streams over one TCP connection, and HTTP/3 runs over QUIC (UDP-based) to eliminate TCP head-of-line blocking; verify which protocol version is actually negotiated for a given connection with direct inspection rather than assuming from server configuration alone.
```bash
curl -v --http2 https://example.com 2>&1 | grep -i "HTTP/2\|ALPN"
curl -v --http3 https://example.com 2>&1 | grep -i "HTTP/3"
```
Verify actual performance benefits of upgrading protocol versions with real measurements (HTTP/2's multiplexing benefit can be reduced by head-of-line blocking at the TCP layer under packet loss, which HTTP/3/QUIC specifically addresses), rather than assuming a newer version automatically improves every workload.
**Pitfalls:** assuming HTTP/2 is negotiated just because the server supports it, without verifying ALPN negotiation actually selected it for the specific client/network path; assuming HTTP/3's UDP-based transport works identically everywhere, without accounting for networks/firewalls that block or throttle UDP traffic.

## NAT, Private Addressing, and Port Forwarding
Network Address Translation lets multiple devices on a private network share one public IP, which affects inbound connectivity (a device behind NAT generally cannot be reached from outside without explicit port forwarding or NAT traversal techniques like STUN/TURN); verify actual reachability with an external testing tool rather than assuming a service is internet-accessible just because it's running.
```bash
curl ifconfig.me                      # public-facing IP as seen by the internet
nc -zv -w3 <public-ip> 8080           # test from an external vantage point, not localhost
```
Verify STUN/TURN fallback is actually configured and tested for peer-to-peer connections (WebRTC) that must traverse NAT, since a purely direct-connection assumption fails for a meaningful fraction of real-world network topologies (symmetric NATs, restrictive firewalls).
**Pitfalls:** assuming a service bound to `0.0.0.0` on a local machine is reachable from the internet without accounting for NAT/router configuration; building peer-to-peer functionality without a TURN relay fallback, failing silently for users behind restrictive NAT types.

## Content Delivery Networks and Edge Caching
CDNs cache content at geographically distributed edge nodes to reduce latency and origin load; verify actual cache-hit behavior with response headers (`X-Cache: HIT/MISS`, `Age`) rather than assuming a CDN is effectively caching just because it's configured in front of an origin, and confirm cache-key configuration (query strings, headers, cookies) matches intent, since an overly broad cache key fragments the cache and an overly narrow one serves wrong content to different users.
```bash
curl -sI https://example.com/api/products | grep -i "x-cache\|age\|cache-control"
```
Verify cache invalidation/purge actually propagates to all edge nodes within the expected time window by testing a real purge request and re-fetching from multiple geographic vantage points, rather than assuming instantaneous global invalidation.
**Pitfalls:** caching personalized or user-specific responses with a cache key that ignores the identifying cookie/header, serving one user's private data to another; assuming a CDN purge is instantaneous everywhere, when propagation to all edge nodes can take a meaningful, provider-specific amount of time.

## Network Security: Firewalls, Segmentation, and Zero-Trust Networking
Network-level security (firewalls, security groups, segmentation into isolated subnets/VLANs) limits blast radius when a single host is compromised; verify actual firewall rules with a direct test from outside the intended trust boundary rather than assuming a rule is enforced just because it's declared in configuration, and confirm segmentation genuinely isolates sensitive systems (a database subnet shouldn't be reachable from a public-facing web tier's subnet beyond the specific required port).
```bash
nmap -p 1-1000 <target-ip>            # verify only intended ports are actually reachable, from an external vantage point
```
Verify east-west (internal, service-to-service) traffic is also subject to explicit allow-listing under a zero-trust network model, rather than assuming anything inside the perimeter is implicitly trusted once it's past the edge firewall.
**Pitfalls:** configuring a firewall rule and never verifying it from an actual external network vantage point, missing a misconfiguration that leaves a port open; trusting all internal/east-west traffic implicitly once inside a perimeter firewall, allowing lateral movement after a single host is compromised.
