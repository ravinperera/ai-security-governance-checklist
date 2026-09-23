# AI Usage, Token, And Cost Telemetry Governance Checklist

Use this checklist when an organisation collects AI usage, token, cache, retry, routing, latency, cost, or productivity telemetry from coding assistants, chat systems, agents, gateways, or model APIs.

The objective is to make optimisation measurable without creating a broader sensitive-data, surveillance, or compliance risk. Apply legal, privacy, employment, security, and records-management review appropriate to the organisation and jurisdictions involved.

## Purpose And Ownership

- [ ] The telemetry purpose is documented: for example capacity, reliability, cost allocation, token efficiency, routing quality, or incident investigation.
- [ ] A business/technical owner is accountable for the dataset and its use.
- [ ] Secondary uses require review instead of silently reusing cost telemetry for unrelated monitoring or performance decisions.
- [ ] The minimum decision that each collected field supports is known.
- [ ] Collection stops or is reduced when the original purpose no longer requires the data.

## Data Minimisation

- [ ] Ordinary cost/usage analytics do not require storing raw prompts, completions, source code, retrieved documents, secrets, credentials, customer content, or full chat transcripts.
- [ ] Prefer counters and metadata such as task category, approved model/tier, token classes, cache signals, attempts, latency, cost basis, and verification outcome.
- [ ] Project, user, repository, or workstation identifiers are pseudonymised or aggregated when named identity is not required.
- [ ] Free-text telemetry fields are avoided or tightly constrained because they can accidentally capture sensitive content.
- [ ] Debug/incident modes that collect richer evidence are time-bounded, explicitly approved, and separated from normal analytics.

## Identity And Workforce Monitoring

- [ ] Individual-level telemetry is collected only when there is a defined operational need that cannot be met with aggregate or pseudonymous data.
- [ ] Applicable employment, works-council, privacy, notice, consultation, and acceptable-use requirements are assessed before telemetry is used to evaluate individuals.
- [ ] Cost, token count, model tier, retry rate, or tool usage is not treated as a standalone measure of employee productivity or quality.
- [ ] Access to identifiable workforce telemetry is narrower than access to aggregate engineering/cost dashboards.
- [ ] People can understand, where required, what is collected, why, how long it is kept, and who can access it.

## Outcome And Productivity Attribution

Usage telemetry can be associated with downstream events such as commits, test runs, pull requests, merges, reverts, deployments, tickets, or review outcomes. Those associations can be useful for analysis, but they are usually **proxies**, not proof that the AI caused the outcome.

- [ ] Attribution rules are documented, including event type, matching key, time window, exclusions, and the version of the rule used for each material analysis.
- [ ] Commit, merge, test, deployment, or ticket proximity is labelled as an association unless causality has been independently established.
- [ ] Session labels such as `productive`, `abandoned`, `successful`, or `wasted` have documented definitions and do not conceal unknown or mixed outcomes.
- [ ] Research, planning, code review, incident analysis, rejected designs, and learning tasks are not automatically treated as zero-value because no nearby commit was created.
- [ ] A nearby or merged commit is not treated as proof of AI-generated quality; verification, review, defects/reverts, safety findings, and the actual task outcome remain relevant.
- [ ] Human work, pair work, autocomplete, background agents, reused generated code, and delayed commits are recognised as attribution-confounding factors where relevant.
- [ ] Unknown or partial attribution is retained as `unknown`/`partial` rather than forced into a positive or negative category.
- [ ] Individual ranking, employment decisions, compensation, disciplinary action, or other consequential workforce decisions are not automated from these proxies and require separate lawful governance and validation.
- [ ] Cross-team or cross-project comparisons control for materially different task mix, tooling, model access, subscription/API charging, cache behaviour, retry policies, and repository characteristics.
- [ ] Productivity or ROI claims state the attribution method, uncertainty, verification basis, and whether the result is correlational or causal.

## Data Boundaries And Transfers

- [ ] Collection, storage, processing region, tenancy, and subprocessors are documented.
- [ ] Telemetry does not silently cross an approved provider, tenant, region, retention, or data-classification boundary merely to enable cheaper analytics.
- [ ] Local-first collection is preferred when centralisation is unnecessary.
- [ ] Central collectors receive only the fields required for their approved purpose.
- [ ] Cross-border or third-party transfers receive the same privacy/security/vendor review as other operational datasets of equivalent sensitivity.

## Access, Security, And Retention

- [ ] Access uses least privilege, approved roles/groups, and strong authentication.
- [ ] Administrative access and bulk export are logged where supported.
- [ ] Retention periods are defined separately for aggregate metrics, identifiable metadata, and any exceptional raw-content captures.
- [ ] Deletion/expiry is technically enforced rather than relying only on policy text where practical.
- [ ] Backup, export, support-dump, and data-lake copies are included in retention and deletion design.
- [ ] Encryption and incident-response controls match the sensitivity of the telemetry.

## Measurement Integrity

- [ ] Input, output, cached-input, cache-write, retry, and fallback values are kept distinct when the provider exposes them.
- [ ] Missing provider telemetry is recorded as `unknown` or unavailable rather than fabricated.
- [ ] Telemetry source, collection method, and material schema/version changes are recorded.
- [ ] Aggregations preserve enough provenance to explain material cost/routing decisions.
- [ ] Dashboard definitions and derived metrics have owners and change control when they drive budget or policy decisions.

## Cost And Savings Claims

- [ ] Billed cost, API-equivalent estimates, and allocated subscription cost are labelled as different cost views.
- [ ] Pricing source, currency, contract/public rate basis, and effective date are recorded for estimates.
- [ ] Fixed subscription usage is not presented as equivalent cash savings solely because an API-equivalent estimate decreased.
- [ ] Retry tax, cache benefit, and routing-waste metrics have documented formulas.
- [ ] Counterfactual savings claims identify the alternative model/route and use paired runs, historical evidence, or another reproducible basis rather than assuming the cheapest model would have succeeded.
- [ ] Productivity, yield, or ROI claims distinguish correlation from causation and identify the outcome-attribution method and uncertainty.
- [ ] Quality, verification, latency, retries, and safety are considered alongside token/cost reduction.

## Routing And Model-Governance Interaction

- [ ] Telemetry used for routing includes only the minimum state needed for the decision.
- [ ] A budget/quota signal cannot override approved provider, tenancy, region, retention, capability, or data-boundary policy.
- [ ] Fallbacks caused by rate limits, quota exhaustion, or model unavailability are recorded without exposing sensitive prompt content.
- [ ] Repeated failed routes trigger investigation or stop conditions rather than unbounded retries.
- [ ] Material routing-policy changes trigger reassessment using the [Model Routing And Fallback Governance Checklist](model-routing-fallback-governance.md).

## Export, Deletion, And Incident Handling

- [ ] Dataset owners know how to export evidence needed for audit or investigation without exporting unrelated user content.
- [ ] Deletion or correction requests can be applied where required and technically feasible.
- [ ] Telemetry leaks, unexpected prompt/source capture, unauthorised workforce monitoring, or cross-boundary export are treated as governance/security/privacy incidents.
- [ ] Incident handling follows the [AI Incident Response Playbook](ai-incident-response-playbook.md) where applicable.
- [ ] After an incident, collection scope and dashboard access are reviewed before normal telemetry resumes.

## Review Triggers

Reassess this control set when any of the following changes materially:

- telemetry fields or granularity;
- identifiable user/workforce linkage;
- provider, collector, region, tenant, or subprocessor;
- retention period;
- pricing/cost-allocation method;
- outcome-attribution or productivity-label methodology;
- routing or fallback policy;
- use of telemetry for performance management, compliance, or automated decisions;
- collection of prompts, completions, source, retrieved documents, or other raw content.

## Minimum Evidence

Retain enough evidence to show:

- approved telemetry purpose and owner;
- field/schema inventory and sensitivity classification;
- access and retention decisions;
- region/tenant/vendor data flow;
- metric definitions and pricing/counterfactual basis where cost claims are made;
- outcome-attribution definitions, version and uncertainty where productivity/ROI claims are made;
- review date and material changes;
- exceptions and their expiry/owner.

## Pattern Note

Local-first, cross-tool observability projects such as [CodeBurn](https://github.com/getagentseal/codeburn) illustrate useful attribution ideas including model/project/task breakdowns, cache-aware accounting, retry cost, routing analysis, subscription tracking, and associations between AI sessions and downstream engineering events. These controls extract vendor-neutral governance principles only; they do not copy implementation code, pricing tables, upstream savings claims, or treat event proximity as independently verified causation. CodeBurn was reviewed 2026-09-23 and is MIT-licensed.
