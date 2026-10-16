# C# and .NET Fundamentals

## .NET Runtime Version and SDK Grounding
.NET has moved to a yearly release cadence with LTS (even-numbered, e.g., .NET 8) and STS (odd-numbered) support windows; language features (C# version tied to SDK, not just runtime) and BCL APIs vary by exact version. Verify both the SDK and target framework moniker (TFM) before assuming a feature is available.
```bash
dotnet --version
dotnet --list-sdks
cat *.csproj | grep TargetFramework      # e.g., net8.0
```
Check Microsoft's official .NET support policy page for the exact end-of-support date of the TFM in production, since running an out-of-support version stops receiving security patches.
**Pitfalls:** using a C# 12 language feature in a project whose `.csproj` doesn't set `LangVersion` high enough despite a new SDK being installed; assuming a package supports a TFM without checking its actual `nuspec` target frameworks.

## Nullable Reference Types and Null Safety
Nullable reference types (enabled via `<Nullable>enable</Nullable>`) make reference-type nullability part of the type system, with the compiler emitting warnings (not hard errors by default) for potential null dereferences; verify the project actually has this enabled and warnings-as-errors configured before trusting the compiler catches null issues.
```csharp
#nullable enable
public class UserService {
    public User? FindById(int id) => _repository.Find(id);   // explicit: may be null

    public string GetDisplayName(int id) {
        User? user = FindById(id);
        return user?.Name ?? "Unknown";                       // explicit null handling required
    }
}
```
Confirm `<TreatWarningsAsErrors>` or specific nullable warnings are elevated to errors in CI, since nullable warnings are non-blocking by default and can silently accumulate.
**Pitfalls:** enabling nullable reference types but leaving warnings as non-blocking, letting null-safety violations accumulate unnoticed; using the null-forgiving operator (`!`) to silence warnings without actually verifying the value can't be null at that point.

## async/await and ConfigureAwait Semantics
C# `async`/`await` captures a `SynchronizationContext` by default (relevant in UI apps, less so in ASP.NET Core which has none by default); library code should use `.ConfigureAwait(false)` to avoid unnecessary context-capturing overhead and potential deadlocks when synchronously blocking on async code. Verify the actual hosting context (console, ASP.NET Core, WPF/WinForms) before assuming `ConfigureAwait` guidance applies uniformly.
```csharp
public async Task<User> GetUserAsync(int id) {
    var response = await _httpClient.GetAsync($"/users/{id}").ConfigureAwait(false);
    return await response.Content.ReadFromJsonAsync<User>().ConfigureAwait(false);
}
```
Never call `.Result` or `.Wait()` on an async method from a context with a `SynchronizationContext`, since this is the classic cause of async deadlocks, verify with a deliberate reproduction rather than assuming it's safe "just this once."
**Pitfalls:** blocking on async code with `.Result`/`.Wait()` in a UI or ASP.NET (Framework) context, causing a deadlock from context-capturing; forgetting `ConfigureAwait(false)` consistently in library code, adding needless context-marshaling overhead in hot paths.

## LINQ Deferred Execution and Materialization
LINQ queries over `IEnumerable<T>` are lazily evaluated (deferred) until enumerated; re-enumerating a query re-executes it (potentially re-querying a database or re-computing an expensive pipeline), while `.ToList()`/`.ToArray()` materializes results once. Verify whether repeated enumeration is intentional or an unnoticed performance bug.
```csharp
var expensiveQuery = dbContext.Orders.Where(o => o.Total > 100).Select(o => ExpensiveTransform(o));
var materialized = expensiveQuery.ToList();   // executes once, results reused safely
foreach (var o in materialized) { /* ... */ }
foreach (var o in materialized) { /* ... */ } // no re-execution
```
Verify with SQL logging (`dbContext` command logging) whether an EF Core `IQueryable` is being enumerated multiple times, which issues duplicate database round-trips each time.
**Pitfalls:** enumerating an `IQueryable` multiple times, unknowingly re-executing a database query each time; capturing a LINQ query with side-effecting `Select` projections without realizing deferred execution delays when, and how often, that side effect actually runs.

# Machine Learning Fundamentals

## Problem Framing and Baseline Establishment
Before choosing an ML approach, precisely define the prediction target, evaluation metric, and a simple baseline (majority-class predictor, linear model, or a heuristic rule), verify any "sophisticated" model actually beats this baseline on a held-out set before adopting added complexity.
```python
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score

baseline = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
print("baseline accuracy:", accuracy_score(y_test, baseline.predict(X_test)))
```
Confirm the chosen metric actually reflects the business objective (e.g., precision matters more than accuracy for imbalanced fraud detection) before optimizing a model against the wrong number.
**Pitfalls:** jumping straight to a complex model without ever measuring a trivial baseline, making it impossible to know if added complexity is worth it; optimizing accuracy on a heavily imbalanced dataset where a trivial "always predict majority class" baseline already scores misleadingly high.

## Train/Validation/Test Split Discipline and Leakage Prevention
Data must be split so the test set represents genuinely unseen data with no information leaking from training (via preprocessing fit on the full dataset, duplicate rows across splits, or time-based leakage in temporal data); verify actual split independence rather than assuming a random split is always sufficient.
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
scaler = StandardScaler().fit(X_train)          # fit ONLY on train
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)         # transform, not fit, on test
```
For time-series data, verify a chronological split (train on past, test on future) is used instead of random shuffling, since random splits leak future information into training.
**Pitfalls:** fitting a scaler/encoder on the full dataset before splitting, leaking test-set statistics into training; randomly splitting time-series data, allowing the model to "see the future" during training.

## Overfitting, Underfitting, and Regularization
A model that fits training data far better than validation data is overfitting (memorizing noise); one that performs poorly on both is underfitting (insufficient capacity or features); verify actual train-vs-validation curves rather than looking at a single final metric to diagnose which regime a model is in.
```python
import matplotlib.pyplot as plt
train_scores, val_scores = [], []
for depth in range(1, 20):
    model = DecisionTreeClassifier(max_depth=depth).fit(X_train, y_train)
    train_scores.append(model.score(X_train, y_train))
    val_scores.append(model.score(X_val, y_val))
plt.plot(range(1, 20), train_scores, label="train")
plt.plot(range(1, 20), val_scores, label="validation")
```
Confirm regularization hyperparameters (L1/L2 penalty strength, dropout rate, early-stopping patience) are actually tuned against validation performance, not left at library defaults which may not suit the dataset's scale.
**Pitfalls:** tuning hyperparameters against the test set instead of a separate validation set, silently leaking test information into model selection; concluding "underfitting" from a single low accuracy number without checking whether training accuracy is also low (which would confirm capacity, not variance, is the issue).

## Feature Engineering and Data Leakage Auditing
Feature quality often matters more than model choice; verify every feature is actually available at true prediction time (no "future" information like a label-derived aggregate computed using data that wouldn't exist yet in production) before training, since this leakage inflates offline metrics without any real-world benefit.
```python
# Leakage: "total_purchases_to_date" computed using data including the future purchase being predicted
df["total_purchases_to_date"] = df.groupby("user_id")["purchase_amount"].cumsum()   # verify cumsum respects true time order, excludes current row's future window
```
Audit engineered features by asking "would this exact value have been computable at the moment of prediction in production," and verify with a strict backtest replicating production data availability constraints.
**Pitfalls:** engineering a feature using an aggregate that includes the target row's own future outcome, creating leakage invisible in a simple correlation check; computing feature statistics on the full dataset (train+test combined) instead of only from information available at prediction time.

# C# and .NET Fundamentals

## Value Types, Reference Types, and Boxing
C# distinguishes value types (`struct`, primitives, copied on assignment, stack-allocated when local) from reference types (`class`, heap-allocated, assignment copies the reference); verify boxing (implicit conversion of a value type to `object`/an interface, causing a heap allocation) isn't happening unintentionally in a hot path, since it's a subtle, easy-to-miss performance cost.
```csharp
struct Point { public int X, Y; }
object boxed = new Point { X = 1, Y = 2 };   // boxing: heap allocation + copy

// Generic constraint avoids boxing entirely for value-type usage
static double Sum<T>(IEnumerable<T> items) where T : struct, INumber<T> { /* ... */ }
```
Verify with a memory profiler (dotMemory, `dotnet-counters`) whether a hot loop is unexpectedly allocating due to boxing (e.g., passing a `struct` through a non-generic `object`-based API), rather than assuming struct usage automatically avoids heap allocation.
**Pitfalls:** passing value types through non-generic collections or APIs typed as `object`, causing hidden boxing allocations in a hot path; assuming all `struct` usage is "free," when large structs copied frequently by value can actually cost more than a reference-type equivalent.

## Dependency Injection and Service Lifetimes
ASP.NET Core's built-in DI container manages three service lifetimes: Transient (new instance every request), Scoped (one instance per HTTP request/scope), and Singleton (one instance for the app's lifetime), verify a service's registered lifetime matches its actual state-sharing requirements, since injecting a Scoped service into a Singleton causes a well-known "captive dependency" bug where the scoped instance is incorrectly held for the app's entire lifetime.
```csharp
builder.Services.AddScoped<IOrderRepository, OrderRepository>();
builder.Services.AddSingleton<ICacheService, MemoryCacheService>();
builder.Services.AddTransient<IEmailValidator, EmailValidator>();
```
Verify no Singleton service captures a Scoped/Transient dependency directly in its constructor (the DI container throws a validation error for this in newer .NET versions when scope validation is enabled) by enabling `ValidateScopes = true` in development.
**Pitfalls:** injecting a Scoped `DbContext` into a Singleton service, causing the same database context instance (and its state/connection) to be incorrectly reused across all requests for the app's lifetime; registering a stateful service as Singleton when it actually holds per-request mutable state, causing cross-request data leakage.

## Records, Pattern Matching, and Structural Equality
C# `record` types (introduced in C# 9) provide concise, immutable-by-default reference types with structural equality and a `with` expression for non-destructive mutation, well-suited to DTOs and domain value objects; verify equality semantics actually match intent, since records use member-wise structural equality by default, which differs from a regular class's default reference equality.
```csharp
public record Address(string Street, string City, string PostalCode);

var original = new Address("123 Main St", "Springfield", "00000");
var updated = original with { City = "Shelbyville" };   // non-destructive copy with one field changed
Console.WriteLine(original == updated);                  // false, structural equality
```
Verify `record class` versus `record struct` choice matches actual copy-semantics needs, and confirm nested mutable reference fields inside a record don't silently break the "immutable" expectation, since records don't deep-freeze nested mutable objects automatically.
**Pitfalls:** assuming a record containing a mutable reference-type field (like a `List<T>`) is fully immutable, when the list itself can still be mutated through the reference after construction; switching an existing `class` to a `record` without checking for reliance on reference equality elsewhere in the codebase, silently changing comparison behavior.

## Garbage Collection and Memory Management Tuning
.NET's generational garbage collector (Gen 0/1/2, plus Large Object Heap) automatically reclaims unused memory, but verify actual GC behavior under production-representative load with `dotnet-counters`/`dotnet-trace` before assuming default settings (Workstation vs. Server GC, concurrent vs. non-concurrent) are optimal for a given workload, since Server GC (multi-threaded, throughput-optimized) versus Workstation GC (lower latency, less parallel) can meaningfully change tail latency for web services.
```bash
dotnet-counters monitor --process-id <pid> System.Runtime
```
```xml
<PropertyGroup><ServerGarbageCollection>true</ServerGarbageCollection></PropertyGroup>
```
Verify large, frequently-allocated objects (arrays over 85,000 bytes) aren't unexpectedly landing on the Large Object Heap and causing fragmentation, by checking actual allocation profiles rather than assuming standard generational collection handles all object sizes uniformly well.
**Pitfalls:** leaving default Workstation GC settings on a high-throughput server workload where Server GC would substantially reduce collection pause impact; repeatedly allocating large arrays that land on the LOH, causing memory fragmentation that isn't addressed by ordinary Gen 0/1/2 collections.

# Machine Learning Fundamentals

## Cross-Validation and Robust Performance Estimation
A single train/test split can give a misleadingly optimistic or pessimistic performance estimate due to sampling variance, especially on small datasets; k-fold cross-validation trains and evaluates across multiple folds to produce a more robust estimate with a confidence interval, and verify the chosen fold strategy (stratified for classification, grouped for data with natural clusters, time-series-aware for temporal data) actually matches the data's structure.
```python
from sklearn.model_selection import cross_val_score, StratifiedKFold

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=cv, scoring="f1_macro")
print(f"{scores.mean():.3f} ± {scores.std():.3f}")
```
Verify no data leakage occurs across folds when preprocessing (feature scaling, target encoding) is fit inside a `Pipeline` per-fold rather than once on the full dataset before cross-validation, which would leak validation-fold information into training.
**Pitfalls:** fitting a preprocessing step on the entire dataset before running cross-validation, leaking information across folds and inflating reported performance; using plain k-fold (not stratified/grouped) on imbalanced or clustered data, producing folds that don't represent the true data distribution.

## Ensemble Methods and Model Combination
Ensemble methods (bagging like Random Forest, boosting like XGBoost/LightGBM, stacking) combine multiple models to reduce variance or bias beyond what a single model achieves; verify the actual mechanism (bagging reduces variance via averaging independent models, boosting reduces bias via sequential error-correction) matches the failure mode observed in a single base model before choosing an ensemble strategy.
```python
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

rf = RandomForestClassifier(n_estimators=300, max_depth=None, n_jobs=-1, random_state=42)
xgb = XGBClassifier(n_estimators=300, learning_rate=0.05, max_depth=6, random_state=42)
```
Verify ensemble hyperparameters (number of estimators, learning rate, tree depth) are tuned against validation performance rather than left at defaults, and confirm the added inference-time cost of an ensemble is acceptable for the deployment's latency budget.
**Pitfalls:** assuming an ensemble is always better without measuring actual validation improvement against a well-tuned single model, paying inference-cost complexity for negligible benefit; using boosting on already-noisy, mislabeled data, where sequential error-correction can overfit to label noise.

## Model Interpretability and Feature Importance
Understanding why a model makes a prediction (feature importance, SHAP values, partial dependence plots) is often as important as raw accuracy for production trust and debugging; verify the interpretability method actually matches the model type, tree-based feature importances can be misleading for correlated features, while SHAP values provide more theoretically grounded per-prediction attribution at higher computational cost.
```python
import shap

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```
Verify feature importance results are stable across multiple training runs with different random seeds before drawing strong conclusions from them, since importance rankings can shift meaningfully with correlated features or limited training data.
**Pitfalls:** trusting default tree-based feature importance rankings at face value when features are highly correlated, since importance can be arbitrarily split between correlated features in misleading ways; using an interpretability method's output to justify a business decision without validating its stability across re-runs or alternate methods.

## Model Deployment, Serving, and Drift Monitoring
A trained model's value depends on reliable production serving and ongoing monitoring for data/concept drift (the relationship between features and target changing over time, silently degrading accuracy without any code change); verify a deployed model's input distribution and prediction distribution are actively monitored against the training distribution, not just deployed once and assumed to remain valid indefinitely.
```python
from scipy.stats import ks_2samp

statistic, p_value = ks_2samp(training_feature_distribution, production_feature_distribution)
if p_value < 0.01:
    alert("Feature distribution drift detected")
```
Verify a retraining/rollback trigger actually exists and is tested (not just a dashboard nobody watches) before relying on drift detection as a real production safeguard, and confirm shadow deployment or canary evaluation is used before fully replacing a production model.
**Pitfalls:** deploying a model once and never monitoring for drift, letting silent accuracy degradation go unnoticed until a downstream business metric visibly suffers; replacing a production model with a new version without a canary/shadow comparison period, risking a regression that offline validation metrics didn't capture.
