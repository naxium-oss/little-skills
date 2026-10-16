# Authentication & Authorization Fundamentals

## Session-Based versus Token-Based Authentication
Session auth stores state server-side (a session ID cookie referencing server memory/DB) while token auth (JWT) embeds claims in a signed, stateless token the client holds; verify which model a system actually uses before reasoning about revocation, since stateless tokens can't be invalidated server-side without extra infrastructure (a denylist or short expiry).
```http
Set-Cookie: session_id=abc123; HttpOnly; Secure; SameSite=Lax; Max-Age=3600
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```
Confirm actual logout behavior: session-based logout can immediately invalidate server-side, while JWT "logout" typically just discards the client copy, the token remains valid until expiry unless a revocation list is checked.
**Pitfalls:** assuming JWT "logout" immediately invalidates the token everywhere; storing JWTs in `localStorage` (accessible to any XSS payload) instead of an `HttpOnly` cookie when persistent storage is needed.

## Password Storage and Verification
Passwords must never be stored in plaintext or reversibly encrypted; use a slow, salted hashing algorithm designed for passwords (bcrypt, scrypt, Argon2), and verify the actual work factor/cost parameter is tuned for current hardware, not a decade-old default.
```javascript
import argon2 from "argon2";
const hash = await argon2.hash(password, { type: argon2.argon2id, memoryCost: 19456, timeCost: 2 });
const valid = await argon2.verify(hash, candidatePassword);
```
Verify the configured cost parameters against current OWASP recommendations (checked at implementation time, since guidance is periodically revised as hardware improves) rather than trusting library defaults blindly.
**Pitfalls:** using fast general-purpose hashes (MD5, SHA-256 alone) for passwords, making brute-force trivial with GPUs; hardcoding a cost factor once and never revisiting it as hardware gets faster.

## OAuth 2.0 and OpenID Connect Flows
OAuth 2.0 is an authorization delegation protocol (not authentication by itself); OpenID Connect adds an identity layer (ID tokens) on top. Verify which grant type is actually appropriate: Authorization Code with PKCE for browser/mobile apps, Client Credentials for machine-to-machine, since using the wrong flow creates real security gaps.
```
GET /authorize?response_type=code&client_id=abc&redirect_uri=https://app.example.com/callback
    &scope=openid profile email&code_challenge=E9Melhoa2...&code_challenge_method=S256
```
Verify `state` and PKCE `code_verifier`/`code_challenge` are actually implemented and checked, not just present in the request, since omitting server-side validation defeats their CSRF/interception protections.
**Pitfalls:** using the deprecated Implicit flow for a new SPA instead of Authorization Code + PKCE; treating an OAuth access token as proof of identity without validating an actual OIDC ID token's signature and claims.

## Authorization Models: RBAC, ABAC, and Object-Level Checks
Role-Based Access Control (RBAC) grants permissions via roles; Attribute-Based Access Control (ABAC) evaluates policies against resource/user/context attributes for finer granularity. Regardless of model, every request must verify object-level authorization (does *this* user own *this specific* resource), not just endpoint-level role checks, missing this is the source of IDOR (Insecure Direct Object Reference) vulnerabilities.
```javascript
app.get("/invoices/:id", requireRole("customer"), async (req, res) => {
  const invoice = await db.invoices.findById(req.params.id);
  if (invoice.customerId !== req.user.id) return res.status(403).end();  // object-level check
  res.json(invoice);
});
```
Verify object-level checks with an actual test that requests another user's resource ID while authenticated as a different user, since role checks alone pass this test incorrectly.
**Pitfalls:** checking only that a user has the "customer" role without verifying they own the specific requested resource; relying on client-side hiding of unauthorized UI elements as if it were a real authorization boundary.

# Automated Testing Frameworks

## Test Pyramid and Framework Selection Grounding
Unit, integration, and end-to-end tests trade off speed, isolation, and realism; verify the actual test framework and version in a project (Jest, Vitest, pytest, JUnit) before assuming API/config syntax, since matcher and mocking APIs differ even between similar-seeming tools.
```bash
npx vitest --version
npx jest --version
```
Confirm which test runner actually executes in CI by reading the pipeline config, not just what's listed in `package.json` scripts, since teams sometimes have stale or unused scripts.
**Pitfalls:** writing tests using Jest-specific globals (`jest.fn()`) in a project that migrated to Vitest, causing silent no-ops or import errors; over-investing in slow E2E tests for logic better covered by fast unit tests.

## Test Isolation and Fixture Design
Tests should be independent and repeatable regardless of execution order; shared mutable fixtures (a global test database, module-level state) cause flaky failures that only appear when tests run in a particular order or in parallel. Verify isolation by running the suite with randomized order and in parallel.
```javascript
beforeEach(async () => {
  await db.query("BEGIN");
});
afterEach(async () => {
  await db.query("ROLLBACK");   // isolate each test's DB writes
});
```
Run the suite with `--randomize`/`--shuffle` (framework-dependent flag) periodically to surface order-dependent flakiness that a fixed default order would hide indefinitely.
**Pitfalls:** relying on test execution order for setup (test B assumes test A already ran and created data); sharing one database/connection across parallel test workers without transaction isolation, causing cross-test data races.

## Mocking, Stubbing, and Fidelity Tradeoffs
Mocks replace real dependencies (network calls, databases, clocks) to isolate the unit under test and make tests fast/deterministic; verify a mock's behavior actually matches the real dependency's contract, since an outdated or oversimplified mock can pass tests while the real integration is broken.
```javascript
vi.mock("./paymentGateway", () => ({
  charge: vi.fn().mockResolvedValue({ status: "succeeded", id: "ch_123" }),
}));
```
Pair unit tests using mocks with a smaller number of real integration/contract tests against the actual dependency (or a high-fidelity sandbox) to catch drift between the mock's assumed behavior and reality.
**Pitfalls:** mocking so extensively that a test verifies nothing but the mock's own configuration; letting a mock's response shape drift from the real API's actual current shape without periodic contract verification.

## Coverage Metrics and Their Limits
Code coverage (line, branch, statement) measures what code executed during tests, not whether it was correctly verified; a test can execute every line with zero meaningful assertions and still show 100% coverage. Verify coverage reports are interpreted alongside actual assertion quality, not treated as a standalone correctness proxy.
```bash
npx vitest run --coverage
pytest --cov=src --cov-report=term-missing
```
Use mutation testing (deliberately introducing bugs and checking tests catch them) periodically to validate that high coverage numbers correspond to actually meaningful assertions, especially for critical business logic paths.
**Pitfalls:** treating a coverage threshold (e.g., "80%") as a proxy for quality and writing assertion-free tests just to hit the number; ignoring branch coverage gaps where only the happy path of an `if/else` was ever executed.

# Authentication & Authorization Fundamentals

## Multi-Factor Authentication and Recovery Flow Design
MFA (TOTP, WebAuthn/passkeys, SMS) significantly reduces account-takeover risk, but verify the actual factor strength (SMS is phishable/SIM-swappable, TOTP is stronger, WebAuthn/passkeys are phishing-resistant) matches the threat model, and confirm recovery flows (backup codes, account recovery) don't create a weaker bypass path than the MFA itself protects against.
```javascript
import { authenticator } from "otplib";
const secret = authenticator.generateSecret();
const isValid = authenticator.verify({ token: userInput, secret });
```
Verify backup/recovery codes are single-use, securely hashed at rest, and rate-limited on verification, since a poorly designed recovery flow is a common way attackers bypass MFA entirely.
**Pitfalls:** treating SMS-based MFA as equivalent in strength to TOTP/WebAuthn when designing threat models for high-value accounts; implementing a recovery flow that doesn't require re-verification of identity, effectively creating a backdoor around MFA.

## CSRF Protection and SameSite Cookie Configuration
Cross-Site Request Forgery exploits a browser's automatic inclusion of credentials (cookies) on requests to a target site initiated from a different origin; verify actual protection via CSRF tokens and/or the `SameSite` cookie attribute (`Lax` blocks most cross-site POSTs by default, `Strict` is more restrictive, `None` requires `Secure` and disables this protection entirely).
```javascript
res.cookie("session", token, { httpOnly: true, secure: true, sameSite: "lax" });
```
```html
<form method="POST" action="/transfer">
  <input type="hidden" name="csrf_token" value="{{csrfToken}}" />
</form>
```
Verify state-changing endpoints (POST/PUT/DELETE) actually validate a CSRF token server-side even when `SameSite=Lax` is set, since relying on cookie attributes alone doesn't protect against all cross-site request vectors (like top-level navigations in some edge cases) or older browsers with weaker `SameSite` support.
**Pitfalls:** relying solely on `SameSite=Lax` without server-side CSRF token validation for high-value state-changing actions; setting `SameSite=None` for cross-site embedding convenience without understanding it disables this specific protection layer entirely.

## API Key and Service-to-Service Authentication
Machine-to-machine authentication (API keys, mTLS, signed JWTs via client credentials flow) needs different handling than user-facing auth, verify API keys are scoped to minimum necessary permissions, rotatable without downtime (supporting overlapping old/new key validity), and never embedded in client-side code where they're publicly extractable.
```javascript
app.use((req, res, next) => {
  const key = req.headers["x-api-key"];
  const scope = apiKeyStore.getScope(key);
  if (!scope) return res.status(401).end();
  req.scope = scope;
  next();
});
```
Verify a key rotation runbook is actually tested (issue new key, confirm both old and new work during a transition window, then revoke old) rather than assuming rotation is simple until an actual incident forces an untested emergency rotation.
**Pitfalls:** embedding a service API key directly in client-side JavaScript or a mobile app binary, where it's trivially extractable; having no tested key-rotation procedure, forcing a risky big-bang rotation during an active security incident.

## Zero Trust and Defense-in-Depth Authorization Layering
A zero-trust posture assumes no implicit trust based on network location alone (internal network ≠ automatically trusted); verify authorization checks exist at every layer an attacker could reach (API gateway, service mesh, application code, database row-level security) rather than relying on a single perimeter check, since a single bypassed layer shouldn't grant full access.
```sql
-- PostgreSQL row-level security as a defense-in-depth layer beneath the application check
ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON invoices USING (tenant_id = current_setting('app.tenant_id')::uuid);
```
Verify each layer is independently tested (a database query run with an unexpected/attacker-controlled tenant context should still be blocked by RLS even if application-layer authorization were somehow bypassed) rather than assuming layers are redundant and only testing one.
**Pitfalls:** relying entirely on application-layer authorization checks with no database or infrastructure-level backstop, so a single application bug grants full cross-tenant access; treating internal-network services as inherently trusted, skipping authentication between them entirely.

# Automated Testing Frameworks

## End-to-End Testing with Browser Automation
End-to-end tests (Playwright, Cypress, Selenium) exercise the full application stack through a real or headless browser, catching integration issues unit/mock-based tests miss, at the cost of speed and flakiness; verify selectors are resilient to UI refactors (prefer accessible roles/test-ids over brittle CSS class chains) and that waits are condition-based, not fixed sleep delays.
```javascript
import { test, expect } from "@playwright/test";

test("user can complete checkout", async ({ page }) => {
  await page.goto("/cart");
  await page.getByRole("button", { name: "Checkout" }).click();
  await expect(page.getByText("Order confirmed")).toBeVisible();
});
```
Verify test stability by running the suite repeatedly (`--repeat-each=5`) in CI-like conditions before merging, since E2E flakiness often only appears under CI's different timing/resource characteristics versus a local machine.
**Pitfalls:** using fixed `sleep(2000)` waits instead of condition-based waiting (`waitFor`, auto-retrying assertions), causing flaky failures under variable CI load; selecting elements by brittle CSS class names that change with every styling refactor instead of stable roles or test IDs.

## Test Doubles: Spies, Stubs, Fakes, and Mocks
Test doubles serve distinct purposes, spies record calls for later assertion, stubs return canned responses, fakes provide a working lightweight implementation (an in-memory database), and mocks combine stubbing with built-in expectation verification; verify the chosen double type actually matches the test's intent, since overusing strict mocks couples tests tightly to implementation details rather than observable behavior.
```javascript
const emailSpy = vi.spyOn(mailer, "send");
await registerUser(newUser);
expect(emailSpy).toHaveBeenCalledWith(expect.objectContaining({ to: newUser.email }));

class InMemoryUserRepo {   // fake: real logic, no external dependency
  #users = new Map();
  save(user) { this.#users.set(user.id, user); }
  find(id) { return this.#users.get(id); }
}
```
Verify tests assert observable behavior/outcomes rather than internal implementation calls wherever possible, since over-mocking internal method calls makes tests brittle to safe refactors that don't change actual behavior.
**Pitfalls:** asserting on exact internal method call sequences (implementation detail) instead of final observable state, breaking tests on every safe refactor; using a fake that has drifted from matching the real dependency's actual constraints (e.g., an in-memory fake DB that doesn't enforce the real database's unique constraints).

## Continuous Test Suite Health and Flaky Test Management
A test suite's value depends on developers trusting its results; flaky tests (intermittently failing without code changes) erode that trust and lead to ignored failures, so verify flaky tests are tracked, quarantined, and fixed with priority rather than allowed to accumulate as "known failures" that get re-run until green.
```bash
npx jest --testPathPattern=checkout --repeat-each=20   # stress-test for flakiness before merging
```
Track flaky test rates over time with CI analytics (rerun counts, pass-rate trends) and treat a rising flake rate as a leading indicator of infrastructure or test-design problems, not just an annoyance to route around.
**Pitfalls:** habitually re-running a failing CI job until it passes without investigating why it flaked, normalizing a culture of ignoring intermittent failures; quarantining a flaky test indefinitely without a tracked follow-up to actually fix or remove it.

## Contract and Schema Validation Testing
Contract tests verify that a service's actual request/response shape matches a shared, versioned contract (OpenAPI, JSON Schema, or consumer-driven contracts like Pact) without requiring both sides to be deployed together, catching integration breakage earlier and cheaper than full E2E tests across services.
```javascript
import { Pact } from "@pact-foundation/pact";
provider.addInteraction({
  state: "an order with id 42 exists",
  uponReceiving: "a request for order 42",
  withRequest: { method: "GET", path: "/orders/42" },
  willRespondWith: { status: 200, body: { id: 42, status: "shipped" } },
});
```
Verify the provider side actually runs the same contract as a "provider verification" step in its own CI, since a consumer-only contract test with no provider-side verification gives false confidence that the real API matches.
**Pitfalls:** writing consumer-driven contract tests without ever running provider-side verification, giving a false sense of integration safety; letting a shared contract file drift out of sync with the actual OpenAPI spec used for other tooling, creating two competing sources of truth.
