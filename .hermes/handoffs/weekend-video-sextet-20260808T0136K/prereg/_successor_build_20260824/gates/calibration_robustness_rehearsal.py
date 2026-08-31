#!/usr/bin/env python3
"""calibration_robustness_rehearsal — the machine-only sweep rehearsal the
principal's pace ruling ordered ("Rehearse and sign tonight"): the FULL 99×51
matrix through the real machinery — the confirmed MappingA one-draw primitive,
the frozen v9 permutation record and adjudication, the ratified grid — on the
FIXTURE mask and fixture calibration. No science data: no imagery, no measured
χ, no γ̂; v9 loaded read-only through the verified manifest.

WHAT REHEARSAL-HELD MEANS AND DOES NOT MEAN, in the draft's own honest-limit
language: HELD here means NO VERDICT FLIP WAS FOUND ON THE EVALUATED GRID, per
draw, against that draw's own γ=0 baseline (the architecture ruling's
within-draw reduction), worst case over all 99 draws. It is a MACHINERY
invariance statement about fixture data. It is NOT invariance_outcome = HELD,
fills no slot, and discharges no BS-6 edge — only the real run can do that.

OUTCOME CATEGORIES per grid cell:
  * an adjudicated verdict token (v9's own, e.g. INCONCLUSIVE) — conclusive
    for comparison purposes;
  * INCONCLUSIVE-BY-CALIBRATION via PathRefusal P07 — the ADMISSIBILITY
    BOUNDARY: the ±0.25 grid deliberately overshoots the region where
    a_LB_b ≥ 0.85 can hold (the draft: gradients steeper than ≈0.21 never
    reach a verdict), so these cells are recorded and counted, never flips;
  * anything else — a rehearsal FAILURE, loudly.
The γ=0 baseline cell must be admissible and adjudicated in every draw.

Grid: γ_j = (j − 25)·Γ/25 for j = 0..50 with Γ = 0.25 ratified — Δγ = 0.01
derived, j₀ = 25 verified EXACTLY zero, endpoints exactly ±Γ."""
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(BASE / "ref"))

import replay_harness as rh  # noqa: E402

GAMMA = 0.25
N_STEPS = 50
J0 = 25
N_DRAWS = 99
N_PERM = 200


def main():
    t_start = time.time()
    gammas = [(j - J0) * GAMMA / J0 for j in range(N_STEPS + 1)]
    assert gammas[J0] == 0.0, "j0 cell is not exactly zero"
    assert gammas[0] == -GAMMA and gammas[-1] == GAMMA, "endpoints not exact"

    bufs = rh._read_and_verify()
    mods, saved = rh._compile_in_order(bufs)
    try:
        gcp = mods["gain_counterfactual_path"]
        import gain_mapping_a as gm
        ident, ident_sha = gm.identity_record()
        mask, _ = gcp._fixture()
        cal = dict(gcp._CAL)

        matrix = []            # 99 rows × 51 outcome tokens
        flips_total = 0
        incal_total = 0
        baselines = {}
        admissible_span = None
        for d in range(N_DRAWS):
            mp = gm.MappingA(d)
            row = []
            for g in gammas:
                try:
                    out = gcp.evaluate_at(g, mask, cal, mp, stage=1, prefix=1,
                                          trial=1, n_perm=N_PERM)
                    row.append(f"V:{out['verdict']}")
                except gcp.PathRefusal as e:
                    if "InconclusiveByCalibration" in str(e):
                        row.append("INCAL")
                        incal_total += 1
                    else:
                        raise
            base = row[J0]
            if not base.startswith("V:"):
                raise RuntimeError(
                    f"draw {d}: the γ=0 baseline is not adjudicated ({base})")
            baselines.setdefault(base, 0)
            baselines[base] += 1
            flips = sum(1 for x in row if x.startswith("V:") and x != base)
            flips_total += flips
            span = [g for g, x in zip(gammas, row) if x.startswith("V:")]
            span_t = (min(span), max(span))
            if admissible_span is None:
                admissible_span = span_t
            elif admissible_span != span_t:
                admissible_span = ("VARIES", "VARIES")
            matrix.append(row)
    finally:
        if saved is not None:
            sys.modules["successor_ref_v9"] = saved
        else:
            sys.modules.pop("successor_ref_v9", None)

    held = flips_total == 0
    matrix_digest = hashlib.sha256(
        json.dumps(matrix, separators=(",", ":")).encode()).hexdigest()
    dt = time.time() - t_start

    lines = [
        "# CALIBRATION ROBUSTNESS REHEARSAL RECEIPT — 2026-08-31",
        "",
        "Machine-only, per the pace ruling: fixture mask (n=240, the path's own "
        "_fixture) and fixture calibration (_CAL); no science data, no imagery, "
        "no measured χ, no γ̂; v9 read-only via the verified manifest (incl. the "
        "ACTIVE confirmed mapping).",
        "",
        f"- grid: Γ = {GAMMA} ratified, Δγ = 0.01 derived, 51 points, j₀ = 25 "
        "verified EXACTLY zero, endpoints exactly ±Γ",
        f"- draws: {N_DRAWS} (SeedSequence(20260830).spawn({N_DRAWS}), zero-based; "
        f"CRN per draw); n_perm = {N_PERM} per cell",
        f"- mapping identity: `{ident_sha}` (convention commitment bound inside)",
        f"- evaluations: {N_DRAWS * (N_STEPS + 1)} cells in {dt:.1f} s",
        f"- baseline verdicts at γ=0 across draws: {baselines}",
        f"- admissible γ span (uniform across draws unless VARIES): "
        f"{admissible_span}",
        f"- INCONCLUSIVE-BY-CALIBRATION cells (the admissibility boundary the "
        f"±0.25 grid deliberately overshoots): {incal_total}",
        f"- VERDICT FLIPS against each draw's own γ=0 baseline, worst case over "
        f"draws: **{flips_total}**",
        f"- outcome-matrix sha256: `{matrix_digest}`",
        "",
        f"**REHEARSAL OUTCOME: {'HELD' if held else 'FAILED'}** — "
        + ("no verdict flip anywhere on the evaluated grid, in any of the 99 "
           "draws. In the draft's own honest-limit language: HELD means only "
           "that no flip was found ON THE EVALUATED GRID; it is a machinery "
           "statement about fixture data, is NOT invariance_outcome = HELD, "
           "fills no slot, and discharges no BS-6 edge."
           if held else
           "a verdict flip was found; per the pace ruling this is a BLOCKER "
           "to surface, not a sign-anyway."),
    ]
    (HERE / "CALIBRATION_ROBUSTNESS_REHEARSAL_RECEIPT_20260831.md").write_text(
        "\n".join(lines) + "\n")
    print("\n".join(lines[-6:]))
    return 0 if held else 1


if __name__ == "__main__":
    sys.exit(main())
