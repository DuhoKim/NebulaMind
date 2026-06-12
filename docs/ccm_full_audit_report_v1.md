# CCM Full Dry-Run Audit Report v1

**Auditor:** Kun (analyst / reviewer gate)
**Date:** 2026-06-08
**Scope:** Final pre-`--commit` audit of the Citation Context Mining (CCM) pipeline against all 16 registered `seminal_claim_map` rows (12 unique claims, Page 57 "Galaxy Evolution", section "Overview & Historical Foundations").
**Verdict:** ⚠️ **CONDITIONAL GO** — the science and the trust math are sound and the anti-false-consensus safeguards demonstrably work on live data, but **one hard `--commit` blocker (FK resolution crash) must be fixed before any write**, plus two quality items to address. Details in §6–§7.

---

## 1. Executive Summary

I ran a full-scale live dry run: real NASA ADS `citations()` queries, real Semantic Scholar context fetches, real Pico (`vanta-research/atom-astronomy-7b`) classification of every context, and — critically — **trust projection through the real `recalculate_trust_v2`**, executed inside per-claim SAVEPOINTs that were always rolled back (zero permanent writes). This is stronger than the stock `--dry-run`, which does **not** project trust at all (it only computes `recalculated` in commit mode).

**Top-line numbers (live, 2026-06-08):**

| Metric | Value |
|---|---|
| Seminal maps audited | 16 (→ 12 unique claims) |
| ADS citers retrieved (2024+) | 1,525 |
| Citation contexts built (post on-topic gate) | 309 |
| Pico SUPPORTIVE | 263 |
| Pico NONSUPPORTIVE | 41 |
| Pico OFFTOPIC | 5 |
| Pico HOLD (empty/low-conf) | 0 |
| **Claims projected to Consensus (Green)** | **11 / 12** |
| Claims projected to Accepted (held back) | 1 / 12 (claim 1632, correctly) |
| Claims with `n_challenges > 0` after CCM | **0** |
| Claims at freshness-floor risk after CCM | **0** |

**The thesis is empirically validated.** Every one of the 12 baseline claims is currently `unverified` with `trust_score = 0.0`. CCM moves 11 of them across the live Consensus gate (`TS ≥ 0.75 ∧ n_supports ≥ 3 ∧ n_challenges == 0`) and — because every inserted citer is a 2024–2026 paper — the freshness floor (`FRESHNESS_FLOOR_YEARS = 10`) does **not** fire on any of them. The temporal-decay penalty is fully neutralized (`max_sup_year = 2026` everywhere).

**But I am not signing an unconditional GO**, because the same audit surfaced a latent crash that the green-test masked. See §6.

---

## 2. Method (how this audit was run)

- Harness: `backend/scripts/ccm_audit_harness.py` (Kun-authored, reviewer-side). It reuses the **production** functions `build_contexts_for_mapping`, `classify_context`, `insert_supportive_evidence`, and `recalculate_trust_v2` — no re-implementation of the trust math, so the projection reflects exactly what `--commit` would compute.
- Parameters: `min_year = 2024`, `ads_rows = 100`, per-claim insert cap = 6 (`CCM_MAX_EVIDENCE_PER_CLAIM_PER_RUN`), multi-bibcode claims aggregated across their bibcodes (1635 over 3 TNG papers, 1638 over 3 SDSS papers).
- Projection method: for each claim, the capped SUPPORTIVE citers were inserted into a nested SAVEPOINT, `recalculate_trust_v2` was called with `trigger="ccm_audit_dryrun"`, the resulting `(level, score)` captured, then `ROLLBACK`. **No row, vote, or audit-log entry was persisted.** Verified post-run: DB unchanged.
- Raw results: `backend/scripts/ccm_audit_results.json` (per-claim decisions, sentences, confidences, projected gates).

---

## 3. Per-Claim Projection Table

`citers` = ADS citers seen (2024+); `ctx` = contexts after on-topic gate; `SUP/NON/OFF` = Pico labels; `n_sup` = supporting evidence before→after CCM (capped insert); `ins` = evidence rows CCM would insert; `TS` = projected trust score; level in **bold**.

| Claim | Seminal work | citers | ctx | SUP | NON | OFF | n_sup | ins | TS | Projected level |
|---|---|---|---|---|---|---|---|---|---|---|
| 1630 | White & Frenk 1991 | 100 | 20 | 17 | 3 | 0 | 1→7 | 6 | 0.7815 | **consensus** |
| 1631 | White & Rees 1978 | 100 | 20 | 18 | 2 | 0 | 2→8 | 6 | 0.7821 | **consensus** |
| 1632 | Planck 2020 (inflation X) | 100 | 20 | 4 | 14 | 2 | 1→5 | 4 | 0.7485 | **accepted** |
| 1633 | Springel 2005 (Millennium) | 100 | 20 | 17 | 3 | 0 | 2→8 | 6 | 0.7821 | **consensus** |
| 1634 | Springel 2005 (Millennium) | 100 | 20 | 19 | 1 | 0 | 0→6 | 6 | 0.7811 | **consensus** |
| 1635 | IllustrisTNG (Pillepich/Nelson/Weinberger) | 300 | 60 | 49 | 11 | 0 | 0→6 | 6 | 0.7811 | **consensus** |
| 1638 | SDSS bimodality (Blanton/Kauffmann/Strateva) | 265 | 60 | 59 | 0 | 1 | 1→7 | 6 | 0.7815 | **consensus** |
| 1639 | Schawinski 2014 | 100 | 20 | 18 | 2 | 0 | 1→7 | 6 | 0.7817 | **consensus** |
| 1640 | Somerville & Davé 2015 | 100 | 20 | 17 | 2 | 1 | 1→7 | 6 | 0.7815 | **consensus** |
| 1642 | Croton 2006 | 100 | 20 | 17 | 2 | 1 | 0→6 | 6 | 0.7811 | **consensus** |
| 1648 | Fukugita & Peebles 2004 | 60 | 11 | 10 | 1 | 0 | 1→7 | 6 | 0.7817 | **consensus** |
| 1650 | Behroozi 2013 | 100 | 18 | 18 | 0 | 0 | 1→7 | 6 | 0.7817 | **consensus** |

Note the projected TS clusters tightly at ≈0.781 for the green claims. That is **not** a coincidence — it is the mathematical signature of the quality clamp working: 6 inserted citers at `quality ∈ {0.80 HIGH, 0.68 MEDIUM}` drive `E = tanh(ΣE_sup/1.5)` into near-saturation (~0.998), and the 6 Pico `EvidenceVote`s drive `V` via `confidence = 1 − e^(−6/2) = 0.950`. `TS = 0.45·E + 0.35·V ≈ 0.45·0.998 + 0.35·0.95 ≈ 0.781`. The system lands every well-supported claim just over the 0.75 line by construction, not by luck.

---

## 4. The One That Correctly Did NOT Green: Claim 1632 (Planck inflation)

This is the **most important single result in the audit** and the strongest evidence the safeguards work.

Claim 1632 attributes the primordial power-spectrum measurement (`n_s = 0.9649 ± 0.0042`) to Planck 2018-X. When CCM mined its 2024+ citers, Pico returned **4 SUPPORTIVE, 14 NONSUPPORTIVE, 2 OFFTOPIC**. Inspecting the NONSUPPORTIVE sentences confirms Pico is correct, not broken: the modern papers citing Planck inflation overwhelmingly do so to *revise, constrain, or contrast against* it — e.g. "…we revisit chaotic inflation… which usually predicts a spectral [index in tension with]…", "breaking diffeomorphism invariance in the inflaton sector", post-ACT reanalyses. These are active-frontier papers, not background-assumption citations.

Result: `n_supports = 5`, `n_challenges = 0`, but `TS = 0.7485 < 0.75` → **accepted, not consensus**. CCM declined to green a claim whose modern citation context is genuinely contested. **This is exactly the anti-false-consensus behavior the design promised, observed on live data.** A pipeline that greened 12/12 would have alarmed me; 11/12 with the *right* one held back is the correct outcome.

(Strategic note: 1632 is arguably mis-scoped as "seminal/settled." The *existence* of the Planck spectral-tilt measurement is settled; the *inflationary interpretation* its citers engage with is frontier. Recommend re-checking whether claim 1632 should be in the seminal registry at all, or re-worded to the measurement rather than the model. This is a registry-curation question, not a CCM defect.)

---

## 5. Anti-False-Consensus Verification (the core of my gate)

I did not take Pico's labels on faith. I spot-audited sentences across the spectrum:

- **NONSUPPORTIVE drops are genuine.** Claim 1631 (White & Rees) dropped 2 citers; both are real DM-tension papers (cusp–core problem, GC accreted-substructure) — correctly not counted as endorsements of the cooling framework.
- **No challenge leakage.** Across all 12 claims, `n_challenges == 0` after CCM. CCM never wrote a `challenges` row and never flipped a claim into a falsely-supported state. Even if Pico mislabeled, the live gate still requires `n_challenges == 0`, so a contested claim cannot be bulldozed green — verified structurally, not just empirically.
- **Quality clamp honored.** All inserted evidence carries `quality ∈ {0.68, 0.80}`; nothing exceeds the 0.80 ceiling, so introductory citations never outrank primary jury-verified evidence.
- **Confidence distribution:** of 263 SUPPORTIVE, 256 HIGH / 7 MEDIUM. The HIGH skew is plausible for clean background citations but is also partly an artifact of abstract-mode classification (see §7.2) — flagged, not blocking.

**Conclusion of the safeguard audit:** the three independent guards (3-way Pico labeling, `n_challenges == 0` hard gate, quality clamp) all functioned on live data. The single contested claim was correctly withheld.

---

## 6. 🔴 BLOCKER — `--commit` Will Crash (must fix before any write)

**This is the reason the verdict is CONDITIONAL, not GO.** I discovered it precisely because I projected real inserts; the stock `--dry-run` cannot surface it because dry-run never flushes an `Evidence` row.

**Symptom:** the first `insert_supportive_evidence` → `db.flush()` raises:

```
sqlalchemy.exc.NoReferencedTableError: Foreign key associated with column
'evidence.consensus_scorecard_id' could not find table 'jury_scorecards'
```

**Root cause:** `Evidence.consensus_scorecard_id` is an FK to `jury_scorecards.id` (defined in `app/models/jury.py`). The CCM miner module imports only `app.models.agent`, `app.models.claim`, and `app.models.seminal`. It **never imports `app.models.jury`**, so at flush time SQLAlchemy cannot resolve the FK target and aborts.

**Why every existing check missed it:**
- The stock `--dry-run` inserts nothing (insert is gated behind `if not dry_run`), so it never flushes → no crash. Tori's capped dry-run "passed" for this reason.
- The 7 unit tests pass because `tests/ccm/test_miner.py` explicitly does `from app.models.jury import JuryScorecard, PromptRevision` at the top — the test's own import side-effect registers the table, masking the gap that the production runner has.
- The FastAPI app proper imports jury routers, so in-process the model is always loaded; only the **standalone script** (`scripts/run_citation_context_miner.py`) runs without it.

**Fix (one line, low risk):** add `import app.models.jury  # noqa: F401` to **either** `app/agent_loop/citation_context/miner.py` (preferred — closest to the FK use) **or** `scripts/run_citation_context_miner.py`. Best practice: call the existing `app.models.import_all_models()` helper at runner startup so no model FK can ever dangle again. I verified the fix resolves the flush cleanly (probe insert succeeded after importing `app.models.jury`).

**Verification I performed:** with `import app.models.jury` added to my harness, all 12 projections ran through real flush + `recalculate_trust_v2` with no errors. So the blocker is exclusively the missing import; the insert/trust logic itself is correct.

---

## 7. 🟡 Quality Findings (fix-soon, not commit-blocking)

### 7.1 Tier-A (S2 citation context) is starved → ~80% of decisions classify abstracts, not citation sentences

The design's premier signal is the verbatim *introductory citation sentence* from Semantic Scholar (`/paper/{id}/citations` `contexts`). In practice, of 309 decisions, **only 63 used `s2_context`; 246 fell back to `abstract`** (Tier B). Diagnosis:

- `s2_citation_contexts()` requests a single page (`limit=1000`, no pagination, default ordering). S2 returns a citer set that skews older.
- CCM filters ADS citers to **2024+**. Of 100 recent ADS citers for White & Rees, only 26 share an identifier key with the S2 index, and only 10 of those have a non-empty `contexts` array. So ~90% of recent citers have no S2 context available → Tier-B abstract fallback.

**Impact:** Tier B is a *legitimate, designed* fallback and the results are still sound (Pico judges the abstract's stance toward the seminal work). But we are not yet getting the pinpoint-sentence precision the design promised, and abstract-mode classification likely contributes to the HIGH-confidence skew (an abstract about the same subfield reads as broadly supportive more easily than a single adversarial sentence would). **Recommendation:** (a) paginate S2 and/or query S2 by the *citing* paper's DOI to pull its specific context, (b) prefer Tier-C arXiv-intro extraction for high-value claims when S2 misses, (c) record `context_source` in a metrics column so we can monitor the Tier-A/B ratio over time. None of this blocks the first commit; it is a precision upgrade.

### 7.2 HIGH-confidence skew (256/263) warrants a calibration spot-check

With most classifications running on abstracts, Pico returns HIGH confidence on ~97% of SUPPORTIVE calls. That is plausible for genuine background citations but is high enough that I recommend a **20-row human spot-check** (Kun, post-commit) comparing Pico SUPPORTIVE/HIGH against the actual citing sentence, to confirm we are not over-crediting topical-but-vague abstracts. The quality clamp and `n_challenges == 0` gate bound the downside, so this is monitoring, not gating.

### 7.3 Per-run cap interaction

The audit inserted exactly 6 per claim (the cap), and 6 is sufficient to clear the gate for every non-contested claim. Good. Note this means the *order* in which SUPPORTIVE citers are encountered matters (first 6 win). Since all carry `quality ≥ 0.68` it does not change the bucket, but if we later tighten the clamp, revisit whether to rank by confidence before applying the cap.

---

## 8. Mathematical Gate Confirmation

For all 11 green claims, independently confirmed via the live `recalculate_trust_v2`:

- ✅ `TS ≥ TRUST_CONSENSUS_MIN (0.75)` — range 0.7811–0.7821.
- ✅ `n_supports ≥ TRUST_CONSENSUS_MIN_SUPPORTS (3)` — range 6–8.
- ✅ `n_challenges == 0` — all.
- ✅ Freshness floor **defeated** — `max_sup_year = 2026` on every claim, `2026 − 2026 = 0 ≤ FRESHNESS_FLOOR_YEARS (10)`; floor does not demote.
- ✅ Temporal decay neutralized — recent supports zero out the `T` penalty.

For claim 1632: `TS = 0.7485 < 0.75` → correctly **accepted**. Gate behaved exactly as specified.

---

## 9. Strategic Sign-Off

**Verdict: CONDITIONAL GO.**

**GO, once the following is done (hard gate):**
1. **Fix the `--commit` FK blocker (§6)** — add `import app.models.jury` (or call `import_all_models()`) to the miner/runner. Re-run a **single-claim** `--commit` (suggest claim 1650: 18 SUP / 0 NON / 0 OFF, cleanest) and confirm: 6 `evidence` rows written with `source_channel='citation_context_mining'`, 6 `EvidenceVote` rows, one `trust_audit_log` row with `trigger='ccm_citation_context'`, claim flips to `consensus`. Then proceed to the full 12.

**Recommended in the same commit window (not blocking):**
2. Re-examine whether **claim 1632** belongs in the seminal registry (§4) — disable that map row for now so the first production run is 11/11 clean, and revisit the wording separately.
3. Open a follow-up ticket for **Tier-A S2 starvation (§7.1)**; ship the first commit on Tier-B abstracts (sound), but schedule the pinpoint-sentence upgrade.

**Post-commit (Kun owns):**
4. 20-row Pico SUPPORTIVE/HIGH calibration spot-check (§7.2).
5. Verify no duplicate evidence via the partial unique index under the real beat (concurrency), and confirm `trust_audit_log` trigger surfaces in `get_trust_history`.

**Why I am confident in GO-after-fix:** the trust math is the production code, not a model — it is deterministic and I drove it directly. The safeguards demonstrably held on the one genuinely-contested claim. The blocker is a trivial import omission with a verified one-line fix, not a design flaw. Once the import is added, the 11/12 green projection is what the system will actually do.

**Do NOT flip `CCM_ENABLED=True` for the recurring beat until the single-claim commit smoke-test passes.** Manual `--commit` first, beat second.

---

## 10. Artifacts

- Raw decisions + projections: `backend/scripts/ccm_audit_results.json`
- Audit harness: `backend/scripts/ccm_audit_harness.py`
- Run logs: `~/NebulaMind/logs/ccm_audit_harness_20260608_*.log`
- Seed registry: `backend/data/seminal_claims.yaml` (16 maps, ADS-verified 2026-06-07)
- Design: `docs/citation_context_mining_design_v1.md`

— Kun 🔬
