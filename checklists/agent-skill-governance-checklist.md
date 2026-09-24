# Agent Skill And Procedural Plugin Governance Checklist

Use this checklist when an AI assistant or agent can load reusable skills, procedural instruction packs, plugins, tool recipes, or similar specialist capability bundles.

These resources can improve consistency and reduce repeated prompting, but they can also introduce executable instructions, hidden dependencies, new data flows, external services, and long-lived trust decisions. Treat a skill as governed software and procedural policy, not as harmless documentation.

## Scope And Ownership

- [ ] Each approved skill or skill bundle has a named business or technical owner.
- [ ] The purpose and permitted use cases are documented.
- [ ] The supported agent hosts, operating systems, runtimes, and environments are identified.
- [ ] High-risk or regulated use cases are explicitly identified rather than inferred from generic approval.
- [ ] The organisation knows whether the skill can execute code, modify files, install packages, call tools, make network requests, or access external data.

## Source, Provenance, And Versioning

- [ ] The canonical source repository, package, or publisher is recorded.
- [ ] The installed release, tag, package version, or commit is recorded when reproducibility matters.
- [ ] Community-contributed or third-party skills receive proportionate review before approval.
- [ ] A floating `latest`, default branch, or unpinned package is not treated as immutable evidence.
- [ ] Material changes to skill instructions, dependencies, permissions, or external services trigger reassessment.
- [ ] Deprecated, compromised, or unmaintained skills have a documented revocation path.

## Installation And Supply Chain

- [ ] Installation is limited to approved sources and methods.
- [ ] Package, binary, container, script, or plugin dependencies are inventoried where practical.
- [ ] Dependency installation does not silently add repositories, privileged services, startup agents, or broad system permissions.
- [ ] Checksums, signatures, lockfiles, package attestations, or equivalent integrity controls are used where risk warrants them.
- [ ] Skill updates are reviewed before rollout when they can materially change agent behaviour or authority.
- [ ] Removing a skill also removes or accounts for its cached artifacts, credentials, downloaded models, and persistent configuration where applicable.

## Rendered Installs And Drift Reconciliation

Use these controls when one canonical agent/skill definition is rendered, converted, copied, or synchronised into tool-specific formats or destinations.

- [ ] The canonical source is distinguishable from generated or installed tool-specific copies.
- [ ] The transformation is deterministic or otherwise reproducible, and the renderer/converter version or revision is recorded when it can change output.
- [ ] Material installations record enough provenance to reconstruct what was written, such as canonical source version/hash, rendered hash, target tool, destination, scope, and relevant provider-specific overrides.
- [ ] Provider-specific overrides are explicit deltas from the canonical definition rather than silent forks of the whole instruction set.
- [ ] Reconciliation can distinguish at least current, source-outdated, locally modified, missing/removed, and unmanaged/foreign states when those distinctions affect update or removal safety.
- [ ] A locally modified installed file is reviewed or backed up before an automated update, overwrite, reset, or deletion.
- [ ] Sync or conversion conflicts fail visibly; the system does not silently choose one provider copy as authoritative when multiple copies changed independently.
- [ ] Tool-specific rendering does not add permissions, network access, tools, or data access that were absent from the approved canonical source unless separately reviewed and authorised.
- [ ] Compatibility claims are tied to the tool/host versions actually tested; successful rendering alone is not treated as proof that a client will discover, prioritise, or obey the installed instructions.
- [ ] Removing or disabling the canonical skill also identifies stale rendered copies that may remain active in other tools or scopes.

## Permissions And External Actions

- [ ] Loading or discovering a skill does not itself grant new permissions.
- [ ] Installation, downloads, external service calls, publication, deletion, or other side effects follow the surrounding approval policy.
- [ ] Skills cannot override higher-priority security, privacy, legal, or human-approval requirements.
- [ ] Tool and data access is checked at execution time rather than assumed from the skill description.
- [ ] Credentials required by a skill are obtained through approved secret-management paths rather than embedded in skill files or prompts.
- [ ] Network destinations and external APIs are approved before sensitive or regulated data is transmitted.

## Data Handling And Boundaries

- [ ] Data classifications permitted for each skill are documented.
- [ ] Skills that use external databases, hosted APIs, browsers, or cloud compute are reviewed for data egress and retention.
- [ ] Tenant, project, repository, customer, and environment boundaries remain enforced after a skill is loaded.
- [ ] A skill cannot convert temporary data access into persistent memory, logs, caches, or external uploads without an approved basis.
- [ ] Sensitive prompt, file, or dataset content is not retained merely to simplify later skill execution.

## Reproducibility And Evidence

- [ ] Material analyses record the skill version together with relevant model, dependency, tool, and data-source versions.
- [ ] Raw or authoritative source data remains recoverable where reproducibility or auditability requires it.
- [ ] Parameters, configuration, seeds, source identifiers, timestamps, and checksums are recorded where they affect results.
- [ ] Derived summaries or agent conclusions are distinguishable from raw evidence.
- [ ] Re-running a workflow does not depend on undocumented local state or an unknown skill revision.

## Human Accountability And High-Stakes Use

- [ ] Specialist skills assist qualified reviewers rather than replacing accountable clinical, regulatory, legal, safety, financial, or similarly high-impact decisions.
- [ ] Required human review occurs before consequential recommendations are acted on.
- [ ] The skill clearly states material limitations, uncertainty, and prerequisites when these affect safe interpretation.
- [ ] External certifications, approvals, diagnoses, release decisions, or compliance conclusions are not inferred merely because a skill generated supporting analysis.
- [ ] Escalation paths exist when the skill produces conflicting, incomplete, or out-of-scope results.

## Runtime Selection And Context Control

- [ ] Agents load only the skills needed for the current task where the runtime supports selective discovery.
- [ ] Overlapping or conflicting skills are resolved explicitly rather than relying on instruction ordering.
- [ ] Unrelated skills are unloaded or excluded when the task changes materially.
- [ ] The agent can identify which skill influenced a material result when auditability matters.
- [ ] Skill content is not allowed to override system-level policy or approved agent authority boundaries.

## Monitoring, Review, And Incident Response

- [ ] Approved skills are included in periodic AI system or tool reviews where they can materially affect behaviour.
- [ ] Security advisories, repository compromise, publisher changes, or dependency vulnerabilities can trigger review or suspension.
- [ ] Material skill installation, update, reconciliation, and revocation events are auditable where risk warrants it.
- [ ] Incident response can disable a skill, revoke credentials, remove cached artifacts, and identify affected workflows.
- [ ] Previously generated outputs are reassessed when a compromised or materially faulty skill may have influenced them.

## Evidence To Retain

Keep evidence proportionate to risk, such as:

- approved source and version or commit;
- owner and permitted-use record;
- dependency and external-service inventory;
- security or code review evidence;
- data-classification and egress decisions;
- installation/update/reconciliation/revocation records;
- canonical and rendered hashes plus tool/scope/destination when cross-tool rendering is used;
- reproducibility records for material analyses;
- human-review and approval evidence for high-stakes use.

## Upstream Pattern References

These public projects illustrate patterns that informed the vendor-neutral controls above. They are design references, not dependencies or proof of compliance:

- [K-Dense Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) demonstrates a large portable skill library with specialist tooling, dependency guidance, reproducibility concerns, and security warnings around installing only needed skills.
- [graft](https://github.com/Zealbase/graft) (MIT; reviewed 2026-09-24) demonstrates canonical agent definitions, provider-specific rendering/synchronisation, and explicit drift/conflict detection.
- [Agency Agents](https://github.com/msitarzewski/agency-agents-app) (MIT; reviewed 2026-09-24) demonstrates deterministic tool-specific renders, an install ledger with source/render identity, reconciliation states, and backup-before-overwrite behaviour for modified installs.

This checklist does not copy their code, skill content, prompts, or implementation-specific schemas, and it does not treat adoption, compatibility, or performance claims as independently verified facts.
