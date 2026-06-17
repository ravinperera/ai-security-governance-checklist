# OWASP LLM Top 10 Mapping

This mapping connects practical controls in this repository to common LLM application security risks.

| Risk Area | Practical Controls |
| --- | --- |
| Prompt injection | Treat user input and retrieved content as untrusted; test prompt injection; require server-side authorization for tool calls. |
| Insecure output handling | Validate, encode, and review AI outputs before passing them to browsers, APIs, shell commands, SQL, or infrastructure tools. |
| Training data poisoning | Control training and fine-tuning data sources; review vendor training terms; validate ingestion pipelines. |
| Model denial of service | Configure rate limits, budgets, quotas, timeouts, and abuse monitoring. |
| Supply chain vulnerabilities | Review AI SDKs, plugins, models, prompts, dependencies, and third-party tools. |
| Sensitive information disclosure | Prohibit secrets and confidential data in prompts; review logs; mask sensitive data. |
| Insecure plugin or tool design | Apply least privilege to tools and plugins; require human approval for high-risk actions. |
| Excessive agency | Restrict what agents can do; require confirmation for destructive or customer-impacting actions. |
| Overreliance | Require human review for legal, security, financial, HR, medical, or customer-impacting outputs. |
| Model theft or abuse | Restrict access, monitor usage, protect model endpoints, and detect abnormal extraction attempts. |

## Related Files

- `checklists/llm-application-security-checklist.md`
- `checklists/ai-governance-checklist.md`
- `checklists/enterprise-ai-usage-policy.md`
- `templates/ai-risk-register.csv`
