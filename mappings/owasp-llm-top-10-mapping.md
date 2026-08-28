# OWASP GenAI LLM Top 10 2026 Mapping

This project mapping aligns practical controls in this repository with the **OWASP GenAI LLM Top 10 2026** risk list.

Source baseline: [OWASP GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) and its [canonical final source](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/tree/main/2026/final), reviewed **2026-08-28**.

This is an interpretive crosswalk maintained by this repository. It is **not** an official OWASP mapping, certification, or statement that the listed controls fully mitigate each risk. Use the OWASP source material for authoritative descriptions and adapt controls to the system's architecture, data, users, tools, and risk profile.

| OWASP 2026 risk | Practical controls in this repository |
| --- | --- |
| **LLM01: Prompt Injection** | Treat user, retrieved, tool, multimodal, and memory content as untrusted; separate instructions from data where the architecture allows; enforce authorization outside the model; constrain tools; test direct and indirect injection; prevent untrusted content from silently writing durable memory. |
| **LLM02: Sensitive Information Disclosure** | Classify data before AI use; prohibit secrets and unapproved confidential data in prompts; minimise retrieved context; redact logs and traces; apply output filtering appropriate to the use case; review vendor retention, training, and access terms. |
| **LLM03: Excessive Agency** | Define an explicit agent contract; grant least-privilege tools and data access; keep authorization deterministic and server-side; require independent approval for high-impact actions; use stage gates, stop conditions, and retry/idempotency controls. |
| **LLM04: Supply Chain** | Inventory models, SDKs, prompts, plugins, MCP servers, tools, datasets, and providers; assess vendors; pin or approve versions where practical; review provenance and change history; reassess when upstream components or trust boundaries change. |
| **LLM05: Data and Model Poisoning** | Record source provenance; validate and approve training, fine-tuning, RAG, and memory ingestion sources; protect write paths; monitor unexpected behaviour; retain rollback/rebuild procedures for poisoned or corrupted data and indexes. |
| **LLM06: Unbounded Consumption** | Apply quotas, budgets, rate limits, timeouts, concurrency limits, and circuit breakers; monitor token/tool usage and cost; bound recursive or delegated agent work; stop workloads that exceed approved resource envelopes. |
| **LLM07: Misinformation** | Treat generated claims as untrusted until verified; require human review for high-impact decisions; preserve citations/evidence where available; test critical facts against authoritative sources; document known limitations and uncertainty. |
| **LLM08: Hidden Context Exposure** | Keep secrets, credentials, internal-only instructions, private retrieval data, and unnecessary infrastructure detail out of model-visible context; minimise tool schemas and hidden context; segregate access by role/tenant; assume hidden context may be exposed under attack. |
| **LLM09: Vector and Embedding Weaknesses** | Enforce authorization at retrieval time; maintain tenant/project isolation; preserve document provenance and ACLs; validate ingestion; track freshness and source revision; invalidate stale indexes; test poisoning and cross-tenant retrieval cases. |
| **LLM10: Improper Output Handling** | Treat model output as untrusted input to downstream systems; validate and encode before browsers, APIs, shell commands, SQL, code, or infrastructure tools; use allowlists/schemas where possible; sandbox risky execution; never let model output bypass downstream authorization. |

## Related Repository Controls

- `checklists/llm-application-security-checklist.md`
- `checklists/ai-governance-checklist.md`
- `checklists/enterprise-ai-usage-policy.md`
- `checklists/agent-memory-governance-checklist.md`
- `checklists/agent-contract-orchestration-gates.md`
- `checklists/ai-vendor-assessment.md`
- `checklists/ai-system-periodic-review-checklist.md`
- `docs/architecture-data-flow.md`
- `docs/threat-model.md`
- `templates/ai-risk-register.csv`

## Maintenance Rule

Re-review this mapping when OWASP publishes a new LLM Top 10 release or materially changes a risk definition. Record the source baseline and review date whenever the mapping changes, and avoid carrying risk names forward from an older release without checking the current canonical source.
