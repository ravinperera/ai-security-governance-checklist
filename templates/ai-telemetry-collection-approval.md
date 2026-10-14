# AI Telemetry Collection Approval Record

Use this record to document one approved collection scope for AI usage telemetry, diagnostics, or optional content/transcript sharing. Create a new version when the purpose, collected fields/content, recipients, processing boundary, retention, or approval conditions change materially.

This template supports governance evidence only. It does not prescribe consent or any other legal basis; apply the organisation's reviewed legal, privacy, employment, security, and records-management requirements.

## Record Identity

| Field | Value |
| --- | --- |
| Record ID | |
| Scope version | |
| Status | Proposed / Approved / Withdrawn / Expired / Superseded |
| Effective date | |
| Expiry/review date | |
| Accountable owner | |
| Technical owner | |

## Purpose And Scope

**Purpose supported by this collection:**

**Systems, tools, teams, projects, or environments in scope:**

**Explicitly out of scope:**

**Collection mode:** Routine metrics / Diagnostic capture / Optional transcript or content sharing / Other

## Data And Content Categories

List only what is required for the approved purpose.

| Category or field | Why required | Sensitivity/classification | Identifiable? | Raw content? |
| --- | --- | --- | --- | --- |
| | | | Yes / No | Yes / No |

**Prohibited or deliberately excluded data:**

## Collection And Transfer Boundary

| Control point | Approved value |
| --- | --- |
| Collection source | |
| Collector/processor | |
| Storage location/region | |
| Tenant/account boundary | |
| Recipients/subprocessors | |
| Export destinations | |
| Cross-border transfer review reference | |

A lower-cost route, support workflow, retry path, or offline queue must not expand these boundaries without a new approval.

## Access, Retention, And Deletion

| Item | Decision |
| --- | --- |
| Access roles/groups | |
| Aggregate retention | |
| Identifiable metadata retention | |
| Raw diagnostic/content retention | |
| Backup/export handling | |
| Deletion/expiry mechanism | |
| Historical-copy exceptions | |

## Approval And Conditions

| Role | Name or accountable group | Decision | Date | Evidence/reference |
| --- | --- | --- | --- | --- |
| Business/technical owner | | Approve / Reject | | |
| Security/privacy review | | Approve / Reject / Not required | | |
| Legal/employment/records review, where applicable | | Approve / Reject / Not required | | |

**Conditions, restrictions, or required notices:**

**Organisation/customer/project policy constraints that override local opt-in:**

## Withdrawal, Queue, And In-Flight Handling

Document what happens if approval or an applicable opt-in is withdrawn while data is queued, offline, retrying, or already in flight.

- Future collection:
- Queued/offline payloads:
- Retried uploads:
- In-flight requests:
- Previously retained copies:
- Evidence that withdrawal/expiry was enforced:

Do not treat disabling a setting as proof that every historical copy was deleted.

## Verification

Record the system/version tested and the observed result.

| Scenario | Expected result | Observed result | Evidence |
| --- | --- | --- | --- |
| Routine telemetry on; optional content sharing off | No transcript/source export | | |
| Approval version superseded | Old approval cannot enable new scope | | |
| Withdrawal while offline/queued | Queued content is cancelled or quarantined per policy | | |
| Local opt-in conflicts with organisation policy | More restrictive rule wins | | |

## Review Triggers

Create a new review/version before materially changing:

- purpose or secondary use;
- collected fields, raw-content categories, or granularity;
- identifiable user/workforce linkage;
- collector, processor, recipient, tenant, region, or subprocessor;
- retention or deletion behaviour;
- optional content/transcript sharing;
- routing/fallback behaviour that changes the processing boundary;
- use for performance management, compliance, or consequential decisions.

## Decision Summary

**Decision:** Approved / Approved with conditions / Rejected / Withdrawn / Expired

**Residual risks or open actions:**

**Next review date:**

**Record/evidence location:**
