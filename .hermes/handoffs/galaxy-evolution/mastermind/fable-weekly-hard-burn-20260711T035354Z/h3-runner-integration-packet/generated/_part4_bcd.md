
---

## (b) Verbatim-carry rule — prose-phase prompt patch

The prose-phase prompt is assembled in the live runner file (`<S>/run_weekend_journal_sprint.py`, sha256 `b6795c05f3b790cc22644addcf2c42f7da33387d986f683c7193ccf94450efa2`) from two functions: `base_prompt()` (lines 466–486, shared by all reviewer lanes, the analyst, the integrator, and the post-fix referee) and `integrator_prompt()` (lines 669–688, the **single writer lane** — the only lane that edits the TeX, so the only place drift is created). The patch touches both: the shared contract line, and a binding writer-side block.

### (b.1) Exact current text — `base_prompt()` (live lines 466–486, quoted verbatim)

```python
def base_prompt(phase: str, candidate: Path) -> str:
    return f"""Phase: {phase}
Sprint: {SPRINT_ID}
Candidate root: {candidate}

Safety locks:
{chr(10).join('- ' + x for x in SAFETY_LOCKS)}

Real-data rules:
{chr(10).join('- ' + x for x in REAL_DATA_RULES)}

Required review behavior:
- Inspect {candidate / 'provenance/REAL_DATA_SOURCE_CUSTODY.json'} before declaring provenance absent; it inventories real source paths, hashes, and row counts without copying the source data.
- Demand concrete section-level improvements for the flagship and supplement.
- Provide real source identifiers for literature suggestions: DOI, arXiv, ADS bibcode, URL, journal volume/page, or explicit "unverified / do not integrate".
- Preserve exact numeric invariants and association-only boundaries.
- Separate integrity blockers from journal-quality blockers.
- End with exactly one verdict line: JOURNAL_LEVEL_PASS: YES or JOURNAL_LEVEL_PASS: NO.
"""
```

The operative sentence today is the single bullet `- Preserve exact numeric invariants and association-only boundaries.` — cycles 6, 7, 8, and 9 prove it does not communicate "verbatim string carry": writers read it as "keep the values right" and re-derive.

### (b.2) Exact proposed replacement — `base_prompt()`

Replace **only** the bullet `- Preserve exact numeric invariants and association-only boundaries.` with the following two bullets (rest of the function byte-identical):

```
- Numeric verbatim-carry contract: every numeral, interval, percentage, SHA-256, and run-ID string already present in the base package is an opaque string. Carry it character-for-character, including formatting ('8,146' vs '8{,}146', 'S/N$\geq3$' vs 'S/N$\geq$3', '[-1.334,-1.283]' spacing). Never re-derive, re-round, reformat, relocate the referent of, or delete such a string - even when recomputation from the custody artifacts looks arithmetically more correct. If a base numeral looks wrong, STOP and report it in your response; do not fix it inline.
- Preserve association-only boundaries.
```

(ASCII hyphen-minus throughout; the block is inside an f-string — it contains no `{`/`}` so no escaping is needed.)

### (b.3) Exact current text — `integrator_prompt()` role block (live lines 669–688, quoted verbatim)

```python
def integrator_prompt(phase: str, cycle: int, candidate: Path, reports: list[Path]) -> str:
    report_text = []
    for path in reports:
        report_text.append(f"\n\n===== {path.name} =====\n{read_text(path, 40_000)}")
    allowed = "\n".join(f"- {candidate / rel}" for rel in TEX_RELATIVES)
    return base_prompt(phase, candidate) + f"""
Role: single manuscript integrator for cycle {cycle}.

You may edit only:
{allowed}
- candidate-local analysis artifacts under {candidate / 'analysis_extensions'} when needed for provenance references.

The real-data analyst and integrator must not overlap; analyst has already finished or was skipped.
Return a concise final response through the CLI output; do not create a separate response file in the candidate.
Do not add padding merely to hit word/count targets. Refuse absent measurements instead of inventing them.

Reviewer reports:
{''.join(report_text)}
"""
```

### (b.4) Exact proposed replacement — `integrator_prompt()`

Insert the following block into the returned f-string, immediately after the line `Do not add padding merely to hit word/count targets. Refuse absent measurements instead of inventing them.` and before `Reviewer reports:` (rest of the function byte-identical; block contains no `{`/`}`):

```
Numeric verbatim-carry rule (binding; cycles 6-9 all failed audit by violating it):
1. Copy, never re-derive: every numeric string in the base TeX is copied character-for-character. Prose around numbers may change; the numeric strings may not.
2. No re-rounding, ever: do not recompute any number from artifacts, tables, or memory. A re-derived value that differs from the base string is a defect even when arithmetically correct. If a base numeral looks wrong, STOP and report; never fix inline.
3. No deletions or rewordings of numeral occurrences (e.g. '249,917', '24.0\%'): removing or paraphrasing one is a numeric change and is out of scope for a prose phase.
4. Referents are invariant: do not change what a quantitative sentence ranges over (e.g. 'across mass bins' vs 'across the displayed table').
5. New numerals only with provenance: a new number is allowed only if your final response states the custody-inventoried artifact and field it comes from, so it can be registered in the invariant manifest.
6. Self-check before finishing: verify every NUMERIC_INVARIANTS string still appears in the flagship TeX and every SUPPLEMENT_NUMERIC_INVARIANTS string in the supplement TeX, unchanged; if any check fails, restore the exact base string.
```

Rules 1–5 are RCA §5.1–§5.5 verbatim in intent; rule 6 is the writer-side mirror of the audit in section (a). The manifest-based pre-audit gate (RCA §5.6, occurrence-count level, via `INVARIANT_MANIFEST.json` + a check script) sits between writer and audit in the cycle loop — that is rollup follow-up item 3's "manifest into the pre-audit flow" and is orchestration, not prompt text; it needs a `run_cycle`-level hook and is listed in section (d) ordering.

---

## (c) Canon adjudication memo — `-1.283` vs `-1.282` and `2.830` vs `2.831`

**Question.** Cycle-5 canon (and the audit list) carry flagship CI `[-1.334,-1.283]` and supplement cell `2.830`. The custody artifacts give raw `-1.2821399375` (nearest 3-dp `-1.282`) and raw `2.83066` (nearest 3-dp `2.831`). Adopt the artifact-nearest strings, or keep canon?

**Evidence for ADOPTING `-1.282` / `2.831` (from RCA, plus live state):**
- RCA E1/E3: the raw custody values nearest-round to `-1.282` and `2.831`. RCA E2: these are the **only two** canon strings (of 105) that are not nearest-roundings of their own artifacts — every other flagship scalar (`-1.309`←`-1.308887`, `0.0045`←`0.00446`, `0.00021`←`0.000210795`) and neighboring table cells (`2.85057→2.851`, `2.83792→2.838`) are nearest-rounded. Canon's `-1.283` is producible only by floor-toward-−∞; `2.830` is a truncation. Both look like cycle-5 mis-roundings, not choices.
- RCA E4 + live cycles 8: four independent prose cycles (6, 7, 8) re-derived and emitted `-1.282` at the same four locations (cycle 8 also `2.831`) — the re-derivation pressure is deterministic and permanent. Keeping canon means every future prose phase must fight its own arithmetic; adopting nearest makes regeneration converge to canon.
- Directional conservatism: `[-1.334,-1.282]` is the *wider* interval; the current canon upper bound `-1.283` was truncated toward the interval interior, i.e. slightly anti-conservative. Adopting nearest cannot be criticized as strengthening the claim.
- Policy simplicity: one stated convention — "every printed value is the nearest-rounding (half away from zero) of its custody-artifact value at printed precision" — makes all 105 invariants mechanically re-derivable and auditable.

**Evidence for KEEPING `-1.283` / `2.830`:**
- Canon-is-canon (RCA §3.2.1): cycle 5 is the only audited clean base (`integrity_blockers: []`); it anchors every hash, snapshot, receipt, and downstream artifact (P2 comparison candidate and P4 claim candidates quote `[-1.334,-1.283]` verbatim). A canon edit ripples into all of them.
- The difference is scientifically nil (last digit of a bootstrap CI bound; one supplement color cell). Zero reader impact, non-zero operational risk: the change touches 4 flagship locations + 1 supplement cell + audit list + manifest, and a *partial* application recreates the livelock in reverse (writer carries new canon, audit demands old — or vice versa).
- The cleanest possible carry-contract precedent is "numeric strings never change, full stop"; adjudicating even a justified change weakens the rule's teaching value at the exact moment it is being installed.
- With the verbatim-carry prompt patch (b) in place, re-derivation pressure should disappear anyway — the livelock argument loses force *if* the prompt patch works.

**Recommendation: ADOPT `-1.282` / `2.831` (Option B), executed only as the atomic three-surface change below, in the same integrator window as (a)+(b).** Rationale: the keep-side's strongest point (prompt patch may suffice) leaves canon permanently mis-rounded against its own artifacts and dependent on prompt compliance by every future model; the adopt-side fixes the root inconsistency once, is conservative in direction, and the ripple risk is exactly what the atomic checklist eliminates. **Until Duho approves, canon stands:** candidates must reproduce `-1.283`/`2.830` character-for-character, and P2/P4 downstream artifacts correctly quote current canon.

**Atomic-change checklist (three surfaces change together or not at all):**

Surfaces: (S1) base-package manuscript TeX; (S2) runner audit list — `NUMERIC_INVARIANTS` line 109 (+ proposed `SUPPLEMENT_NUMERIC_INVARIANTS`); (S3) `INVARIANT_MANIFEST.json`.

0. Preconditions: written Duho approval of Option B; runner idle (sprint ended or between cycle slots — the running PID does not reload the script, so S2 lands at sprint end / next-sprint seed; do NOT edit mid-sprint expecting live effect).
1. Freeze: record sha256 of S1 (both TeX), S2 (runner script), S3 (manifest).
2. Identify the current clean base package at execution time (today `cycle_05_package`; re-verify with `grep -F -c -- '[-1.334,-1.283]' <flagship.tex>` → 4 and `grep -F -c -- ' 2.830 ' <supplement.tex>` → 1).
3. S1 flagship: replace all 4 occurrences `[-1.334,-1.283]` → `[-1.334,-1.282]` (lines 13/57/65/74: abstract, Table-1 row, `$…$` Fig.-2 caption, conclusion).
4. S1 supplement: line 188 row cell `2.830` → `2.831` (the `11.0--12.5 & 0.02--0.05 & 390 & 0.856 & 0.610 & 2.830 \\` row).
5. S2: in `NUMERIC_INVARIANTS`, `'[-1.334,-1.283]'` → `'[-1.334,-1.282]'`; in the extended lists (section a), update `FLG-ROW-057`'s row string (contains the CI) and `SUP-ROW-188`'s row string (contains `2.830`) to the new cell values.
6. S3: update entries `FLG-CI95` and `FLG-ROW-057` (flagship) and the line-188 table-row entry `SUP-ROW-188` (supplement) to the new exact strings; delete/annotate `known_rounding_anomalies`; add the convention line ("printed values are nearest-roundings, half away from zero, of custody-artifact values at printed precision"); regenerate counts with P1's `tools/build_manifest.py` if preferred.
7. Verify: `tools/derive_audit_extension.py` (this packet) against the edited files → 105/105, 0 problems; grep acceptance: old strings count 0 everywhere, new strings count 4 (flagship CI) and 1 (supplement cell); dry-run `journal_metrics()` on the base → `numeric_invariants_missing: []`.
8. Record new sha256s of S1/S2/S3 beside the step-1 values in the change receipt; downstream note: P2 comparison candidate and P4 claim candidates quote the old CI string — mark them "re-quote from canon at integration" (section d).
9. Rollback (any step fails or any check mismatches): restore S1+S2+S3 from the step-1 snapshot byte-exact, verify hashes match step-1, state PARTIAL-REVERTED in the receipt. Never leave the three surfaces disagreeing.

---

## (d) Integration sequencing

Dependency-ordered; each step is separately gated (rollup: "every item GATED, needs separate Duho approval").

1. **Decide (c) first** — it determines the CI/cell strings that (a)'s lists and (S1) manuscripts carry. A "keep canon" decision costs nothing (lists below already carry current canon); an "adopt" decision folds the checklist in (c) into step 2's window.
2. **One integrator window applies (a) + (b) [+ (c) if adopted] together** at a runner-idle boundary (sprint end / next-sprint seed — the live PID 45665 never reloads the script). (a) and (b) are the gate side and writer side of the same contract: shipping the audit extension without the prompt patch produces hard-fails on every prose phase (cycles 6–9 show base-rate ~4/4); shipping the prompt patch without the audit extension leaves supplement drift (D2/D3 class) invisible. The manifest pre-audit gate (RCA §5.6; `INVARIANT_MANIFEST.json` + count-level checker between writer and audit) belongs to this same window as orchestration work.
3. **Verification artifacts for step 2** are in this packet: paste-ready lists (a.2), one-line metrics change (a.2), exact prompt texts before/after (b), and `tools/derive_audit_extension.py` as the cross-validator (105/105 green precondition for merge).
4. **P2 prior-work comparison candidate — integrates only after the network pass (rollup follow-up item 1) upgrades its leads.** Its own GATE block requires (1) the approved network-verification pass over the `NEEDS_NETWORK_VERIFICATION` ledger entries it cites (N01, N05, … — 39 leads in `SOURCE_LEAD_LEDGER.json`), and (2) a separate integrator approval; bracketed status tags travel with the text until then. Additional dependency introduced by this packet: it quotes `[-1.334,-1.283]` verbatim from cycle-5 canon — if (c) adopts Option B, re-quote its RP-1 numerals from post-adjudication canon before insertion; after insertion, register any adopted external (prior-work) values in the manifest per RCA §5.3. Note: its target blocker (`missing explicit quantitative comparison to prior work`) is a *quality* blocker, so sequencing it late costs pass-rate but not integrity.
5. **Same gating class, listed for completeness:** literature EXT-1..EXT-4 quantitative slots in `INTRODUCTION_LITERATURE_REFERENCE.md` (sha256 verified this burn) also wait on follow-up item 1 + manifest registration; P4 wiki-side candidates are item 4, independent of this packet.
6. **After the first post-integration cycle:** confirm the audit JSON shows `numeric_invariants_missing: []` with the extended lists, and that the integrator's self-check (b.4 rule 6) appears in its lane report; then the manifest gate's occurrence-level counts become the promotion criterion, per RCA §5.6.

Sequencing summary: **(c) decision → [(a)+(b)(+c-apply)] one atomic runner-side window → item-1 network pass → P2 candidate + EXT slots (with manifest registration) → subsequent cycles under the full contract.**

---

Prepared offline by Fable lane H3; no file outside `h3-runner-integration-packet/` was created or modified; the runner tree, candidates, manuscript, audit config, and repo were read-only throughout. Custody, hashes, and poll log: `H3_RECEIPT.md`.

FABLE_HARD_BURN_H3_INTEGRATION_PACKET_20260711T035354Z
