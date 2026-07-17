# AI Security & Governance Checklist

A practical AI security and governance checklist for engineering, DevOps, SaaS, and regulated environments.

This repository helps teams adopt AI tools safely by providing ready-to-use checklists, templates, and framework mappings. It is designed for CTOs, CISOs, DevOps teams, security engineers, compliance teams, and SaaS companies rolling out tools such as ChatGPT, GitHub Copilot, Claude, Gemini, internal LLMs, RAG systems, and AI agents.

## Why This Exists

Many companies are adopting AI faster than their governance, security, and compliance processes can keep up. The problem is usually not lack of interest. The problem is lack of simple, usable controls.

This repository focuses on practical questions:

- Which AI tools are approved?
- What data can and cannot be entered into AI systems?
- How should AI-generated code be reviewed?
- How do we manage prompt injection, data leakage, and insecure outputs?
- How do we assess AI vendors?
- What evidence do we need for ISO 27001, SOC 2, GDPR, and client assurance reviews?
- How do we track AI systems, risks, owners, and mitigations?

## What's Included

```text
.
├── checklists/
│   ├── ai-governance-checklist.md
│   ├── ai-data-handling-decision-guide.md
│   ├── llm-application-security-checklist.md
│   ├── enterprise-ai-usage-policy.md
│   ├── ai-vendor-assessment.md
│   ├── shadow-ai-risk-checklist.md
│   ├── ai-incident-response-playbook.md
│   └── ai-system-periodic-review-checklist.md
├── mappings/
│   ├── owasp-llm-top-10-mapping.md
│   ├── nist-ai-rmf-mapping.md
│   └── iso27001-ai-control-mapping.md
├── templates/
│   ├── ai-control-ownership-matrix.csv
│   ├── ai-risk-register.csv
│   ├── ai-system-inventory.csv
│   ├── ai-vendor-questionnaire.md
│   ├── ai-tool-exception-request.md
│   └── approved-ai-tools-register.csv
├── CONTRIBUTING.md
└── README.md
```

## 30-Second Company Adoption Quick Start

Use the repository in this order:

1. **Inventory:** copy `templates/ai-system-inventory.csv` and record every approved, trial, internally developed, and known shadow AI system.
2. **Risk register:** copy `templates/ai-risk-register.csv`, record the main data, security, legal, operational, and vendor risks, and assign an owner to each one.
3. **Usage policy:** adapt `checklists/enterprise-ai-usage-policy.md` and `checklists/ai-data-handling-decision-guide.md` so staff know which tools and data uses are allowed.
4. **Vendor review:** assess external providers with `checklists/ai-vendor-assessment.md` and retain the completed evidence before approval.
5. **Application checklist:** review internally built LLM, RAG, and agent applications with `checklists/llm-application-security-checklist.md` before production use.

Start with a small, named group of systems rather than trying to complete every control at once. Treat the templates as working records with owners, review dates, evidence links, and time-limited exceptions.

### Suggested One-Week Rollout

| Day | Focus | Practical outcome |
| --- | --- | --- |
| 1 | Assign an executive sponsor and working owners from engineering, security, compliance, procurement, and legal where relevant. | Named decision-makers and a shared working location for governance records. |
| 2 | Build the initial AI system inventory, including pilots and known shadow AI usage. | A prioritised list of systems, vendors, owners, data types, and business purposes. |
| 3 | Create the first risk-register entries for the highest-impact systems. | Initial risk ratings, mitigations, due dates, and accountable owners. |
| 4 | Publish an interim usage policy and data-handling rules. | Clear guidance on approved tools, prohibited data, human review, and exception requests. |
| 5 | Complete vendor and application reviews for the highest-priority systems. | Approval, remediation, restricted use, or rejection decisions with retained evidence. |
| 6 | Review gaps, assign follow-up actions, and define escalation and incident contacts. | A tracked remediation plan and clear path for suspected data exposure or unsafe AI behaviour. |
| 7 | Approve the first governance baseline and schedule periodic reviews. | A documented baseline, review cadence, and next checkpoint for unresolved risks. |

After the first week, use `templates/ai-control-ownership-matrix.csv` to formalise ownership, `templates/approved-ai-tools-register.csv` to publish approved tools, and `checklists/ai-system-periodic-review-checklist.md` for scheduled and event-driven reassessments.

## Contributing

Contributions are welcome. See `CONTRIBUTING.md` for the preferred workflow, checklist wording guidance, and safety rules for examples and templates.

## Who This Is For

- SaaS companies adopting AI tools
- Engineering and DevOps teams using AI coding assistants
- Security teams reviewing AI risks
- Compliance teams preparing for ISO 27001, SOC 2, GDPR, or client due diligence
- Startups that need simple AI governance without heavy bureaucracy
- Enterprises trying to control shadow AI usage

## Core Principles

- Do not paste secrets, customer data, credentials, source code, or confidential business data into unapproved AI tools.
- Treat AI-generated code as untrusted until reviewed, tested, and scanned.
- Keep an inventory of approved AI systems and vendors.
- Assign owners for AI systems and risks.
- Review AI outputs before using them in production, legal, customer, financial, or security-sensitive contexts.
- Monitor for shadow AI usage and data leakage.
- Require vendor due diligence before approving AI tools.

## Framework Alignment

This repository is designed to help teams reason about controls using:

- OWASP Top 10 for LLM Applications
- NIST AI Risk Management Framework
- ISO 27001-style information security governance
- SOC 2-style access, change, risk, and vendor management evidence
- GDPR-style personal data protection principles

## Disclaimer

This repository is not legal advice, compliance certification, or a replacement for a formal risk assessment. Treat it as a practical starting point and adapt it to your organisation's risk profile, regulatory requirements, and legal obligations.
