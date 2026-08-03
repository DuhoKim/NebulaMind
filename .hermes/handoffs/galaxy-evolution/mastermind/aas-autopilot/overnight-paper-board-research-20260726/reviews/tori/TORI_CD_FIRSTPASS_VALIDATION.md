# Tori Validation — Packets C/D First Pass

Marker: `OVERNIGHT_PAPER_BOARD_TORI_CD_FIRSTPASS_VALIDATION_V1`

Status: `C1_DONE__C2_DONE_COMPILED_ISOLATED__D1_BLOCKED__D2_PARTIAL__PUBLICATION_NOT_EXECUTED`

## Independent checks

- Immutable Lab source manifest: all 38 files PASS `baseline/INPUT_SHA256.txt`.
- Packet C receipt marker count: 1.
- Packet D Kun receipt marker count: 1.
- Packet D Goru receipt marker count: 1.
- Candidate/source unified diff: exactly 3 hunks.
- Candidate figure copy: byte-identical to source.
- Candidate PDF: SHA-256 `eed8992dbcfd2a23abc5e459dddbd2660a9add3607e9f34035df9115ac26b98e`; 82,670 bytes; 2 letter-sized pages; PDF 1.5.
- Candidate compile: `tectonic 0.16.9`, saved rc=0; zero `error:`/`fatal`/leading-`!` matches in `compile.log`; cosmetic underfull-box warnings only.
- Extracted PDF text: title, O/H-scale caveat, Tension caveat, and Provenance caveat all visibly present.
- Packet D deliverable hashes match both receipts.

## Honest outcomes

### Packet C1 — `2ab3c92eea8a`

`DONE` as a structural outline only. The source provides no draft and no quantitative result beyond its summary/figure; all scientific value slots remain `TO BE COMPUTED — NOT IN SOURCE`. This is not a publishable paper.

### Packet C2 — `gated-e2e-demo`

`DONE` as an isolated AI candidate with compiled PDF. The scientific document body differs from source only through the Hwao-adopted citation connective split and append-only caveats/provenance; non-rendered AI/provenance comments were also added. The reference block retains all five source entries. The O/H caveat correctly says differences remain confounded and cannot be interpreted as physical until a common calibration exists.

This artifact remains a forced-demo-lineage, `TENSION`, scale-confounded research note. It must not be represented as a validated measurement or an accepted paper. Any public promotion must visibly retain the AI-draft, forced/demo, TENSION, and unresolved-calibration disclosures.

### Packet D1 — `7cb504ea7ad3`

`BLOCKED`. The source review uses a prose verdict and requires substantial improvement. Observational comparison, uncertainty/error analysis, and selection/bias analysis are absent and cannot be closed tonight without new data/runner work. No prose patch was produced.

### Packet D2 — `fesc002`

`PARTIAL`. The draft is compiled and `MINOR`, but three inline citations are absent from the formal reference list, and `citation_entailment.checked=0` means zero positive entailment coverage. No draft patch was produced.

## Promotion consequence

No candidate has crossed a public-write gate yet. Packet C2 is the only compiled promotion candidate, and only as a clearly labelled autonomous Lab research-note draft. A publication packet must still identify the current served public target, immutable candidate hash, current-target backup/hash, exact before/after files, rollback command, visible labels, smoke tests, and packet-specific phrase `APPROVE PUBLISH <packet_id>`. Until that packet is reviewed, public status is `AWAITING_EXPLICIT_PUBLISH_APPROVAL`.

## Safety

- Source/current Lab mutations: 0
- Existing PDF replacements: 0
- Public/static-root writes: 0
- DB/SQL/API/wiki/page-version writes: 0
- Deploy/restart: 0
- Git writes: 0
- Cron/browser/account/billing/cloud changes: 0
- New paid API / Nous purchased-balance routes: 0

`OVERNIGHT_PAPER_BOARD_TORI_CD_FIRSTPASS_VALIDATION_V1`
