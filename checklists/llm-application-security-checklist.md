# LLM Application Security Checklist

Use this checklist when building or approving applications that use large language models, retrieval-augmented generation, plugins, tools, or agents.

## Application Design

- [ ] AI system purpose is documented.
- [ ] Model provider and model version are documented.
- [ ] Data flow is documented.
- [ ] User roles and permissions are documented.
- [ ] External tools, plugins, APIs, and agents are documented.
- [ ] Human approval points are defined for high-impact actions.

## Prompt Injection

- [ ] System prompts are treated as sensitive configuration.
- [ ] User input is never trusted as instruction hierarchy.
- [ ] Retrieved content is treated as untrusted input.
- [ ] Tool calls require server-side authorization.
- [ ] Model output cannot directly override security controls.
- [ ] Prompt injection test cases are included in testing.

## Output Handling

- [ ] AI output is validated before use by downstream systems.
- [ ] AI output is encoded or escaped before rendering in browsers.
- [ ] AI output is not directly executed as code or shell commands.
- [ ] AI-generated SQL, scripts, or infrastructure changes require human review.
- [ ] AI output used in customer communication is reviewed where appropriate.

## Sensitive Information Disclosure

- [ ] Secrets are never included in prompts.
- [ ] Customer data is masked or excluded unless approved.
- [ ] Logs do not capture sensitive prompts or outputs unnecessarily.
- [ ] System prompts are not exposed to users.
- [ ] Data retention settings are understood and documented.

## Excessive Agency

- [ ] Agents cannot perform high-risk actions without approval.
- [ ] Tool permissions are least privilege.
- [ ] Agents cannot access unnecessary systems.
- [ ] Destructive actions require confirmation.
- [ ] Rate limits and budget controls are configured.
- [ ] Audit logs capture tool calls and outcomes.

## Supply Chain

- [ ] Model provider is approved.
- [ ] SDKs and AI libraries are dependency-scanned.
- [ ] Third-party prompts, plugins, and tools are reviewed.
- [ ] Model updates are tested before production rollout.
- [ ] Container images are scanned.
- [ ] CI/CD workflows are protected.

## RAG And Vector Stores

- [ ] Data sources are approved.
- [ ] Document ingestion process is controlled.
- [ ] Access controls are applied before retrieval.
- [ ] Private documents are not retrievable by unauthorized users.
- [ ] Embedding stores are backed up and protected.
- [ ] Index deletion and retention are documented.

## Testing

- [ ] Prompt injection tests are performed.
- [ ] Data leakage tests are performed.
- [ ] Role bypass tests are performed.
- [ ] Unsafe output tests are performed.
- [ ] Cost exhaustion tests are performed.
- [ ] Abuse and rate-limit tests are performed.

## Operations

- [ ] Monitoring is enabled.
- [ ] Incident response process includes AI-specific scenarios.
- [ ] Rollback path exists for model or prompt changes.
- [ ] Cost monitoring is enabled.
- [ ] Abuse monitoring is enabled.
