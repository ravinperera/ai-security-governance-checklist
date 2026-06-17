# ISO 27001-Style AI Control Mapping

This is a practical mapping for organisations using ISO 27001-style security governance. It is not a formal certification mapping.

| Control Theme | AI Governance Activity | Evidence Example |
| --- | --- | --- |
| Asset management | Maintain AI system inventory | `templates/ai-system-inventory.csv` |
| Acceptable use | Define AI usage policy | `checklists/enterprise-ai-usage-policy.md` |
| Access control | Use SSO, MFA, and group-based access for AI tools | Access review export, approved tools register |
| Supplier security | Assess AI vendors before approval | `checklists/ai-vendor-assessment.md` |
| Information classification | Define what data can be used in AI tools | AI usage policy, data classification rules |
| Secure development | Review AI-generated code | Pull request evidence, SAST results, dependency scans |
| Logging and monitoring | Monitor AI tool usage and admin activity | Vendor audit logs, SIEM events |
| Incident management | Include AI data leakage and unsafe output scenarios | Incident tickets, post-incident review |
| Risk management | Record AI-specific risks and treatments | `templates/ai-risk-register.csv` |
| Awareness training | Train staff on safe AI use | Training records, policy acknowledgement |
| Compliance | Review privacy, contractual, and regulatory requirements | DPIA, DPA, vendor assessment |

## Suggested Evidence Pack

For audits or client assurance reviews, keep:

- AI usage policy
- Approved AI tools register
- AI system inventory
- AI risk register
- Vendor assessments
- Access review evidence
- Training evidence
- Incident records
- Exception approvals
