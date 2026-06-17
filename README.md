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
│   ├── llm-application-security-checklist.md
│   ├── enterprise-ai-usage-policy.md
│   ├── ai-vendor-assessment.md
│   └── shadow-ai-risk-checklist.md
├── mappings/
│   ├── owasp-llm-top-10-mapping.md
│   ├── nist-ai-rmf-mapping.md
│   └── iso27001-ai-control-mapping.md
├── templates/
│   ├── ai-risk-register.csv
│   ├── ai-system-inventory.csv
│   ├── ai-vendor-questionnaire.md
│   └── approved-ai-tools-register.csv
└── README.md
```

## Quick Start

1. Start with `checklists/ai-governance-checklist.md`.
2. Create an AI system inventory using `templates/ai-system-inventory.csv`.
3. Record risks in `templates/ai-risk-register.csv`.
4. Define approved tools using `templates/approved-ai-tools-register.csv`.
5. Use `checklists/ai-vendor-assessment.md` before approving external AI vendors.
6. Use the mappings folder to align controls with OWASP LLM Top 10, NIST AI RMF, and ISO 27001-style governance.

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
