# Agent Memory And Code Index Governance Checklist

Use this checklist when an AI assistant, coding agent, RAG system, or MCP-style tool persists information across sessions. This includes conversation memory, summaries, retrieval caches, embeddings, code indexes, structural knowledge graphs, checkpoints, and other durable agent state.

Persistent memory can improve continuity and reduce repeated retrieval, but it also creates a new data store with its own access, retention, freshness, and incident risks.

## Scope And Ownership

- [ ] Each persistent memory or index has a named business and technical owner.
- [ ] The purpose of the store is documented separately from the model or agent purpose.
- [ ] Approved source systems, repositories, projects, tenants, and data classifications are defined.
- [ ] The organisation knows whether the store contains raw content, summaries, embeddings, structural metadata, decisions, credentials, or tool outputs.
- [ ] Sensitive categories that must never be persisted are explicitly defined.

## Isolation And Access Control

- [ ] Tenant, customer, repository, environment, and project boundaries are enforced in the storage and retrieval layer.
- [ ] An agent cannot query another project's memory merely because it can name that project or index.
- [ ] Retrieval authorization is checked at query time and is not assumed from the permissions that existed when content was originally indexed.
- [ ] Service identities and users have least-privilege read, write, update, and deletion permissions.
- [ ] Administrative or cross-project search access is restricted and auditable.

## Provenance And Integrity

- [ ] Stored entries identify their source, owner or producing process, and creation/update time where practical.
- [ ] Repository-derived memory records the repository and revision, commit, artifact version, or other freshness reference when correctness depends on source state.
- [ ] Model-generated summaries and inferred relationships are distinguishable from authoritative source records.
- [ ] Integrity controls detect corrupted, partially written, or schema-invalid state before it is trusted.
- [ ] High-impact decisions are verified against authoritative current sources rather than relying only on remembered or indexed state.

## Freshness And Invalidation

- [ ] The system defines when memory, indexes, embeddings, or graph edges become stale.
- [ ] Relevant source changes trigger refresh, invalidation, or a clearly documented stale-state warning.
- [ ] Deleted or revoked source content is removed or made inaccessible from derived indexes and caches within the required timeframe.
- [ ] Queries can identify which source revision or refresh point their result came from when that matters to correctness.
- [ ] The agent fails safely or falls back to authoritative retrieval when memory freshness cannot be established for a material action.

## Retention And Deletion

- [ ] Retention periods are documented for raw memory, summaries, indexes, embeddings, checkpoints, and logs.
- [ ] Data minimisation is applied so full transcripts or source files are not persisted when smaller durable records are sufficient.
- [ ] User, customer, project, or repository deletion requirements propagate to derived memory stores where applicable.
- [ ] Backup and recovery processes do not unintentionally restore data that should remain deleted or revoked.
- [ ] Exit procedures cover export, migration, and verified deletion when a memory provider or agent platform is retired.

## Secrets And Sensitive Data

- [ ] Secrets, credentials, tokens, private keys, and other prohibited data are filtered or rejected before persistence where practical.
- [ ] Memory stores use encryption and access controls appropriate to the data classification.
- [ ] Logs avoid capturing complete sensitive prompts, retrieved documents, or memory entries unless explicitly required and protected.
- [ ] Prompt injection or retrieved content cannot silently mark itself as trusted durable memory without validation.
- [ ] Users and agents cannot convert temporary access to sensitive content into indefinite persistence without an approved basis.

## Agent Behaviour And Authority

- [ ] Remembered instructions cannot override higher-priority policy, current authorization, or explicit human approval requirements.
- [ ] Memory does not grant new tool permissions or expand an agent's authority.
- [ ] Checkpoints record workflow state without being treated as proof that an approval or external action actually occurred unless supported by authoritative evidence.
- [ ] Contradictory, superseded, or ambiguous memory causes verification or escalation rather than silent selection of the most convenient record.
- [ ] Automated consolidation or summarisation has a recovery path when persistence fails.

## Monitoring And Audit

- [ ] Material writes, updates, deletions, refreshes, and privileged retrievals are auditable where risk warrants it.
- [ ] Monitoring detects unusual cross-project queries, bulk extraction, repeated authorization failures, or unexpected memory growth.
- [ ] Cost and storage growth are monitored so persistent memory cannot expand without operational visibility.
- [ ] Incident response includes containment, invalidation, re-indexing, deletion, and credential rotation where memory exposure could reveal sensitive data.
- [ ] Periodic review confirms that stored data, permissions, retention, and source mappings still match the approved design.

## Testing

- [ ] Tests verify tenant/project isolation and query-time authorization.
- [ ] Tests cover revoked access, deleted source content, and stale index behaviour.
- [ ] Tests cover malicious retrieved content attempting to become durable instructions or memory.
- [ ] Tests verify that invalid or corrupted checkpoints/index entries fail safely.
- [ ] Recovery tests confirm that required state can be restored without reintroducing data that should remain deleted.

## Evidence To Retain

Keep evidence proportionate to risk, such as:

- architecture and data-flow diagrams;
- data classification and retention decisions;
- index/memory schemas and source mappings;
- access-control configuration and review records;
- deletion/invalidation test results;
- incident and recovery procedures;
- periodic review records.

This checklist is vendor-neutral. A persistent code graph, vector database, conversation-memory service, or local index may implement these controls differently, but the governance questions remain the same.
