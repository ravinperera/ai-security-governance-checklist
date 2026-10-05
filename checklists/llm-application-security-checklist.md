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

### Artifact And Publisher Verification

- [ ] Before approving an AI-suggested dependency, the owner verifies its intended package name, namespace, publisher and canonical source independently of the generated recommendation. A plausible or existing registry name is not sufficient evidence of identity or suitability.
- [ ] Model-registry organisations, upload destinations and access invitations are verified through an approved independent channel before private artifacts or permissions are shared; visual branding or a matching organisation name is not sufficient.
- [ ] Downloaded model/data artifacts record publisher, source, exact revision or digest, format and loader requirements. Custom loading code, install hooks and executable deserialization paths receive review before execution; an artifact described as data is not assumed inert.
- [ ] Integrity checks use approved source/digest or signing-key evidence. A valid signature, checksum or clean vulnerability scan does not replace publisher review, loader analysis or behavioural validation.
- [ ] Initial evaluation uses an approved isolated environment, bounded network/process permissions and no production credentials. Model, loader or dataset changes trigger applicable behavioural and security checks before promotion.
- [ ] The approval record identifies the reviewer, artifact/version, permitted use, checks, unresolved risks and rollback source. Component terms and skill dependencies follow the existing [skill licence and supply-chain review](agent-skill-governance-checklist.md), rather than assuming one top-level licence covers everything.

## RAG And Vector Stores

- [ ] Data sources are approved.
- [ ] Document ingestion process is controlled.
- [ ] Access controls are applied before retrieval.
- [ ] Private documents are not retrievable by unauthorized users.
- [ ] Embedding stores are backed up and protected.
- [ ] Index deletion and retention are documented.

### End-To-End Poisoned-Source Scenario

This is a test design for adopting systems, not a runtime test implemented by this repository. Use an authorised disposable corpus with fictional documents, identifiers and mocked side-effect tools; do not send malicious material to real employees or production indexes.

- [ ] Compare a legitimate source with a fictional externally supplied message that contains conflicting instructions or decision-critical facts, then trace ingestion, indexing, retrieval and the resulting answer/action under the same authorised user scope.
- [ ] Retrieval permission does not promote source content to trusted instructions. Consequential values are checked against the designated authoritative fixture; conflicting retrieved claims trigger verification or escalation rather than silently replacing the authoritative record.
- [ ] Required human approval and server-side tool authorization remain effective. Record that mocked prohibited disclosure/actions did not occur, alongside the legitimate-task result; an injection alert alone is not the acceptance criterion.
- [ ] Recovery quarantines the suspect source while preserving restricted evidence and checks affected indexes, summaries, caches and durable memory. Repeat retrieval after invalidation/re-indexing and recovery so removed or revoked content is not silently restored; use the [memory lifecycle checks](agent-memory-governance-checklist.md).
- [ ] Retain fixture/source revisions, model and ingestion/index versions, caller scope, expected versus observed outcomes, reviewer and unresolved gaps. Report the scenario's limits rather than claiming that one passing test eliminates prompt injection.

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

## Source And Scope Of The Added Scenarios

Datadog's *AI Security Best Practices Guide*, supplied 19-page PDF, reports poisoned-email/RAG examples on pp. 5 and 15–18 and hallucinated-package, registry-impersonation and model-loader risks on pp. 10–13. Reviewed 2026-10-05; [publisher landing page](https://www.datadoghq.com/resources/ai-security-best-practices/). PDF SHA-256: `8dc1ffa039c7c6ba60c7860baf1270ef69b4ccbc84897f99cc5399995013d737`. The intake records and synthetic acceptance/recovery checks above are original local recommendations informed by those reported examples, not an independent investigation of the incidents or a copied vendor test suite. No PDF text, artwork, live attack or product subscription is included or required. For the infrastructure-abuse example, use the existing [incident-response playbook](ai-incident-response-playbook.md).
