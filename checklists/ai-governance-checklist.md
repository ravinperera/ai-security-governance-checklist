# AI Governance Checklist

Use this baseline before approving or expanding AI use inside an organisation. It is intentionally short: when a trigger below applies, use the linked specialist checklist rather than duplicating the detailed controls here.

## Ownership

- [ ] AI governance owner is assigned.
- [ ] Security owner is assigned.
- [ ] Legal/privacy owner is assigned.
- [ ] Business owner is assigned for each AI system.
- [ ] Technical owner is assigned for each AI system.
- [ ] Escalation path exists for AI incidents or policy breaches.

## AI System Inventory

- [ ] All approved AI tools are recorded.
- [ ] Internal AI systems are recorded.
- [ ] AI vendors are recorded.
- [ ] AI coding assistants are recorded.
- [ ] AI features embedded in SaaS products are recorded.
- [ ] Each system has owner, purpose, data classification, approval status, and review date.

## Data Protection

- [ ] Rules define what data can be entered into AI tools.
- [ ] Customer data is blocked unless formally approved.
- [ ] Secrets, API keys, credentials, and tokens are prohibited.
- [ ] Confidential business data is prohibited unless vendor and contract controls are approved.
- [ ] Personal data use is reviewed for privacy impact.
- [ ] Data retention and training-use terms are reviewed.

## Security Controls

- [ ] AI tools require SSO where available.
- [ ] MFA is enforced for administrative access.
- [ ] Access is granted through groups or approved roles.
- [ ] Admin users are reviewed regularly.
- [ ] Audit logs are enabled where available.
- [ ] Data export and sharing settings are reviewed.
- [ ] Vendor security documentation is reviewed.

## Engineering Controls

- [ ] AI-generated code is reviewed before merge.
- [ ] AI-generated code is scanned by SAST/dependency tools.
- [ ] Developers are told not to paste secrets or proprietary source code into unapproved AI tools.
- [ ] Generated infrastructure code is reviewed by qualified engineers.
- [ ] Generated scripts are tested in non-production first.
- [ ] Pull requests identify material AI-generated contributions where required by policy.
- [ ] Internally built LLM, RAG, or agent applications complete the [LLM Application Security Checklist](llm-application-security-checklist.md) before production use.

## Agents, Tools, And Memory

- [ ] Agents that can select tools, delegate work, advance workflow stages, or take external actions have explicit authority boundaries, success gates, and approval rules using the [Agent Contract And Orchestration Gate Governance Checklist](agent-contract-orchestration-gates.md).
- [ ] Persistent conversation memory, summaries, checkpoints, embeddings, retrieval caches, or code indexes are reviewed using the [Agent Memory And Code Index Governance Checklist](agent-memory-governance-checklist.md).
- [ ] Retrieval and tool authorization is evaluated at the time of access or action, not assumed from what the agent previously knew.
- [ ] High-impact autonomous actions fail closed when required approval, evidence, or policy checks are missing.

## Risk Management

- [ ] AI risks are recorded in a risk register.
- [ ] Risks are rated by likelihood and impact.
- [ ] Risk treatment owner is assigned.
- [ ] Residual risk is accepted by the right owner.
- [ ] High-risk AI use cases require formal approval.
- [ ] Exceptions have expiry dates.

## Vendor Management

- [ ] AI vendors complete security review.
- [ ] AI vendors complete privacy review.
- [ ] Data processing terms are reviewed.
- [ ] Subprocessors are reviewed.
- [ ] Training-on-customer-data settings are reviewed.
- [ ] Breach notification terms are reviewed.
- [ ] Exit and data deletion process is understood.
- [ ] New or materially changed providers are assessed with the [AI Vendor Assessment](ai-vendor-assessment.md).

## Transparency And User-Facing Obligations

- [ ] User-facing AI interactions and generated/manipulated content are assessed for disclosure or marking obligations in each relevant jurisdiction.
- [ ] EU-facing systems and content use cases are triaged with the [EU AI Act Article 50 Transparency Readiness Checklist](eu-ai-act-article-50-transparency.md) when Article 50 may apply.
- [ ] Required notices, markings, decisions, exceptions, and legal interpretations have an accountable owner and retained evidence.

## Monitoring, Incidents, And Review

- [ ] Approved AI tools are reviewed at least quarterly or on the organisation's documented risk-based cadence.
- [ ] Material model, provider, data-flow, tool, memory, autonomy, policy, or regulatory changes trigger reassessment rather than waiting for the next scheduled review.
- [ ] Shadow AI usage is reviewed.
- [ ] Logs are monitored where available.
- [ ] Suspected AI security, privacy, safety, or governance incidents follow the [AI Incident Response Playbook](ai-incident-response-playbook.md).
- [ ] Scheduled and event-driven reassessments use the [AI System Periodic Review Checklist](ai-system-periodic-review-checklist.md).
- [ ] Lessons learned are added to policy, controls, and training.

## Conditional Deep-Dive Router

Use the specialist document when the trigger applies:

| Trigger | Specialist control set |
| --- | --- |
| Internal LLM, RAG, or agent application | [LLM Application Security Checklist](llm-application-security-checklist.md) |
| Agent chooses tools, delegates, advances stages, or executes external actions | [Agent Contract And Orchestration Gate Governance Checklist](agent-contract-orchestration-gates.md) |
| Persistent memory, embeddings, retrieval caches, checkpoints, or code indexes | [Agent Memory And Code Index Governance Checklist](agent-memory-governance-checklist.md) |
| External AI provider or material vendor change | [AI Vendor Assessment](ai-vendor-assessment.md) |
| EU-facing interaction or generated/manipulated content where Article 50 may apply | [EU AI Act Article 50 Transparency Readiness Checklist](eu-ai-act-article-50-transparency.md) |
| Suspected AI security, privacy, safety, or policy incident | [AI Incident Response Playbook](ai-incident-response-playbook.md) |
| Scheduled review or material system change | [AI System Periodic Review Checklist](ai-system-periodic-review-checklist.md) |
| Unapproved or unknown AI usage | [Shadow AI Risk Checklist](shadow-ai-risk-checklist.md) |

The specialist checklists are implementation aids, not substitutes for system-specific legal, privacy, security, or risk assessment.
