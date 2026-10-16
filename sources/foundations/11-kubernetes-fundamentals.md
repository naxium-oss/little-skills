# Kubernetes Fundamentals

## Cluster and API Version Grounding
Kubernetes API resources move through `alpha` → `beta` → stable (`v1`) maturity and can be deprecated/removed between minor versions (e.g., `PodSecurityPolicy` removed in 1.25); verify the exact cluster version and API availability before writing manifests.
```bash
kubectl version --short
kubectl api-versions | grep autoscaling
kubectl explain deployment.spec.strategy --api-version=apps/v1
```
Cross-check the Kubernetes deprecation guide for the specific version range being upgraded through, since skipping guidance across multiple minor versions can silently break manifests referencing removed API groups.
**Pitfalls:** applying a manifest using `apiVersion: extensions/v1beta1` against a modern cluster where it was removed years ago; assuming a managed cluster (EKS/GKE/AKS) is on the latest upstream version without checking its console/API.

## Pods, Deployments, and Desired-State Reconciliation
Kubernetes controllers continuously reconcile actual state toward declared desired state; a Deployment manages ReplicaSets which manage Pods, and directly editing a Pod owned by a Deployment gets silently overwritten on the next reconciliation. Verify ownership chains with `kubectl get pod -o yaml` before debugging "my change disappeared."
```bash
kubectl get deploy web -o yaml
kubectl rollout status deployment/web
kubectl describe pod web-7d8f9c6b5-xk2pl   # events reveal scheduling/crash reasons
```
Confirm actual desired replica count and rollout status match expectations rather than assuming from the manifest alone, since a stuck rollout can leave old and new ReplicaSets both partially active.
**Pitfalls:** manually `kubectl edit`-ing a Pod managed by a Deployment and being confused when it reverts; not checking `kubectl describe pod` events, missing the actual scheduling/image-pull/crash reason shown there.

## Services, DNS, and Network Policy
A Service provides a stable virtual IP and DNS name (`service.namespace.svc.cluster.local`) load-balancing across matching Pods by label selector; verify label selectors actually match target Pod labels, a very common silent misconfiguration with zero error message.
```bash
kubectl get endpoints web-service     # empty means selector matches no pods
kubectl get svc web-service -o jsonpath='{.spec.selector}'
kubectl get pods --show-labels
```
Confirm NetworkPolicy resources are actually enforced (requires a CNI plugin that implements them, some default CNIs silently ignore NetworkPolicy objects), rather than assuming policy YAML alone provides isolation.
**Pitfalls:** mismatched `selector` labels between a Service and its target Pods, resulting in zero endpoints with no obvious error; assuming NetworkPolicy is enforced without confirming the cluster's CNI actually supports it.

## ConfigMaps, Secrets, and Resource Requests/Limits
ConfigMaps/Secrets inject configuration without rebuilding images; Secrets are only base64-encoded (not encrypted) by default at rest unless encryption-at-rest is explicitly configured on the cluster. Resource `requests`/`limits` drive scheduling and OOM/throttling behavior, verify actual usage against configured limits with real metrics, not guesses.
```yaml
resources:
  requests: { cpu: "250m", memory: "256Mi" }
  limits: { cpu: "500m", memory: "512Mi" }
```
```bash
kubectl top pod web-7d8f9c6b5-xk2pl
kubectl get secret db-creds -o jsonpath='{.data.password}' | base64 -d
```
Verify whether a Pod was OOMKilled (`kubectl describe pod` shows `Reason: OOMKilled`) versus CPU-throttled, since the symptoms (slowness, restarts) look similar but require different remediation.
**Pitfalls:** treating base64-encoded Secrets as encrypted and storing them in plaintext version control; setting memory `limits` far below actual peak usage observed via `kubectl top`, causing avoidable OOM kills.

# AWS Cloud Fundamentals

## Region, Account, and Service Quota Grounding
AWS resources are region-scoped (with a few global exceptions like IAM and Route 53), and default service quotas (VPCs per region, Lambda concurrency, EC2 instance limits) vary by account history and region. Verify the active region, account ID, and relevant quota before assuming a deployment will succeed.
```bash
aws sts get-caller-identity
aws configure get region
aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A
```
Confirm pricing and availability of a specific instance type/service in the target region via the actual AWS pricing page or `aws pricing` API, since prices and even service availability differ meaningfully by region.
**Pitfalls:** assuming a resource created in `us-east-1` is visible/usable in `us-west-2` without explicit replication; hitting an undocumented-to-the-team default quota limit in production because it was never verified in advance.

## IAM Least-Privilege Policy Design
IAM policies are deny-by-default; an explicit `Deny` always overrides any `Allow`, and policies can be attached to users, groups, roles, or resources (resource-based policies). Verify actual effective permissions with the IAM Policy Simulator or `aws iam simulate-principal-policy` rather than assuming from a single policy document.
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject"],
    "Resource": "arn:aws:s3:::my-app-bucket/uploads/*",
    "Condition": { "StringEquals": { "aws:PrincipalTag/team": "payments" } }
  }]
}
```
Test least-privilege policies against real use cases before rollout, since overly narrow scoping breaks functionality while overly broad scoping (e.g., `"Resource": "*"`) creates unnecessary blast radius.
**Pitfalls:** granting `"Action": "*"` or `"Resource": "*"` as a temporary fix that becomes permanent; forgetting that resource-based policies (like an S3 bucket policy) combine with identity-based policies, and an explicit `Deny` anywhere wins.

## VPC Networking Fundamentals
A VPC provides an isolated network with subnets (public/private determined by route table association to an Internet Gateway), security groups (stateful, instance-level) and NACLs (stateless, subnet-level). Verify actual route tables and security group rules rather than assuming "private subnet" means no internet access at all (NAT gateways can still allow outbound).
```bash
aws ec2 describe-route-tables --filters "Name=association.subnet-id,Values=subnet-0123abcd"
aws ec2 describe-security-groups --group-ids sg-0123abcd
```
Confirm security group rules are as narrow as intended (specific ports/CIDRs, not `0.0.0.0/0` on sensitive ports) by reviewing actual inbound/outbound rule sets, not just the intended design doc.
**Pitfalls:** assuming a "private" subnet has zero outbound internet access when a NAT gateway is attached; leaving a security group rule open to `0.0.0.0/0` on a database port from an early testing phase.

## Cost Visibility and Dated Pricing Verification
AWS pricing changes over time and varies by region, instance family, and purchasing option (on-demand, reserved, spot, savings plans); never quote a price from memory, verify with AWS Cost Explorer, the Pricing Calculator, or the current pricing page, and record the retrieval date.
```bash
aws ce get-cost-and-usage --time-period Start=2025-01-01,End=2025-02-01 \
  --granularity MONTHLY --metrics "UnblendedCost" --group-by Type=DIMENSION,Key=SERVICE
```
Tag resources consistently (`cost-center`, `environment`) so Cost Explorer can attribute spend accurately, and re-verify any previously quoted price before including it in a report, since AWS revises pricing without individualized notice.
**Pitfalls:** quoting an EC2/S3 price from memory or an old blog post as current; forgetting spot price volatility means a "cheap" instance type can spike or be reclaimed without notice.

# Kubernetes Fundamentals

## StatefulSets and Persistent Volume Claims
StatefulSets provide stable network identities and persistent storage for workloads that need it (databases, queues), unlike Deployments' interchangeable Pods; verify PersistentVolumeClaims actually bind to the intended StorageClass and that volume reclaim policy matches expectations (`Retain` vs `Delete`) before assuming data survives Pod/StatefulSet deletion.
```bash
kubectl get pvc -o wide
kubectl get storageclass
kubectl get pv <pv-name> -o jsonpath='{.spec.persistentVolumeReclaimPolicy}'
```
Verify ordinal Pod naming/network identity (`db-0`, `db-1`) is actually relied upon correctly by the stateful application's clustering logic, and test a real Pod deletion/rescheduling to confirm the same PVC reattaches to the recreated Pod.
**Pitfalls:** assuming a Deployment's ephemeral Pods are appropriate for a stateful database, losing data on every rescheduling event; using a `Delete` reclaim policy on a StorageClass for critical data, unexpectedly losing volumes when a PVC is removed during a routine cleanup.

## Horizontal Pod Autoscaling and Resource-Based Scaling Decisions
The Horizontal Pod Autoscaler (HPA) scales replica count based on observed metrics (CPU/memory by default, or custom/external metrics via an adapter); verify the HPA's target metric actually correlates with real load (CPU may not reflect I/O-bound bottlenecks) and that resource `requests` are set, since HPA's CPU-percentage calculations are relative to requested CPU, not absolute usage.
```bash
kubectl autoscale deployment web --cpu-percent=60 --min=2 --max=10
kubectl get hpa web --watch
kubectl describe hpa web    # shows current vs. target metric values driving scaling decisions
```
Verify scaling actually triggers under a real load test rather than trusting the configuration alone, and confirm scale-down stabilization windows don't cause flapping (rapid scale up/down) under bursty traffic.
**Pitfalls:** omitting resource `requests` on the target Deployment, causing HPA's percentage-based CPU target to be meaningless or the HPA to fail to compute metrics at all; scaling on CPU alone for an I/O-bound or queue-depth-driven workload, missing the actual bottleneck signal entirely.

## RBAC Roles, RoleBindings, and Service Account Scoping
Kubernetes RBAC controls which principals (users, groups, ServiceAccounts) can perform which verbs on which resources, scoped per-namespace (Role/RoleBinding) or cluster-wide (ClusterRole/ClusterRoleBinding); verify a workload's ServiceAccount has only the minimum permissions it actually needs by testing with `kubectl auth can-i` rather than assuming the default ServiceAccount's permissions are appropriately scoped.
```bash
kubectl auth can-i delete pods --as=system:serviceaccount:default:web-sa -n default
kubectl create role pod-reader --verb=get,list,watch --resource=pods -n default
kubectl create rolebinding read-pods --role=pod-reader --serviceaccount=default:web-sa -n default
```
Verify Pods aren't running with the default ServiceAccount's broad or unintended cluster permissions by explicitly assigning a scoped ServiceAccount to every workload rather than relying on namespace defaults.
**Pitfalls:** granting `cluster-admin` broadly as a shortcut during initial setup and never revisiting it, leaving a workload with far more access than needed; leaving `automountServiceAccountToken: true` (the default) on Pods that don't need API server access at all, unnecessarily widening the attack surface if the Pod is compromised.

## Kubernetes Ingress and Gateway API Routing
Ingress resources (or the newer, more expressive Gateway API) route external HTTP(S) traffic to internal Services based on host/path rules, but actual behavior depends entirely on which Ingress controller (nginx-ingress, Traefik, cloud-provider-managed) is installed, since the Ingress spec itself is just an interface implemented differently by each controller. Verify the specific controller's annotations/CRDs and version in the cluster before applying configuration copied from documentation for a different controller.
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-ingress
  annotations: { nginx.ingress.kubernetes.io/rewrite-target: /$1 }
spec:
  rules:
    - host: app.example.com
      http:
        paths: [{ path: /api/(.*), pathType: Prefix, backend: { service: { name: api, port: { number: 80 } } } }]
```
Verify which Ingress controller is actually running (`kubectl get pods -n ingress-nginx` or equivalent) before using controller-specific annotations, since annotations are silently ignored (not errored) by a different controller.
**Pitfalls:** copying nginx-ingress-specific annotations into a cluster running Traefik or a cloud-managed controller, having them silently ignored with no routing effect; assuming TLS termination happens automatically without verifying a cert-manager (or equivalent) integration is actually configured and issuing valid certificates.

# AWS Cloud Fundamentals

## S3 Storage Classes, Lifecycle Rules, and Consistency Model
S3 offers storage classes (Standard, Infrequent Access, Glacier variants) with different cost/retrieval-time tradeoffs, and lifecycle rules automate transitions/expiration; verify S3's strong read-after-write consistency (now standard for all operations since December 2020) isn't confused with older eventual-consistency assumptions from outdated documentation or tutorials.
```bash
aws s3api put-bucket-lifecycle-configuration --bucket my-bucket --lifecycle-configuration file://lifecycle.json
aws s3api head-object --bucket my-bucket --key archive/2024/report.pdf   # verify actual storage class
```
Verify retrieval time and cost implications of a Glacier-class object before an application path assumes synchronous, immediate access, since Glacier retrieval can take minutes to hours depending on the retrieval tier chosen.
**Pitfalls:** applying an aggressive lifecycle rule that transitions frequently-accessed objects to Glacier, causing unexpected retrieval latency/cost when accessed; assuming outdated eventual-consistency caveats from old blog posts still apply to modern S3 behavior without checking current documentation.

## Lambda Execution Model, Cold Starts, and Concurrency Limits
AWS Lambda executes code in ephemeral, isolated execution environments that can be reused ("warm") across invocations or freshly initialized ("cold start," with additional latency for initialization code outside the handler); verify actual cold-start latency for the specific runtime/package size/VPC configuration in use, since VPC-attached Lambdas historically had materially higher cold-start costs (improved but not eliminated in recent AWS networking updates).
```bash
aws lambda get-function-configuration --function-name my-function --query "{Runtime:Runtime,MemorySize:MemorySize,Timeout:Timeout}"
aws lambda put-function-concurrency --function-name my-function --reserved-concurrent-executions 50
```
Verify reserved/provisioned concurrency settings match actual traffic patterns by testing under realistic load, and confirm account-level concurrent execution limits (a regional quota) won't be exhausted by one function starving others.
**Pitfalls:** placing initialization-heavy code (large SDK client setup, model loading) inside the handler instead of the module-level scope, forcing it to re-run on every invocation instead of being reused across warm starts; not setting reserved concurrency limits, allowing one runaway function to consume the account's entire concurrency quota and throttle unrelated functions.

## RDS Multi-AZ, Read Replicas, and Failover Behavior
RDS Multi-AZ deployments provide synchronous standby replication for automatic failover (availability), while read replicas provide asynchronous copies for read scaling (not primarily for availability); verify which feature is actually configured, since conflating them leads to wrong assumptions about failover time and replica lag tolerance.
```bash
aws rds describe-db-instances --db-instance-identifier mydb --query "DBInstances[0].{MultiAZ:MultiAZ,ReadReplicaDBInstanceIdentifiers:ReadReplicaDBInstanceIdentifiers}"
aws rds failover-db-cluster --db-cluster-identifier mydb-cluster   # test failover deliberately in staging
```
Test an actual failover in a staging environment to measure real downtime and confirm application retry/reconnect logic handles the endpoint DNS change correctly, rather than trusting documented failover time estimates alone.
**Pitfalls:** assuming a read replica provides automatic failover/high-availability like Multi-AZ does, when it requires manual promotion and isn't designed for that purpose; not testing application reconnection behavior during failover, discovering connection-pool/DNS-caching issues only during a real incident.

## CloudFormation and Infrastructure Drift
CloudFormation manages AWS resources declaratively via templates and stacks, similar in spirit to Terraform but AWS-native; verify actual stack drift (manual changes made outside CloudFormation) with `detect-stack-drift` periodically, since undetected drift causes future stack updates to behave unpredictably or fail.
```bash
aws cloudformation detect-stack-drift --stack-name my-stack
aws cloudformation describe-stack-resource-drifts --stack-name my-stack --stack-resource-drift-status-filters MODIFIED
```
Verify a stack update's changeset (`create-change-set` + review before `execute-change-set`) doesn't include unintended resource replacements before applying, especially for stateful resources like databases.
**Pitfalls:** manually editing a CloudFormation-managed resource in the console for a quick fix, causing drift that silently breaks the next automated stack update; executing a change set without reviewing it first, missing an unexpected resource replacement that would cause data loss.
