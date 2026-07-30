# Contributing

Thank you for helping improve the AI Security & Governance Checklist. This project is intended to be practical, lightweight, and safe for teams adopting AI tools.

## Good contributions

Useful contributions include:

- New checklist items with clear, actionable wording.
- Improvements to existing controls, templates, or framework mappings.
- Examples that help teams apply the guidance in engineering, DevOps, SaaS, security, or compliance workflows.
- Corrections that make the repository clearer, safer, or easier to use.

## Before you start

1. Open or select an issue that describes the problem and proposed outcome.
2. Use the checklist-improvement or framework-mapping issue template where applicable.
3. Keep each pull request focused on one clear change.
4. Confirm that no confidential data, credentials, private URLs, or customer material are included.

## Contribution workflow

1. Create a branch from `main`.
2. Make the smallest change that fully addresses the issue.
3. Update related README links, templates, examples, mappings, or release notes when needed.
4. Run the dependency-free repository validation:

   ```bash
   python3 -m unittest discover -s tests -p 'test_validate_repository.py' -v
   python3 scripts/validate_repository.py
   ```

5. Open a pull request that explains the problem, scope, validation performed, and any assumptions.

## Checklist item guidance

When adding a new control or checklist item, include where practical:

- The risk being reduced.
- The owner or team likely to action it.
- Evidence that could demonstrate the control exists.
- Any caveats, exclusions, or assumptions.

Prefer direct wording such as “Review AI-generated code before production use” instead of vague wording such as “Use AI responsibly.”

## Framework mapping guidance

Framework mappings should:

- Reference the exact framework version, publication date, or control identifier.
- Link to an authoritative source where licensing and access permit.
- Explain the nature of the relationship rather than claiming automatic compliance.
- Identify partial, indirect, or organisation-dependent mappings.
- State clearly when legal, regulatory, or certification interpretation requires specialist review.

## Templates and examples

Keep templates easy to copy and adapt. Completed examples must be fictional or safely anonymised, and they must not imply that a named product, vendor, risk rating, or approval decision is suitable for every organisation.

## Safety and confidentiality

Do not include:

- Secrets, credentials, API keys, tokens, or private URLs.
- Customer data, production logs, proprietary prompts, or confidential source code.
- Unverified legal or compliance claims.
- Instructions that help bypass security controls.

Use anonymised examples and placeholders where needed.

## Pull request checklist

Before opening a pull request, check that:

- The change is practical and reusable.
- The scope matches the linked issue.
- No confidential data is included.
- No legal advice is presented as final legal guidance.
- Markdown tables render correctly.
- Templates remain easy to copy and use.
- Local validation passes.
- `CHANGELOG.md` is updated when the change affects published guidance, templates, mappings, or repository behaviour.

## Tone

Keep the guidance practical and accessible. The goal is to help teams adopt AI safely without creating unnecessary bureaucracy.
