# Support and Stability

This repository is a public reference project. It aims to keep checklists, templates, examples, mappings, and validation tooling useful and understandable, but it does not provide a commercial support commitment or a compatibility guarantee for every file.

## Stability expectations

Repository content falls into four practical categories:

| Category | Examples | Expectation |
| --- | --- | --- |
| Maintained reference content | `checklists/`, `templates/` | Changes should preserve intent where practical. Material structure or schema changes should be called out in `CHANGELOG.md`. |
| Framework mappings | `mappings/` | Informative mappings may change when source frameworks or repository interpretations evolve. Adopters should verify against the framework version they use. |
| Fictional examples | `examples/` | Illustrative only. Values, ratings, owners, and decisions may change without compatibility guarantees. |
| Repository tooling | `scripts/`, `tests/`, `.github/workflows/` | Maintained for this repository's own quality checks. These files are not a supported external API. |

## Change handling

When a checklist or reusable template changes materially, contributors should keep the change focused, update affected documentation and examples, and record notable user-facing changes in `CHANGELOG.md`.

For CSV templates, changes to column names, order, or meaning should be treated as schema changes. Where practical, the pull request should explain how an existing copied register can be adapted.

If a file is replaced or retired, prefer a clear transition path over silently removing the old guidance. Update repository links at the same time so users do not land on stale paths.

## What adopters should pin locally

Organisations should copy the files they adopt into their own controlled repository and review them against their requirements. A local copy provides a clear approval point and prevents upstream wording changes from silently altering an internal control set.

Record the source repository commit or release reference when traceability matters. Re-review upstream changes before incorporating them into an approved internal baseline.

## Support boundaries

Issues and pull requests are appropriate for reproducible documentation defects, unclear checklist wording, template consistency problems, and proposed framework-mapping improvements. Organisation-specific legal, regulatory, risk-acceptance, or product-approval decisions remain outside the scope of this repository.

For repository security concerns, follow [`SECURITY.md`](SECURITY.md) rather than posting sensitive details in a public issue.

## Versioning

The project uses `CHANGELOG.md` for notable changes but does not currently promise Semantic Versioning or a long-term support branch. Consumers that need strict compatibility should pin the exact content they have reviewed and test later updates before adoption.
