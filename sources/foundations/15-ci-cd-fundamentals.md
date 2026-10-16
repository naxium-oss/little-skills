# CI/CD Fundamentals

## Pipeline Stage Design and Fail-Fast Ordering
A CI/CD pipeline should order stages to fail fast and cheap (lint/format → unit tests → build → integration tests → deploy), avoiding expensive stages running before cheap ones would have already caught an obvious error. Verify the actual configured stage order in the pipeline file, not the assumed logical order.
```yaml
stages: [lint, test, build, integration, deploy]
lint:
  script: [npm run lint]
test:
  script: [npm test]
  needs: [lint]
```
Confirm stage dependencies (`needs`/`depends_on`) actually enforce the intended ordering and short-circuit on failure, since a misconfigured pipeline can run all stages in parallel regardless of declared order.
**Pitfalls:** running a slow integration/E2E suite before a fast lint/unit stage, wasting compute and developer wait time on failures that could've been caught in seconds; assuming stage order in a YAML file guarantees execution order without checking actual dependency declarations.

## Environment Promotion and Deployment Strategies
Code should move through consistent environments (dev → staging → production) with the same build artifact promoted forward rather than rebuilt per environment, ensuring what's tested is exactly what's deployed. Verify the pipeline actually reuses one immutable artifact rather than rebuilding at each stage, which can introduce drift (different dependency resolution, different commit).
```yaml
deploy_staging:
  script: [./deploy.sh --artifact "$CI_COMMIT_SHA" --env staging]
deploy_production:
  script: [./deploy.sh --artifact "$CI_COMMIT_SHA" --env production]
  when: manual
  needs: [deploy_staging]
```
Confirm rollback procedures are tested (not just documented) by executing an actual rollback in staging periodically, since an untested rollback script is a common cause of extended incidents.
**Pitfalls:** rebuilding the artifact separately for staging and production, allowing subtle version drift between what was tested and what ships; having no tested rollback path, discovering during an incident that the rollback script itself is broken.

## Secrets Management in CI Pipelines
CI secrets (API keys, deploy credentials) must be stored in the CI platform's encrypted secret store, never in the repository or plain pipeline YAML; verify actual secret masking in logs, since some tools only mask exact-match strings and leak secrets when transformed (base64-encoded, concatenated) before printing.
```yaml
deploy:
  script:
    - echo "Deploying with token length ${#DEPLOY_TOKEN}"   # avoid ever echoing the secret itself
  variables:
    DEPLOY_TOKEN: $DEPLOY_TOKEN   # sourced from CI secret store, not committed
```
Confirm secrets aren't exposed to untrusted contexts (fork pull request pipelines) by checking the CI platform's actual documented behavior for secret exposure on forked-PR triggered runs.
**Pitfalls:** printing an environment variable for debugging that happens to contain a secret, leaking it into build logs retained for months; exposing repository secrets to pipeline runs triggered by untrusted fork pull requests.

## Build Caching and Reproducibility
Dependency and build caches speed up CI runs but must use correct cache keys (based on lockfile hashes, not just branch name) to avoid serving stale dependencies after a lockfile change. Verify cache hit/miss behavior in pipeline logs rather than assuming caching "just works."
```yaml
cache:
  key:
    files: [package-lock.json]
  paths: [node_modules/]
```
Periodically run a clean, cache-disabled build to confirm the project still builds reproducibly from scratch, since accumulated cache state can mask a broken from-scratch build.
**Pitfalls:** keying a cache only by branch name, silently serving stale dependencies after a lockfile update on the same branch; never testing a cold/no-cache build, only discovering a reproducibility break during an actual cache invalidation incident.

# Data Structures & Algorithms Fundamentals

## Big-O Complexity Analysis and Verification
Asymptotic complexity describes growth rate, not actual speed at small input sizes; verify a claimed complexity class empirically with increasing input sizes and timing measurements rather than trusting a memorized label, since real-world constant factors and cache effects matter for practical performance.
```python
import time
for n in [10_000, 100_000, 1_000_000]:
    data = list(range(n))
    start = time.perf_counter()
    _ = sorted(data, reverse=True)
    print(n, time.perf_counter() - start)
```
Confirm whether a claimed O(n log n) algorithm's measured runtime roughly follows that growth curve across several magnitudes of `n`, distinguishing genuine algorithmic complexity from a fixed but large constant overhead.
**Pitfalls:** assuming a "faster" algorithm on paper is actually faster for the specific input sizes in production, ignoring constant-factor and cache-locality effects; benchmarking on tiny inputs where overhead dominates and complexity differences don't yet appear.

## Hash Tables and Amortized Analysis
Hash tables provide expected O(1) average-case lookup/insert via a hash function and collision resolution (chaining or open addressing); worst-case degrades to O(n) with poor hash distribution or adversarial input. Verify hash function quality and load factor rather than assuming O(1) universally holds.
```python
d = {}
for i in range(1_000_000):
    d[i] = i * 2
print(len(d), d[999_999])   # average O(1) lookup, but verify with timing under real key distributions
```
Confirm whether keys are attacker-controlled (e.g., HTTP headers used as dict keys), some languages randomize hash seeds specifically to prevent hash-flooding denial-of-service attacks exploiting worst-case collision behavior.
**Pitfalls:** assuming dictionary/hash-map operations are always O(1) regardless of key distribution or adversarial input; iterating a hash map and assuming insertion or sorted order without verifying the specific language/version's actual guarantees.

## Trees, Graphs, and Traversal Correctness
Tree/graph traversal choice (BFS for shortest unweighted path/level-order, DFS for path existence/topological sort, Dijkstra/A* for weighted shortest path) must match the actual problem constraints; verify graph properties (directed/undirected, weighted/unweighted, cyclic) before selecting an algorithm.
```python
from collections import deque

def bfs_shortest_path(graph, start, goal):
    visited, queue = {start}, deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None
```
Verify cycle-handling explicitly with a visited-set/color-marking scheme, and confirm whether the graph can have negative edge weights before choosing Dijkstra (requires non-negative weights) over Bellman-Ford.
**Pitfalls:** using DFS for shortest-path-in-unweighted-graph problems, giving a valid but not necessarily shortest path; running Dijkstra on a graph with negative edge weights, silently producing incorrect results without an error.

## Sorting Stability and Algorithm Selection
Sorting algorithms differ in stability (whether equal elements retain relative order), time complexity, and memory use; verify a language's built-in sort's actual guaranteed algorithm and stability (Python's Timsort is stable; many C `qsort` implementations are not) before relying on stability for multi-key sorts.
```python
records = [{"name": "b", "score": 1}, {"name": "a", "score": 1}]
records.sort(key=lambda r: r["score"])   # stable: original relative order of ties preserved
records.sort(key=lambda r: r["name"])    # can then sort by name preserving score-tie order, pattern for multi-key sort
```
Confirm whether a downstream requirement (e.g., "sort by date, then by name, preserving insertion order for exact duplicates") actually depends on stability before choosing an unstable sort for a performance gain.
**Pitfalls:** relying on sort stability in a language/library where the underlying algorithm doesn't guarantee it; re-sorting data assuming a previous sort's order is preserved without verifying the specific sort call is stable.

# CI/CD Fundamentals

## Feature Flags and Progressive Delivery
Feature flags decouple deployment (code shipped to production) from release (feature exposed to users), enabling gradual rollout, kill switches, and trunk-based development without long-lived feature branches; verify flag evaluation is actually fast and reliable (a flag service outage shouldn't take down the whole app) and that stale flags are cleaned up after full rollout rather than accumulating indefinitely as untested dead branches.
```javascript
if (await flags.isEnabled("new-checkout-flow", { userId })) {
  return renderNewCheckout();
}
return renderLegacyCheckout();
```
Verify a flag's default/fallback behavior when the flag service is unreachable (fail open to old behavior vs. fail closed) matches the risk profile of the specific feature before relying on it in a critical path.
**Pitfalls:** never removing flags after a feature fully ships, accumulating stale conditional branches that make code harder to reason about and test; not defining a safe fallback behavior for flag-service downtime, causing an outage in the flagging system to cascade into application errors.

## Blue-Green and Canary Deployment Verification
Blue-green deployments run two full production environments and switch traffic atomically, enabling instant rollback; canary deployments gradually shift a small percentage of traffic to the new version while monitoring key metrics before a full rollout. Verify the actual traffic-shifting mechanism (load balancer weight, DNS, service mesh routing) and confirm automated rollback triggers on real metric degradation, not just manual observation.
```yaml
canaryStrategy:
  steps:
    - setWeight: 10
    - pause: { duration: 300 }
    - analysis: { templates: [{ templateName: error-rate-check }] }
    - setWeight: 50
    - pause: { duration: 300 }
    - setWeight: 100
```
Verify the analysis/monitoring window is long enough to catch delayed failure modes (memory leaks, slow-building error rates) rather than only fast, obvious regressions, since a too-short canary window gives false confidence.
**Pitfalls:** running a canary for too short a duration to catch slow-onset regressions (memory leaks, gradual latency creep) before promoting to 100%; lacking automated rollback triggers, requiring a human to notice a regression during an on-call-unfriendly time window.

## Infrastructure Pipeline Testing and Staging Parity
Deployment pipelines themselves need testing, verify a staging environment is representative enough of production (same infrastructure-as-code templates, comparable data volume/shape, same third-party service configurations) that a "works in staging" result is actually predictive, rather than a superficially similar environment that misses real integration issues.
```bash
terraform workspace select staging
terraform plan -var-file=staging.tfvars    # same templates as production, different variable values
```
Periodically run a full disaster-recovery/rollback drill against staging to verify the pipeline's rollback path is actually exercised and functional, not just theoretically present in a runbook.
**Pitfalls:** letting staging environment configuration drift significantly from production over time (different instance sizes, missing third-party integrations), reducing its predictive value; never actually testing the documented rollback procedure until a real incident forces it, discovering it's broken under pressure.

## Build Provenance and Supply Chain Verification in Pipelines
Modern CI/CD should produce verifiable build provenance (SLSA-style attestations, signed artifacts) so a deployed artifact can be traced back to the exact source commit, dependencies, and build environment that produced it; verify signing/attestation actually happens and is checked at deploy time, not merely generated and ignored.
```bash
cosign sign --key cosign.key my-registry/app:1.4.0
cosign verify --key cosign.pub my-registry/app:1.4.0
slsa-verifier verify-image my-registry/app:1.4.0 --source-uri github.com/org/repo
```
Verify the deployment step actually rejects unsigned or attestation-mismatched artifacts rather than only logging a warning, since an unenforced verification step provides no real security benefit.
**Pitfalls:** generating build attestations/signatures but never actually enforcing verification at deploy time, providing a false sense of supply-chain security; signing artifacts with a key stored insecurely in the same pipeline that consumes it, undermining the trust boundary the signature is meant to provide.

# Data Structures & Algorithms Fundamentals

## Dynamic Programming: Memoization and Tabulation
Dynamic programming solves problems with overlapping subproblems and optimal substructure by caching subproblem results (memoization, top-down) or building up a table iteratively (tabulation, bottom-up); verify a problem actually exhibits overlapping subproblems (not just recursion) before applying DP, since applying it to a problem without genuine overlap adds memory overhead for no benefit.
```python
def fib_memo(n, cache={}):
    if n in cache: return cache[n]
    if n <= 1: return n
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]

def fib_tabulation(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```
Verify actual memory usage tradeoffs between memoization (can use more memory for the recursion stack plus cache) and tabulation (often allows O(1) space with careful rolling-array optimization) for the specific problem's constraints.
**Pitfalls:** applying memoization to a problem whose subproblems don't actually overlap, adding cache overhead without any speedup; using a mutable default argument as a cache across unrelated calls (as in naive Python examples), leaking state between logically independent invocations.

## Two-Pointer and Sliding Window Techniques
Two-pointer and sliding-window techniques solve array/string problems in O(n) by maintaining a moving range instead of nested loops (O(n²)); verify the specific invariant maintained by the window (sum, count, uniqueness) is correctly updated on every expansion and contraction, since an off-by-one error in window boundary adjustment is the most common bug in this pattern.
```python
def longest_unique_substring(s: str) -> int:
    seen = {}
    left = longest = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        longest = max(longest, right - left + 1)
    return longest
```
Trace through a small example by hand (or with print statements) verifying the window's invariant holds at every step, especially at the boundaries (empty window, single element, full array) which are the most common sources of off-by-one bugs.
**Pitfalls:** forgetting to update the window's tracking state (a frequency map, running sum) symmetrically on both expansion and contraction, causing incorrect results after the window shrinks; not handling empty-input or single-element edge cases explicitly, causing index errors.

## Binary Search and Its Variants
Binary search finds a target (or a boundary condition) in O(log n) on sorted data, but verify the search space is genuinely sorted/monotonic with respect to the condition being checked, binary search generalizes beyond "find exact value" to "find the first/last position satisfying a predicate," a pattern often missed by only memorizing the classic exact-match template.
```python
def find_first_true(predicate, lo: int, hi: int) -> int:
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if predicate(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo   # first index where predicate(index) is True
```
Verify loop-termination and boundary conditions (`lo <= hi` vs `lo < hi`, `mid = lo + (hi-lo)//2` to avoid overflow in languages with fixed-width integers) with small hand-traced examples of size 0, 1, and 2 before trusting the implementation on larger inputs.
**Pitfalls:** using `(lo + hi) // 2` in languages with fixed-width integer overflow risk instead of `lo + (hi - lo) // 2`; applying binary search to data that isn't actually sorted/monotonic with respect to the target predicate, silently returning wrong results without an error.

## Space-Time Tradeoffs and Caching Strategies
Many algorithmic optimizations trade memory for speed (precomputed lookup tables, memoization, indexes) or vice versa (streaming algorithms that trade some accuracy/completeness for constant memory); verify the actual memory budget and latency requirements of the deployment environment before choosing a tradeoff point, since an optimization ideal for a server with abundant RAM may be wrong for a memory-constrained edge device.
```python
import functools

@functools.lru_cache(maxsize=10_000)
def expensive_lookup(key: str) -> dict:
    return compute_expensive_result(key)
```
Verify cache size limits (`maxsize`) are tuned against actual working-set size observed in production, since an unbounded cache risks memory exhaustion while an undersized one thrashes and provides little benefit.
**Pitfalls:** using an unbounded in-memory cache in a long-running process, eventually causing memory exhaustion under real production key cardinality; choosing a precomputed-table approach for a memory-constrained environment without verifying the table actually fits within budget.
