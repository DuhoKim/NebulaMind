PASS_AUTHORIZATION_PIN

Gate: KUN_GATE_AUTHPIN_20260820 — authorization-pin one-liner in inference_runner.py
Seat: kimi gate seat (Nous route), fresh one-shot. Findings-only. No network used.
Date: 2026-08-20 (KST). Lane: .hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg

VERDICT: PASS. The single-line pin change is exactly what it claims, points at the real frozen
authorization on disk, and every refusal/bypass boundary of the runner survives it intact.
This was the last gate before the K-8 crossing; all six numbered checks below pass.

================================================================================
1. THE DIFF IS EXACTLY ONE LINE — CONFIRMED
================================================================================
git diff vs last committed build (aa6c24ee / 0923db16):
    diff --numstat ->  1  1  (1 insertion, 1 deletion)
    The single changed line is line 32:
      - AUTHORIZATION_SHA256 = "05fc06ddb5088b161782318b2bdda9abbdc78795bc995fcdb77cf58c1224664a"
      + AUTHORIZATION_SHA256 = "c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69"
No other line of the runner changed. Behavior identical to gated build except the pin value
(14/14 tests OK, section 4).

Placeholder grep (05fc06dd) across tree: 3 hits, all documentation, NONE executable:
    ./KUN_INFERENCE_GATE_20260820.md            (prior gate report — historical record)
    ./_inference_20260820/AUTHORIZATION_PIN_NOTE_20260820.md  (the reconciliation note)
    ./KICKOFF_GATE_AUTHPIN.txt                  (this kickoff)
  -> The placeholder survives only as prose describing the change. It is gone from all code.
New-hash grep (c1068759...) across tree: exactly ONE executable occurrence —
    inference_runner.py:32  (the pin itself)
  plus prose mentions in AUTHORIZATION_PIN_NOTE_20260820.md and KICKOFF_GATE_AUTHPIN.txt.
  -> No stray second copy, no divergence.

2. PINNED HASH MATCHES THE AUTHORIZATION ON DISK + MODE 444 — CONFIRMED
    shasum -a 256 K8_CROSSING_AUTHORIZATION_20260820.md
      -> c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69  (EXACT match to pin)
    stat -> -r--r--r--  444  K8_CROSSING_AUTHORIZATION_20260820.md   (read-only, correct mode)

3. AUTHORIZATION DOCUMENT CONTENT — CONFIRMED (read in full, 59 lines)
   - Verbatim Duho authorization present: 'Duho, 2026-08-20 22:20 KST, verbatim:
     "freeze it and authorize the crossing"' — given after reading the gated amendment and
     K8_CROSSING_BRIEF_20260820.md.
   - The SIX binding conditions are all present in section 3:
       (1) Partial-tertile prohibition (tertiles computed exactly once, on the complete
           accepted population, after the last cutout; never as a diagnostic).
       (2) No aggregation (chi is per-object with a receipt; no sky statistic / dipole /
           summary until the frozen order reaches it).
       (3) The amendment governs (sign convention AM-A, Jeffreys priors + estimate firewall
           AM-B, sparse-cell rule AM-C).
       (4) Sign discipline (inverted polarity on real data is a bug -> HOLD, never a sign flip).
       (5) Gated code only (gated runner + gated plumbing + gated cutouts from
           digest-verified bricks; any change after crossing is a parameter change).
       (6) Stop conditions (weights-hash mismatch, IC-contract failure, identity-property
           failure, or any gated-program refusal stops the run and goes to Duho).
   - Section 4 explicit NON-authorizations present: does NOT authorize the sky estimand,
     unblinding, the hand-check itself, or publication. (Pilot's 150 labels remain a
     separate act under PILOT_DECISION_20260818.md.)
   Document is what it claims.

4. TEST SUITE (prereg/venv_torch/bin/python) — 14 TESTS, ALL OK
    torch 2.8.0, numpy 1.26.4. Ran: python -m unittest test_inference_runner -v
    Ran 14 tests in 0.325s -> OK  (all 14 pass; includes the refusal and antisymmetry tests)

5. REFUSAL PATHS STILL WORK (tested myself with temp files) — CONFIRMED
    (a) No --authorization on a real-data path:
        -> {"status": "REFUSED", "code": "REFUSED_REAL_DATA_UNAUTHORIZED"}  exit=2
    (b) WRONG-hash authorization file (/tmp/gate_authpin_wrongauth.txt,
        sha 21a70b51... != pin):
        -> {"status": "REFUSED", "code": "REFUSED_AUTHORIZATION_SHA256"}    exit=2
    (c) CORRECT authorization file -> verify_authorization accepts and returns exactly
        c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69.

6. NO REAL-TENSOR READ PATH BYPASSES AUTHORIZATION — CONFIRMED
    Authorization chain (grep of all call sites):
      CLI main -> run_paths -> [synthetic=False] verify_authorization FIRST (line 383),
      before load_frozen_model / Committee / any input open; then read_ic6_tensor ->
      guard_input_scope -> verify_authorization for any real-root OR non-synthetic path.
    Empirical probes:
      B1  synthetic=True on a real-root path (contradictory flag) -> REFUSED_REAL_DATA_UNAUTHORIZED
          raised with pathlib.Path.open mocked to fail -> refusal happens BEFORE any open.
      B2  run_paths(synthetic=False, authorization=None): instrumented Path.open shows the
          weights/committee files were NEVER opened before the refusal -> auth is validated
          before any model/committee/input I/O.
      B3  synthetic=True on a genuine synthetic tensor, no auth -> reads fine (intended
          synthetic-only default boundary).
      B4  guard_input_scope: `if real_path or not synthetic: verify_authorization(...)` —
          a real-root path is treated as real regardless of the flag, and _is_within uses
          resolve(strict=False) so a symlink alias into the real root is also caught.
    Live state: /Users/duhokim/NebulaMindData/cutouts_dr10_south/tensors/ holds real cutouts
    (2640 entries) — the guard is load-bearing and holds.

================================================================================
FACT vs INFERENCE
================================================================================
FACT (recomputed by me, not inherited): the one-line numstat; both grep sweeps; the on-disk
sha256 of the authorization; its 444 mode; 14/14 test result; the three refusal/accept probes;
the before-any-open ordering (B1/B2). INFERENCE: that the pin note's narrative ("placeholder
matched no file that ever existed") is consistent with the placeholder now appearing only in
prose — I did not attempt to prove a negative across all of history, only that it is absent
from every executable file in the tree today.

NOT INSPECTED / OUT OF SCOPE (per brief, gate ONE change then stop): the amendment content
itself, committee.py internals, weights contents, and any lane other than _inference_20260820.
No network was touched. Temp files written only under /tmp (gate_authpin_*); no repo state
modified other than this report.

COMPLETION MARKER: PASS_AUTHORIZATION_PIN
