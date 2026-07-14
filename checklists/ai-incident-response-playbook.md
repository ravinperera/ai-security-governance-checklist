# AI Incident Response Playbook

Use this playbook when an AI system, coding assistant, agent, model integration, or vendor may have caused data exposure, unsafe automation, security compromise, or material business harm.

> Do not place secrets, personal data, customer content, proprietary prompts, access tokens, or raw incident evidence in public issues or public chat channels.

## 1. Declare and assign

Record the incident in the approved incident-management system and assign:

- incident commander
- technical lead
- security or privacy representative
- communications owner
- vendor contact, when relevant

Treat the event as **suspected** until evidence supports a confirmed conclusion. Do not delay containment while waiting for certainty.

## 2. Initial triage

Capture the minimum safe facts:

- affected AI tool, model, agent, integration, or vendor
- environment and business process involved
- time first observed and time last known safe
- data types potentially involved
- identities, credentials, tools, and downstream systems the AI component could access
- whether automated actions were executed
- current user or customer impact

### Suggested severity guide

| Severity | Example |
| --- | --- |
| Critical | Confirmed sensitive-data disclosure, destructive autonomous action, active credential compromise, or broad customer impact |
| High | Likely sensitive exposure, material prompt injection, unauthorised system action, or production integrity risk |
| Medium | Contained unsafe output, policy breach, or limited exposure with no evidence of external access |
| Low | Near miss, blocked attempt, or control weakness without impact |

## 3. Immediate containment

Choose the least disruptive actions that stop further harm:

- disable the affected integration, agent, plugin, API key, or workflow
- revoke and rotate exposed credentials or tokens
- remove tool access to sensitive repositories, data stores, and production systems
- pause automated decisions or require human approval
- block known malicious prompts, files, domains, or inputs
- preserve a safe copy of relevant configuration before changing it
- notify the vendor through its security channel when vendor action is required

Do not delete logs or conversation history unless legal, privacy, or security leadership explicitly directs it.

## 4. Preserve evidence safely

Store evidence only in approved restricted locations. Preserve:

- timestamps and user or service identities
- model, tool, and integration versions
- prompts and outputs, redacted where possible
- audit, access, API, application, and network logs
- workflow runs and configuration changes
- affected data classifications and record counts
- screenshots or exports with an evidence owner and collection time

Record what was collected, by whom, from which system, and whether it was altered or redacted.

## 5. Assess exposure and obligations

Determine:

- whether data left an approved boundary
- whether the vendor stores or trains on submitted content
- whether personal, customer, regulated, confidential, or source-code data was involved
- whether credentials or signing material were exposed
- which systems or decisions relied on unsafe output
- whether legal, privacy, regulatory, contractual, cyber-insurance, or customer notification duties may apply

Escalate these decisions to authorised legal, privacy, compliance, and security owners. This playbook is not a substitute for formal breach-assessment procedures.

## 6. Eradication and recovery

Before restoring service:

- remove malicious or unsafe inputs, extensions, tools, and configurations
- rotate affected secrets and invalidate active sessions
- patch the integration or strengthen input/output controls
- reduce permissions and data access to the minimum required
- re-run security tests and representative misuse cases
- validate logs, alerts, approval gates, and rollback procedures
- confirm the recovery decision and accountable approver

Restore gradually where possible and monitor for recurrence.

## 7. Communications

Use approved incident communications channels. Provide factual updates that distinguish:

- confirmed facts
- working hypotheses
- containment already completed
- remaining risk
- next decision point

Do not speculate about attribution, impact, or notification obligations.

## 8. Closure and follow-up

Close the incident only when:

- containment and recovery are verified
- residual risk is accepted by an authorised owner
- required notifications are complete
- evidence and decisions are retained appropriately
- follow-up actions have owners and due dates

Complete a lessons-learned review covering:

- root cause and contributing conditions
- which preventive and detective controls failed or succeeded
- changes to the AI system inventory and risk register
- policy, vendor, access, testing, monitoring, or training improvements
- whether similar systems require review

## Incident record template

```text
Incident ID:
Date/time detected:
Reporter:
Incident commander:
Affected AI system/vendor:
Environment:
Severity:
Status: suspected / confirmed / closed
Potential data involved:
Potential systems/actions involved:
Containment completed:
Evidence location:
Legal/privacy/security escalation:
Recovery validation:
Residual risk owner:
Follow-up actions:
```
