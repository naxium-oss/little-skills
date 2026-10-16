# Google Cloud Platform Fundamentals

## Project, IAM, and Resource Hierarchy Grounding
GCP resources live under a hierarchy of Organization → Folders → Projects → Resources, and IAM roles (basic, predefined, custom) can be granted at any level with inheritance flowing downward. Verify the active project and effective IAM bindings rather than assuming from a single `gcloud` config.
```bash
gcloud config get-value project
gcloud projects get-iam-policy my-project-id
gcloud auth list                     # confirm which identity is active
```
Confirm the active configuration (`gcloud config configurations list`) when multiple projects/accounts are used locally, since commands silently target whichever project is currently active.
**Pitfalls:** running a destructive command against the wrong active project because a `gcloud config` switch wasn't verified first; assuming an IAM role granted at the project level doesn't also apply to newly created resources within it (it does, via inheritance).

## Compute Options: GCE, Cloud Run, and GKE Selection
GCP offers a spectrum from unmanaged VMs (Compute Engine) to fully managed containers (Cloud Run, scales to zero, request-based) to orchestrated clusters (GKE); the right choice depends on actual traffic pattern, statefulness, and control needs, verify these before defaulting to the most familiar option.
```bash
gcloud run deploy my-api --image gcr.io/my-project/my-api:1.4.0 --region us-central1 \
  --min-instances=0 --max-instances=10 --memory=512Mi
```
Verify Cloud Run's concurrency and cold-start characteristics against actual latency requirements with a load test rather than assuming they match GKE's always-on pod behavior.
**Pitfalls:** choosing GKE for a simple stateless API that Cloud Run would serve more cheaply and with less operational overhead; assuming Cloud Run's `min-instances=0` has no cold-start latency impact on the first request after idling.

## Cloud Storage and IAM Uniform Bucket-Level Access
Cloud Storage buckets can use legacy ACLs or uniform bucket-level access (recommended); mixing them causes confusing permission behavior. Verify a bucket's actual access-control mode before debugging unexpected public/private exposure.
```bash
gsutil uniformbucketlevelaccess get gs://my-app-bucket
gcloud storage buckets describe gs://my-app-bucket --format="value(iamConfiguration)"
```
Audit public access with `gcloud storage buckets get-iam-policy` and check for `allUsers`/`allAuthenticatedUsers` bindings, which grant internet-wide or any-Google-account access respectively, verify this is intentional before shipping.
**Pitfalls:** leaving a bucket with legacy ACLs where an object-level ACL unexpectedly grants broader access than the bucket policy suggests; granting `allUsers` read access for a "quick public link" and forgetting to revoke it.

## Observability with Cloud Logging and Monitoring
Cloud Logging and Cloud Monitoring aggregate logs/metrics per project by default with query languages (Logging Query Language, MQL/PromQL for Monitoring) that must be verified for exact syntax against the current console version. Confirm log-based metrics and alert policies actually fire by triggering a test condition rather than trusting the configuration alone.
```bash
gcloud logging read 'resource.type="cloud_run_revision" AND severity>=ERROR' --limit 20 --format=json
```
Verify log retention settings and export sinks (BigQuery, Cloud Storage) are configured before relying on long-term log analysis, since default retention is time-limited.
**Pitfalls:** assuming default log retention is indefinite when it's time-bounded per bucket configuration; writing an alert policy and never validating it fires by testing an actual threshold breach.

# Microsoft Azure Fundamentals

## Subscription, Resource Group, and RBAC Grounding
Azure organizes resources into Subscriptions and Resource Groups, with Azure RBAC roles assignable at management group, subscription, resource group, or resource scope with inheritance. Verify the active subscription context before any deployment, since CLI/portal context can silently point to an unintended subscription.
```bash
az account show
az account list --output table
az role assignment list --assignee <principal-id> --all
```
Confirm effective permissions with `az role assignment list --include-inherited` rather than checking only directly assigned roles, since inherited scope grants are easy to miss.
**Pitfalls:** deploying to the wrong subscription because `az account set` wasn't called or verified after a context switch; assuming a "Reader" role at the subscription level doesn't apply to a specific resource group (it does, via inheritance).

## Compute Options: App Service, Azure Functions, and AKS
Azure App Service suits standard web apps with managed scaling, Azure Functions suits event-driven/serverless workloads with consumption or premium plans, and AKS provides full Kubernetes control; verify actual scaling/cold-start needs against the specific plan tier before choosing, since tiers (Free/Basic/Standard/Premium/Consumption) have materially different SLAs and cold-start behavior.
```bash
az functionapp create --resource-group rg-prod --consumption-plan-location eastus \
  --runtime node --runtime-version 20 --functions-version 4 --name my-func-app \
  --storage-account mystorageacct
```
Verify the specific plan's documented cold-start and always-on characteristics for the exact tier chosen, since "serverless" consumption plans can have multi-second cold starts unsuitable for latency-sensitive APIs.
**Pitfalls:** choosing a Consumption plan for a latency-sensitive API without measuring cold-start impact, then discovering intermittent multi-second delays in production; assuming App Service auto-scale rules trigger instantly rather than after the configured evaluation window.

## Azure Storage and Blob Access Control
Azure Blob Storage supports Shared Key, SAS (Shared Access Signature) tokens, and Azure AD-based RBAC for access control; verify which mechanism is actually configured on a storage account, since SAS tokens embed their own expiry/permissions independent of RBAC changes made later.
```bash
az storage account show --name mystorageacct --query "allowBlobPublicAccess"
az storage blob generate-sas --account-name mystorageacct --container-name uploads \
  --name file.pdf --permissions r --expiry 2025-12-31T00:00:00Z
```
Confirm a previously issued SAS token's expiry and permission scope before assuming revoking an RBAC role also invalidates it, standalone SAS tokens (not tied to a stored access policy) remain valid until their own expiry regardless of RBAC changes.
**Pitfalls:** assuming revoking a user's RBAC role immediately invalidates SAS tokens they previously generated; leaving `allowBlobPublicAccess` enabled account-wide when only one specific container needs public read access.

## Azure Monitor, Log Analytics, and Cost Management
Azure Monitor aggregates metrics and logs through Log Analytics workspaces queried with Kusto Query Language (KQL); verify the exact workspace and retention period in use, and confirm cost alerts are configured and tested, since Azure billing can span multiple subscriptions under one Enterprise Agreement.
```kusto
AppRequests
| where TimestampUTC > ago(1h) and Success == false
| summarize FailureCount = count() by bin(TimestampUTC, 5m), Name
```
```bash
az consumption budget list --output table
```
Verify a configured budget alert actually notifies the right recipients by checking its action group configuration, not just its existence, and confirm the KQL table/column names match the exact resource type being queried (they differ between App Insights, Log Analytics, and Sentinel schemas).
**Pitfalls:** assuming a budget alert exists means someone will be notified, without checking the linked action group has valid, current contacts; querying the wrong table schema variant and getting silently empty results instead of an error.

# Google Cloud Platform Fundamentals

## BigQuery Query Cost and Partitioning Design
BigQuery bills primarily by bytes scanned (on-demand pricing) or by reserved slot-time (capacity pricing); verify a query's actual scanned-byte estimate with a dry run before executing on a large table, and confirm tables are partitioned/clustered on commonly filtered columns, since an unpartitioned table forces a full scan even for a query targeting one day's data.
```bash
bq query --dry_run --use_legacy_sql=false 'SELECT * FROM `proj.dataset.events` WHERE event_date = "2025-06-01"'
```
```sql
CREATE TABLE dataset.events (event_date DATE, user_id STRING, payload JSON)
PARTITION BY event_date
CLUSTER BY user_id;
```
Verify actual query cost after execution via the job's statistics (`bq show -j <job_id>`) rather than only trusting a pre-execution estimate, since dry-run estimates can differ from actual billed bytes in edge cases.
**Pitfalls:** running `SELECT *` on a large unpartitioned table when only a narrow date range is needed, incurring full-table-scan costs; forgetting clustering doesn't reduce bytes scanned the way partitioning pruning does, it only improves performance within already-selected partitions.

## Pub/Sub Messaging Guarantees and Ordering
Cloud Pub/Sub provides at-least-once delivery by default (exactly-once delivery is available but has specific configuration and latency tradeoffs) and does not guarantee message ordering unless ordering keys are explicitly enabled per topic, at the cost of some throughput; verify actual configured guarantees match consumer assumptions rather than assuming ordering "usually" holds.
```bash
gcloud pubsub topics create orders --message-storage-policy-allowed-regions=us-central1
gcloud pubsub subscriptions create orders-sub --topic=orders --enable-exactly-once-delivery
```
Verify consumer code is idempotent regardless of the exactly-once setting, since edge cases (subscriber crash mid-ack) can still occasionally cause redelivery in practice, and test message reordering behavior explicitly if ordering keys aren't enabled.
**Pitfalls:** assuming default Pub/Sub delivery preserves message order across a topic without enabling ordering keys, then debugging out-of-order side effects downstream; enabling exactly-once delivery and assuming it removes all need for idempotent consumer logic, when edge cases can still occasionally redeliver.

## GCP IAM Conditional Bindings and Organization Policies
Beyond basic role bindings, GCP supports conditional IAM bindings (grant access only if a condition like time window or resource tag matches) and Organization Policies (constraints that apply org-wide regardless of individual IAM grants, like disallowing public bucket access); verify org policies aren't silently blocking an otherwise-valid IAM grant, since org policy constraints take precedence.
```bash
gcloud resource-manager org-policies describe constraints/storage.publicAccessPrevention --organization=123456789
gcloud projects add-iam-policy-binding my-project --member="user:dev@example.com" --role="roles/storage.objectViewer" \
  --condition="expression=request.time < timestamp('2025-12-31T00:00:00Z'),title=temporary-access"
```
Verify a conditional binding's expiry actually takes effect by testing access after the condition's boundary passes, and confirm no organization policy is silently overriding an intended project-level IAM grant.
**Pitfalls:** granting a broad IAM role assuming it takes full effect, without checking an organization policy constraint is silently blocking part of that access (e.g., public access prevention overriding a bucket ACL); forgetting conditional bindings' time-based expressions use the resource's actual evaluation time, which can behave unexpectedly across time zones if not specified in UTC.

## Terraform and Deployment Manager for GCP Infrastructure
GCP infrastructure is commonly managed via Terraform's Google provider (more widely adopted) or the native Deployment Manager; verify which tool a project actually uses and the exact provider version, since the Google Terraform provider's resource schemas change across major versions and can require state migration on upgrade.
```hcl
resource "google_cloud_run_v2_service" "api" {
  name     = "api"
  location = "us-central1"
  template {
    containers { image = "gcr.io/my-project/api:1.4.0" }
  }
}
```
Verify `terraform plan` output doesn't show unexpected resource replacement after a provider version bump, since GCP resource identity fields (like Cloud Run's revision naming) have changed behavior across provider major versions.
**Pitfalls:** upgrading the Google Terraform provider without reading its changelog, triggering unexpected resource replacement (and downtime) on the next apply; mixing manually-created GCP resources with Terraform-managed ones in the same project without importing them, causing drift and confusing plan output.

# Microsoft Azure Fundamentals

## Azure Active Directory (Entra ID) Application Registration
Azure AD (rebranded Microsoft Entra ID) app registrations define how applications authenticate and what permissions they're granted (via API permissions and consent); verify actual granted permissions (not just requested ones) with admin consent status, since a requested permission without admin consent silently fails at runtime for organizational accounts.
```bash
az ad app create --display-name "my-app" --sign-in-audience AzureADMyOrg
az ad app permission list --id <app-id>
az ad app permission admin-consent --id <app-id>
```
Verify redirect URIs registered on the app exactly match what the application sends (including trailing slashes and protocol), since Azure AD's OAuth flow rejects any mismatch without a helpful diagnostic beyond a generic error.
**Pitfalls:** requesting an API permission in the app registration but never obtaining admin consent, causing silent authorization failures only in production tenants requiring consent; a redirect URI mismatch (missing trailing slash) causing a cryptic `AADSTS50011` error that's often misdiagnosed as a code bug.

## Azure Resource Manager (ARM) Templates and Bicep
Azure infrastructure-as-code is expressed via ARM JSON templates or the more concise Bicep DSL (which compiles to ARM JSON); verify the actual deployed template matches source by checking the deployment history, since manual portal changes create drift invisible to the Bicep/ARM source files.
```bicep
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'mystorageacct'
  location: resourceGroup().location
  sku: { name: 'Standard_LRS' }
  kind: 'StorageV2'
}
```
```bash
az deployment group what-if --resource-group rg-prod --template-file main.bicep
```
Always run `what-if` before an actual deployment to preview changes, since it surfaces unexpected resource replacements the same way Terraform's plan does.
**Pitfalls:** applying a Bicep deployment without `what-if` review, missing an unexpected resource replacement flagged only in the preview; making manual portal changes to a Bicep-managed resource, causing silent drift that the next deployment may unexpectedly overwrite.

## Azure Functions Triggers and Bindings
Azure Functions integrate with triggers (HTTP, Timer, Queue, Blob) and input/output bindings that declaratively wire data sources without manual SDK boilerplate; verify the exact binding extension version installed matches the runtime's expected version, since binding extension bundles are versioned independently of the Functions runtime itself and can drift.
```json
{
  "bindings": [
    { "type": "queueTrigger", "direction": "in", "name": "msg", "queueName": "orders", "connection": "AzureWebJobsStorage" },
    { "type": "table", "direction": "out", "name": "outputTable", "tableName": "ProcessedOrders", "connection": "AzureWebJobsStorage" }
  ]
}
```
Verify local emulator behavior (Azurite for storage bindings) matches production Azure Storage behavior for the specific binding types used, since some edge-case behaviors (large blob handling, queue visibility timeout defaults) can differ.
**Pitfalls:** relying on a binding extension bundle version that's incompatible with the deployed Functions runtime major version, causing deployment-time or first-invocation failures; developing exclusively against the Azurite emulator without ever validating against real Azure Storage before production release.

## Cost Management: Reserved Instances and Right-Sizing
Azure offers Reserved Instances and Savings Plans for predictable workloads at a discount versus pay-as-you-go, but committing requires confidence in sustained usage; verify actual historical usage patterns via Azure Monitor/Cost Management data before purchasing a reservation, since an incorrect commitment locks in cost without the flexibility to right-size later without penalty.
```bash
az consumption usage list --start-date 2025-01-01 --end-date 2025-02-01 --query "[].{resource:instanceName, cost:pretaxCost}"
az advisor recommendation list --category Cost   # surfaces right-sizing suggestions based on observed usage
```
Verify Azure Advisor's right-sizing recommendations against actual peak usage windows (not just averages) before downsizing a resource, since averages can mask periodic peak loads that justify current sizing.
**Pitfalls:** purchasing a multi-year Reserved Instance commitment based on a short observation window that doesn't reflect seasonal or growth-driven usage changes; downsizing a resource based on average utilization alone without checking peak-load windows, causing performance degradation during actual demand spikes.
