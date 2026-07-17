# AI Data Handling Decision Guide

Use this guide before entering a prompt, uploading a file, connecting a data source, or enabling an AI integration. It supports a practical decision; it does not replace legal, privacy, security, or contractual review.

## Decision outcome

Choose one outcome:

- **Proceed** — the tool and use are approved, the data is permitted, and required controls are in place.
- **Proceed with controls** — use only after applying documented safeguards and obtaining any required approval.
- **Escalate** — the risk or approval status is unclear; ask the security, privacy, legal, compliance, or data owner.
- **Stop** — the proposed use includes prohibited data or an unapproved high-risk capability.

## Step 1: Is the tool and use case approved?

- Confirm the exact tool, model, account type, plugins, integrations, and environment are approved.
- Confirm the proposed use is within the approved purpose and user group.
- Check whether provider training, retention, telemetry, human review, or subprocessors are enabled.

**If the tool or use case is unapproved:** stop or use the AI tool exception request process before sharing data.

## Step 2: Does the input contain secrets or authentication material?

Examples include passwords, API keys, tokens, private keys, session cookies, connection strings, recovery codes, and unredacted configuration files.

**If yes:** stop. Remove and rotate exposed credentials where necessary. Do not rely on a provider setting to make secret disclosure acceptable.

## Step 3: Classify the data

Identify the highest classification present:

- **Public** — intentionally published and safe for unrestricted disclosure.
- **Internal** — non-public operational information with limited impact if disclosed.
- **Confidential** — customer information, contracts, proprietary source code, security findings, financial data, or sensitive business information.
- **Restricted** — regulated, highly sensitive, privileged, safety-critical, or access-controlled data.

**If classification is unknown:** escalate to the data owner before proceeding.

## Step 4: Check for personal, customer, or regulated data

Ask whether the input contains:

- Names, contact details, identifiers, account details, location, behavioural data, or employee information.
- Customer or client files, tickets, messages, recordings, transactions, or support data.
- Health, financial, criminal, biometric, children’s, or other specially protected data.
- Data subject to contractual confidentiality, residency, retention, or deletion requirements.

**If yes:** proceed only where the use, provider, region, agreement, retention settings, access controls, and lawful basis have been approved. Otherwise escalate or stop.

## Step 5: Check source code, logs, and operational data

Before sharing code or technical artefacts, remove or replace:

- Credentials, private URLs, hostnames, IP addresses, account IDs, tenant IDs, and internal repository names.
- Customer content, production payloads, stack traces containing sensitive values, and security control details.
- Proprietary algorithms or code that the approved tool is not authorised to process.

Prefer minimal reproductions, synthetic examples, and isolated snippets over whole repositories, production logs, or database exports.

## Step 6: Assess integrations and actions

For tools that can browse, retrieve data, call APIs, run commands, change infrastructure, or send messages:

- Use least-privilege credentials and read-only access where possible.
- Restrict accessible repositories, folders, systems, networks, and actions.
- Require human approval for destructive, privileged, financial, customer-facing, or production changes.
- Treat retrieved content as untrusted and consider prompt-injection risk.
- Confirm logs and outputs do not create a new sensitive-data store.

**If the tool can take high-impact actions without effective approval or rollback:** stop until safeguards are added.

## Step 7: Minimise the data

Share only what is necessary for the task. Prefer, in order:

1. Synthetic data that preserves the required structure.
2. Public examples.
3. Redacted or masked data with identifiers and sensitive context removed.
4. Aggregated or sampled data.
5. Approved confidential data only when the tool and controls explicitly permit it.

Redaction and anonymisation reduce risk but may not eliminate it. Consider whether remaining fields, combinations, metadata, or context could re-identify a person or reveal confidential information.

## Step 8: Confirm output handling

Before using or storing the result:

- Review for fabricated, insecure, biased, confidential, or legally sensitive content.
- Do not treat generated output as authoritative evidence without verification.
- Store outputs according to the classification of the input and result.
- Remove temporary uploads, chats, exports, and access when no longer required.
- Record approvals and evidence where the use is risk-sensitive.

## Quick decision table

| Situation | Default outcome |
|---|---|
| Approved tool using public data for an approved purpose | Proceed |
| Internal data with clear approval and required controls | Proceed with controls |
| Unknown classification, retention, residency, or contractual status | Escalate |
| Secrets, credentials, or private keys | Stop |
| Restricted data without explicit approval and safeguards | Stop |
| Production or customer data where synthetic data would work | Use synthetic data instead |
| Agent can make privileged or destructive changes without approval | Stop |

## Evidence to retain

For higher-risk uses, record:

- Tool, model, account, region, and configuration.
- Approved purpose, users, data classification, and data owner.
- Provider retention and training settings.
- Integrations, permissions, and human approval points.
- Risk assessment, exception, or review record.
- Expiry date and owner for reassessment.
