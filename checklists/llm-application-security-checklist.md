# LLM Application Security Checklist

Use this checklist when building or approving applications that use large language models, retrieval-augmented generation, plugins, tools, or agents.

## Application Design

- [ ] AI system purpose is documented.
- [ ] Model provider and model version are documented.
- [ ] Data flow is documented.
- [ ] User roles and permissions are documented.
- [ ] External tools, plugins, APIs, and agents are documented.
- [ ] Human approval points are defined for high-impact actions.

## Prompt Injection

- [ ] System prompts are treated as sensitive configuration.
- [ ] User input is never trusted as instruction hierarchy.
- [ ] Retrieved content is treated as untrusted input.
- [ ] Tool calls require server-side authorization.
- [ ] Model output cannot directly override security controls.
- [ ] Prompt injection test cases are included in testing.

## Output Handling

- [ ] AI output is validated before use by downstream systems.
- [ ] AI output is encoded or escaped before rendering in browsers.
- [ ] AI output is not directly executed as code or shell commands.
- [ ] AI-generated SQL, scripts, or infrastructure changes require human review.
- [ ] AI output used in customer communication is reviewed where appropriate.

## Sensitive Information Disclosure

- [ ] Secrets are never included in prompts.
- [ ] Customer data is masked or excluded unless approved.
- [ ] Logs do not capture sensitive prompts or outputs unnecessarily.
- [ ] System prompts are not exposed to users.
- [ ] Data retention settings are understood and documented.

## Excessive Agency

- [ ] Agents cannot perform high-risk actions without approval.
- [ ] Tool permissions are least privilege.
- [ ] Agents cannot access unnecessary systems.
- [ ] Destructive actions require confirmation.
- [ ] Rate limits and budget controls are configured.
- [ ] Audit logs capture tool calls and outcomes.

## Multi-Agent Workflows

- [ ] Each agent has a documented role, permitted tools, data boundary, and action scope.
- [ ] Generation, independent validation, and approval are separated where the workflow's risk warrants it.
- [ ] An agent cannot increase its own authority by delegating or handing work to another agent.
- [ ] Downstream agents independently enforce authorization instead of trusting permission claims in an upstream prompt or handoff.
- [ ] Agent-to-agent handoffs use a defined schema or validated fields for task identity, recipient, state reference, and requested action where practical.
- [ ] Handoffs point to pinned or otherwise unambiguous source state for high-impact work, such as a commit SHA, immutable artifact, or versioned record.
- [ ] Untrusted model output, retrieved content, or external messages cannot silently become higher-priority instructions for another agent.
- [ ] Durable audit evidence records material handoffs, tool actions, approvals, failures, and outcomes without storing unnecessary sensitive prompt content.
- [ ] Conflicting instructions, ambiguous ownership, inconsistent workflow state, or missing approvals cause the workflow to stop or escalate rather than guess.
- [ ] Retry and delegation limits prevent loops, uncontrolled fan-out, cost exhaustion, and repeated high-impact actions.
- [ ] Human escalation is defined for privileged, destructive, externally consequential, or otherwise high-impact decisions.
- [ ] Tests cover attempts to bypass role boundaries, propagate excessive permissions, forge handoff state, or induce unsafe cross-agent actions.

## Supply Chain

- [ ] Model provider is approved.
- [ ] SDKs and AI libraries are dependency-scanned.
- [ ] Third-party prompts, plugins, and tools are reviewed.
- [ ] Model updates are tested before production rollout.
- [ ] Container images are scanned.
- [ ] CI/CD workflows are protected.

## RAG And Vector Stores

- [ ] Data sources are approved.
- [ ] Document ingestion process is controlled.
- [ ] Access controls are applied before retrieval.
- [ ] Private documents are not retrievable by unauthorized users.
- [ ] Embedding stores are backed up and protected.
- [ ] Index deletion and retention are documented.

## Persistent Agent Memory And Code Indexes

- [ ] Persistent memory, summaries, retrieval caches, embeddings, structural code indexes, and checkpoints are inventoried where used.
- [ ] Retrieval permissions are enforced at query time, not inherited indefinitely from the original indexing event.
- [ ] Tenant, repository, project, and environment boundaries are enforced in both storage and retrieval.
- [ ] Stored knowledge has enough provenance and revision information to detect stale or superseded state when correctness depends on freshness.
- [ ] Retention, invalidation, deletion, backup, and incident-response requirements include derived memory and indexes.
- [ ] Remembered instructions cannot override current authorization, policy, or human approval requirements.

Use the [Agent Memory And Code Index Governance Checklist](agent-memory-governance-checklist.md) for the full lifecycle review.

## Testing

- [ ] Prompt injection tests are performed.
- [ ] Data leakage tests are performed.
- [ ] Role bypass tests are performed.
- [ ] Unsafe output tests are performed.
- [ ] Cost exhaustion tests are performed.
- [ ] Abuse and rate-limit tests are performed.

## Operations

- [ ] Monitoring is enabled.
- [ ] Incident response process includes AI-specific scenarios.
- [ ] Rollback path exists for model or prompt changes.
- [ ] Cost monitoring is enabled.
- [ ] Abuse monitoring is enabled.
