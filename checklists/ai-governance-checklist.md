# AI Governance Checklist

Use this checklist before approving or expanding AI use inside an organisation.

## Ownership

- [ ] AI governance owner is assigned.
- [ ] Security owner is assigned.
- [ ] Legal/privacy owner is assigned.
- [ ] Business owner is assigned for each AI system.
- [ ] Technical owner is assigned for each AI system.
- [ ] Escalation path exists for AI incidents or policy breaches.

## AI System Inventory

- [ ] All approved AI tools are recorded.
- [ ] Internal AI systems are recorded.
- [ ] AI vendors are recorded.
- [ ] AI coding assistants are recorded.
- [ ] AI features embedded in SaaS products are recorded.
- [ ] Each system has owner, purpose, data classification, and approval status.

## Data Protection

- [ ] Rules define what data can be entered into AI tools.
- [ ] Customer data is blocked unless formally approved.
- [ ] Secrets, API keys, credentials, and tokens are prohibited.
- [ ] Confidential business data is prohibited unless vendor and contract controls are approved.
- [ ] Personal data use is reviewed for privacy impact.
- [ ] Data retention and training-use terms are reviewed.

## Security Controls

- [ ] AI tools require SSO where available.
- [ ] MFA is enforced for administrative access.
- [ ] Access is granted through groups or approved roles.
- [ ] Admin users are reviewed regularly.
- [ ] Audit logs are enabled where available.
- [ ] Data export and sharing settings are reviewed.
- [ ] Vendor security documentation is reviewed.

## Engineering Controls

- [ ] AI-generated code is reviewed before merge.
- [ ] AI-generated code is scanned by SAST/dependency tools.
- [ ] Developers are told not to paste secrets or proprietary source code into unapproved AI tools.
- [ ] Generated infrastructure code is reviewed by qualified engineers.
- [ ] Generated scripts are tested in non-production first.
- [ ] Pull requests identify material AI-generated contributions where required by policy.

## Risk Management

- [ ] AI risks are recorded in a risk register.
- [ ] Risks are rated by likelihood and impact.
- [ ] Risk treatment owner is assigned.
- [ ] Residual risk is accepted by the right owner.
- [ ] High-risk AI use cases require formal approval.
- [ ] Exceptions have expiry dates.

## Vendor Management

- [ ] AI vendors complete security review.
- [ ] AI vendors complete privacy review.
- [ ] Data processing terms are reviewed.
- [ ] Subprocessors are reviewed.
- [ ] Training-on-customer-data settings are reviewed.
- [ ] Breach notification terms are reviewed.
- [ ] Exit and data deletion process is understood.

## Monitoring And Review

- [ ] Approved AI tools are reviewed at least quarterly.
- [ ] Shadow AI usage is reviewed.
- [ ] Logs are monitored where available.
- [ ] Incidents involving AI systems are tracked.
- [ ] Lessons learned are added to policy and training.
