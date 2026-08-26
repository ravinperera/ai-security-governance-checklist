# Agent Contract And Orchestration Gate Governance Checklist

Use this checklist when an AI system can choose tools, delegate work, coordinate specialist agents, advance through multi-stage workflows, or take actions that persist outside the model conversation.

The goal is to make authority and stage transitions explicit. A detailed persona or capable model is not an authorization model, and an agent saying that a task is complete is not sufficient evidence for a high-impact transition.

## Agent Contract

Define an auditable contract for each agent or specialist role.

- [ ] The agent has a unique name/identifier and a named business and technical owner.
- [ ] The business purpose and supported use cases are documented.
- [ ] Expected inputs and required input validation are defined.
- [ ] Expected outputs, schemas, quality criteria, and downstream consumers are defined.
- [ ] Permitted tools, connectors, APIs, repositories, environments, and data classes are explicitly listed or policy-resolved.
- [ ] Prohibited tools, data, environments, and actions are explicit rather than inferred from absence.
- [ ] The agent's authority boundary states which actions it may recommend, prepare, execute, or never perform.
- [ ] Human approval requirements are defined for security-sensitive, financial, legal, customer-facing, production, destructive, or otherwise high-impact actions.
- [ ] Success criteria are measurable enough to verify independently of the agent's own narrative.
- [ ] Escalation triggers cover ambiguity, missing evidence, policy conflict, repeated failure, unexpected scope growth, and unsafe or unverified state.
- [ ] Cost, token, time, rate, concurrency, and other relevant resource limits are defined where runaway execution could create risk.

## Delegation And Specialist Agents

- [ ] The parent/orchestrator may delegate only tasks that are inside its own authority boundary.
- [ ] Delegation does not increase permissions merely because a specialist role would normally need broader access.
- [ ] Each delegated task carries a scoped objective, inputs, constraints, expected output, and completion criteria.
- [ ] Specialists receive only the data and tools required for their task rather than the orchestrator's full context by default.
- [ ] A delegation chain remains attributable to the initiating user/workflow and accountable owner.
- [ ] Sub-agents cannot create further agents or delegate again unless that capability is explicitly approved.
- [ ] Conflicting specialist outputs are resolved through evidence, deterministic checks, independent review, or escalation rather than majority vote alone.
- [ ] Coordination overhead is measured so adding more agents does not silently increase cost or reduce reliability.

## Workflow Stage Contract

For each material workflow stage, define:

- [ ] entry criteria and required inputs;
- [ ] permitted tools/actions during the stage;
- [ ] expected artifacts and their schema/version;
- [ ] deterministic validations available before exit;
- [ ] review criteria that cannot be reduced to deterministic checks;
- [ ] required approver or reviewer based on risk;
- [ ] success, retry, rollback, escalation, and terminal-failure conditions;
- [ ] the exact next stage(s) that may follow.

A useful model is:

```text
entry criteria -> execute scoped work -> validate artifacts -> review/approve -> checkpoint -> advance
```

Do not allow a free-form model response to skip required stages or gates merely because it claims the outcome is safe.

## Validation And Approval Gates

- [ ] Prefer deterministic validation for machine-checkable properties such as schema validity, tests, signatures, policy rules, checksums, allowed targets, and required fields.
- [ ] Keep deterministic validation separate from model self-review so failures cannot be talked around.
- [ ] Treat model self-review as additional evidence, not as independent approval.
- [ ] Independent review is performed by a genuinely separate person/system when policy requires independence; the same agent re-labelling itself as a reviewer does not create independence.
- [ ] Human approvals identify the approver, decision, scope, timestamp, and artifact/version approved.
- [ ] Approval is bound to the exact action or artifact so later material changes invalidate or re-trigger the gate.
- [ ] If a required gate cannot be evaluated, the workflow fails closed or escalates rather than silently advancing.
- [ ] Time-limited approvals and exceptions expire automatically or are revalidated before reuse.

## External Actions And Side Effects

- [ ] Read-only discovery is distinguished from state-changing actions.
- [ ] The agent previews high-impact actions and their targets before approval where practical.
- [ ] Idempotency keys, deduplication, or equivalent safeguards exist for retryable external actions where duplicate execution would be harmful.
- [ ] Retries distinguish transient technical failure from an action that may already have succeeded remotely.
- [ ] The workflow verifies authoritative post-action state rather than trusting only a tool response or conversational memory.
- [ ] Rollback/compensation is defined where a reversible external action can fail part-way through a workflow.
- [ ] Destructive or irreversible actions have stronger confirmation and authorization controls than ordinary writes.

## Checkpoints And Resumability

- [ ] A checkpoint records the workflow/stage identifier, objective, current state, completed artifacts, next permitted action, and unresolved blockers.
- [ ] Checkpoints identify source versions/revisions needed to detect stale resumed work.
- [ ] Decisions record the evidence or policy basis needed to understand why a path was chosen.
- [ ] Approval evidence is referenced rather than replaced by a model-generated statement that approval occurred.
- [ ] Resume logic revalidates time-sensitive authorization, source state, policy, and external-resource state before continuing.
- [ ] A resumed workflow cannot replay a completed side effect merely because the previous conversation is unavailable.
- [ ] Corrupted, partial, or unverified checkpoints fail safely.

For persistence, retention, tenant isolation, provenance, and deletion of checkpoints or durable state, also use the [Agent Memory And Code Index Governance Checklist](agent-memory-governance-checklist.md).

## Evidence And Auditability

Retain evidence proportionate to risk, such as:

- agent contract/version and owner;
- tool/data permission policy;
- workflow/stage manifest or equivalent design record;
- validation results and produced artifact hashes/versions;
- review and approval records;
- delegation graph or task lineage for material workflows;
- decision and exception records;
- external action receipts and authoritative post-action verification;
- cost/token/time/resource usage where limits are part of the control;
- checkpoint/resume and rollback/recovery test results.

## Testing

- [ ] Tests prove agents cannot invoke prohibited tools or cross defined data/environment boundaries.
- [ ] Tests prove delegated agents do not inherit unauthorized capabilities.
- [ ] Tests cover missing, failed, and stale validation/approval gates.
- [ ] Tests cover duplicate/retried external actions and ambiguous remote success.
- [ ] Tests cover resume after interruption, including stale checkpoints and changed source state.
- [ ] Tests verify that a model's claim of success cannot bypass a failing deterministic control.
- [ ] Tabletop or simulation tests cover escalation when reviewers, approvers, tools, or authoritative evidence are unavailable.

For application-level prompt injection, tool-output trust, least privilege, and secure action design, also use the [LLM Application Security Checklist](llm-application-security-checklist.md).

## Design References

This checklist is vendor-neutral. Public projects demonstrate patterns worth translating into controls without making their architecture a requirement:

- Agency Agents uses explicit specialist role definitions with missions, workflows, deliverables, and success metrics: https://github.com/msitarzewski/agency-agents
- OpenMontage documents declarative pipeline stages, review criteria, success gates, checkpoints, and human approval in an agent-driven workflow: https://github.com/calesthio/OpenMontage

These are design references, not endorsements, dependencies, or proof that a particular implementation satisfies this checklist.
