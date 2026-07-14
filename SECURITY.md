# Security Policy

## Supported content

This repository contains guidance, checklists, mappings, and templates rather than a deployed application. Security fixes are applied to the current default branch. Older copies, forks, downloaded templates, and adapted versions are not maintained by this repository.

## Reporting a security concern

Please report security concerns privately when they involve:

- a vulnerability in repository automation or configuration
- credentials, tokens, personal data, customer data, or confidential material committed by mistake
- guidance that could cause a material security failure when followed as written
- a malicious link, dependency, example, or contribution
- a weakness that would be unsafe to demonstrate publicly before remediation

Use GitHub's **Report a vulnerability** option on the repository Security page when it is available. This is the preferred channel because it creates a private discussion with the repository maintainer.

When private vulnerability reporting is not available, open a public issue containing only a minimal request for a private contact channel. Do not include exploit details, sensitive evidence, secrets, personal data, customer information, or confidential prompts in that issue.

## What to include

Provide only the information needed to understand and reproduce the concern safely:

- affected file, workflow, template, or guidance section
- concise description of the risk and likely impact
- safe reproduction steps or a redacted proof of concept
- conditions required for exploitation or misuse
- suggested remediation, when known
- whether the issue may involve exposed data or credentials

Use placeholders and synthetic examples instead of live credentials, production identifiers, or real customer data.

## Response approach

The maintainer will aim to:

1. acknowledge a privately reported concern
2. assess its scope, severity, and whether sensitive material must be removed or rotated
3. coordinate a correction before public disclosure when that reduces risk
4. credit the reporter when requested and appropriate
5. publish a concise remediation note when users need to update copied guidance or templates

Response times cannot be guaranteed. Urgent credential exposure should also be handled immediately through the relevant provider's revocation and rotation process; a repository report is not a substitute for containment.

## Responsible disclosure

Please allow reasonable time for assessment and remediation before publishing technical details. Avoid testing against systems, accounts, vendors, or data that you do not own or have explicit permission to assess.

## Scope limitations

This policy does not cover vulnerabilities in third-party AI products, cloud services, frameworks, or standards merely referenced by this repository. Report those issues directly to the relevant vendor or project. However, please report broken, misleading, or unsafe guidance in this repository so it can be corrected.
