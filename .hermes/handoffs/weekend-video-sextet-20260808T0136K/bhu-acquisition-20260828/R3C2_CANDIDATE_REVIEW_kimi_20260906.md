ACCESS_SHA=cb78eef0f4167759a415b5381b73fd075bb5475172e5290afa24d9a1c3820cfe
SEAT=kimi
CANDIDATE_D1=SOUND_WITH_REPAIRS
CANDIDATE_D7=SOUND_WITH_REPAIRS
BATCH_PREP=UNSOUND
TOOLING_MATCHES_CLAUSE=NO
COUNTEREXAMPLE_HANDLED=YES
IMPORTED_RULE_BREAKS_PARTITION=YES
STAGED_TESTS=PASS

# R3C2 candidate review — seat kimi, 2026-09-06

Adversarial, independent review of `R3C2_D1_D7_CANDIDATE_CLAUSES_20260906.md`, `R3C2_BATCH_PREPARATION_UNADOPTED_20260906.md`
and the staged kit `r3c2_staged_d1d7/`. V23 (`R3C2_V23_DESIGN_OF_RECORD_55b466fa.md`) and the living draft
(`R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md`) were read for context only and are not reviewed here. Nothing in this
report adopts, freezes or runs anything. All my own fixtures and outputs are under `r3c2_staged_d1d7/_review_kimi/kimi_work/`;
no other file was modified. (Note: `_review_kimi/` also contains a concurrent `codex_yecco2mj/` probe tree from another
process; I did not read its results and my probes below are built from my own files in `kimi_work/`.)

## A. Pin sheet

`shasum -a 256 -c r3c2_staged_d1d7/R3C2_STAGED_D1D7.sha256` from the working directory — all six entries OK
(ledger STAGED cf42430a…, batch STAGED bf3a3524…, tests 96c17920…, README 429edfb9…, partition e8ca431c…, exhibit 856dd4d0…).
After I re-ran the kit (which regenerates the exhibit and `_ctl/`), the pin sheet still verifies: the exhibit regenerates
byte-identical — the kit is deterministic.

## B. The kit, run by me

`cd r3c2_staged_d1d7 && /usr/bin/python3 -E r3c2_staged_tests.py`. Last three lines:

```
exhibit written: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/r3c2_staged_d1d7/C6_COUNTEREXAMPLE_EXHIBIT.txt
controls=44 passed=44 failed=0
STAGED_TESTS=PASS
```

My own synthetic counterexample, built from files I wrote myself (`kimi_work/out/src/`): sources `paperX.txt`, `paperY.txt`;
the §1-required passage is `paperY.txt:4` numeral `17.4` ("We obtain w = 17.4 from the fit." — unambiguously the paper's own
result). BOTH seat ledgers omit it; my auditor's enumeration retains it (`a4`). Commands run, in order:

1. `audit seal-enumeration k_aud_c.json k_aud_x.json k_stage1.txt` → auditor digests sealed (`fad6ad1d…`, `fb6522d9…`).
2. `audit select k_sealed_c.json abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789 k_sel.json` → `N=2 R=1 k=1 audited=2`.
3. `audit compare k_stage1.txt k_aud_c.json k_aud_x.json k_sealed_c.json k_sealed_x.json k_sealed_l.json k_sel.json k_red.json k_C6_AUDIT.json` → emitted:

```
FAIL: COMPLETENESS audit_included_absent_from_sealed: ['paperY.txt', 4, '17.4']
C6_AUDIT_SAMPLE=FAIL
```

Reverse omission (sealed includes `paperY.txt:4 '17.4'` as included; the auditor's enumeration lacks it):

```
FAIL: COMPLETENESS sealed_included_absent_from_audit_enumeration: ['paperY.txt', 4, '17.4']
C6_AUDIT_SAMPLE=FAIL
```

Word-for-word against the clause: the three predicates the brief names DO match the code — (i) `C6_AUDIT_SAMPLE=PASS` only
with the artefact printed, no audited-claim `MISMATCH`, and no omission in EITHER direction (verified both directions above
and by kit probes 1–2); (ii) the both-directions completeness rule fails and lists each side (verified); (iii) the
`AUDIT_INCLUSION_DISPUTED` 10% rule fails strictly above 10% of the sealed (included) denominator and passes at exactly 10%
listed-and-counted (kit probes 3–4: 2/20 PASS, 3/20 FAIL). BUT four other clause sentences do not match the code — findings
F4, F5, F6, F7 below — hence `TOOLING_MATCHES_CLAUSE=NO`.

Additional probes I ran (all under `kimi_work/out/`):

- K3: a sealed EXCLUDED passage (`paperY.txt:3 '2022'`, kind DATE) absent from the auditor's entire enumeration →
  `C6_AUDIT_SAMPLE=PASS` with every completeness list empty: the sealed-excluded row is silently unlisted (finding F6).
- K4: an auditor candidate file with `declared_candidate_count=99`, `declared_included_count=88` passes `audit compare`
  (`C6_AUDIT_SAMPLE=PASS`); the SAME file under the pinned `census` fails (`C1_DENOMINATOR_PRINTED=FAIL`,
  "declared_candidate_count=99 but recomputed 3"). The clause's "(census PASS required)" is not enforced (finding F4).
- K5a–K5g: D1 validate cases (section C).
- K6: batch join with a batch-1 LEDGER record citing a batch-2 text → `JOIN=PASS`; per-batch `validate` of that ledger in a
  batch-1-only directory → `FAIL: j1: cannot read external value line bt3.txt:2`; the same ledger validated against the full
  corpus → `C3_NO_SUBSTITUTION=PASS` (finding F9).

## C. D1 — do the two wordings reach identical filings?

Constructed cases (`kimi_work/out/d1src/`, borrower `paperP.txt`, source `paperQ.txt`), each run through the staged
`validate`:

| case | source line | review's wording (evidence at borrower's sentence) | Tori's wording (evidence at source's line) |
|---|---|---|---|
| K5a | "We fit b = 7 to the data." | PASS (IMPORTED/ORIG_CITATION) | same classification |
| K5b | "We measure c = 3 in the lab." | PASS | same classification |
| K5c | "We adopt d = 11 from Zee (1999)." | PASS | same classification |
| ("we choose") | (kit's own positive control: "we choose a = 2") | PASS | same classification |
| K5d | value machine-matches at TWO lines (4 and 7); filed at line 7 | PASS — no tie-break | same |

On CLASSIFICATIONS (status `PRINTED`, origin `IMPORTED`, value) the two wordings reach identical filings on every case I can
construct. They do NOT reach identical records: the evidence site differs (borrower's citing sentence vs the source's own
line), so `origin_evidence.source_file/source_line/verbatim` differ between the wordings. The candidate's "My clause reaches
the same filings" is therefore true at the classification level and imprecise at the record level (finding F1).

Which wording is safer against a seat filing CHOSEN for an import, and why: THE V25 REVIEW'S. Under it, the quoted evidence is
the BORROWER'S sentence, which names the external source, so C3's existing precedence — "`ORIG_CITATION` first; a sentence
that names an external source for the value is a citation whatever else it says" — mechanically forces `IMPORTED`. Under
Tori's, the quote is the SOURCE'S own line; a line reading "we choose"/"we fit" matches `ORIG_CHOICE_STATED`/`ORIG_FIT_STATED`
under the ordinary precedence, so the clause must carry a special exemption ("the reason-code precedence is not applied to
the source's line at the borrower") — and that exemption is seat-applied and machine-uncheckable. Demonstrated: K5f, a seat
quoting the source's "We fit b = 7 to the data." line and filing `FITTED` passes `validate` (`C3_NO_SUBSTITUTION=PASS`) — the
misfiled import is caught only by the second seat and the C6 re-classification, never by the machine. The candidate's own
recommendation (the review's wording) is the right call; the mechanism above is the reason, and the candidate could state it
in one sentence.

Two further D1 facts from my runs: K5d — when the value machine-matches at two source lines, `validate` accepts either; no
tie-break exists and no downstream control compares `source_line` (finding F2). K5g — a "citing sentence" quoted from a THIRD
pinned text (not the borrower) passes `validate`; the only self-file check is `origin_evidence.source_file != record.source_file`
(r3c2_ledger_tools_STAGED.py:92) (finding F3).

## D. D7 — is source-only enumeration before ANY ledger exposure actually enforced?

Partially. What the staged procedure enforces in CODE: (1) enumeration FIXITY — `audit compare` refuses with `C6_STAGE_ORDER`
if the auditor's enumeration differs from its stage-1 seal (verified by the kit's negative + deletion probe); (2) selection
binding — the selection carries `sealed_candidates_sha256` and compare refuses a mismatch. What it does NOT enforce: the
TEMPORAL precedence itself — that the enumeration was made, and sealed, before the auditor saw any sealed ledger. The stage-1
seal is two digests written by the custodian; it carries no timestamp and no external receipt (unlike the design's receipts P
and T), and nothing binds "sealed" to "before exposure" except the custodian's act and the dispatch layout.

Every way an auditor could see a sealed ledger before its stage-1 seal that the design does not close:

1. The custodian runs `audit seal-enumeration` LATE (after the auditor had ledger access). The tool cannot detect this; no
   receipt or timestamp exists. CUSTODY matter — but the candidate does not restate it.
2. The auditor is dispatched with the sealed artefacts inside its working directory. No staged dispatch-inventory,
   `ACCESS_SHA` or path-list control exists for the auditor seat (C4's floor for seats is self-reported and labelled
   procedural). CUSTODY matter — not restated.
3. Prior exposure through the lane: the tally commit exists in the lane before the auditor runs; an auditor seat of the same
   engine family may have seen it, and "cannot prove a seat has no prior exposure from training or an earlier session" is the
   floor V23 already states for seats. CUSTODY matter — not restated for the auditor.
4. The RE-DERIVATIONS are never sealed. The clause orders "the sealed ledgers are opened to it only after its own enumeration
   AND re-derivations are printed"; the tool seals only the enumeration (`cmd_audit_seal` hashes candidates+exclusions;
   `cmd_audit_compare` merely READS the re-derivation file; no `seal-rederivation` subcommand exists). Re-derivations written
   after ledger exposure are indistinguishable from honest ones — `MATCH` can be manufactured. This one is a CLAUSE/TOOL
   defect, not custody: the seal pattern already exists and is applied to exactly one of the two artefacts the clause orders
   before exposure (finding F5).

Verdict of the comparison the candidate makes (stronger vs weaker) is CORRECT: under the weaker version the auditor is
anchored on the seats' lists and a both-seats-missed passage is structurally invisible; under the stronger it is found and
now fails the census (my B-section runs). The "LESS LIKELY … direction only, no magnitude has been measured" hedge is honest.

## E. Batch preparation — does one denominator survive the partition?

The §5 argument is: "§1's inclusion rule is per passage and §2's arithmetic is per claim; neither consults any other text.
Therefore the enumeration of the whole corpus equals the union of the enumerations of any partition of it, PROVIDED every
text is in exactly one batch and no batch cites outside itself. Both provisos are controls, not assumptions."

The premise is FALSE and the second proviso is NOT fully controlled:

- §1's inclusion rule is per passage — granted. But §2 contains the IMPORTED rule (living draft lines 85–89; V23 §2; the very
  rule D1 strengthens): "A value the paper does not print but traces to a named source that is itself an enumerable text in
  `R3C2_CORPUS_MANIFEST.md` is classified `PRINTED` from that source … and the value machine-matched there." That rule
  consults ANOTHER text — the named source's file and line — which may sit in a DIFFERENT batch.
- Demonstrated (K6): a batch-1 session whose directory holds "ONLY batch k's texts" cannot machine-match an import whose
  source is in batch 2 — `validate` fails: "cannot read external value line bt3.txt:2". The seat cannot execute the IMPORTED
  rule inside the batch layout as staged; it must either fail its own C3 control on a legitimate import or read out of its
  directory — the exact improvisation that killed seat B (the death finding this preparation answers).
- And the proviso "no batch cites outside itself" is controlled only for CANDIDATE rows: `join` checks each candidate's
  `source_file` against the batch's text list (r3c2_batch_tools_STAGED.py:51–52) but never checks the LEDGER records'
  `source_file` or `origin_evidence.source_file`. Demonstrated (K6): a batch-1 ledger record citing a batch-2 text passes
  `JOIN=PASS`.
- The same break reaches the D7 audit: the auditor re-classifies "each of its inputs' origin from the pinned sources" — an
  imported input's evidence spans two batches, and the audit's re-derivation-stage layout is not specified.

What the candidate must add (any one mechanism, plus the control):

(a) batch directories carry all 89 texts READ-ONLY for the machine-match, with the session-layout sentence and the C4
    path-list discipline amended to say: enumeration is per batch, but any manifest text is readable for an import match; or
(b) imports whose named source is outside the batch are filed with the external match PENDING, and a named, pinned lane-side
    step machine-matches them over the JOINED ledger against the full corpus — I verified this passes (K6 full-corpus
    validate → `C3_NO_SUBSTITUTION=PASS`) — with per-batch validate scoped accordingly;
AND in both cases: extend `join`'s scope check to ledger records (`source_file` and `origin_evidence.source_file`), failing
or explicitly exempting-and-controlling cross-batch citations; and state the auditor-side equivalent for D7
re-classification. §5's "neither consults any other text" must be rewritten to name the one cross-text rule and show the
mechanism that keeps it inside the partition argument.

Because the load-bearing "ONE census with ONE denominator" argument rests on a false premise as printed, and the seat cannot
execute a cross-batch import under the staged layout, I rule the batch preparation UNSOUND AS WRITTEN. It is repairable — the
additions above are mechanical, and everything else I tested (partition, seal, join-as-function, coverage) verified clean —
but it is not a wording repair; a mechanism and a control must be added.

## F. Overclaims and the findings

Each finding: verbatim quote — the defect — the exact replacement I require — the consequence for what the census could
conclude.

### D1

F1. Quote: "My clause reaches the same filings by declaring the source's line the citation; the review's reaches them by
quoting the borrower's sentence." (and the tooling bullet "D1 in code (validate): …")
Defect: two overstatements. (i) The wordings reach the same CLASSIFICATIONS, not the same filings — the records' evidence
file/line/verbatim differ. (ii) The candidate carries two wordings but nowhere states that the staged tool implements ONLY
the review's: under Tori's wording `origin_evidence` names the source's own line, so `origin_evidence.source_file ==
record.source_file`, which the staged check at r3c2_ledger_tools_STAGED.py:92 rejects — my K5e: "FAIL: j1: IMPORTED PRINTED
record names its own file as the external source". If Duho accepts Tori's wording and the staged tool is installed, every D1
record fails C3.
Exact replacement: "The two wordings reach the same classifications (status/origin/value), not byte-identical records; the
staged tool implements the review's wording only — under Tori's, origin_evidence names the source's own line and trips the
self-file check, so accepting Tori's wording requires re-staging the validate rule."
Consequence: as written, choosing Tori's wording plus the staged kit reproduces exactly the BLOCKED-or-split outcome D1
exists to prevent.

F2. Quote: "`ORIG_CITATION` quoting the cited line verbatim with its file and line" / "the external value line where the
number machine-matches".
Defect: no tie-break when the value machine-matches at MORE THAN ONE line of the named source. K5d: a filing at the second
matching line passes `validate`. Two seats can file different `source_line` for the same input; `merge` compares input_id
sets and origins only, C6 re-classifies origin not lines — the divergence is invisible to every control.
Exact replacement: add to either wording: "When the value machine-matches at more than one line of the named source, the
seat files the first matching line."
Consequence: small (rests_on is unaffected), but two seats can file silently different evidence for the same import and no
control ever sees it.

F3. Quote: "has its verbatim matched at the CLAIMING paper's citing sentence (`origin_evidence.source_file/source_line`)".
Defect: the machine check cannot verify the citing sentence is in the CLAIMING paper — the only self-file check is
`origin_evidence.source_file != record.source_file`. K5g: a "citing sentence" quoted from a third pinned text passes
`validate`. The tooling description says "not the record's own file", which the check cannot establish (the schema carries
no field for the record's own file).
Exact replacement: state the floor in the candidate — "the machine checks the two cited files differ and are pinned; that
the quoting sentence lies in the claiming paper is seat judgement, caught by the second seat and the C6 re-classification,
never by the machine" — or carry the claiming file in the schema and check it.
Consequence: as written the tooling paragraph claims a check the code does not perform; the actual floor is the
second-reader floor the design already states elsewhere.

### D7

F4. Quote: "writes its own candidate and exclusion ledgers (`census` PASS required)" and "an auditor `census` PASS becomes a
precondition of `C6_AUDIT_SAMPLE=PASS`".
Defect: the staged `audit compare` never runs or checks `census` over the auditor's files. K4: an auditor candidate file
with `declared_candidate_count=99` / `declared_included_count=88` passes compare (`C6_AUDIT_SAMPLE=PASS`) while the pinned
`census` FAILS the same file ("declared_candidate_count=99 but recomputed 3", `C1_DENOMINATOR_PRINTED=FAIL`).
Exact replacement (code): "`audit compare` first runs the pinned `census` over the auditor's (joined) candidate and
exclusion files and refuses unless `C1_DENOMINATOR_PRINTED=PASS`" — or strike the precondition from the clause and the
consequence paragraph.
Consequence: as staged, an internally inconsistent auditor enumeration can ground a `C6_AUDIT_SAMPLE=PASS` — the
denominator the audit vouches for may not be the denominator its own files describe.

F5. Quote: "**Only then** are the sealed ledgers opened to it; it writes `C6_AUDIT.json`" — the clause orders the auditor's
"own enumeration and re-derivations" printed before any sealed ledger is opened.
Defect: the tool seals only the enumeration. `cmd_audit_seal` hashes the auditor's candidate/exclusion files; no subcommand
seals the re-derivations; `cmd_audit_compare` merely READS the re-derivation file (no digest check anywhere). Re-derivations
written after the auditor has seen the sealed ledgers are indistinguishable from honest ones: `MATCH` can be manufactured,
and with it `C6_AUDIT_SAMPLE=PASS`.
Exact replacement: add `audit seal-rederivation <red.json> <out>` — the custodian records the re-derivation digest after the
selection and BEFORE any sealed ledger is released; `audit compare` refuses with `C6_STAGE_ORDER` on a digest mismatch (the
stage-1 pattern, reused verbatim).
Consequence: as staged, the "strongest statement in the design" rests on the custodian's clock for the exact artefact that
produces MATCH/MISMATCH; the clause's ordering sentence is unenforced for the artefact that matters most.

F6. Quote: "(i) the completeness comparison — every candidate in the sealed ledgers matched to its own enumeration or listed
as unmatched, and every passage in its own enumeration absent from the sealed ledgers listed".
Defect: the code lists only the two INCLUDED-direction asymmetries (sealed-included vs auditor-all; auditor-included vs
sealed-all) plus kind differences on SHARED exclusions. K3: a sealed EXCLUDED passage absent from the auditor's entire
enumeration is silently unlisted and the audit PASSes. Symmetrically, an auditor-EXCLUDED passage the seats never enumerated
is unlisted. "Every candidate in the sealed ledgers … listed as unmatched" is not implemented for excluded rows, in either
direction.
Exact replacement: list all four asymmetries, and state each one's PASS effect — my judgement: sealed-excluded-absent lists
as unmatched and feeds the dispute count; auditor-excluded-absent lists and FAILS like the included direction (a passage the
seats missed entirely is ledger incompleteness whatever the auditor's disposition).
Consequence: as staged, the exclusion-ledger audit — the control that exists so "nothing is hidden by being excluded" — has
a silent hole: a wrongful exclusion the auditor misses (rather than disputes) leaves no trace in `C6_AUDIT.json`.

F7. Quote: "no passage the auditor includes under §1 that both sealed ledgers omit".
Defect: receipt T seals the MERGED ledgers, and the tool compares against the single merged sealed file. A passage exactly
one seat listed that reconciliation dropped is absent from the merged file: the tool FAILs it as an omission although the
clause's literal "both sealed ledgers omit" excludes it. The code is stricter than the words.
Exact replacement: "no passage the auditor includes under §1 that is absent from the sealed (merged) candidate and exclusion
ledgers" — name the actual comparison object.
Consequence: none harmful (the code errs on the strict side), but adopting the clause as written bakes in another
describe-vs-compute mismatch of the kind this lane keeps filing.

F8. Quote: "first enumerates and classifies candidate passages itself from EVERY pinned source … with no access to either
seat's candidate, exclusion, input or outcome ledgers".
Defect: "no access" is enforced only by the dispatch layout, and the candidate does not restate the floor. The stage-1 seal
carries no timestamp and no external receipt (unlike P and T); no staged dispatch inventory, `ACCESS_SHA` or path-list
control exists for the auditor seat; prior exposure through the lane's tally commit is the C4 floor V23 already states for
seats ("It cannot prove a seat has no prior exposure from training or an earlier session").
Exact replacement: add to the clause: "The stage-1 seal fixes the enumeration; it does not prove the enumeration preceded
exposure. That precedence rests on the custodian's dispatch record and is receipted externally (as P and T), and the
auditor's dispatch directory is inventoried and access-proven as the seats' are. Prior exposure cannot be excluded — the
same floor stated for the seats in C4."
Consequence: as written the clause asserts an independence the staged artefacts do not by themselves establish; the honest
strength is "a sealed enumeration the custodian receipted before releasing the ledgers", not "no access".

### Batch preparation

F9. Quote: "§1's inclusion rule is per passage and §2's arithmetic is per claim; neither consults any other text. Therefore
the enumeration of the whole corpus equals the union of the enumerations of any partition of it, PROVIDED every text is in
exactly one batch and no batch cites outside itself. Both provisos are controls, not assumptions".
Defect: the premise is false (§2's IMPORTED rule consults a named source's line in another text — the subject of D1) and the
second proviso is not a control for the ledger (join checks only candidate rows; K6: cross-batch ledger citation passes
`JOIN=PASS`, and the batch session cannot machine-match it — `validate` FAILs "cannot read external value line"). See
section E for the full attack and the required additions (read-only full-corpus match access, or a pinned post-join match
step; join scope extended to ledger records; the auditor-side equivalent under D7).
Exact replacement: "§1's inclusion rule is per passage; §2's arithmetic is per claim; §2's IMPORTED rule consults one named
source line in another manifest text, and that consultation is handled by [the added mechanism], so the union-of-partition
equality holds under it. The provisos — every text in exactly one batch; no candidate or ledger record citing outside its
batch except through [the added mechanism] — are controls, named here."
Consequence: as written, accepting D1 and the batch preparation together yields seats that cannot file the D1 record
whenever borrower and source land in different batches (11/12 of cross-text imports under 12 batches): the seat fails C3 or
improvises out-of-batch reads — the failure mode this preparation exists to eliminate — and an uncontrolled cross-batch
citation channel passes `join` silently.

F10. Quote: "Controls in `r3c2_staged_tests.py` (sha256 `89c0202fc9283233ad349025a67959dad7b532234825ac7db343a69bdfbb165a`),
run 2026-09-06 20:01 KST … `STAGED_TESTS=PASS` (37/37 over the whole staged kit)"; "the pinned-form `census` (staged copy,
sha256 `60a191f36a757c6c15e01f3e778518c8e20935bde464deab3e0d9e65fac082ff`)"; and in the candidate document's own pin table:
"`README_STAGED_UNADOPTED.md` | `2af80608477c59eadcc257962a0b72db6949c80d90d183c30a5508f6cf061899`".
Defect: all stale. The pinned test file is `96c1792085d799a82b6ac488599ea0bc8d8a58a0dc3b3d79cf925f842c2de0c1` (pin sheet
verifies; I re-hashed it); the kit runs 44 controls, not 37 (`controls=44 passed=44 failed=0`); no file hashing `60a191f3…`
exists in the kit or the pin sheet — the census in the staged tests runs inside the STAGED seat tool (`cf42430a…`). The
README on disk hashes to `429edfb956995daec6353698f6b490ffa12f17e57f151d1ce1d0af39b6883f57` (pin sheet verifies), not the
`2af80608…` the candidate's table prints — the candidate packet's own pin table has one stale row.
Exact replacement: both documents cite `r3c2_staged_d1d7/R3C2_STAGED_D1D7.sha256` and print no per-file hashes of their own;
re-print after any re-run (this lane's own rule, stated in the candidate's errata section: "the load-bearing kind of stale
copy").
Consequence: a verifier checking the batch preparation against the pinned kit finds mismatched hashes and cannot tell which
state of the kit was tested — the exact V4-row failure family, present in the packet under review.

F11. Quote: "A later session cannot alter an earlier batch's files because they are not in its directory".
Defect: "cannot" overclaims. The working-directory layout does not deny out-of-directory writes — V23's C4 says exactly this
about the lane ("This is procedural, not enforced by the filesystem: nothing here denies a seat an absolute path"). What the
design has is DETECTION: "`join` refuses any artefact whose digest differs from its seal."
Exact replacement: "A later session is not furnished earlier batches' files; an out-of-directory alteration is detected at
join, which refuses any artefact whose digest differs from its seal — detection, not prevention, the same floor C4 states
for the seats."
Consequence: as written the preparation claims a stronger isolation than the design's own accepted floor; a reader relying
on "cannot" would over-rate what the seal proves.

F12. Quote: "Twelve, not eight: the seat that died was handling sets of eleven; seven or eight texts (roughly 8–10 thousand
non-blank lines) is what one session can read completely and still do the arithmetic."
Defect: the capability claim is evidenced only by one failure at eleven; no successful 7–8-text session is exhibited.
Exact replacement: "The seat that died was handling sets of eleven; this preparation proposes seven or eight per batch —
below the observed failure and itself untested; batch 1's report confirms the size before batch 2 is dispatched."
Consequence: if eight texts also exceeds capacity, the run discovers it mid-census under seal; the first-batch confirmation
makes that failure cheap instead of fatal.

F13. Quote: "The partition changes nothing about what the audit compares."
Defect: true of the compare step (joined vs joined) but silent about the auditor's re-derivation stage: re-classifying an
imported input needs the external source text, which sits in another batch's directory (the F9 defect, audit side).
Exact replacement: "The compare step is unchanged — it runs over the auditor's joined files against the sealed joined files;
the auditor's re-derivation stage reads cross-batch import sources under the same mechanism the seats use (section E)."
Consequence: as written the audit-under-batch claim covers the easy half of the audit and leaves the half that touches the
IMPORTED rule unspecified.

F14. Quote: "For each batch k, each seat is a fresh process of the same engine under the same kernel profile".
Defect: ambiguous between "each seat keeps one engine across its twelve sessions" and "both census seats run the same
engine". D7 requires the auditor "on a different engine from both census seats", so the reading matters.
Exact replacement: "Each seat's twelve sessions run one engine and one kernel profile; the two seats are as V23 specifies,
and the auditor is on a different engine from both."
Consequence: wording only, but the audit's independence clause depends on which reading is intended.

### Candidate document

F15. Quote: "The audit's PASS becomes the strongest statement in the design."
Defect: unmeasurable superlative; no metric ranks it above the two-seat agreement itself.
Exact replacement: "The audit's PASS then rests on an independent enumeration and blind re-derivation rather than on an
anchored review of the seats' lists."
Consequence: none to the mechanism; the sentence as written claims a ranking the design does not define.

F16. Quote (README): "`partition_12_of_89.{json,txt}` — the candidate partition of the real manifest … printed."
Defect: the pin sheet pins only `partition_12_of_89.json`; the printed `.txt` is unpinned.
Exact replacement: pin the `.txt` beside the `.json` or drop the mention.
Consequence: trivial; an unpinned file presented as part of a pinned kit.

## What verified clean (tested, not asserted)

- The pin sheet verifies 6/6, and verifies again after I re-ran the kit — the exhibit regenerates byte-identical
  (deterministic kit).
- `STAGED_TESTS=PASS`, `controls=44 passed=44 failed=0`, run by me. The 13 deletion probes each prove their check is
  load-bearing.
- The real partition recomputes byte-identical: I ran `partition R3C2_CORPUS_MANIFEST.md 12` and compared bytes with the
  pinned `partition_12_of_89.json` — identical (`e8ca431c…`). "A function of the manifest and the number 12 alone" checks out.
- The D7 both-directions PASS predicate, the 10% dispute boundary (strictly above 10% of the sealed included denominator
  fails; at 10% passes, listed and counted), the selection formula `k = min(max(1, ceil(0.20 × N)), R)` with the 64-hex
  external seed, and the stage-order check all match the clause word for word (my K1/K2; kit probes 1–4).
- The counterexample repair is real: my own both-seats-omit case fails and is listed; the reverse direction fails and is
  listed; the deletion probes show the checks are what fail them.
- The D7 stronger-vs-weaker verdict is correct: the weaker version cannot find a both-seats-missed passage by construction.
- The README's claim that the pinned seat tool remains `r3c2_ledger_tools.py` sha256 `230359eb…` checks out against the file.
- The "LESS LIKELY … direction only, no magnitude has been measured" hedge is honest, and "Not validated by anyone yet" is
  accurate — this review is the independent validation that sentence anticipated.

## Rulings requested of the principal, restated as tested

- D1: accept the REVIEW'S wording (safer against a CHOSEN-filed import for the reason in section C); if Tori's wording is
  preferred, the staged validate rule must be re-staged first (F1). Add the first-match tie-break (F2) and state the
  third-text floor (F3).
- D7: accept the stronger version AFTER the clause and the staged tool are brought into agreement on F4–F7 and the floor is
  restated per F8; the re-derivation seal (F5) is the one addition without which the audit's MATCH is custodian-trust, not
  evidence.
- Batch: do not accept as written; the IMPORTED rule breaks the partition argument (section E). The named additions make it
  acceptable, and the rest of the mechanism (partition/seal/join/coverage) tested clean.

Nothing in this review adopts, freezes, installs or runs anything. All fixtures and outputs are mine, under
`r3c2_staged_d1d7/_review_kimi/kimi_work/`; the staged kit, the candidate documents and every other file are untouched.

R3C2_CANDIDATE_REVIEW_kimi — UNADOPTED-REVIEW
