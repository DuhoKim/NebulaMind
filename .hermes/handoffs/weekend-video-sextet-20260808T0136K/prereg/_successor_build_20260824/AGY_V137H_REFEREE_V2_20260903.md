ACCESS_SHA=700fd0d29d7f06b9e938b7e48bac729080cc9661bf00f08bbd24a2ad467fd190

F1: CLOSED
The repaired §7 row (line 941) states:
> `19ffcbab574a8663e248b4d837be9734e48843e8c9ab8ea59489ef2558cf5818`; 0 of 5,049 cells are `INCONCLUSIVE-BY-CALIBRATION`; minimum `a_lb_b` is `0.8639832635983262`; receipt field `sigma_gamma` is `0.04790176316993866`. Under reading (i), this FAILED receipt is a true record that blocks: the slot stays UNFILLED, and the design decision that follows belongs to the principal and is PENDING; this draft does not pre-empt it.

The repaired §11 bullet (line 1252) states:
> - **BS-3g headroom evaluation — FAILED (Duho rulings (a), 16:52 KST, direction #66, and "as their recs", 19:37 KST, direction #69):** preserve `n_steps = 50`, seed 20260830, `numpy-1.26.4-PCG64-default_rng`, 99 draws, CRN, mapping A worst case, and option (b); set only BS-3g DESIGN accuracy a₀ = 0.95 and Γ = 0.10, deriving Δγ = 0.004. `gates/bs3g_headroom_experiment/HEADROOM_RESULTS_20260903.md` measured the 0.95 edge at 0.12 (analytic 0.121181392) with σ_γ 0.047901763. The prior receipt `a8277a193caffa826ac3a1c2884545f0112b64e7cd3f6a6556dcc996041e49ba` remains the true FAILED 0.88 record; the new receipt and V2 tooling pins — producer `48b2cc6607b91b1e746c2ee7cb21c9b624fb247be5aee3922fb3572351848e82`, verifier `ca6e2ea35b38bebb020b053839477306cbce97a7791de4ad76d9f524afe21454`, in `BS3G_TOOLING_PIN_V2_20260903.md` — are the verifier-valid FAILED result. The fresh V137-H sweep's `invariance_outcome` is **FAILED**: draw 94 at `gamma = -0.10` is `REPRODUCED-LONGO` versus the baseline `INCONCLUSIVE`, a decision-changing cell. Two independent runs produced the identical `run/classp_candidates/BS-3g.json` receipt digest sha256 `19ffcbab574a8663e248b4d837be9734e48843e8c9ab8ea59489ef2558cf5818`; 0 of 5,049 cells are `INCONCLUSIVE-BY-CALIBRATION`; minimum `a_lb_b` is `0.8639832635983262`; receipt field `sigma_gamma` is `0.04790176316993866`. Under reading (i), this FAILED receipt is a true record that blocks: the slot stays UNFILLED, and the design decision that follows belongs to the principal and is PENDING; this draft does not pre-empt it.

Every number byte-for-byte matches `run/classp_candidates/BS-3g.json` and `V137_BS3G_RANGE_RECORD_20260903.md`. The FAILED outcome is accurately recorded, not softened, and the design decision is stated as pending with the principal.

**TASK B: Verbatim preservation**
Compared against git `HEAD~1` using:
`git -C /Users/duhokim/NebulaMind/NebulaMind diff HEAD~1 .hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V137_20260903.md`
Output is empty. No other line changed.

**CHECKS:**
1. **Numbers match byte-for-byte.**
   Evidence:
   `shasum -a 256 run/classp_candidates/BS-3g.json` -> `19ffcbab574a8663e248b4d837be9734e48843e8c9ab8ea59489ef2558cf5818`
   `python3 gates/verify_bs3g_receipt.py run/classp_candidates/BS-3g.json` -> `BS-3g receipt verifier: 20/20 fields PASS; outcome FAILED`
   Draft specifies a0=0.95, Γ=0.10, grid 99x51, cell counts 0 of 5,049, min a_lb_b=0.8639832635983262, receipt field sigma_gamma=0.04790176316993866, all exactly matching JSON and range record.
2. **Trace check.**
   Command: `python3 ../../../../../tools/prereg_trace.py --check PREREG_SUCCESSOR_DRAFT_V137_20260903.md .`
   Output:
   ```
   prereg trace check — PREREG_SUCCESSOR_DRAFT_V137_20260903.md
     136 computed transition(s); 0 problem(s)
   ```
3. **Manifest check.**
   Command: `shasum -a 256 -c P0_PACKAGE_MANIFEST_20260831.txt | wc -l` -> 30, and checking manually they all output OK. Any non-OK is FATAL, but none were non-OK.
4. **Amendment section and mechanism.**
   Predecessor (V136) and chat signature via Blanc are correctly documented.
   Lines 1619-1620 are blank: `SIGNATURE UTC: ` and `DUHO SIGNATURE: `
   Diff shows V135/V136 amendment records were untouched.
5. **Producer parameters untouched.**
   Command: `shasum -a 256 ref/gain_counterfactual_path.py ref/DRAW_MECHANICS_COMMIT_20260830.md`
   Output:
   ```
   92cbbdf89bd2a494c9cfb9f19fb12a46cf59a16731246cea2e74c56d2454a9b7  ref/gain_counterfactual_path.py
   32673bd05f988b757a51eb445ae10d5e6a0dbe3d3a7593459db295917192790f  ref/DRAW_MECHANICS_COMMIT_20260830.md
   ```
   Matches P0 manifest perfectly.

SEAT: AGY
VERSION: V137H-REFEREE-V2
VERDICT: SIGNABLE
COUNT: 0
