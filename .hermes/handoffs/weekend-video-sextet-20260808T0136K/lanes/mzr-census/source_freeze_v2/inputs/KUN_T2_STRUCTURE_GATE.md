# KUN T2 STRUCTURE GATE — T2_ELIGIBILITY_CONTRACT_V1_DRAFT.md (contract structure only)

Lane: mzr-archive-census-20260805T1857K. Seat: Kun, adversarial review, findings only.
Verdict vocabulary per brief: T2 CONTRACT STRUCTURE GATE: PASS | PASS_WITH_EDITS | FAIL.
Scope: structure only. Whether specific tables are correctly classified is the evidence pass.
Not read this pass: T1_MZR_MANIFEST.json, T1_EVIDENCE_DIGEST.txt. No network. Nothing executed.

## 0. Custody and ground truth (verified, not inherited)

- Read from disk and re-derived: T2_ELIGIBILITY_CONTRACT_V1_DRAFT.md, T1_FINDINGS.md,
  MZR_CENSUS_CONTRACT_V1.md, CENSUS_APPENDIX_RECALL_SET.md. FACT.
- `MZR_CENSUS_CONTRACT_V1.md` is `-r--r--r--`, sha256 prefix `84e1d9b6ed147dd0` — the draft §1
  inheritance claim is TRUE, verified read-only. FACT.
- `CENSUS_APPENDIX_RECALL_SET.md` is `-r--r--r--`, sha256 prefix `b76c14ce40749720` — matches
  the census contract §6.3 pin. FACT.
- The draft is `-rw-r--r--`, consistent with its DRAFT-not-frozen status. FACT.
- Draft §1 counts (157 candidates, 178 pre-filter, 21 dropped, DONE, 0 channels failed) trace
  to T1_FINDINGS §1–2. FACT. §7 advisories (A1 type-instability, S8 case-completeness wording,
  24 clipped descriptions) trace to T1_FINDINGS §5. FACT.

## S1. Item 2 — the diagnosis survives attack; do NOT withdraw

The author asked first whether the census already covered this and C1 was misread. It did not,
and it was not. Census §6.3 froze: R1–R7 recall members (must appear); C1, self-described as a
precision control, whose appendix text is "present, but **no redshift axis** across all 58
columns" — a MISSING-axis instrument, excluded by the three-axis intersection itself; C2/C3
verified-absent anti-hallucination controls with `J/MNRAS/488/4638` as the ID-collision trap.
No frozen control exercises the mode T1 actually exhibits: a table passing all three axes on
symbol matching while semantically wrong. The F1/F2 species/provenance gates exist as routing
RULES but no frozen test item ever exercised them; T1's run is the empirical proof of the hole
(obvious non-galaxy catalogues in the manifest despite a fully-passed control set). The contract
is necessary. FACT, from census §6.3 + appendix + T1_FINDINGS §1/§3.

Minor wording edit (required): §2's headline "the census froze recall controls only" overstates
— the census's own §6.3 labels C1 a precision control, and the draft's very next sentence
concedes it. Make the headline match the body: the census froze no control for the
axis-passing semantic-contamination mode.

## S2. Item 1 — anti-circularity: real bounds, under-mechanized (not theatre)

§5.1 (no table_id, automatic FAIL) is a mechanism. §5.2 (freeze before ruling logic) is the
genuine control — ordering prevents the dangerous direction (test tuned to rule) and is present.
§5.3 (the six are a test, not the criteria) is a NORM with no mechanism, and it carries the
whole residual risk (rule tuned to test):

- (a) "Not stated generally enough" has no named adjudicator. The rule-author grades their own
  generality. REQUIRED EDIT: freeze the adjudicator now — a seat that is not the rule-author.
- (b) §5.1 bans naming identifiers but not SEMANTIC special-casing: a clause whose trigger
  fires on exactly the six and nothing else is special-casing in general clothing and passes
  §5.1 as written. REQUIRED EDIT: per-clause fire-counts across the 157 must be reported;
  clauses firing only on the six are flagged as presumptive special-casing.
- (c) §6 PASS does not require the full 157-candidate disposition table with per-candidate
  quoted evidence, so a rule mistreating the other 151 need never surface. REQUIRED EDIT: make
  the complete disposition table a PASS precondition; this mechanizes §5.3's "silent about the
  other 151".

Note for the record: a held-out control set is NOT a stronger control here — the author has
read the whole manifest, so any holdout is already known. Ordering plus independent adjudication
plus fire-counts is the available bound; the draft has the first and lacks the other two.

## S3. Item 3 — new-defect check: one freeze-blocking unpinned number

(a) FREEZE-BLOCKING. §6's "62 candidates carrying explicit gas-phase evidence" has no backing
anywhere in the permitted evidence corpus. T1_FINDINGS records 178/21/157, the per-channel
counts, and 28 fully-disqualified + 5 mixed — never 62. An unpinned count in a freeze document
is exactly the spin-lane failure shape: sha-pin a number whose provenance nobody can re-derive.
REQUIRED EDIT: pin 62 to a recorded, re-runnable derivation over the manifest (frozen query +
result), or strike the number; the qualitative shortfall-visibility clause stands without it.

(b) Every quoted ucd/description cell in §3 and §4 rests on manifest evidence outside this
pass's corpus. P1–P3's tables appear NOWHERE in T1_FINDINGS; the anchors' genuineness is wholly
delegated to the evidence pass. Structure-side exposure: §7 obliges T2 to consult
`descriptions_clipped` before quoting any description as evidence, yet the contract itself
quotes ~15 descriptions without asserting its own quotes were so checked. REQUIRED EDIT: label
each quoted cell as manifest-verbatim and add a freeze-time assertion that every quote was
verified full-length against the manifest and against `descriptions_clipped`. If the evidence
pass falsifies any anchor cell, the affected control is a landmine and this contract re-gates.

(c) Verified TRUE in this pass (read-only): the parent sha/chmod claims (§0); the T1 outcome
counts; the C1 characterization; D1's "no observations at all" (T1_FINDINGS §3 verbatim: "no
galaxies, no observations, and no redshift"). No other outside-world claims in the draft were
verifiable from the permitted corpus; none found contradicted by it.

## S4. Item 4 — §6 outcomes: HONEST_FAILURE exists; two boundary states undefined

Candidate-level HONEST_FAILURE is genuinely available and correctly armored: valid terminal
state, reported as a count, never resolved by fetching or by name-guessing. That matches the
inherited §5/F8 discipline. Three gaps:

- (a) REQUIRED EDIT — undefined run-level outcomes. The six have no honest-failure outlet: PASS
  requires all six to behave, FAIL requires a decoy retained or an anchor excluded on its trap.
  If recorded evidence proves insufficient to rule a CONTROL candidate, the run lands in neither
  state. Same hole at the other boundary: P1 sets no trap ("none — the clean control"), so
  excluding P1 for a non-trap reason is literally neither PASS nor FAIL as worded. Define the
  run-level outcome for control-unruleability (recommend: a finding against the CONTRACT —
  control mis-specified — triggering re-gate, not a silent T2 fail), and word FAIL as "any
  anchor excluded", with trap-exclusion as the emphasized case.
- (b) The 62 functions as a soft target despite the no-special-standing clause: recording an
  expected count "so a large post-T2 shortfall is visible" makes the shortfall consequential,
  and consequence is the pressure. Intent is disclaimed; effect is not. Fix per S3(a).
- (c) REQUIRED EDIT — a degenerate unruled-heavy run can still PASS the six. Require the
  unruled count to publish its named dominant cause, mirroring census §8(b).

## S5. Item 5 — P3 scoping: principled, not ducking

The frozen expectation covers exactly the axis the control exists to test (redshift: the
`pos.heliocentric` qualifier collision with D3 plus the "star" substring). Pre-ruling the mass
axis would (i) exceed the control's purpose — the trap does not depend on the mass ruling — and
(ii) violate §5.2: a pre-ruled mass axis embeds T2 ruling logic in a contract that freezes
before the logic exists. "Either ruling is acceptable; an unexplained one is not" binds the
author to accept both outcomes — the opposite of protecting a committed control; a protected
control would pre-rule "retain". Methodologically consistent with how C1's expectation was
frozen on its only relevant axis. FACT, from the draft's own structure.

Residual: the scoping's evidentiary basis (molecular-gas masses, stellar-to-gas ratio) is
manifest-only and unverified in this pass — folds into S3(b). Wording suggestion (non-blocking):
state explicitly that the redshift-axis expectation is a control definition, not a T2 ruling.

## S6. Cross-cutting, freeze-blocking — disposition vocabulary collides at the inheritance boundary

§3's "MUST EXCLUDE" and §6's "any decoy retained" never define the target disposition, and the
inherited vocabulary makes that load-bearing: census §2 defines EXCLUDED as E1-fail ONLY, with
F1/F2 strata routed to CENSUS-ONLY ("grids are census-only under a named rule"). D1–D3 pass E1
as symbol-matched, so under inherited vocabulary their natural disposition is CENSUS-ONLY, and
D1 double-routes (semantic E1-fail AND F2 census-only) — the two dispositions carry different
counts in the inherited §8 funnel headline. A T2 applying the inherited vocabulary literally
routes all three decoys to CENSUS-ONLY, and a grader reading §3 could call that a fail; the
contract is internally ambiguous across its own inheritance boundary. REQUIRED EDIT: define
"exclude"/"retained" in §3/§6 as a named disposition set (e.g., "any disposition other than
ELIGIBLE") and state which named rule disposes each decoy.

## S7. Evidence-form coverage, from the permitted corpus only (classification-neutral)

T1_FINDINGS §3 names FOUR axis-passing contaminants; the decoy set spans three mechanisms but a
single EVIDENCE FORM — every decoy carries a disqualifying UCD qualifier (`phys.composition`,
`pos.galactocentric`, `pos.heliocentric`). The fourth recorded contaminant, `I/355/paramp`
(`z-Flame`), is `src.redshift` UNQUALIFIED: its disqualification is description-only. A rule
keyed purely on qualifier semantics passes the six and misses the description-only form — §5.3's
generality hole made concrete from T1_FINDINGS alone. Whether a fourth decoy is added is the
evidence pass's call; the structure finding is that the decoy set's evidence-form coverage is
narrower than the lane's own recorded contamination forms, and §5's norm is the only current
guard — which is why S2(b)/(c) are required, not advisory.

## Disposition

The diagnosis is sound and the inheritance is respected (parent untouched, pins verified). The
structure fails freeze-readiness on three points: the unpinned 62 (S3a), the undefined
disposition vocabulary (S6), and the undefined run-level outcomes (S4a); the remaining edits are
text-level and bounded. None requires redesign.

Sole lane write this pass: this report. No manifest/digest reads, no network, no executions, no
DB/git/cockpit touches. stat/shasum were read-only verification of the draft's own freeze claims.

T2 CONTRACT STRUCTURE GATE: PASS_WITH_EDITS
