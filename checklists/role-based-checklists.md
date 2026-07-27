# Role-Based AI Governance Checklists

Use these short views alongside the main [AI governance checklist](ai-governance-checklist.md). They do not create separate control frameworks; they show what each role should own, verify and hand off.

Mark each item as complete, not applicable or assigned with an owner and due date. Keep evidence in approved internal systems rather than this public repository.

## Engineering and DevOps

Before approving or operating an AI-enabled application:

- [ ] Record the system, business purpose, technical owner, model or provider and environments in the AI system inventory.
- [ ] Document every data source, connector, tool, plugin, MCP server, agent action and external destination.
- [ ] Classify the data used for prompts, retrieval, fine-tuning, logs and evaluation.
- [ ] Keep secrets and credentials in an approved secret manager; do not place them in prompts, examples or logs.
- [ ] Apply least privilege to service identities, tools and agent actions.
- [ ] Treat model output as untrusted; validate, encode and authorise it before execution or display.
- [ ] Add controls for prompt injection, insecure tool use, data leakage and excessive agency.
- [ ] Separate development, test and production access and data where practical.
- [ ] Define human approval points for production, financial, legal, security-sensitive or destructive actions.
- [ ] Add monitoring for failures, unsafe actions, unusual usage, cost and data-flow changes.
- [ ] Test rollback, disablement and provider or model fallback before production use.
- [ ] Retain architecture, threat-model, test, approval and release evidence.

**Handoff:** provide security with the architecture and threat model; provide compliance with inventory and evidence links; provide operations with monitoring, incident and rollback instructions.

## Security

Before giving a security recommendation:

- [ ] Confirm the system owner, scope, data classification and intended users.
- [ ] Review identity, authentication, authorisation and tenant-isolation boundaries.
- [ ] Review provider, model, plugin, connector and supply-chain provenance.
- [ ] Assess prompt injection, sensitive-data disclosure, insecure output handling and agent privilege escalation.
- [ ] Verify that secrets, source code, customer data and regulated data follow approved handling rules.
- [ ] Check network egress, external destinations and data-retention settings.
- [ ] Verify least privilege, short-lived credentials and auditable human approval for high-impact actions.
- [ ] Confirm logging is useful without recording sensitive prompt or response content unnecessarily.
- [ ] Define security monitoring, abuse detection and incident-response triggers.
- [ ] Record findings, severity, owner, due date, compensating controls and residual risk.
- [ ] Require reassessment after material model, provider, data, tool or permission changes.
- [ ] Escalate unacceptable residual risk to the named risk owner rather than silently accepting it.

**Handoff:** provide engineering with required fixes; provide compliance with mapped controls and evidence; provide leadership with material risks and unresolved decisions.

## Compliance, Privacy and Legal

Before confirming governance readiness:

- [ ] Identify applicable laws, contracts, policies, client commitments and sector requirements.
- [ ] Confirm whether the organisation is acting as provider, deployer, customer, processor or another relevant role.
- [ ] Record the lawful purpose and approved use cases for personal or regulated data.
- [ ] Verify transparency notices, user communications and human-review requirements where applicable.
- [ ] Review retention, deletion, data-location, international-transfer and data-subject-rights arrangements.
- [ ] Confirm vendor terms cover data use, model training, confidentiality, subprocessors, incidents and audit evidence.
- [ ] Record intellectual-property, licensing and output-ownership considerations.
- [ ] Confirm decisions affecting people have suitable human oversight, challenge and appeal routes.
- [ ] Map controls to the organisation's required frameworks without claiming certification from a checklist alone.
- [ ] Keep decision records, approvals, exceptions, review dates and evidence references.
- [ ] Set event-driven reassessment triggers for regulatory, contractual or product changes.
- [ ] Obtain qualified advice for jurisdiction-specific questions or material uncertainty.

**Handoff:** provide procurement with mandatory contract clauses; provide engineering with notice and data-handling requirements; provide leadership with decisions requiring formal risk acceptance.

## Procurement and Vendor Management

Before onboarding or renewing an AI supplier:

- [ ] Define the business need, owner, users, data categories and expected integrations.
- [ ] Check the approved-tools register before starting a new purchase.
- [ ] Complete the AI vendor assessment and retain supporting evidence.
- [ ] Review security certifications, independent reports, penetration testing and vulnerability-management practices.
- [ ] Review identity, access, encryption, logging, availability, backup and incident-notification controls.
- [ ] Confirm how prompts, files, outputs and telemetry are stored, reused or used for model training.
- [ ] Identify subprocessors, hosting regions, transfer mechanisms and deletion commitments.
- [ ] Require contract terms for confidentiality, data use, incidents, service levels, exit and evidence access.
- [ ] Confirm pricing, usage limits, cost monitoring and termination obligations.
- [ ] Record security, privacy, legal and business approvals before enabling production access.
- [ ] Add renewal, material-change and periodic-review dates.
- [ ] Maintain an exit plan for data export, deletion, credential revocation and replacement service continuity.

**Handoff:** provide system owners with approved scope and restrictions; provide security and compliance with retained evidence; provide finance and leadership with cost and concentration risks.

## Leadership and Risk Owners

Before approving material AI use:

- [ ] Confirm a named executive sponsor and accountable system owner.
- [ ] Verify the use case supports an agreed business objective and is not technology adoption without a clear need.
- [ ] Review the highest security, privacy, legal, operational, financial and reputational risks.
- [ ] Confirm high-impact systems have appropriate human oversight and decision accountability.
- [ ] Ensure engineering, security, compliance, legal and procurement responsibilities are assigned.
- [ ] Confirm required controls, evidence and remediation funding are available.
- [ ] Review unresolved findings, exceptions, compensating controls and expiry dates.
- [ ] Accept residual risk explicitly or require additional mitigation; do not treat silence as approval.
- [ ] Set risk appetite, prohibited uses and escalation thresholds.
- [ ] Require meaningful measures for safety, quality, incidents, adoption, cost and business value.
- [ ] Schedule periodic portfolio review and event-driven reassessment.
- [ ] Ensure the organisation can suspend or retire a system safely.

**Handoff:** communicate approved risk appetite and decisions to delivery teams; assign owners and deadlines for unresolved actions; retain the formal decision record.

## Shared Decision Record

For each approval, restriction, exception or rejection, record:

| Field | Required information |
| --- | --- |
| System | Inventory identifier and name |
| Decision | Approved, restricted, pilot only, remediation required or rejected |
| Scope | Users, environments, data and permitted use cases |
| Owners | Business, technical and risk owners |
| Evidence | Links to assessments, tests, contracts and control records |
| Conditions | Required controls, usage restrictions and monitoring |
| Exceptions | Compensating controls, approver and expiry date |
| Residual risk | Accepted risks and accountable approver |
| Review | Next review date and event-driven triggers |
| Exit | Disablement, data deletion and credential-revocation plan |

## Suggested Operating Cadence

- **Before pilot:** inventory, initial data decision, vendor or application review and named owners.
- **Before production:** completed security, compliance and operational evidence; approval decision; monitoring and rollback.
- **Monthly or quarterly:** review incidents, usage, cost, exceptions, provider changes and overdue actions according to risk.
- **At renewal:** repeat vendor, contract, data-use and concentration-risk review.
- **After material change:** reassess when the model, provider, data, tools, permissions, users or business purpose changes.
- **At retirement:** revoke access, delete or export data as required, update inventories and retain the closure record.

These role views are a practical starting point, not legal advice, certification or a substitute for the organisation's formal risk-management process.
