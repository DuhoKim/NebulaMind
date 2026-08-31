#!/usr/bin/env python3
"""calibration_rehearsal — the P0-queue rehearsal the BS-1 early resolution
unblocked: ONE receipted chain proving the pinned tools COMPOSE, end to end, on
synthetic data, before the principal signs P0.

WHAT IT TOUCHES AND WHAT IT NEVER TOUCHES, stated first: synthetic positions,
synthetic committee calls, fixture masks — no survey imagery (BS-6 stays
blocked), no χ measurement (γ̂ stays unmeasured), no real catalog rows beyond
what the pinned tier-2 harness already sanctioned. v9 is loaded READ-ONLY
through the replay harness's verified loader. A rehearsal that needed anything
blocked would be a different experiment; this one exists to show the plumbing
holds so the freeze package can be signed with the machinery already exercised.

THE CHAIN (each stage's receipt lands in the rehearsal receipt):
  S1  verified v9 load (manifest roots incl. the ACTIVE confirmed mapping)
  S2  synthetic accepted-partition positions → v9.calibration_bins →
      bs2f_boundary_verifier CERTIFIED receipt (the calibration half)
  S3  synthetic committee calls + |χ| → stratum_index_producer (TEST schema
      commitment) → the INDEPENDENT verifier green (the stratum half)
  S4  per-object (cal_bin × stratum) cells → v9.allocate_handcheck at the
      frozen constants (3 × 9, floors 10/30, budget 500) — allocation feasible
  S5  replay_machinery_proof — one real permutation verdict through the frozen
      machinery under the audit-hook census
  S6  gain_mapping_a self-test (the confirmed mapping's own 9 checks)
  S7  terminal_ceremony --selftest (the P9 flow, both refusal paths)
Receipt: gates/CALIBRATION_REHEARSAL_RECEIPT_20260831.md — per-stage receipts,
tool shas, PASS/FAIL; any stage failing fails the rehearsal loudly."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(BASE / "ref"))

import replay_harness as rh  # noqa: E402
import bs2f_boundary_verifier as b2f  # noqa: E402
import stratum_index_producer as sip  # noqa: E402
import stratum_index_verifier as siv  # noqa: E402


def main():
    lines = ["# CALIBRATION REHEARSAL RECEIPT — 2026-08-31",
             "",
             "Synthetic data only; v9 read-only via the verified loader; no "
             "imagery, no χ, no γ̂.", ""]
    fails = []

    def stage(tag, msg):
        lines.append(f"- **{tag}**: {msg}")
        print(f"{tag}: {msg[:110]}")

    # S1 — verified load, three ACTIVE roots
    bufs = rh._read_and_verify()
    mods, saved = rh._compile_in_order(bufs)
    try:
        v9 = mods["successor_ref_v9"]
        stage("S1 PASS", f"verified roots loaded: "
              + ", ".join(f"{n}={bufs[n][2][:12]}…" for n in sorted(bufs)))

        # S2 — calibration half on synthetic positions
        rng = np.random.default_rng(20260831)
        c = np.sort(rng.uniform(-1, 1, 540)).astype("<f8")
        sealed = v9.calibration_bins(c).copy()
        rec2 = b2f.verify_boundaries(sealed, c)
        if rec2["verdict"] != "CERTIFIED":
            raise RuntimeError("bs2f did not certify")
        stage("S2 PASS", f"540 synthetic positions → boundaries "
              f"{[round(x,4) for x in sealed.tolist()]} CERTIFIED "
              f"(artifact {rec2['artifact_digest'][:12]}…, v9 {rec2['v9_sha256'][:12]}…)")

        # S3 — stratum half: 540 objects, calls + |χ| engineered to fill all 9
        oids = [f"o{i:03d}" for i in range(540)]
        states = ["SS", "ZZ", "SZ"]
        calls, chis = {}, []
        for i, o in enumerate(oids):
            s = states[i % 3]
            calls[o] = (s[0], s[1])
            chis.append((o, float(i) / 540.0))
        T = {"tag": "stratum-index-REHEARSAL",
             "schema_digest": hashlib.sha256(b"rehearsal-schema").hexdigest()}
        writes = []
        art, receipt3, _ = sip.produce(calls, chis, T, lambda b: writes.append(b))
        siv.verify_stratum_index(writes[0], receipt3, calls, chis, T)
        idx = sip.build_index(calls, chis)
        if sum(idx["stratum_counts"].values()) != 540 or \
                len(idx["stratum_counts"]) != 9:
            raise RuntimeError(f"strata not fully populated: "
                               f"{idx['stratum_counts']}")
        stage("S3 PASS", f"9/9 strata populated over 540 objects; sealed "
              f"receipt {receipt3[:12]}…; independent verifier green")

        # S4 — the allocation at the frozen constants
        stratum_keys = sorted(idx["stratum_counts"])
        bins = v9.assign_bins(np.array([x[1] for x in chis], dtype="<f8"), sealed)
        cells = np.zeros((v9.N_CAL_BINS, v9.N_HC_STRATA), dtype=np.int64)
        by_obj_stratum = {r["object_id"]: stratum_keys.index(
            f"{r['state']}|{r['tertile']}") for r in idx["rows"]}
        for (o, _), b in zip(chis, bins):
            cells[int(b), by_obj_stratum[o]] += 1
        alloc = v9.allocate_handcheck(cells)
        if int(alloc.sum()) > v9.HC_REAL_LABELS or (alloc < 0).any():
            raise RuntimeError("allocation out of budget")
        stage("S4 PASS", f"allocate_handcheck at the frozen constants "
              f"(3×9, floors {v9.HC_MIN_PER_CELL}/{v9.HC_MIN_PER_STRATUM}, "
              f"budget {v9.HC_REAL_LABELS}): allocated {int(alloc.sum())} "
              f"labels over {int((cells > 0).sum())} live cells")
    finally:
        if saved is not None:
            sys.modules["successor_ref_v9"] = saved
        else:
            sys.modules.pop("successor_ref_v9", None)

    # S5 — the replay machinery proof (its own verified load inside)
    out = rh.replay_machinery_proof()
    stage("S5 PASS", f"replay machinery proof: one real permutation verdict "
          f"(p={out['p']:.4f}) under the audit-hook census; harness "
          f"{out['harness_sha256'][:12]}…")

    # S6 — the confirmed mapping's own self-test
    r6 = subprocess.run([sys.executable, str(BASE / "ref" / "gain_mapping_a.py")],
                        capture_output=True, text=True)
    if r6.returncode != 0:
        raise RuntimeError(f"mapping self-test failed:\n{r6.stdout[-500:]}")
    stage("S6 PASS", "gain_mapping_a self-test green (the confirmed mapping, "
          "CRN identity through the frozen machinery)")

    # S7 — the P9 ceremony flow
    r7 = subprocess.run([sys.executable, str(HERE / "terminal_ceremony.py"),
                         "--selftest"], capture_output=True, text=True)
    if r7.returncode != 0 or "green" not in r7.stdout:
        raise RuntimeError(f"ceremony selftest failed:\n{r7.stdout[-500:]}")
    stage("S7 PASS", "terminal ceremony selftest green (clean signing path + "
          "both refusal paths through the real CLI)")

    lines += ["", "## Tool identities at rehearsal time", ""]
    for f in ("replay_harness.py", "bs2f_boundary_verifier.py",
              "stratum_index_producer.py", "stratum_index_verifier.py",
              "canonical_decoder.py", "enumeration_verifier.py",
              "terminal_review_verifier.py", "terminal_ceremony.py",
              "count_oracle_harness.py"):
        sha = hashlib.sha256((HERE / f).read_bytes()).hexdigest()
        lines.append(f"- `{f}` sha256 `{sha}`")
    lines += ["", "**VERDICT: REHEARSAL PASS — the pinned tools compose end to "
              "end on synthetic data; the freeze package can be signed with "
              "the machinery already exercised.**"]
    (HERE / "CALIBRATION_REHEARSAL_RECEIPT_20260831.md").write_text(
        "\n".join(lines) + "\n")
    print("receipt written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
