# EU AI Act Article 50 Transparency Readiness Checklist

> **Important:** This checklist is practical engineering/governance guidance, not legal advice. Article 50 applicability depends on the system, role, deployment context, jurisdiction, and facts. Obtain jurisdiction-specific legal/compliance review before relying on an exemption or concluding that an obligation does not apply.

Article 50 transparency obligations apply from **2 August 2026**. The European Commission's final guidance distinguishes obligations for providers and deployers of certain interactive, generative, emotion-recognition, biometric-categorisation, and deepfake-related AI systems.

Use this checklist to triage applicability, assign owners, implement controls, and retain evidence. Record detailed evidence in [`templates/ai-transparency-evidence-register.csv`](../templates/ai-transparency-evidence-register.csv).

## Applicability Triage

- [ ] Identify the legal entity acting as **provider**, **deployer**, or both for each relevant AI system and use case.
- [ ] Confirm whether the system interacts directly with natural persons through a genuine two-way exchange.
- [ ] Confirm whether the system generates or manipulates synthetic text, audio, image, or video content.
- [ ] Confirm whether the deployment uses emotion recognition or biometric categorisation.
- [ ] Confirm whether generated or manipulated image, audio, or video could constitute a deepfake in the deployment context.
- [ ] Confirm whether generated or manipulated text is published to inform the public on matters of public interest.
- [ ] Record whether published public-interest text receives substantive human review or editorial control and whether editorial responsibility is assigned.
- [ ] Record whether a personal/non-professional-use exclusion, law-enforcement authorisation, or another specific exclusion may apply and obtain legal review before relying on it.
- [ ] Record the date the system was placed on the market or put into service where transition rules may matter.
- [ ] Assign legal/compliance, product, engineering, and operational owners for the final applicability decision.

## Provider: Direct AI Interaction Notice

For AI systems designed to interact directly with natural persons:

- [ ] Determine whether the fact that the person is interacting with AI is already objectively obvious in the specific context; treat this exception narrowly.
- [ ] Where notice is required, present it from the start of the first interaction.
- [ ] Make the notice clear, distinguishable, understandable, and accessible.
- [ ] Test the notice across supported channels such as web, mobile, voice, chat, avatar, or embedded experiences.
- [ ] Prevent UI changes, A/B tests, localisation, or white-labelling from silently removing the notice.
- [ ] Retain screenshots, copy/version history, accessibility evidence, and release records showing when the notice became effective.

## Provider: Machine-Readable Marking And Detectability

For providers of systems generating or manipulating synthetic text, audio, image, or video:

- [ ] Determine whether Article 50(2) marking/detectability applies to the output type and use case.
- [ ] Implement effective, reliable, robust, and interoperable machine-readable marking/detection measures appropriate to the content type and state of the art.
- [ ] Verify that marks survive normal generation, export, delivery, and supported transformation paths where technically expected.
- [ ] Document known limitations, failure modes, content types, and transformations that may reduce detectability.
- [ ] Verify that deployer-facing documentation explains what marking is present and what additional visible disclosure may still be required.
- [ ] Do not treat machine-readable marking as a substitute for deployer deepfake/public-interest-text disclosure where a separate deployer obligation applies.
- [ ] Record whether the system performs only an assistive standard-editing function or otherwise falls within a Commission-described exclusion; obtain legal review before relying on that conclusion.

### Outputs To Triage Carefully

The Commission guidance identifies examples that can fall outside Article 50(2) marking scope or receive narrower treatment. Document the basis before excluding them, including where relevant:

- short sequences of numbers, symbols, or letters;
- source code;
- outputs intended only for machine-to-machine processing without human exposure;
- non-final outputs used only in closed-loop industrial/product-development environments;
- standard editing that is merely assistive and does not materially change the input or its semantics;
- narrowly defined business-to-business or industrial-context cases described in the Commission guidance.

These are not blanket exemptions for all B2B, editing, development, or machine-generated content.

## Deployer: Emotion Recognition And Biometric Categorisation

- [ ] Identify whether natural persons are exposed to emotion-recognition or biometric-categorisation operation, including real-time and ex-post processing.
- [ ] Provide the required information to exposed persons in an appropriate, clear, and accessible manner.
- [ ] Define how notice works for employees, customers, visitors, remote participants, or other affected groups.
- [ ] Record the locations/channels where notice is presented and test that it remains visible after product or workplace changes.
- [ ] Coordinate Article 50 transparency with privacy/data-protection notices and other applicable employment, equality, biometric, or sector-specific requirements; do not assume one notice satisfies all regimes.

## Deployer: Deepfake Disclosure

- [ ] Assess whether generated or manipulated image, audio, or video could falsely appear authentic or truthful to the intended or reasonably foreseeable audience.
- [ ] Where disclosure is required, make it clear and perceptible to a natural person no later than first exposure.
- [ ] Do not rely only on hidden or machine-readable metadata to satisfy a visible/audible disclosure obligation.
- [ ] For evidently artistic, creative, satirical, fictional, or analogous works/programmes, document the basis and use an appropriate disclosure that does not unnecessarily impair display or enjoyment.
- [ ] Where a law-enforcement authorisation exception is considered, retain the authoritative legal basis and approval rather than a product-team assertion.
- [ ] Test disclosure placement for reposting, clipping, thumbnails, audio-only playback, exports, and other reasonably foreseeable distribution paths.

## Deployer: Public-Interest Text

For AI-generated or manipulated text published to inform the public on matters of public interest:

- [ ] Determine whether the text is actually **published**, intended to **inform the public**, and concerns a **matter of public interest**.
- [ ] If relying on the human-review/editorial-control exemption, require substantive examination by a qualified natural person rather than spell-checking, formatting, or other superficial review.
- [ ] Record who had authority to approve, alter, or reject the substance of the text and who carries editorial responsibility.
- [ ] Where the exemption does not apply, clearly label the text as artificially generated or manipulated in a manner appropriate to the publication channel.
- [ ] Retain publication, review, approval, and label evidence for audit or challenge.

## Transition Dates

- [ ] Treat **2 August 2026** as the general Article 50 applicability date.
- [ ] For AI systems placed on the market before 2 August 2026, assess the Commission-described limited transition for the Article 50(2) machine-readable marking/detection obligation; the Commission FAQ states compliance for those systems is required from **2 December 2026**.
- [ ] Do not extend that limited transition automatically to direct-interaction notices, deployer disclosures, or other Article 50 obligations.
- [ ] Do not assume content generated before 2 August 2026 must be labelled retroactively; record the organisation's policy if it chooses voluntary retroactive labelling.
- [ ] Re-check official sources before relying on transition dates because legislative or Commission guidance can change.

## Product And Engineering Evidence

Retain evidence proportionate to the use case, such as:

- system/use-case inventory and provider/deployer role assessment;
- user journeys showing AI-interaction notices;
- localisation and accessibility test results;
- machine-readable marking design, interoperability/detectability tests, and known limitations;
- release/version evidence tying transparency controls to deployed versions;
- deepfake/public-interest-text label designs and distribution-path tests;
- human-review/editorial workflow configuration and approval logs;
- monitoring or incident records for missing/incorrect notices and labels.

## Legal And Compliance Evidence

- [ ] Document the applicability analysis and specific Article 50 paragraph(s) considered.
- [ ] Document any exclusion/exemption relied upon, who approved it, supporting authority, and review date.
- [ ] Track the applicable EU Member State/market context and any other relevant law or regulator guidance.
- [ ] Record whether the organisation relies on the voluntary Code of Practice for marking/labelling or an alternative compliance approach.
- [ ] Set review triggers for material product changes, new content modalities, new deployment channels, or changed guidance/legislation.

## Operations And Ownership

- [ ] Give each transparency control a named control owner and implementation owner.
- [ ] Define monitoring for missing notices, lost metadata/marks, failed labels, or bypassed human review.
- [ ] Define incident/escalation steps when required transparency is absent after release.
- [ ] Include transparency controls in change management and release acceptance criteria.
- [ ] Schedule a periodic review and record the next review date.
- [ ] Track time-limited exceptions with an approver, expiry date, compensating controls, and remediation owner.

## Evidence Register

Use [`templates/ai-transparency-evidence-register.csv`](../templates/ai-transparency-evidence-register.csv) to record at least:

- system/use case;
- provider/deployer role;
- obligation/control;
- owner;
- implementation status;
- evidence reference;
- legal/compliance reviewer;
- review date;
- exception and expiry;
- next action.

## Primary Sources

Verify current obligations against official sources rather than relying only on this checklist:

- European Commission Article 50 guidelines: https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems
- European Commission Article 50 Q&A: https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act
- European Commission transparency policy page: https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations
- Code of Practice on Transparency of AI-generated Content: https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content

Last checked against Commission guidance: **26 August 2026**.
