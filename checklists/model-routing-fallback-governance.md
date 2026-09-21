# Model Routing And Fallback Governance Checklist

Use this checklist when an AI application, gateway, coding assistant, or agent can choose between model tiers, providers, deployments, regions, or fallback routes based on capability, cost, quota, cache state, latency, or availability.

The goal is to keep optimisation inside an approved authorization boundary. A cheaper or available route is not automatically an acceptable route.

## Approved Route Inventory

- [ ] Each permitted route has an identifier, owner, provider, model/deployment class, tenancy, region, retention policy, and applicable data classifications.
- [ ] Approved routes identify their intended capability/risk tier rather than relying only on provider model names.
- [ ] Prohibited providers, regions, tenants, training/data-use modes, and deployment types are explicit.
- [ ] Route approval records include the security/vendor review or policy basis for use.
- [ ] Changes to provider terms, retention, hosting region, model family, or data-use policy trigger re-evaluation before the route remains eligible.

## Task Classification And Selection

- [ ] Routing considers task risk, reversibility, sensitivity, required capability, and verification cost rather than prompt length or price alone.
- [ ] Security, production, architecture, privacy, legal, financial, regulated, or destructive work has defined minimum capability and review requirements.
- [ ] The router chooses only from routes already approved for the task's data classification and purpose.
- [ ] A low-cost route is rejected when it cannot meet the required capability or verification standard.
- [ ] User- or policy-selected provider/model constraints cannot be silently overridden for cost or latency.

## Budget, Quota, And Rate Controls

- [ ] Relevant per-request, per-task, tenant, project, or period budgets are documented where runaway usage creates material risk.
- [ ] Retry and fallback attempts count toward the same resource budget rather than resetting it silently.
- [ ] Quota exhaustion, rate limiting, or latency pressure has defined stop, queue, degrade, or escalation behaviour.
- [ ] Budget ceilings do not authorize crossing a provider, tenancy, region, retention, or data boundary.
- [ ] When no approved capable route remains, the workflow stops or requests explicit approval instead of silently degrading.

## Governed Fallbacks

- [ ] Fallback order is explicit and testable rather than inferred dynamically from cheapest current price.
- [ ] Each fallback preserves the minimum required capability and all applicable data-handling, retention, regional, security, and contractual controls.
- [ ] Crossing to a different provider, tenant, region, retention policy, or model family is treated as a material route change and requires prior policy approval.
- [ ] Fallback events record why the primary route failed or became unavailable.
- [ ] The fallback result receives the same or stronger verification required for the task.
- [ ] Fallback chains have a bounded attempt count and terminal stop condition.
- [ ] Ambiguous external failures are distinguished from confirmed non-execution so retries do not duplicate consequential actions.

## Cache Affinity And Context Reuse

- [ ] Cache affinity is used only between routes already approved and capable for the task.
- [ ] Cached prefixes, summaries, or retrieved context are bound to the correct project/tenant and are invalidated when source state or authorization changes.
- [ ] Cache savings never override a required model escalation or fresh evidence requirement.
- [ ] Cache-hit or cache-write telemetry is interpreted using the provider's documented semantics and pricing basis.
- [ ] Sensitive cached content follows the same access, retention, deletion, and incident controls as equivalent uncached content.

## Routing Telemetry And Privacy

Record enough metadata to explain material routing decisions without collecting prompt/source content unnecessarily.

- [ ] Telemetry includes task/request identifier, risk/capability class, selected route, fallback/escalation reason, attempts, latency, verification result, and final route.
- [ ] Token and cache metrics are recorded only when actually exposed or clearly labelled as estimates.
- [ ] Cost records distinguish actual billed cost from API-equivalent estimates and internally allocated subscription cost.
- [ ] Price-based comparisons record the source and effective date used.
- [ ] Project/user identifiers are pseudonymised where full identity is not necessary.
- [ ] Routine routing telemetry excludes prompts, source code, secrets, retrieved documents, and personal data unless a separately approved use requires them.
- [ ] Access and retention for routing telemetry are defined and proportionate to its operational/audit purpose.

## Verification And Escalation

- [ ] Each capability tier has a minimum verification standard appropriate to its use cases.
- [ ] A stronger model does not replace deterministic tests, policy checks, or required human approval.
- [ ] A cheaper model is not accepted merely because it produced syntactically valid output.
- [ ] Verification failure, material ambiguity, repeated incorrect results, or unexpected scope growth triggers escalation or stop.
- [ ] High-impact route changes are visible to the operator/reviewer when they materially affect risk, data handling, or evidence quality.

## Evidence And Review

Retain evidence proportionate to risk, such as:

- approved route inventory and owner;
- data/classification policy used for route eligibility;
- routing and fallback policy version;
- budget/quota configuration;
- route-change approvals and exceptions;
- fallback/retry records;
- cost/cache telemetry methodology;
- verification outcomes;
- periodic review of provider, deployment, pricing-assumption, and retention changes.

## Testing

- [ ] Tests prove the router cannot select an unapproved provider, tenancy, region, retention mode, or data boundary.
- [ ] Tests cover primary-route outage, quota exhaustion, rate limiting, and timeout scenarios.
- [ ] Tests prove fallback chains stop when no approved capable route remains.
- [ ] Tests cover a high-risk task being rejected by a lower capability tier even when it is cheaper.
- [ ] Tests verify cache state cannot leak across projects/tenants or bypass freshness controls.
- [ ] Tests verify retry/fallback accounting does not hide total cost or exceed configured attempt limits.
- [ ] Tests confirm routing telemetry remains useful without requiring raw prompts or source content.

## Design References

This checklist is vendor-neutral. The controls are informed by general cost-aware routing, caching, fallback, and observability patterns used in public AI gateways, including [OmniRoute](https://github.com/BunsDev/omniroute), and by the companion [AI Token Efficiency Playbook model-routing guidance](https://github.com/ravinperera/ai-token-efficiency-playbook/blob/main/guidelines/model-routing.md).

These are design references, not dependencies or evidence that a particular gateway satisfies this checklist. Do not reuse provider price tables or savings claims as durable governance facts; independently validate any quantitative claim used for a real deployment.
