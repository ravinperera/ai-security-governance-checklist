# EU AI Act Article 50 Transparency Readiness Checklist

> **Important:** This is an engineering and governance readiness aid, not legal advice, a legal opinion, or evidence of compliance. Article 50 applicability depends on the facts, the organisation's role, the system, the output, the audience, and other EU or national law. Obtain qualified legal review before relying on an exception or deploying a control in production.

## Current timing

- The European Commission published its Article 50 implementation guidelines on **20 July 2026**.
- Article 50 transparency obligations apply from **2 August 2026**.
- The Commission describes a limited transition only for the Article 50(2) machine-readable marking and detection obligation for systems placed on the market before 2 August 2026. Providers of those systems must meet that obligation from **2 December 2026**.
- Content generated before 2 August 2026 does not require retroactive labelling under the Commission FAQ, although voluntary labelling is encouraged where possible.

Record the legal source version and review date used for every assessment. Guidance, codes, technical standards, and product behaviour may change.

## Article 50 at a glance

| Control area | Primary responsible role | Practical requirement |
| --- | --- | --- |
| Direct interaction with AI | Provider | Design the system so a person is informed that they are interacting with AI, unless it is objectively obvious in context |
| Synthetic content marking and detection | Provider | Apply effective, interoperable, robust, reliable, machine-readable marking to in-scope synthetic audio, image, video, or text, as technically feasible |
| Emotion recognition and biometric categorisation | Deployer | Inform exposed natural persons that the system is operating and meet applicable personal-data obligations |
| Deepfakes | Deployer | Clearly disclose that qualifying image, audio, or video was artificially generated or manipulated |
| Public-interest text | Deployer | Clearly disclose qualifying AI-generated or manipulated text published to inform the public, unless the human-review/editorial-control exception is satisfied |
| Notice quality and timing | Provider or deployer | Provide required information clearly, distinguishably, accessibly, and no later than first interaction or exposure |

An organisation may be a provider for one system and a deployer for another. It may also perform both roles for the same service.

---

## 1. Establish scope and ownership

- [ ] Create or update the AI system inventory before assessing Article 50.
- [ ] Record the system name, version, product owner, technical owner, legal/compliance owner, and security owner.
- [ ] Record where the provider and deployer are established.
- [ ] Record whether the system is placed on the EU market, put into service in the EU, or produces output used in the EU.
- [ ] Identify whether your organisation is the **provider**, **deployer**, or both.
- [ ] Identify downstream providers, integrators, customers, contractors, and content publishers that may carry separate obligations.
- [ ] Record the system's market-placement or put-into-service date.
- [ ] Record the model, system, feature, and content types in scope: text, image, audio, video, biometric categorisation, emotion recognition, agent, avatar, chatbot, or other interface.
- [ ] Assign one accountable owner for the Article 50 assessment.
- [ ] Set a review date before launch and after any material change to model, interface, output type, audience, disclosure, or marking method.

### Evidence to retain

- AI system inventory entry
- role and responsibility analysis
- architecture and data-flow diagrams
- provider and deployer contracts
- system and model version records
- EU market and audience analysis
- approval and review records

---

## 2. Applicability triage

Answer every question and record the rationale in the [AI transparency evidence register](../templates/ai-transparency-evidence-register.csv).

### A. Direct AI interaction: Article 50(1)

- [ ] Is the product an AI system within the organisation's documented AI Act classification process?
- [ ] Is it designed for a genuine two-way exchange with natural persons?
- [ ] Does the AI system communicate directly with the person rather than exclusively through a human intermediary?
- [ ] Could an EU consumer, employee, contractor, professional, applicant, customer, or other natural person interact with it?
- [ ] Does it operate only in the background or exclusively through machine-to-machine communication? If yes, record why direct-interaction notice is out of scope.
- [ ] Is AI interaction objectively obvious to a reasonably well-informed, observant, and circumspect person in the specific context?
- [ ] If relying on the “obvious” exception, has legal/compliance approved a written, evidence-based rationale? Treat this exception narrowly.
- [ ] Is a law-enforcement authorisation exception being considered? If yes, stop and obtain specialist legal review; do not self-approve it through this checklist.

### B. Synthetic content marking and detection: Article 50(2)

- [ ] Does the provider's system generate or manipulate synthetic **audio, image, video, or text**?
- [ ] Does the output reach or potentially reach a human?
- [ ] Is the output more than a short sequence of numbers, symbols, or letters?
- [ ] Is the output source code? The Commission guidance identifies source code as outside this marking obligation; retain the applicability rationale.
- [ ] Is the output intended exclusively for machine-to-machine communication and automatic processing, with no human exposure?
- [ ] Is the output used only inside a closed-loop industrial or product-development environment and not exposed as a final output?
- [ ] Does the system only perform an assistive function for standard editing?
- [ ] Does it leave the deployer's input and semantics substantially unchanged?
- [ ] Is a narrow business-to-business or industrial-context exclusion being considered? Obtain legal review and document every condition from the current Commission guidance rather than assuming all B2B output is excluded.
- [ ] Is a law-enforcement authorisation exception being considered? Escalate for specialist legal review.
- [ ] If in scope, can the marking be applied to every relevant delivery path, export format, API response, and downstream transformation?

### C. Emotion recognition or biometric categorisation: Article 50(3)

- [ ] Does the deployed system infer or recognise emotions from biometric data?
- [ ] Does it assign people to categories using biometric data?
- [ ] Are natural persons exposed in real time or through later processing?
- [ ] Is the system prohibited or high-risk under another AI Act provision? Article 50 readiness does not replace that assessment.
- [ ] Is personal data processed consistently with applicable data-protection law and the organisation's privacy review?
- [ ] Is a law-enforcement exception being considered? Escalate for specialist legal review.

### D. Deepfake disclosure: Article 50(4)

- [ ] Does the deployed system generate or manipulate image, audio, or video?
- [ ] Does the result resemble an existing person, object, place, entity, or event?
- [ ] Could it falsely appear authentic or truthful to the intended or reasonably foreseeable audience?
- [ ] Have context, resemblance, substantive message, audience expectations, and foreseeable deployment been documented?
- [ ] Is the content part of an evidently artistic, creative, satirical, fictional, or analogous work? If yes, document the appropriate disclosure method that does not unreasonably hamper enjoyment of the work.
- [ ] Is a law-enforcement exception being considered? Escalate for specialist legal review.

### E. Public-interest text disclosure: Article 50(4)

- [ ] Is AI-generated or manipulated text **published**?
- [ ] Is it intended to inform the public?
- [ ] Does it concern a matter of public interest, such as politics, democratic processes, public administration, justice, law enforcement, fundamental rights, public security, public health, the environment, or other matters identified in current guidance?
- [ ] Did the content undergo meaningful human review or editorial control?
- [ ] Does an identifiable natural or legal person hold editorial responsibility for publication?
- [ ] If relying on the human-review/editorial-control exception, is the review substantive, documented, and completed before publication?
- [ ] Is a law-enforcement exception being considered? Escalate for specialist legal review.

### F. Personal, non-professional use

- [ ] Is a natural person using the system solely in a personal, non-professional capacity?
- [ ] Is there no regular economic benefit, business, trade, occupation, freelance activity, or use under a legal person's authority?
- [ ] If relying on the personal-use exclusion, document why the activity is not professional. Do not apply it to a company merely because an employee operates the tool.

---

## 3. Provider control: direct-interaction notice

For each in-scope chatbot, agent, avatar, voice interface, support assistant, or other interactive AI system:

- [ ] Display or communicate the AI notice no later than the beginning of the first interaction.
- [ ] Make the notice clear and distinguishable from ordinary content, terms, marketing, or privacy text.
- [ ] Use language a typical user can understand.
- [ ] Meet applicable accessibility requirements for visual, audio, keyboard, screen-reader, caption, and other supported channels.
- [ ] Ensure notice works on every interface: web, mobile, voice, API-powered UI, embedded widget, messaging channel, and white-label deployment.
- [ ] Repeat or preserve the notice where a session can be entered mid-flow or handed over between channels.
- [ ] Explain human handover or escalation where relevant without implying that the notice alone describes every system limitation.
- [ ] Test notice rendering, timing, accessibility, localisation, and failure behaviour before release.
- [ ] Prevent downstream customers from silently removing a required notice, or clearly allocate implementation responsibility by contract and technical documentation.
- [ ] Record screenshots, transcripts, accessibility checks, product requirements, and release evidence.

### Minimum test cases

- [ ] First-time user on every supported channel
- [ ] Returning user with a new session
- [ ] Direct/deep link into an active conversation
- [ ] Voice-only interaction
- [ ] Screen-reader and keyboard-only use
- [ ] Localised interfaces
- [ ] Network or component failure during notice display
- [ ] Human-to-AI and AI-to-human handover

---

## 4. Provider control: machine-readable marking and detectability

For in-scope synthetic content:

- [ ] Define the marking method for each content type and output format.
- [ ] Document why the method is effective, interoperable, robust, and reliable within current technical feasibility and state of the art.
- [ ] Document known limitations, false positives, false negatives, transformations, and removal risks.
- [ ] Apply marking by default rather than depending on an end user to enable it.
- [ ] Preserve marking through supported exports, downloads, compression, resizing, transcoding, and content-delivery paths where technically feasible.
- [ ] Provide downstream technical instructions for detecting and preserving the mark.
- [ ] Define behaviour when marking fails: block output, retry, warn, quarantine, or follow an approved fallback.
- [ ] Monitor marking coverage and failure rate.
- [ ] Test detection using an independently implemented or appropriately separated validation process where practical.
- [ ] Pin and record the marking component, algorithm, configuration, and version.
- [ ] Retain sample outputs and detection results without storing unnecessary personal or confidential content.
- [ ] Review the voluntary EU Code of Practice on Transparency of AI-Generated Content and document whether the organisation signs it or uses alternative adequate controls.

### Content-type test matrix

- [ ] Plain text and structured text
- [ ] Common image formats and metadata-stripped images
- [ ] Audio formats, clips, and transcoded output
- [ ] Video formats, edited clips, and platform upload/download cycles
- [ ] API, batch, streaming, and interactive generation
- [ ] Content copied into downstream tools
- [ ] Content resized, compressed, translated, summarised, or reformatted
- [ ] Output created during partial failure or retry

### Transition assessment

- [ ] Record whether the system was placed on the market before 2 August 2026.
- [ ] If relying on the limited transition until 2 December 2026, confirm that it applies only to Article 50(2) marking and detection, not to unrelated transparency duties.
- [ ] Record the remediation plan, owner, milestones, and evidence required before 2 December 2026.
- [ ] Do not treat content created before 2 August 2026 as automatically requiring retroactive labelling; record any voluntary labelling decision separately.

---

## 5. Deployer control: emotion recognition and biometric categorisation notice

- [ ] Notify exposed people that the system is operating.
- [ ] Provide the notice no later than first exposure.
- [ ] Make the notice clear, distinguishable, understandable, and accessible.
- [ ] Cover both real-time and ex-post processing.
- [ ] Identify locations, channels, and populations where exposure occurs.
- [ ] Coordinate the notice with privacy information, lawful-basis analysis, DPIA or equivalent review, retention, rights handling, and access controls.
- [ ] Do not imply that Article 50 notice makes an otherwise prohibited or unlawful use permissible.
- [ ] Test notice visibility in physical, digital, audio, and remote contexts as applicable.
- [ ] Record deployment dates, notice versions, language coverage, and evidence of operation.

---

## 6. Deployer control: deepfake disclosure

- [ ] Classify the content before release using the documented deepfake criteria.
- [ ] Disclose artificial generation or manipulation no later than first exposure.
- [ ] Use a clear, distinguishable, understandable, and perceivable visual or audible label.
- [ ] Do not rely solely on the provider's machine-readable mark; the deployer disclosure must be perceivable without special technical tools.
- [ ] Place the disclosure where it remains associated with the content during common sharing or embedding paths.
- [ ] For artistic, creative, satirical, fictional, or analogous work, select an appropriate disclosure that preserves transparency without unnecessarily hampering display or enjoyment.
- [ ] Define label text and placement for image, audio, video, live, short-form, long-form, and embedded media.
- [ ] Preserve disclosure after editing, clipping, reposting, localisation, captioning, and platform conversion where the organisation controls those steps.
- [ ] Require contractors, agencies, and publishers to follow the same approved process.
- [ ] Retain the unlabelled source, labelled final output, approval, publication location, and publication date in an access-controlled evidence store where appropriate.

---

## 7. Deployer control: public-interest text disclosure

- [ ] Establish an editorial triage for AI-generated or manipulated public-facing text.
- [ ] Determine whether the text is published to inform the public on a matter of public interest.
- [ ] If no human-review exception applies, clearly label the text as artificially generated or manipulated.
- [ ] Provide the disclosure no later than first exposure and make it clear, distinguishable, and accessible.
- [ ] If relying on human review/editorial control, define the reviewer, review standard, approval record, and legal or natural person holding editorial responsibility.
- [ ] Require the reviewer to verify facts, sources, material omissions, misleading framing, discrimination, defamation, safety, privacy, and applicable sector rules.
- [ ] Record the AI contribution, source material, reviewer, decision, changes made, and final approval.
- [ ] Reassess after material AI regeneration or editing; an approval should not automatically cover a later version.
- [ ] Ensure syndication, translation, reposting, and content-management templates preserve required disclosure.

---

## 8. Common notice requirements

For every required Article 50 notice or disclosure:

- [ ] Delivered no later than first interaction or exposure
- [ ] Clear and distinguishable from surrounding information
- [ ] Understandable to the intended audience
- [ ] Perceivable without specialist tools where a deployer disclosure is required
- [ ] Accessible under applicable accessibility requirements
- [ ] Available in supported languages
- [ ] Consistent across channels and versions
- [ ] Tested before release and after material interface changes
- [ ] Monitored for removal, suppression, rendering failure, or localisation gaps
- [ ] Versioned with an owner, effective date, and review date

Do not bury a required notice only in terms of service, privacy documentation, or a help page when the obligation requires notification at first interaction or exposure.

---

## 9. Evidence by team

### Product and design

- [ ] Product requirement describing the Article 50 scenario
- [ ] User journey showing first interaction or exposure
- [ ] Approved notice wording and placement
- [ ] Accessibility and localisation evidence
- [ ] Design-system component and version
- [ ] User testing or design review

### Engineering and platform

- [ ] Architecture and content-flow diagram
- [ ] System and model versions
- [ ] Marking implementation and configuration
- [ ] Detection and transformation test results
- [ ] Feature flags and fail-safe behaviour
- [ ] Monitoring, logging, alerting, and incident runbook
- [ ] Release and rollback evidence
- [ ] Downstream integration instructions

### Legal, privacy, and compliance

- [ ] Provider/deployer role analysis
- [ ] Applicability and exception rationale
- [ ] Legal review and approval
- [ ] Privacy review, DPIA, or equivalent where applicable
- [ ] Contractual allocation of provider/deployer responsibilities
- [ ] Current source links and guidance version
- [ ] Code of Practice decision
- [ ] Exception and expiry approval

### Content, communications, and operations

- [ ] Content classification decision
- [ ] Human-review/editorial-control record
- [ ] Final labelled asset or publication
- [ ] Publication channel and date
- [ ] Contractor or agency instruction
- [ ] Complaints, corrections, takedowns, and incident records
- [ ] Periodic sampling and quality review

---

## 10. Monitoring, incidents, and change control

- [ ] Add Article 50 controls to release and content-publishing checklists.
- [ ] Monitor notice rendering, label presence, marking coverage, and detection success.
- [ ] Define thresholds and owners for marking or disclosure failures.
- [ ] Create an incident path for missing notices, removed labels, marking failures, misleading content, or incorrect reliance on an exception.
- [ ] Preserve affected versions, logs, approvals, and publication records.
- [ ] Assess whether content should be corrected, labelled, withdrawn, or notified to customers or authorities with legal advice.
- [ ] Review Article 50 applicability after changes to model, content modality, user interface, audience, distribution channel, market, role, or downstream customer configuration.
- [ ] Track guidance, Code of Practice, standards, enforcement decisions, and product-platform changes.
- [ ] Revalidate controls at least annually and before the recorded review date.

---

## 11. Exception management

- [ ] Identify the exact legal or guidance basis for the proposed exception.
- [ ] Record the facts and evidence supporting every condition.
- [ ] Obtain named legal/compliance approval.
- [ ] Record the system version, use case, geography, audience, and output types covered.
- [ ] Set a review date and expiry date.
- [ ] Define compensating transparency measures where appropriate.
- [ ] Revoke the exception after material change or when any condition is no longer met.
- [ ] Never use a business preference, technical inconvenience, or customer request as an undocumented exception.

---

## 12. Final readiness decision

Record one outcome:

- **Ready:** all applicable controls implemented, tested, evidenced, and approved.
- **Conditionally ready:** documented low-risk gaps have owners, deadlines, compensating controls, and legal/compliance approval.
- **Not ready:** a required notice, disclosure, marking, detection, legal analysis, or evidence control is missing.
- **Out of scope:** a documented, reviewed applicability assessment supports this outcome and has a review date.

### Approval record

```text
System:
Version:
Provider / deployer role:
In-scope Article 50 paragraphs:
Decision:
Open gaps:
Compensating controls:
Technical owner:
Product owner:
Legal/compliance approver:
Security/privacy approver:
Approval date:
Next review date:
Evidence location:
```

---

## Official sources

- [Commission press release: Article 50 transparency guidelines, 20 July 2026](https://digital-strategy.ec.europa.eu/en/news/commission-publishes-guidelines-transparency-obligations-providers-and-deployers-certain-ai-systems)
- [Commission guidelines library](https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems)
- [Commission Article 50 questions and answers](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act)
- [Commission quick facts on transparency rules](https://digital-strategy.ec.europa.eu/en/factpages/quick-facts-transparency-rules-ai-systems)
- [AI Act Service Desk: Article 50 text and summary](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50)

Check these sources for updates before each formal assessment.