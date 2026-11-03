# Documentary coding framework

Coding guidance: AI assurance maps, UK and EU

Draft for you to finalise, 28 October 2026. Your words are in quotation marks and marked as yours; section 9 says where every part comes from. Tags such as (P2) mark wording taken from Claude.ai’s second coding test.

1. How to use this guidance

These are guidelines, not rules. The examples show the kind of thing that belongs in a cell; they are never a complete list, and nothing here limits what a cell can hold. Code what a document officially sets out or provides. Where the guidance does not fit a passage, use judgement and say so in the note.

2. What is mapped

The object: “any AI tool used in the public sector by public officials or in public services” (yours), as an object of governance: “who authorised it, must it be published, can it be challenged” (your framework).

The domain: AI assurance in the public sector.

The maps: two, one for the UK and one for the EU, each built from that side’s documents among the 37.

What to code: everything a document officially gives anyone in relation to the object.

Edge cases: if a passage is about AI used by others against the body (for example, checking whether incoming content is AI-generated), say so in the note (P11).

Model providers and others in the value chain: code their duties too, since their models sit inside public-sector tools (yours).

Reports: skip statements that only report what another instrument or body has set out or done, such as that a tool has been approved, or a body’s own mandate. Code these from the instrument itself if it is in the corpus (yours).

3. The rows (functions)

Decision-making: “authority over anything relevant” (yours).

For example: deciding whether a tool is used, approved, paused or stopped; overriding outputs; setting priorities, direction or standards; issuing mandates; deciding scope and exemptions; appointing who decides.

Whoever sets a standard is decision-making; whoever carries out the check is delivery (yours).

Where someone must “ensure” something is in place, it is usually decision-making if they can approve or stop it, and delivery if they must do it themselves; note when the document gives neither (P2).

Advising, proposing or guiding is usually not authority: consider coordination or resources, and note it (P3).

Delivery: “Who is formally responsible for delivery” (your framework).

For example: testing, evaluation, validation, monitoring, logging, recording, human review of outputs, impact assessment.

Coordination: “Which formal mechanisms connect actors” (your framework).

For example: contact points, notifications, shared templates, registers and databases, supplier contracts, cross-government groups and networks, referrals between bodies.

Accountability: “Who must answer to whom, with what consequence” (your framework).

For example: named accountable roles, sign-off, publication, registration, reporting to regulators or boards, audit, complaint and redress routes, sanctions.

Note to whom the holder answers and with what consequence, or write “not stated” (P8).

4. The columns (dimensions)

Design: “what is official[ly] set out” (yours), including what the document says is to be done or checked.

Requirements and recommendations both count. Note the verb (must, shall, should, consider, may); where a passage appears both in the body text and in a summary box, quote the body text (P6).

Questions: questions a document asks (for example, of audit committees) are coded as design, with the level of obligation “good practice: question” (yours).

Statutory or non-statutory: for every entry, say whether the requirement is statutory (set by legislation: an Act, a statutory instrument, an EU regulation) or non-statutory (policy, guidance, standards, codes), and give the basis, for example “statutory: AI Act Art. 53(1)” or “non-statutory: government policy”. A requirement can be mandatory without being statutory, as the ATRS is (yours).

Level of obligation: how binding the requirement is (yours). For example:

Statutory duty or power: set by legislation, e.g. the AI Act’s documentation duty (Art. 53).

Mandatory by policy for a named group: “It is mandatory for all government departments, and for ALBs which deliver public or frontline services, or directly interact with the general public.” (ATRS guidance, UK086)

Mandatory approval gate: “it’s mandatory to assure all non-business-as-usual spend above £100,000 for digital activities … through your assurance boards” (AI Playbook, UK174)

Comply or explain: “All central government departments and their arm’s length bodies are expected to follow this on a ‘comply or explain’ basis” (AI Playbook, on the DDaT Playbook)

Recommended: “the ATRS is recommended by the Data Standards Authority for use across the entire public sector” (UK086)

Good practice or question: “Is there a robust, planned and resourced testing regime?” (NAO guide, UK266)

Non-binding interpretation: for example the Commission’s guidelines on the AI Act (EU088).

One instrument can sit at two levels for different groups: the ATRS is mandatory for central government and recommended for the rest of the public sector. Resources that are provided carry no level.

If not met: what the document says happens if the requirement is not met (for example fines, recall, suspension, loss of an exemption, more scrutiny), or “not stated” (yours). In the pilot, only the statutory requirements say what happens.

For a check, note what triggers it (before use, on change, ongoing), what it compares against, and the metric, or write “not stated” (P9).

A proposal awaiting approval can be coded as design; note its status and whether approval is recorded (P14).

Resources: “what is official[ly] provided to implement what is in the design cell” (yours).

For example: roles and staff, skills and training, money, time, tools, templates, data, access, information, outside support.

Note which design entry it serves, and whether it is provided by a named actor or required of the holder; both belong here (P4, your yes).

Tools or services the document points people to can count: record who offers them, including non-state providers, and note whether it is an official offer or only a mention (P5).

Operation: what happens in practice. Not coded (yours). Case studies and worked examples are usually practice unless the document says to follow them (P12).

5. Each entry

Your framework: “Each cell records the holder, the level, and the holder’s position relative to the state.”

Holder: as the document names them; a cell can hold several. If the holder is unnamed or the sentence is passive, write “not stated” and give the nearest named actor in the note (P7). Where a document says “you”, record who the document says it applies to. Where a document speaks of “the organisation” without naming it, the holder is the organisation (yours).

Level: where in the system the holder sits. For example: international · EU · national · local · organisation · team · individual. Use the document’s own terms where they fit better (P1).

Position relative to the state: whether the holder is public authority. Inside the state, for example: core government departments, arm’s-length bodies, independent regulators and auditors. Outside, for example: private companies, civil society and academia, international standards bodies. In the EU map, EU institutions, agencies and member-state authorities count as public authority. Say in the note if a holder does not fit (P1).

Quote: verbatim, the shortest span that carries the point.

Location: page, paragraph or section.

Several cells: one passage can be coded to several cells: one entry per cell, with the others cross-referenced in the note (yours; P13).

6. Empty cells

Per document: For each document, write a short note for each empty cell saying why it is empty, in your own words, quoting where the document says something relevant. Things that may come up, for example: the document says nothing; it says it leaves the matter open; it points to another instrument; the tool falls outside its scope; only part of the document is held.

Per map: after all documents on one side are coded, explain each empty cell of the map using your framework’s reasons for absence: “the function is not allocated (about the world); no instrument in the corpus allocates it (about the corpus); nobody in the sample occupied a position from which it is visible (about the sample).”

7. Output

One Excel workbook in this folder. One row per entry: Document | Function | Dimension | Statutory or non-statutory | Level of obligation | If not met | Holder | Level | Position relative to the state | Quote | Location | Note. Empty-cell notes go in as rows with no holder. A second sheet describes each document: what it is, who wrote it, what it is for, and any other important notes (yours, 28 October).

8. Process

Claude Code codes all 37 documents first; you then check every entry (yours).

9. Where each part comes from
