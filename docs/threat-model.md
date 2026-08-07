# Repository Threat Model

This threat model covers the public content and contribution workflow of this repository. It does not model any organisation that adopts the checklists, any AI vendor, or a production AI system.

## Assets

The main assets are:

- the integrity of security and governance guidance;
- reusable templates, registers, and checklists that teams may adapt;
- framework mappings and explanatory references;
- fictional examples that demonstrate expected record quality;
- contributor and maintainer trust in repository changes;
- the confidentiality of information submitted through issues and pull requests.

## Threat actors and failure modes

Relevant threats include deliberate abuse and ordinary mistakes:

- a malicious contributor proposes weakened controls, misleading examples, or unsafe links;
- a compromised maintainer account changes guidance or merges unreviewed content;
- a well-intentioned contributor includes secrets, customer data, private URLs, proprietary prompts, or production evidence;
- stale or incorrect framework mappings are treated as current compliance requirements;
- fictional examples are mistaken for approved real-world decisions or vendor recommendations;
- copied CSV or Markdown content introduces unsafe formulas, links, or instructions into another workflow;
- readers apply generic guidance without adapting it to their own legal, regulatory, technical, or risk context.

## Trust boundaries

### External contribution to repository

Issues and pull requests are untrusted input until reviewed. Repository validation can detect structural problems, broken local links, malformed CSV files, and text-hygiene issues, but it cannot prove that security advice is correct.

### Repository guidance to organisational policy

Published content is a starting point, not an approval decision. A team crossing this boundary must add its own owners, evidence, risk acceptance, legal review, technical testing, and exception process.

### External frameworks to local mappings

NIST, OWASP, ISO-style controls, privacy principles, and other external sources remain authoritative for their own requirements. Local mappings can become stale or incomplete and should not be treated as certification evidence.

### Public examples to real records

Examples are fictional and intentionally contain no real customer, employee, vendor, credential, or production information. Real governance evidence should be stored only in systems approved for its classification and access requirements.

## Existing mitigations

This repository reduces these risks through:

- a contribution guide and focused pull-request template;
- dependency-free repository validation for Markdown, CSV, JSON, YAML, and local links;
- fictional example data rather than production evidence;
- explicit warnings against publishing secrets or confidential material;
- human review expectations for AI-generated code, policy changes, vendor assessments, exceptions, and high-impact decisions;
- a changelog for notable guidance changes;
- a repository disclaimer that the material is not legal advice or compliance certification.

These controls improve consistency; they do not establish that a control is sufficient for a particular organisation.

## Residual risk

Important residual risks remain:

- guidance may become outdated as AI capabilities, threats, regulations, and standards evolve;
- technically valid content may still be misleading, incomplete, or unsuitable for a specific environment;
- public review cannot prevent all account compromise, social engineering, or malicious-link risk;
- organisations may copy templates without assigning accountable owners or testing the controls they record;
- external links and framework references can change independently of this repository.

## Review triggers

Review this threat model when any of the following changes materially:

- the repository adds executable code, integrations, generated content, or new automation;
- contribution or release controls change;
- new categories of sensitive evidence or examples are introduced;
- a material security issue is reported against repository content or its contribution process;
- framework mappings or the repository's intended audience expand significantly.

When a proposed change crosses into credentials, live systems, executable integrations, or production-impacting automation, perform a separate implementation-specific threat model rather than extending this document by assumption.
