# AI Governance Architecture and Data-Flow Reference

This document gives adopters a vendor-neutral view of where the repository's controls apply. It is a reference model, not a required product architecture: real systems may combine or split these components, but the trust boundaries and control questions should still be made explicit.

## Reference architecture

```text
people / business process
          |
          v
+-----------------------+
| AI application / UI   |
+-----------------------+
    |        |        |
    |        |        +--------------------+
    |        |                             |
    v        v                             v
model /   retrieval +                 tools / agents
provider  enterprise data             external actions
    |        |                             |
    +--------+-------------+---------------+
                           |
                           v
                    memory / indexes
                           |
                           v
                 logs, evidence, audit
```

A production design should document the concrete identity, network, data-classification, retention, approval, and monitoring boundaries behind each arrow rather than assuming that components sharing one application also share one trust level.

## Main trust boundaries

### 1. Human or business process -> AI application

The application should know who is asking, what business purpose is permitted, what data classifications are allowed, and when an output requires human review.

Use:

- [AI Governance Checklist](../checklists/ai-governance-checklist.md)
- [Enterprise AI Usage Policy](../checklists/enterprise-ai-usage-policy.md)
- [AI Data Handling Decision Guide](../checklists/ai-data-handling-decision-guide.md)
- [Role-Based AI Governance Checklists](../checklists/role-based-checklists.md)

**Stop condition:** do not accept the request when the user, purpose, data class, or approved-tool boundary cannot be established for a sensitive use case.

### 2. AI application -> model or model provider

Prompts may contain user input, retrieved enterprise data, system instructions, code, files, and prior conversation context. The provider boundary therefore needs explicit decisions about tenancy, region, retention, training use, access controls, contractual terms, and supported security controls.

Use:

- [AI Vendor Assessment](../checklists/ai-vendor-assessment.md)
- [LLM Application Security Checklist](../checklists/llm-application-security-checklist.md)
- [AI System Inventory](../templates/ai-system-inventory.csv)

**Stop condition:** do not transmit restricted information when the destination provider, account, region, retention behaviour, or contractual approval is unknown or outside policy.

### 3. External or enterprise data -> retrieval layer -> model

RAG and search flows can convert a user who has limited application access into a broad data reader if authorization is enforced only at ingestion time. Retrieval should preserve source identity, authorization scope, provenance, and freshness at query time.

Use:

- [LLM Application Security Checklist](../checklists/llm-application-security-checklist.md)
- [Agent Memory and Code Index Governance Checklist](../checklists/agent-memory-governance-checklist.md)
- [AI Data Handling Decision Guide](../checklists/ai-data-handling-decision-guide.md)

**Stop condition:** fail closed when the system cannot prove the requesting identity is entitled to the retrieved source, or when stale/unverifiable material would materially affect the decision.

### 4. Model or orchestrator -> tools, agents, and external actions

Tool calls can turn probabilistic output into durable change. Treat tool selection, delegated agents, shell/cloud access, writes, purchases, messages, deployments, and destructive operations as separate authorization events rather than natural extensions of text generation.

Use:

- [Agent Contract and Orchestration Gate Governance Checklist](../checklists/agent-contract-orchestration-gates.md)
- [LLM Application Security Checklist](../checklists/llm-application-security-checklist.md)
- [AI Incident Response Playbook](../checklists/ai-incident-response-playbook.md)

**Stop condition:** block execution when the requested action exceeds the agent contract, lacks required approval, cannot be made idempotent/retry-safe, or cannot produce the required validation and audit evidence.

### 5. Application / tools / retrieval -> durable memory or structural indexes

Conversation summaries, embeddings, checkpoints, code indexes, caches, and other persistent memory may outlive the original authorization context. Persistence therefore needs project or tenant isolation, query-time authorization, provenance, staleness handling, retention, deletion, and revocation behaviour.

Use:

- [Agent Memory and Code Index Governance Checklist](../checklists/agent-memory-governance-checklist.md)
- [AI System Periodic Review Checklist](../checklists/ai-system-periodic-review-checklist.md)

**Stop condition:** do not persist or retrieve durable memory when ownership, permitted lifetime, isolation boundary, provenance, or deletion path is undefined for sensitive information.

### 6. All components -> logs, evidence, and monitoring

Audit data should prove important decisions without becoming a second uncontrolled copy of prompts, secrets, personal data, retrieved documents, or model outputs. Capture the minimum evidence needed for accountability and incident response, apply access controls, and define retention.

Use:

- [AI Risk Register](../templates/ai-risk-register.csv)
- [AI Control Ownership Matrix](../templates/ai-control-ownership-matrix.csv)
- [AI Incident Response Playbook](../checklists/ai-incident-response-playbook.md)
- [AI System Periodic Review Checklist](../checklists/ai-system-periodic-review-checklist.md)

**Stop condition:** pause a high-impact workflow if required audit evidence cannot be recorded, or if logging would create an unapproved sensitive-data copy that cannot be protected appropriately.

## Minimum data-flow record

For each material path, record at least:

| Field | Question to answer |
| --- | --- |
| Source | Which user, system, repository, datastore, or vendor produces the data? |
| Destination | Which application, model, tool, memory store, log, or external service receives it? |
| Identity | Which human or workload identity authorizes the transfer? |
| Data class | What sensitivity, personal-data, customer, source-code, or secret classifications can cross the boundary? |
| Purpose | Why is the transfer required for the approved use case? |
| Authorization | Where is access checked, and is it re-evaluated at retrieval/action time? |
| Retention | How long can the destination retain the data, including backups and derived memory? |
| Transformation | Is the data filtered, redacted, summarized, embedded, or otherwise transformed? |
| Evidence | What proves the control operated without unnecessarily duplicating sensitive content? |
| Failure mode | What happens when identity, policy, provenance, approval, or a downstream dependency cannot be verified? |

## Control placement principle

Controls should sit as close as practical to the boundary they protect. A policy document alone cannot enforce retrieval authorization; a model prompt alone cannot safely authorize a production write; and an audit log created after an action cannot replace a missing approval gate.

For each high-impact flow, combine preventive controls (authorization, allow-lists, data filtering, approval gates), detective controls (logging, monitoring, evaluation), and recovery controls (revocation, rollback, incident response). Record any residual risk in the risk register with an accountable owner.

## Review triggers

Revisit the architecture and data-flow record when a new model/provider, tool, agent, datastore, memory/index, identity path, region, data class, automated action, or retention mode is introduced; when an authorization model changes; or after an incident exposes an unexpected data path.

Use the [repository threat model](threat-model.md) for risks associated with this public guidance repository itself. Adopters should create a system-specific threat model for their deployed architecture rather than treating this reference diagram as a substitute.
