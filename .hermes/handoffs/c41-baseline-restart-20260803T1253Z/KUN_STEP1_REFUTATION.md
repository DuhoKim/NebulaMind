# KUN STEP-1 REFUTATION — C41 corpus protocol + filter + selection

Lane: `c41-baseline-restart-20260803T1253Z`
Reviewer: Kun (Kimi K3 via Nous). Date: 2026-08-03 ~23:20 KST → 2026-08-04 ~00:10 KST.
Target: Tori's `STEP1_CORPUS_PROTOCOL.md` (`C41_STEP1_V1`), `step1_filter.py`, `SELECTION_INCLUDED.json` (180), `SELECTION_EXCLUDED.json` (11 classes), `SELECTION_SHAS.txt`, `TORI_STEP1_REPORT.md`. Ground: frozen question (sha 9ac5ca1f…, mode 0444), engine inputs.

## VERDICT: SEALED_WITH_PATCHES

The protocol is conclusion-blind by construction, deterministic, byte-reproducible, and the partition arithmetic is exact. My decoys — real C41 members chosen to tempt a motivated selector — were retained whenever they carried axis signal regardless of which side of the expected map outcome they cut, and the two that fell did so on conclusion-blind rules (capacity cut in open rank order). The filter has NO kill-switch through which a conclusion-aware exclusion could be smuggled: exclusion requires firing one of 11 named metadata rules, all verifiable per-record in the published JSON. The patches below are fidelity/disclosure items, none of which change tonight's 180.

---

## Attack 1 — Determinism: PASS

- Re-ran `python3 step1_filter.py` in the lane (the script hard-fails from other directories by design — `REPO_ROOT = parents[3]`, so my `_tmp_kun_rerun/` copy correctly refused to run rather than improvise; that fail-closed behavior is itself verified).
- Second in-lane run: both selection JSONs **byte-identical** (`diff` empty); shas match `SELECTION_SHAS.txt` (`4a0ba6e7…` included, `1496765f…` excluded) — the same values Tori receipted. Outputs are runtime-free; ordering is a total order (priority → score → year → cites → identity string), so set-iteration nondeterminism cannot leak in.
- All 11 input-manifest sha pins in the outputs re-verified against the live files: 11/11 OK, including `frozen_question` 9ac5ca1f… and the 420MB base corpus e5a91e5f… (matches my earlier audits' pins — the input state is the same one tonight's other lanes used).

## Attack 2 — Rules-vs-outputs fidelity: PASS with one nit

- All 11 protocol rule classes exist in code (`RULE_TEXT`) and the classification chain implements them in the protocol's own precedence (DUPLICATE pre-loop, then MALFORMED → UNSUPPORTED → LRD → INSTRUMENT → NAMED_TOPIC → NO_AXIS → NO_HIGH_Z; caps REVIEW → ANCHOR → CAPACITY in rank order). First-firing rule per record; every excluded record in the JSON carries its class; no record appears in two classes; 180 + 1,137 = 1,317 exactly; ranks 1–180 sequential; included identities unique; no `exclusion_rule` leaks into included records.
- Exclusion counts match Tori's report table exactly (LRD 41, instrument 5, named-topic 7, no-axis 151, no-high-z 280, anchor-cap 75, capacity 578, caps 0).
- NIT (N1): protocol rule 9 says the review cap binds "beyond the first 24 reviews **encountered in deterministic rank order**"; the code increments the counter only on INCLUDED reviews (a review consumed by the earlier anchor cap would not consume a review slot). Same outcome tonight (9 review-flagged, 0 included), but the prose and code define the counter differently. One-line patch.
- The strict-lexicon copy is verbatim-faithful to `rank_frontiers_v3.py` (STRICT_TERMS identical, physics-tension strip regex character-identical). The dispersion lexicon is a proper subset snapshot of `nm_dispersion_v2.py`'s registry restricted to axis-relevant quantities — and the filter hard-fails if `dispersion_v2.json` lacks verdicts for any of the 9 relevant quantities (fail-closed, verified in code path `load_direct_measurements`).

## Attack 3 — DECOY TEST: PASS (7 real decoys + 7 synthetic)

Real C41 members I selected from the corpus myself, each designed to tempt a conclusion-aware selector:

| Decoy | Bibcode | Why a motivated selector wants it gone (or kept) | Fate | Rule/ Rank | Verdict |
|---|---|---|---|---|---|
| D1 | 2024JCAP...07..078C | Feedback-regulated SF+ionizing modeling — cuts AGAINST feedback-free-efficiency excitement on Axis 1 | INCLUDED | rank 125, p2 (strict lexicon) | rule-blind keep |
| D2 | 2025A&A...696A..87C | z=14 luminous galaxy w/ feedback + low gas fraction — complicates the "too massive too early" narrative | INCLUDED | rank 171, p1 | rule-blind keep |
| D2b | 2025ApJ...988...73L | Efficient ionizers with LOW Hβ+[OIII] EW — cuts the EW→ionizing proxy the map will rely on | INCLUDED | rank 102, p2 | rule-blind keep |
| D4 | 2026PASA...43...60H | 0-citation paper reporting CONSISTENT UV/optical metallicities — anti-tension, prestige-tempting to drop | INCLUDED | rank 128, p2 | rule-blind keep |
| D5 | 2025OJAp....8E.171M | "Beyond No No Tension: JWST z>10 push sims to the limit" — contrarian framing either side could fear | INCLUDED | rank 136, p2 | rule-blind keep |
| D1b | 2023MNRAS.526.1324Q | "Implications of z≳12 JWST galaxies" (34 cites) — a selector curating narrative might force this in | EXCLUDED | CAPACITY_BELOW_TOP_180, p1 score 0.7360 vs cut 0.8458 | conclusion-blind cut in open rank order |
| D3 | 2025ApJ...991..217T | High-ionization lines at high-z, LRD-flagged, 48 cites — drama-keeping temptation | EXCLUDED | CAPACITY (p0; passed LRD rule on strong ionizing hit, then lost on rank) | conclusion-blind cut |

Key structural point: the two excluded decoys fell at the CAPACITY rule, which sorts by (priority, fixed score) computed from year/citations/review-flag only — no textual judgment of conclusions exists anywhere in the score. There is no exclusion path in the code that can see a conclusion.

Synthetic decoys through `classify_candidate` (attacking rule conclusion-blindness directly):
- S1 "Feedback-free starbursts RULED OUT at z=8" → eligible, p2. S2 "f_esc consistent with ZERO at z>7" → eligible, p1. (Anti-narrative conclusions survive.)
- S3 pure LRD-nature ("LRDs are obscured AGN", no axis content) → `LRD_AGN_OUTSIDE_THREE_AXES`, with and without a z marker. S4 same title + one axis-bearing sentence (AGN contamination biases bright-end UVLF/ionizing budgets) → eligible. The LRD boundary fires on metadata content, not on the word "LRD".
- S6 900-cite irrelevant cosmology paper → `NO_THREE_AXIS_SIGNAL` (prestige cannot buy entry). S7 mergers-as-topic → NAMED_TOPIC. S8 instrument-only → INSTRUMENT. S8b instrument+completeness+axis → eligible (the documented exception works). S9 cosmic-noon quenching → NAMED_TOPIC.

## Attack 4 — Ordering/weights/caps: PASS with one disclosure patch

- Priority ladder implements "contested-measurement-first": 58 p4 (direct contested-quantity measurement) + 10 p3 + 97 p2 + 15 p1 + 0 p0 included; the capacity cut falls entirely inside p1/p0 (578 excluded: 433 p1, 145 p0; **zero p≥2 records lost to capacity** — the contested core cannot be crowded out by recency noise). The boundary is clean: last included p1 score 0.8458, first excluded p1 0.8405.
- Weights match the plan: 0.75 recency / 0.23 log-cite / 0.02 review, exact code constants; missing delta citations = 0 not guessed (verified: the one included delta, arxiv:2607.16404, the variable-IMF simulations paper — directly on-axis for the FFE/burstiness battleground — ranked in on its strict-lexicon p2 despite zero citations).
- Review cap (24) never fired (0 reviews included; 9 flagged, all lost on merit). No distortion.
- FINDING F1 (disclosure patch): the calibration-anchor cap (8) DID distort within the anchor class: 75 anchors capped out, including 7 with p2 strict-tension signal (e.g., "Strongly Inverted Metallicity Gradients at z~2 — 'cannot explain'", 2019; "Local ΣSFR–metallicity relation — 'discrepan'", 2020). Meanwhile 9 lower-ranked p2 non-anchors sit in the 180. The protocol's own text discloses the cap mechanism ("beyond the first eight such records in deterministic rank order") — so this is not hidden — but it does NOT disclose the consequence: the cap ranks anchors against each other, not against the whole pool, so a capped class trades slots with strictly-lower-ranked non-class records. Given the frozen question makes calibration comparability an explicit Axis-2 sub-question, the trade deserves one sentence in the protocol and in Tori's report. Not a rule change; a disclosure.
- Included anchors are all Te/direct-method calibration lineage (ranks 30–57) — sensible; the cap did its stated job (8 = 4.4% of 180).

## Attack 5 — LRD boundary: PASS (implementation is the frozen rule, with one inspected approximation)

- Rule as implemented: LRD/AGN-tagged record is IN iff it carries a STRONG axis hit (chemical/ionizing always strong; formation strong only via efficiency/regulation/feedback/burstiness/IMF/UVLF/bright-end terms). That IS the frozen question's "in only as bearing on the three axes; nature not a fourth axis" — bearing is operationalized as strong-axis lexicon, declared in the protocol before titles.
- All 20 included LRD/AGN-tagged records have strong hits (verified individually — e.g. rank 12 N-emitters, rank 2 JADES luminous-galaxy enrichment).
- 41 excluded: 26 with weak formation-only hits, 15 with no axis hit. I title-inspected all 41 for axis-bearing leaks: 37 are genuinely nature/survey/misc; 4 title-suspicious (two UVLF papers at z=0.4–1.2 — below z≳6 scope anyway; one "Seven Wonders of Cosmic Dawn … galaxies and AGN at z≃9–11" — no strong hit because its abstract apparently names abundance/high-abundance rather than the strong lexicon; one SMUVS z~4–5 starburst paper — below z scope). APPROXIMATION (F2): "bearing" = lexicon strength, so an LRD paper whose axis-bearing is expressed without the strong vocabulary (the "Seven Wonders" case, which bears on bright-end abundance at z 9–11) is excluded. This is the declared price of rule-decided-not-judgment selection, it errs in the conservative direction (drops rather than admits), and it is disclosed by construction. Acceptable; record it as a known recall limit for Step 2's fulltext stage to re-admit through the documented door if the map needs it.

## Attack 6 — Peek-log honesty: PASS (no evidence of peek-dependent rules)

- Every rule is derivable from declared pre-titles knowledge: the frozen question (axes, LRD clause, z≳6), field schemas, source-code lexicons (STRICT_TERMS copied verbatim from engine code; dispersion registry snapshot), and aggregate counts (1,317 universe; 83 anchor-class candidates → cap 8 ≈ 10%; 24/180 = 13.3% arithmetic checks out exactly).
- No rule references any specific paper, author, venue, or result. The caps' numbers are round arithmetic of the 180 ceiling, not tuned to specific records (I checked: no cap sits at a value that conveniently excludes a specific named paper — the anchor boundary at 8 falls mid-class of 83).
- The disclosed incidental exposure (the plan quoting one example title) is honestly logged and could not have shaped any rule (no rule names it).

## Findings ranked

- F1 (LOW-MEDIUM, disclosure): anchor-cap slot-trading consequence undisclosed (Attack 4). Patch: one sentence in protocol + report.
- F2 (LOW, known-limit): LRD boundary is recall-limited by lexicon strength (Attack 5); conservative direction; note for Step 2.
- N1 (NIT): review-cap counter definition prose-vs-code (Attack 2). One-line patch.
- Everything else: attacks failed (see per-attack PASS).

## Failed attacks (for the record)

Tried and failed to find: nondeterminism (byte-identical rerun); unnamed exclusions or partition leaks (none — exact 1,317 cover); conclusion-aware exclusion paths (none exist in code); prestige/citation capture (900-cite irrelevant synthetic excluded; 0-cite anti-tension decoy included on merit); priority-system crowding (zero p≥2 lost to capacity); review-cap distortion (never fired); peek-derived rules (none derivable only from record-level knowledge); frozen-question tampering (sha re-verified, mode 0444 held).

## Evidence ledger

Commands/computations (all read-only on inputs; writes only `_tmp_kun_*` in this lane):
- `python3 step1_filter.py` twice in-lane (second run 3.49s) + `diff` of both JSONs vs saved copies → byte-identical; `shasum -a 256` vs `SELECTION_SHAS.txt` → match; attempted run from `_tmp_kun_rerun/` copy → correctly fail-closed on path layout.
- Input-manifest re-verification: recomputed sha256 of all 11 pinned files → 11/11 OK.
- Partition audit (python): counts, ranks, cross-class duplication, identity uniqueness, field leaks.
- Decoy selection: streamed base corpus (read-only), keyword-scanned C41 member titles/abstracts to pick 7 real decoys; fates looked up in published JSONs; boundary stats for the 2 excluded decoys.
- Synthetic decoys: `classify_candidate` imported from `step1_filter.py` (read-only import; module loads inputs but writes nothing on import), 9 synthetic records (S1–S9) classified.
- Full code read of `step1_filter.py` (861 lines); regex fidelity checks vs `rank_frontiers_v3.py` (verbatim); protocol-vs-code rule-by-rule comparison; cap-consequence analysis (anchor class: 75 capped incl. 7 p2; boundary scores; review-flag census: 9 flagged/0 included/5 capacity).
- Lane state preserved: Tori's outputs untouched (shas unchanged after my rerun — verified post-hoc: `4a0ba6e7…`/`1496765f…` still match `SELECTION_SHAS.txt`).

Temps: `_tmp_kun_rerun/` contains only the saved pre-rerun copies + the non-runnable duplicate script/question/protocol (kept as evidence of the fail-closed path check).

## Uncertainties

- The 4 title-suspicious LRD exclusions (F2) were judged from titles/flags only, within my own brief's allowance for decoy selection; I did not open full texts — a Step-2 fulltext pass is the right place to test recall, not Step 1.
- I verified the dispersion verdict strings the filter consumed ("contested"/"mild" per quantity) but not the scientific correctness of those verdicts themselves — that is upstream machinery (`nm_dispersion_v2.py`), out of this refutation's scope.

---

KUN_C41_STEP1_REFUTATION_COMPLETE_20260803
