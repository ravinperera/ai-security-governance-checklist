# AI System Periodic Review Checklist

Use this checklist to confirm that an approved AI system, model integration, coding assistant, RAG application, or agent remains appropriate and controlled over time.

## Review triggers

Run a review at the defined cadence and whenever a material change occurs.

### Scheduled review

- [ ] Review date is within the approved cadence for the system's risk level.
- [ ] System owner, business owner, security contact, and vendor owner are still current.
- [ ] The next review date is recorded before this review is closed.

### Event-driven review

Start an out-of-cycle review after any of the following:

- [ ] New model, provider, plugin, agent capability, or major version.
- [ ] New data source, data classification, customer population, or geography.
- [ ] New automated action, production permission, or downstream integration.
- [ ] Material change to prompts, retrieval, tools, guardrails, or system instructions.
- [ ] Security incident, policy breach, harmful output, data leakage, or significant near miss.
- [ ] Vendor terms, retention, training-data use, subprocessors, hosting, or assurance evidence changes.
- [ ] Regulatory, contractual, or internal policy change.
- [ ] Material decline in quality, safety, explainability, monitoring, or business value.

## Scope and ownership

- [ ] Inventory record accurately describes the system and its purpose.
- [ ] Approved use cases are still valid and actual use has not drifted beyond them.
- [ ] Accountable owner accepts responsibility for continued operation.
- [ ] Users and administrators are identifiable and access is periodically reviewed.
- [ ] Unapproved shadow integrations or duplicate tools have been removed or assessed.

## Data and privacy

- [ ] Data classifications used by the system remain approved.
- [ ] Collection, prompts, retrieval sources, outputs, logs, and feedback data are necessary and proportionate.
- [ ] Retention and deletion settings remain appropriate and are verified where possible.
- [ ] Personal, customer, confidential, and regulated data handling matches policy and contractual commitments.
- [ ] Vendor training or product-improvement settings are understood and configured appropriately.
- [ ] Data residency, subprocessors, and cross-border transfers have not changed unexpectedly.

## Security and access

- [ ] Service accounts, API keys, tokens, and secrets are stored and rotated appropriately.
- [ ] Permissions remain least privilege for users, agents, tools, repositories, data stores, and production systems.
- [ ] Human approval remains required for high-impact or irreversible actions.
- [ ] Input validation, prompt-injection defences, output handling, and tool restrictions remain effective.
- [ ] Logging and alerting cover sensitive access, policy violations, unusual usage, and automated actions.
- [ ] Known vulnerabilities, unsafe dependencies, and security advisories have been assessed.

## Quality, safety, and testing

- [ ] Representative functional tests still pass.
- [ ] Misuse, adversarial, prompt-injection, and unsafe-output tests reflect current use cases.
- [ ] Hallucination, bias, toxicity, privacy, and security risks are tested where relevant.
- [ ] Human review requirements remain practical and are being followed.
- [ ] Model or vendor changes have not invalidated previous evaluation results.
- [ ] Monitoring shows acceptable error, override, escalation, and incident rates.

## Vendor and resilience

- [ ] Vendor security, privacy, availability, and compliance evidence remains current enough for the risk level.
- [ ] Contract terms, service limits, support arrangements, and exit rights remain acceptable.
- [ ] Business continuity, fallback, manual process, and rollback options are documented and tested where required.
- [ ] Concentration risk and critical dependency on a single model or provider are understood.
- [ ] Export, deletion, and migration options remain workable.

## Risk and compliance

- [ ] Risk register entries reflect current likelihood, impact, controls, and residual risk.
- [ ] Previous remediation actions are complete or have current owners and due dates.
- [ ] Exceptions and risk acceptances are still valid and approved by authorised owners.
- [ ] Required legal, privacy, compliance, works council, client, or regulatory reviews are current.
- [ ] Evidence needed for audits or customer assurance is retained in an approved location.

## Review outcome

Select one outcome:

- [ ] **Continue** — controls remain effective and residual risk is acceptable.
- [ ] **Continue with actions** — operation may continue while time-bound improvements are completed.
- [ ] **Restrict** — reduce users, data, capabilities, permissions, or environments until risk is addressed.
- [ ] **Suspend** — stop use pending remediation or formal reassessment.
- [ ] **Retire** — remove the system, revoke access, delete or export data as required, and update inventories.

## Review record

```text
System name:
Inventory ID:
Review date:
Review type: scheduled / event-driven
Trigger, if event-driven:
System owner:
Reviewers:
Current risk rating:
Key evidence reviewed:
Material changes identified:
Incidents or exceptions since last review:
Outcome:
Required actions, owners, and dates:
Residual risk approver:
Next review date:
```
