# K4 — FROZEN PRE-REGISTRATION: does a genuine causal boundary in the TRANSFER physics move the large-angle CMB statistic?

**Tori, 2026-09-04 13:19 KST. Version 1. FROZEN pending the fresh referee gate. ORDERED by Duho ("k4", relayed by Blanc
2026-09-04 13:15 KST).**

Predecessor: `K4_BOUNDARY_TRANSFER_PREREG_DRAFT_20260903.md` (DRAFT — NOT ORDERED), gated `PREREG_SOUND_WITH_REPAIRS`
2026-09-03 20:20 KST (`K4_DRAFT_GATE_agy.md`); its four repairs are applied and were re-verified clause by clause on
2026-09-04 09:58 KST (`ℓ ≤ 30` replaced by an `ℓ_max` deferred to a receipted pin in three places; the C1 percentile
receipt corrected from synthesis L82–83 to L96–97, re-verified against the source). This version is the draft plus the
requirements of Duho's order. **No derivation has been run, no Planck pixel has been touched under this document.**

Nothing below may be revised once the gate returns; a defect found later is an amendment with its own record.

---

## 0. What this is for

`PROGRAM_A_FREEDOM_MAP_20260902.md` closed topic (A) with the cutoff amplitude provably free, and recorded one
residual, verbatim at its **L174–177**: every row assumed "standard infinite-volume ΛCDM transfer physics with only the
primordial spectrum modified", and "a genuine causal boundary could alter the mode structure, projection, or evolution
themselves, and no receipt here constrains that."

K2 now supplies a boundary that is derived rather than posited. **This step imposes it on the PERTURBATIONS and asks
whether the large-angle statistic moves.**

## 1. The input we stand on, named exactly, with its failure mode

**K4 stands on one K2 cell: the B1 comoving timelike boundary at `k = 0`, `Λ = 0`, class `J_SMOOTH_EXPANDING` — entry
56's own cell** (`K2_RESULT_20260903.md` §2, row 1; mass relation `M = 43π χ 3 ρ0` [sic] at entry 56 `gaztanaga_mass_mnras_clean.txt` **L143**
(the pinned text is OCR: it renders the fraction 4/3 as `43` and the cube as a trailing ` 3`; the relation is the
standard `M = (4/3)π χ*³ ρ₀`, and K2 pinned the same line for the same relation)). It also uses K2's B3 theorem (`K2_RESULT_20260903.md` §3.1): a boundary with
no shell exists **iff** it is comoving, so the comoving edge is not one choice among many — it is the only shell-free
option, which is what makes the perturbed junction well posed.

**If that K2 class is later narrowed, K4 fails with it, and how it fails is stated now:**

- If B1 `k=0, Λ=0` were narrowed away from `J_SMOOTH_EXPANDING` (a shell required at the comoving edge), then the
  perturbed junction conditions of §3 are not the Darmois conditions and **every class filed under this document is
  void**; K4 would be re-preregistered against whatever junction replaced it, not patched.
- If the B3 theorem were narrowed (a shell-free non-comoving boundary shown to exist), K4's classes **survive for the
  comoving cell** but lose their claim to be the only boundary; the record would then say the result is conditional on
  comovingness rather than derived for all shell-free boundaries.
- K2's own stated limits (dust only, exact spherical symmetry, `0 ≤ Λ ≤ Λ_c`; `K2_RESULT_20260903.md` §4) are inherited
  wholesale and restated in every K4 output. K4 cannot be more general than its input.

## 2. Objects, every symbol bound

- **Background:** the K2 B1 cell — `k = 0`, `Λ = 0` comoving dust top-hat of comoving radius `χ*`, `M = (4/3)π χ*³ ρ₀`
  (entry 56 L143), matched to Schwarzschild.
- **Causal scale:** `χ_§` as entry 23 defines it, `χ_§ = 3.149 c/H₀ = 14,015 Mpc`
  (`PROGRAM_C_FLUX_PREREG_20260902.md` §1 L18). Used at the recorded value; not re-derived here.
- **Perturbations:** scalar linear perturbations of the dust interior, in a gauge **the seat declares in its script
  header before computing**, with the perturbed Darmois conditions at the comoving edge as boundary conditions. The
  background junction is K2's; the **perturbed** junction is the new computation and is the whole content of this step.
- **Observable:** the pre-registered Phase (b) estimator — the uniform-weight pixel-pair `S₁/₂` on the pinned Planck
  SMICA map and common mask (`PROGRAM_A_FREEDOM_MAP_20260902.md` L203; the lane's tracked implementation
  `cutoffA_s12_machinery.py`, with `phaseB_c2.py` and `phaseB_export_cls.py`), and the lane's percentile machinery.
  Assets already in the lane: `planck_data/COM_CMB_IQU-smica_2048_R3.00_full.fits` and
  `planck_data/COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits`.
- **`ℓ_max`:** deferred to a receipted pin computed at step 1 from the freedom map's own `S₁/₂` range, printed by the
  seat's script before any `C_ℓ` is compared.

## 3. The question, exactly

With the boundary imposed on the **perturbations** rather than only on the background, what is the predicted `C_ℓ`
modification for `ℓ ≤ ℓ_max` (pinned at step 1), and what is the resulting Phase (b) percentile at the recorded `χ_§`?

## 4. The falsifier, stated exactly — both limbs, per Duho's order

**Limb 1 — the bar.** The best existing refinement is `2.2–2.8 %`
(`PROGRAM_A_FREEDOM_MAP_20260902.md` **L212**, Reading A, `2π/χ_§`). **A derived prediction whose Phase (b) percentile
is at or below `2.8 %` REFUTES the claim that a genuine causal boundary in the transfer physics buys anything the
spectral-window rows did not already buy.** It does not refute the boundary; it refutes its usefulness for this
statistic, and that is the claim under test.

**Limb 2 — a priori death.** If the perturbed junction reduces to an F1/F2-type condition
(`PROGRAM_C_FLUX_RESULT_20260902.md` **L15–22**: F1 touches only the unobservable monopole `ℓ = 0`, leaving every
`C_ℓ` for `ℓ ≥ 1` exactly unchanged; F2 forces `W̃(k) δ̃(k) = 0`, admitting no continuous power spectrum except `P ≡ 0`),
**the route is dead before any map is touched** and no Planck computation is run at all. This limb is checked and
reported **first**.

Neither limb may be softened after seeing a number.

## 5. Outcome classes — declared now, before computing

1. **K4_BOUNDARY_INERT** — the perturbed junction yields an F1/F2-type condition; no low-`ℓ` modification. Report
   which of F1/F2 and the derivation.
2. **K4_BOUNDARY_MODIFIES_BELOW_BAR** — a computed `C_ℓ` modification whose Phase (b) percentile is `≤ 2.8 %`. Report
   the percentile and the modification.
3. **K4_BOUNDARY_MODIFIES_ABOVE_BAR** — percentile `> 2.8 %`. Report the percentile, the modification, and the margin.
4. **K4_UNDETERMINED** — the perturbed junction admits a family of boundary conditions not fixed by the Darmois
   conditions. **INCONCLUSIVE**; name the freedom exactly — which mode, which parameter, which range — and **do not
   manufacture a boundary condition** to close it.
5. **K4_INPUT_VOID** — the K2 cell of §1 is found not to support the perturbed junction as stated. Nothing else is
   filed; the step returns to preregistration.
6. **K4_NO_CLASS** — a control fails in both seats after two attempts.

## 6. Controls, each with an exact named code

- **C1 — no-boundary limit.** With the boundary removed (`χ* → ∞`) the pipeline must reproduce the freedom map's ΛCDM
  row, percentile `0.15–0.20 %` (`BHU_CORPUS_SYNTHESIS_20260902.md` **L96–97**). Exact assertion:
  `C1_NO_BOUNDARY_LCDM_ROW=PASS`.
- **C2 — background junction.** The background must reproduce K2's B1 cell with all jumps zero. Exact assertion:
  `C2_BACKGROUND_JUNCTION_K2=PASS`.
- **C3 — deletion probe.** Replacing the Darmois boundary condition by the freedom map's spectral window must reproduce
  that row's percentile; **the exact row is named in the script header before running.** Exact assertion:
  `C3_WINDOW_ROW_REPRODUCED=PASS`.
- **C4 — seat agreement.** Two seats' `C_ℓ` must agree to the estimator's Monte-Carlo error at every `ℓ ≤ ℓ_max`
  (pinned at step 1). Failure routes to a third seat, not to a class. Exact assertion: `C4_SEATS_AGREE=PASS`.
- **C5 — estimator identity.** The estimator must reproduce the lane's recorded value on the real masked SMICA map,
  `1,223 μK⁴` (`PROGRAM_A_FREEDOM_MAP_20260902.md` L203), before any prediction is scored. Exact assertion:
  `C5_ESTIMATOR_C2_REPRODUCED=PASS`.
- **C6 — non-circularity.** No CMB statistic may enter the derivation; the prediction script must execute to
  completion and save its output before a separate script loads the Planck map or calls the estimator. Exact
  assertion: `C6_PREDICTION_BEFORE_DATA=PASS`.

The check sheet asserts the exact set `{C1_NO_BOUNDARY_LCDM_ROW, C2_BACKGROUND_JUNCTION_K2, C3_WINDOW_ROW_REPRODUCED,
C4_SEATS_AGREE, C5_ESTIMATOR_C2_REPRODUCED, C6_PREDICTION_BEFORE_DATA}` by name, and a deletion probe confirms that
removing a check removes its code.

## 7. Executable discipline — the defect this lane has now found twice

Twice this lane has filed a record that cited an executable which did not do what the prose claimed: `K2_route2_agy.py`
was a no-output stub cited as executable support (repaired 2026-09-04 in `RECORD_SUPPORT_AUDIT_20260904.md`), and
`cutoff_phase1_camb.py` was cited as "the complete executable" while absent from the repository (repaired the same day
in `CUTOFF_PHASE1_RECEIPT_20260904.md`). **Under this document, before any K4 output is filed:**

1. every script it cites **exists** at the cited path;
2. every script it cites **runs** to completion under `python3`, re-executed by Tori, not only by its author;
3. every script's **output is preserved** as a file in the lane and hashed in the check sheet;
4. no sentence calls a script executable support unless clauses 1–3 hold for that script;
5. the check sheet lists the sha256 of every script **and** of every preserved output.

A named script is not a receipt until someone runs it.

## 8. Seats — Duho's "both" standard

Blind double (codex and the Claude seat) on the perturbation derivation, each declaring its gauge before computing;
a third seat through `nm_referee_dispatch.sh` (ACCESS_SHA proof or no verdict) on any split; an **independent second
route** by a different method — a different gauge, or a mode-by-mode Green's-function construction versus a direct
junction-matching solve — blind to route 1; Kimi via the Moonshot route on the check-sheet arithmetic, with a
no-fallback control; a one-page human check sheet; Tori re-runs every script.

## 9. What makes this INCONCLUSIVE

Class 4; or C1/C2/C5 failing in both seats after two attempts (class 6); or route 1 and route 2 disagreeing on the
percentile beyond Monte-Carlo error after a third seat. In every such case the residual freedom is stated exactly and
**no boundary condition is manufactured**.

## 10. Non-circularity and scope

The Planck map enters **only** through the pre-registered estimator, at the end, after the prediction is printed (C6).
No CMB statistic is an input. Scope is this document: K3 step 3, K5, K6 and the downstream bounce study from K3 step 2
remain **NOT ORDERED**; K1 stage 2 stays stopped; the Tuesday neutron-star mass watch stays armed. No tier, warrant
token, standing or stamp moves on Tori's authority — the result proposes and Duho rules. Paper HOLD; nothing outward.

## 11. Cost and stopping rule

Ten to fourteen seat-days; Planck map and mask already in the lane; laptop compute. If limb 2 of the falsifier fires,
stop and file `K4_BOUNDARY_INERT` without touching a pixel. Otherwise stop and file whatever class is reached if the
derivation has not converged after the second route plus one third seat.

---

## 12. Gate record (V1 -> V2), including the referee's advice AGAINST running this

`K4_PREREG_GATE_20260904_agy.md` (fresh seat via `nm_referee_dispatch.sh`, ACCESS PROVEN,
`ACCESS_SHA=cf51fdc7081a8f04bb7939905a9852907dbbf5c8157cf20544591ff7a1e6af7c`) returned
`GATE=PREREG_SOUND_WITH_REPAIRS` with three repairs, **all applied**:

1. **Numeral tracing.** The entry-56 citation quoted the relation in clean notation while the pinned text is OCR.
   Applied verbatim, with a factual note on how the OCR renders the fraction.
2. **C6 was unenforceable.** As written it was a seat's promise not to peek at the map. It is now a structural
   separation: the prediction script must run to completion and save its output before any script loads the Planck map.
   This is the strongest of the three repairs and the document was weaker without it.
3. **Class 1 declared a standing outcome** ("the freedom map's residual closes"). Removed.

The referee also judged, as the brief asked it to, that **the step is not worth the ten to fourteen seat-days**, on the
ground that the freedom map already shows even an optimal explicit cutoff cannot lift the Phase (b) percentile far
above about 3%, so a derived boundary condition can at best reproduce a suppression already known to be insufficient.

**Tori's assessment, recorded and carried to Duho rather than resolved here.** The referee is measuring worth by
whether K4 could yield a positive detection, and on that measure it is probably right. But the freedom map records an
open structural residual at its own L174-177 — every row there assumes ΛCDM transfer physics, and nothing constrains a
genuine boundary — and **both** `K4_BOUNDARY_INERT` and `K4_BOUNDARY_MODIFIES_BELOW_BAR` close that residual. Closing
an admitted hole is the purpose Duho's order names, and it does not require a detection.

Where the referee's cost point does bite is sequencing, and this document already answers it: §4 limb 2 is checked
**first**, and §11 stops the study without touching a pixel if it fires. That is a cheap decision point, not ten to
fourteen days. The expensive half is only reached if the boundary is not inert.

K4_PREREG_V2_FROZEN
