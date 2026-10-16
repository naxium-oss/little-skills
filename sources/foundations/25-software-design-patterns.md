# Software Design Patterns

## Factory and Builder Patterns for Object Construction
Factory patterns centralize object creation logic so callers depend on an interface rather than concrete constructors, useful when construction requires conditional logic or configuration; Builder patterns handle objects with many optional parameters step-by-step, avoiding unwieldy constructors ("telescoping constructor" anti-pattern). Verify a factory/builder is actually solving a real construction complexity problem, not adding indirection to a trivial `new`.
```typescript
class HttpClientBuilder {
  private timeoutMs = 5000;
  private headers: Record<string, string> = {};
  withTimeout(ms: number): this { this.timeoutMs = ms; return this; }
  withHeader(key: string, value: string): this { this.headers[key] = value; return this; }
  build(): HttpClient { return new HttpClient(this.timeoutMs, this.headers); }
}
const client = new HttpClientBuilder().withTimeout(10_000).withHeader("X-Api-Key", key).build();
```
Verify the pattern is warranted by checking if the target class truly has enough optional/conditional construction paths to justify it, applying Builder to a two-field class adds needless ceremony.
**Pitfalls:** wrapping a trivial constructor in a Factory "for future flexibility" that never materializes; making a Builder mutable and shared across threads without considering thread-safety of the builder instance itself.

## Observer and Publish-Subscribe Patterns
The Observer pattern lets objects (subscribers) react to state changes in a subject without tight coupling; verify subscription cleanup is handled (unsubscribing on teardown) to prevent memory leaks from observers that outlive their intended lifecycle, a very common real-world bug in UI and event-driven systems.
```javascript
class EventBus {
  #listeners = new Map();
  on(event, handler) {
    if (!this.#listeners.has(event)) this.#listeners.set(event, new Set());
    this.#listeners.get(event).add(handler);
    return () => this.#listeners.get(event).delete(handler);   // unsubscribe function
  }
  emit(event, payload) {
    this.#listeners.get(event)?.forEach((handler) => handler(payload));
  }
}
```
Verify with a memory profiler or explicit lifecycle test that unsubscribing actually removes the reference, especially in frameworks where component unmount doesn't automatically clean up manually registered listeners.
**Pitfalls:** subscribing to an event bus/observable in a component without capturing and calling the returned unsubscribe function on teardown, leaking memory and causing handlers to fire on unmounted/stale state; broadcasting synchronously to observers that themselves mutate the observer list during iteration, causing skipped or duplicated notifications.

## Strategy Pattern versus Conditional Logic
The Strategy pattern extracts interchangeable algorithms behind a common interface, replacing large conditional/switch blocks that branch on type; verify the actual variability is real (multiple algorithms genuinely needed, likely to grow) before introducing the pattern, since a single stable algorithm doesn't need strategy indirection.
```python
from typing import Protocol

class DiscountStrategy(Protocol):
    def apply(self, total: float) -> float: ...

class PercentageDiscount:
    def __init__(self, pct: float): self.pct = pct
    def apply(self, total: float) -> float: return total * (1 - self.pct)

def checkout(total: float, strategy: DiscountStrategy) -> float:
    return strategy.apply(total)
```
Verify the strategy interface's method signature is stable across all current and reasonably foreseeable implementations before finalizing it, since a poorly designed interface forces awkward parameter additions later.
**Pitfalls:** introducing Strategy for a single, unlikely-to-change algorithm, adding indirection with no real benefit; designing the strategy interface too narrowly, forcing every new strategy variant to hack around missing parameters.

## Anti-Patterns: God Objects and Premature Abstraction
A "God Object" accumulates too many responsibilities, becoming a bottleneck for understanding and change; premature abstraction (building generic, configurable systems before real variability is observed) adds complexity that doesn't pay for itself. Verify a proposed abstraction is backed by at least two or three real concrete use cases, not a hypothetical future one, before generalizing.
```python
# Anti-pattern signal: a class with unrelated responsibilities and dozens of methods
class ApplicationManager:
    def parse_config(self): ...
    def send_email(self): ...
    def render_report(self): ...
    def validate_user(self): ...
    # ...50 more methods spanning unrelated domains
```
Verify refactoring away from a God Object by checking whether extracted classes each have a single, clearly nameable responsibility and can be tested independently without dragging in unrelated setup.
**Pitfalls:** building a highly configurable, plugin-based abstraction for a feature that has exactly one real use case, guessing at future requirements that never materialize; letting a central "manager"/"utils" class silently absorb new unrelated responsibilities over time until it becomes a bottleneck for every change.

# Infrastructure as Code & Terraform

## Provider Version and State Backend Grounding
Terraform behavior depends on the core Terraform CLI version, each provider's version (which can introduce breaking schema changes independently of Terraform itself), and the configured state backend (local, S3+DynamoDB, Terraform Cloud); verify all three before applying a plan, since a provider upgrade can silently change resource behavior or require state migration.
```bash
terraform version
terraform providers                  # lists resolved provider versions from the lock file
cat .terraform.lock.hcl | grep -A2 "provider \"registry"
```
Confirm the state backend is actually locked during operations (`DynamoDB` lock table for S3 backend, or Terraform Cloud's native locking) to prevent concurrent applies from corrupting state, verify by checking for a lock file/table entry during a deliberately slow apply.
**Pitfalls:** running `terraform apply` from two different machines/CI jobs without state locking configured, corrupting shared state; upgrading a provider version without reading its changelog, triggering unexpected resource replacement on the next plan.

## Plan Review and Blast Radius Assessment
`terraform plan` shows proposed changes (create/update/destroy) before they're applied; verify every planned destroy/replace action is intentional by reading the full plan output, since a seemingly small config change (like changing an immutable attribute) can force a full resource replacement with data loss implications.
```bash
terraform plan -out=tfplan
terraform show -json tfplan | jq '.resource_changes[] | select(.change.actions[] == "delete")'
terraform apply tfplan
```
Confirm any resource marked for replacement (not just update) is safe to destroy-and-recreate by checking whether it holds stateful data (a database, persistent volume) that would be lost, and use `lifecycle { prevent_destroy = true }` on critical resources as a safety net.
**Pitfalls:** applying a plan without reading the full diff, missing an unexpected `forces replacement` on a stateful resource like a database instance; not setting `prevent_destroy` on critical resources, allowing an accidental `terraform destroy` or config typo to delete production data.

## Module Design and Reusability Boundaries
Terraform modules encapsulate reusable infrastructure patterns with defined input variables and outputs; verify a module's interface (variables/outputs) is stable and well-documented before it's consumed by multiple environments, since changing a module's variable names/types is a breaking change for every consumer.
```hcl
module "vpc" {
  source  = "./modules/vpc"
  version = "2.3.1"
  cidr_block = "10.0.0.0/16"
  environment = "production"
}
```
Pin module source versions explicitly (a Git tag or registry version, not a mutable branch reference) so a module update doesn't silently change behavior across all its consumers simultaneously.
**Pitfalls:** referencing a module by a mutable branch (`?ref=main`) instead of a pinned tag, causing unreviewed changes to propagate to every environment using it on the next `terraform init -upgrade`; designing a module with too many tightly-coupled responsibilities, making it hard to reuse across genuinely different environments.

## Drift Detection and State Reconciliation
Infrastructure can drift from the Terraform-managed state when changes are made outside Terraform (manual console edits, other automation); verify actual cloud resource state matches Terraform state periodically with `terraform plan` (showing unexpected diffs) rather than assuming state always reflects reality.
```bash
terraform plan -refresh-only          # shows drift without proposing to "fix" it back yet
terraform apply -refresh-only         # updates state to match real infrastructure after reviewing drift
```
Investigate the root cause of any detected drift (who/what made the out-of-band change) before blindly reconciling state, since drift sometimes reveals an urgent manual incident-response change that needs to be properly codified, not just accepted.
**Pitfalls:** running `terraform apply` to "fix" drift without understanding why it occurred, potentially reverting an intentional emergency fix made outside Terraform during an incident; never running drift detection at all, letting Terraform state silently diverge from reality until the next full apply causes an unexpected large-scale change.

# Software Design Patterns

## Adapter and Facade Patterns for Integration Boundaries
The Adapter pattern converts one interface into another a client expects (bridging an incompatible third-party API to your codebase's conventions), while a Facade provides a simplified, unified interface over a complex subsystem; verify an adapter's translation layer is thin and doesn't leak the wrapped library's quirks/exceptions directly into calling code, defeating the purpose of the abstraction.
```typescript
interface PaymentProcessor { charge(amountCents: number): Promise<string>; }

class LegacyGatewayAdapter implements PaymentProcessor {
  constructor(private legacy: LegacyPaymentSDK) {}
  async charge(amountCents: number): Promise<string> {
    const result = await this.legacy.doChargeInDollars(amountCents / 100);  // adapts unit + shape
    return result.transactionRef;
  }
}
```
Verify the adapter actually isolates callers from the wrapped library's specific exception types/error codes by translating them into the application's own error taxonomy, rather than letting third-party exception types leak through the abstraction boundary.
**Pitfalls:** writing an adapter that still throws the wrapped library's raw exception types, forcing calling code to know about and handle the underlying library's specifics anyway; building a facade so thin it adds indirection without actually simplifying the complex subsystem's usage.

## Command Pattern for Undo/Redo and Task Queuing
The Command pattern encapsulates a request (and often its inverse) as an object, enabling undo/redo stacks, deferred execution, and queuing of operations; verify a command's `execute`/`undo` pair is actually symmetric and idempotent where needed, since an undo implementation that doesn't perfectly reverse the forward operation's side effects silently corrupts state after repeated undo/redo cycles.
```typescript
interface Command { execute(): void; undo(): void; }

class AddTextCommand implements Command {
  constructor(private doc: Document, private text: string) {}
  execute() { this.doc.append(this.text); }
  undo() { this.doc.removeLast(this.text.length); }
}

class CommandHistory {
  private undoStack: Command[] = [];
  run(cmd: Command) { cmd.execute(); this.undoStack.push(cmd); }
  undo() { this.undoStack.pop()?.undo(); }
}
```
Verify undo correctness with a property-based test that executes a random sequence of commands and their undos, confirming the resulting state always matches an equivalent prefix of the original sequence.
**Pitfalls:** implementing `undo()` based on assumed inverse logic that doesn't account for state changes made by other commands in between, corrupting document/application state on multi-step undo sequences; storing commands with references to mutable external state that changes independently of the command history, breaking replay/undo correctness.

## Repository Pattern and Persistence Abstraction
The Repository pattern abstracts data access behind a domain-oriented interface (`findById`, `save`) rather than exposing raw query/ORM details to business logic, enabling easier testing (swap in an in-memory fake) and reducing coupling to a specific persistence technology; verify the abstraction doesn't leak persistence-specific concepts (SQL-specific query objects, ORM entity types) through its public interface, which would defeat the isolation it's meant to provide.
```typescript
interface OrderRepository {
  findById(id: string): Promise<Order | null>;
  save(order: Order): Promise<void>;
}

class PostgresOrderRepository implements OrderRepository {
  async findById(id: string): Promise<Order | null> {
    const row = await db.query("SELECT * FROM orders WHERE id = $1", [id]);
    return row ? Order.fromRow(row) : null;   // translates persistence shape to domain model
  }
}
```
Verify business logic depends only on the repository interface (not the concrete implementation) by checking that unit tests can substitute an in-memory fake without any changes to the code under test.
**Pitfalls:** leaking ORM-specific query builder objects or SQL fragments through the repository interface, coupling business logic to the underlying persistence technology anyway; creating an overly generic repository interface (`query(criteria: any)`) that just re-exposes raw query capability instead of meaningful domain operations.

## Anti-Corruption Layer for Legacy System Integration
An Anti-Corruption Layer (ACL) isolates a clean domain model from a legacy or external system's different (often lower-quality or incompatible) conceptual model, translating between them at a well-defined boundary so the legacy system's quirks and inconsistencies don't spread throughout the new codebase; verify the ACL is the only place legacy-specific assumptions (field naming, unit conventions, implicit business rules baked into old code) appear.
```typescript
class LegacyCustomerAcl {
  toDomainCustomer(legacyRecord: LegacyCustomerRecord): Customer {
    return new Customer({
      id: legacyRecord.CUST_ID.trim(),                 // legacy fixed-width field quirk isolated here
      email: legacyRecord.EMAIL_ADDR?.toLowerCase() ?? null,
      creditLimitCents: Math.round(legacyRecord.CREDIT_LIMIT_DOLLARS * 100),
    });
  }
}
```
Verify no code outside the ACL directly references legacy field names or formats by searching the codebase for legacy-specific identifiers, confirming the translation boundary is actually being respected everywhere.
**Pitfalls:** allowing legacy-specific field names or unit conventions to leak past the ACL into new domain code "just this once," gradually eroding the isolation the pattern was meant to provide; building an ACL that only translates data shape but not the differing business rules/semantics embedded in the legacy system, causing subtle behavioral mismatches.

# Infrastructure as Code & Terraform

## Workspace and Environment Separation Strategies
Terraform workspaces provide one mechanism for managing multiple environments (dev/staging/prod) from the same configuration with separate state files, but verify whether a project actually uses workspaces, separate state backends per environment, or entirely separate root modules/directories, since these approaches have different blast-radius and variable-management implications that must be understood before making changes.
```bash
terraform workspace list
terraform workspace select production
terraform plan -var-file=production.tfvars
```
Verify variable files are actually environment-specific and reviewed carefully before an apply, since accidentally applying production variable values while in a staging workspace (or vice versa) is a common and dangerous mistake, especially when workspace and var-file selection are two separate manual steps.
**Pitfalls:** using Terraform workspaces for environments with fundamentally different resource configurations (not just variable values), fighting the tool's design intent and creating unwieldy conditional logic; forgetting to switch workspace before an apply, applying a plan intended for one environment against a different environment's state.

## Secrets Management in Infrastructure Code
Terraform configuration and state files can contain sensitive values (database passwords, API keys) in plaintext unless explicitly handled, verify secrets are sourced from a dedicated secrets manager (Vault, AWS Secrets Manager, SOPS-encrypted files) rather than hardcoded in `.tf` files or `.tfvars`, and confirm the state backend itself is encrypted, since Terraform state stores resource attributes (including some secrets) in plaintext by default within the state file.
```hcl
data "aws_secretsmanager_secret_version" "db_password" {
  secret_id = "prod/db/password"
}
resource "aws_db_instance" "main" {
  password = data.aws_secretsmanager_secret_version.db_password.secret_string
}
```
Verify `.tfvars` files containing any sensitive values are never committed to version control (add to `.gitignore` and verify with a history scan), and confirm the state backend (S3, Terraform Cloud) has encryption-at-rest and access-controlled read permissions, since anyone who can read state can potentially read embedded secrets.
**Pitfalls:** hardcoding a database password directly in a `.tf` file or committed `.tfvars`, exposing it in version control history indefinitely even after later removal; leaving Terraform state readable by overly broad IAM permissions, exposing secrets embedded in resource attributes to anyone with state-read access.

## Testing Infrastructure Code with Terratest and Policy-as-Code
Infrastructure code benefits from automated testing just like application code: Terratest (Go-based) spins up real infrastructure in a test account and asserts on actual behavior, while policy-as-code tools (OPA/Conftest, Sentinel) enforce organizational rules (no public S3 buckets, mandatory tags) against a plan before it's ever applied. Verify policy checks actually run as a blocking CI gate rather than an optional, ignorable report.
```rego
package terraform.security

deny[msg] {
  resource := input.resource_changes[_]
  resource.type == "aws_s3_bucket"
  resource.change.after.acl == "public-read"
  msg := sprintf("S3 bucket %s must not be publicly readable", [resource.address])
}
```
Verify Terratest-based infrastructure tests actually tear down provisioned test resources reliably (even on test failure) to avoid leaking real cloud costs from abandoned test infrastructure, using deferred cleanup patterns.
**Pitfalls:** running policy-as-code checks in report-only mode indefinitely instead of promoting them to a blocking CI gate once trusted, allowing known-bad configurations to still reach production; writing infrastructure integration tests that provision real cloud resources without guaranteed cleanup on failure, silently accumulating orphaned billable resources.

## Multi-Cloud and Provider Abstraction Tradeoffs
Some organizations attempt cloud-agnostic infrastructure code (abstracting over AWS/GCP/Azure differences) for portability, but verify the actual business need justifies the substantial added complexity, since cloud-specific managed services (which usually offer the best cost/operational tradeoffs) are exactly what a portability-focused abstraction typically has to avoid using, often resulting in a lowest-common-denominator design that captures little of any single cloud's real value.
```hcl
module "compute" {
  source  = var.cloud_provider == "aws" ? "./modules/aws-compute" : "./modules/gcp-compute"
  # ...
}
```
Verify a claimed "multi-cloud" design has actually been tested end-to-end on every targeted cloud recently, rather than assuming untested abstraction layers remain correct as each underlying provider's APIs evolve independently over time.
**Pitfalls:** investing heavily in cloud-agnostic abstractions for a hypothetical future multi-cloud migration that never materializes, paying ongoing complexity cost for unused optionality; building a multi-cloud abstraction that's only ever tested against one actual provider, silently accumulating untested/broken code paths for the others.
