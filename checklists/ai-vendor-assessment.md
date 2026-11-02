# AI Vendor Assessment Checklist

Use this checklist before approving an AI vendor or AI-enabled SaaS platform.

## Vendor Overview

- [ ] Vendor legal name recorded.
- [ ] Product name recorded.
- [ ] Business owner assigned.
- [ ] Technical owner assigned.
- [ ] Use case documented.
- [ ] Data classification documented.
- [ ] Intended users documented.

## Security

- [ ] Vendor provides SOC 2, ISO 27001, or equivalent assurance evidence.
- [ ] MFA/SSO support is available.
- [ ] Role-based access control is available.
- [ ] Admin activity logging is available.
- [ ] Encryption in transit is documented.
- [ ] Encryption at rest is documented.
- [ ] Vulnerability management process is documented.
- [ ] Incident response and breach notification process is documented.

## AI-Specific Controls

- [ ] Vendor confirms whether customer data is used for model training.
- [ ] Opt-out from model training is available where required.
- [ ] Data retention period is documented.
- [ ] Prompt and output logging behaviour is documented.
- [ ] Subprocessors used for AI processing are documented.
- [ ] Model provider and hosting region are documented.
- [ ] Human review or moderation controls are available where required.
- [ ] Controls exist for prompt injection or unsafe output where relevant.

## Privacy And Legal

- [ ] Data Processing Agreement is reviewed.
- [ ] GDPR basis and roles are understood.
- [ ] International transfer mechanism is reviewed.
- [ ] Data deletion process is documented.
- [ ] User data export process is documented.
- [ ] Privacy policy is reviewed.
- [ ] Terms of service are reviewed.

## Operational Fit

- [ ] Integration method is documented.
- [ ] API limits and cost model are understood.
- [ ] Availability SLA is reviewed.
- [ ] Support model is reviewed.
- [ ] Exit plan is documented.
- [ ] Backup or export requirements are understood.

## Conditional AI Integration Review Gates

Apply the following questions **when the proposed product supports the capability**. Refer to the linked canonical control set for detailed verification; a vendor claim, questionnaire answer or product demo is not proof that a deployment meets the control.

- [ ] **Model routing or fallback:** Can the supplier disclose the actual model/hosting route, all potential fallback providers, processing regions and retention boundaries, and prevent unapproved route changes when quotas or failures occur? Review [model routing and fallback governance](model-routing-fallback-governance.md).
- [ ] **Agents, tools, skills or plugins:** Which actions, files, network destinations, dependencies and third-party skills may be loaded or executed? Are source versions, permissions, installs, upgrades, downloads and consequential actions subject to appropriate customer approval? Review [agent skill governance](agent-skill-governance-checklist.md) and [agent contract/orchestration gates](agent-contract-orchestration-gates.md).
- [ ] **Persistent memory or retrieval:** Does the product retain embeddings, conversation memory, source documents, retrieval caches or code indexes? Can the customer verify query-time authorisation, tenant isolation, provenance/freshness, retention and deletion across copies? Review [agent memory and code index governance](agent-memory-governance-checklist.md).
- [ ] **Usage telemetry or content sharing:** What minimum operational counters are collected, and are optional prompts, completions, source code, transcripts and diagnostics controlled separately? Can collection/export scope be approved, reviewed and withdrawn without queued exports bypassing that decision? Review [AI usage telemetry governance](ai-usage-telemetry-governance.md) and the [collection approval record](../templates/ai-telemetry-collection-approval.md).

For each applicable gate, record the **specific vendor evidence**, the deployed version/configuration, the responsible reviewer, any necessary customer-side test, and the decision in the normal vendor assessment record. Mark an inapplicable gate `N/A` **with a reason**, not simply as passed. Keep unsupported or unverified capabilities open with a named owner and remediation/exception decision; do not automatically approve sensitive data flows or privileged actions based on a generic vendor approval.

## Approval Decision

- [ ] Approved
- [ ] Approved with conditions
- [ ] Rejected
- [ ] Exception required

## Conditions Or Exceptions

Record required controls, compensating measures, or expiry date for approval exceptions.
