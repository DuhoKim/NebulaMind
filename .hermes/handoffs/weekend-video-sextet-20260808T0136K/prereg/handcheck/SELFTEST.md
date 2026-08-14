# HC-1H synthetic self-test receipt

Verdict: `PASS_HC1H_SYNTHETIC_SELFTEST`

Scope: generated rows and generated PNGs only. No real sky image, real object row, real model output, or actual hand-check label was used. This is build verification, not protocol acceptance and not an actual HC-1H result.

Accepted authority pinned by the harness:

- `LANA_ONE_HUMAN_ATTENUATION_20260814.md` SHA-256 `b2590e4213e225f9869fe782cfe0f55d8d8979dcb470752836a5cd31a58453fd`
- `_tmp_YUI_HARNESS_HC1H_BRIEF.md`
- `HC1H_ACCEPTANCE_20260815.md`
- `KUN_HC1H_CLOSE_20260814.md`

## Commands executed

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_nm_handcheck
PYTHONDONTWRITEBYTECODE=1 python3 run_hc1h_synthetic_selftest.py
PYTHONDONTWRITEBYTECODE=1 python3 independent_verify_hc1h.py
```

The Python modules were also compiled with `python3 -m py_compile` in the final verification pass.

## Contract suite

Final result: **28/28 PASS**. The suite exercises both new HC-1H behavior and retained low-level custody/session regressions. HC-1H-specific checks include:

- exact three-state committee vocabulary crossed with accepted-real-population |chi| tertiles;
- capacity-aware Neyman allocation by `N_s sqrt(a_s(1-a_s))`;
- floor 30 and integer closure to 500 real labels;
- authorized full and pilot count overrides rejected;
- one `checker_H` package and no A/B/J package from the HC-1H preparation path;
- 500 real + 200 injection + 150 repeat stream construction;
- every repeat occurs later than its first presentation and has complementary mirror parity;
- checker package contains no item type, source identity, truth, instrument sign, stratum, or parity;
- checker package contains no replacement group, repeat parent/dependent link, or session-MAC key; those remain in the private committed control file;
- ordinary package-derived SHA-256 event-chain forgery rejected because HC-1H events require the private HMAC key;
- accepted-real-population |chi| cutpoints applied unchanged to injections;
- repeat replacement parents are distinct and absent from the original 30% repeat-parent set;
- aggregate committee-state disagreement/low-confidence diagnostics are explicitly marked as excluded from attenuation;
- specific HC-7 UI flag, discard, and same-category/stratum opaque replacement;
- automatic replacement of a future repeat when its first presentation is flagged;
- systematic HC-7 exposure terminal path;
- replacement-reserve exhaustion recorded as a terminal hard-inconclusive event rather than a rejected flag followed by an answer;
- stale-token rejection, debounce, lossless resume, HMAC-chain validation, fsync, and inter-process append exclusion;
- pilot 90/40/20 closure, required UI ergonomics event, and `PASS-TO-FULL-HC1H`;
- pilot injections absent from any claimed final epsilon path;
- corrected stratum rates, accepted-population weighting, Wilson-68 variances, and the shared global-epsilon covariance term;
- explicit additional covariance added to total variance, with authorized full preparation refusing an absent separately approved value;
- repeat non-flip and per-injection-stratum 2-sigma diagnostics;
- exact unrounded thresholds, including a deliberately borderline lower bound of `0.849` remaining inconclusive;
- adopted power-bound `N=130,076` and `a_gate=0.7905` pinned in preparation, verdict, and reduction;
- F-10 public masking and private/public path separation;
- F-10 masked cells force the public stratum gate and final decision to `WITHHELD_F10_MASKED_STRATA`, preventing failure identity from being deduced by elimination;
- reduction cannot call `unseal_key` before the sole required stream is complete.

## Accepted-shape full synthetic run

The full runner generated 1,080 accepted-population stand-ins and 270 injection-pool stand-ins across all nine machine-state × |chi| strata. It then prepared and completed the exact 850-label shape:

- 500 synthetic stand-ins for real selected rows;
- 200 blind known-truth injections;
- 150 mirrored re-presentations;
- one checker capability;
- all nine strata present;
- minimum realized real allocation at least 30;
- real allocation total exactly 500;
- 150/150 repeats later than their first presentation;
- 150/150 repeats with complementary mirror parity;
- one pre-key synthetic-exposure flag discarded and replaced without changing 500/200/150 counts;
- 17 mandatory break acknowledgements across 851 viewed presentations (850 valid labels plus one discarded flag);
- global synthetic error exactly `10/200 = 1/20`;
- mirrored-repeat non-flips exactly `6/150`;
- repeat non-flips retained by enforced 50-presentation session block for fatigue/drift inspection;
- private synthetic fixture verdict `PASS_HC1H_ATTENUATION`; public verdict `WITHHELD_F10_MASKED_STRATA` because the Neyman allocation includes a sub-50 cell.

The runner writes `hc1h_synthetic_selftest_receipt.json` plus stdout/stderr logs. The receipt records exact counts, gates, and source/test hashes.

## Accepted-shape pilot synthetic run

The same runner separately prepared and completed:

- 90 real stand-ins, exactly 10 per stratum;
- 40 pilot-only injections;
- 20 mirrored retests;
- 150 total labels;
- two mandatory break acknowledgements, after presentations 50 and 100;
- UI-recorded acceptable ergonomics;
- outcome `PASS-TO-FULL-HC1H`;
- no pilot attenuation, corrected-real-stratum, or repeat-rate statistic emitted and no real/retest value used for PASS;
- explicit `synthetics_count_toward_full = false`.
- a second accepted-shape full preparation chained to the pilot PASS, with every selected/reserve pilot synthetic identity excluded from the fresh full injection set.

No pilot injection was copied into the chained fresh-full preparation or its epsilon. Automated carry-forward of the pilot's 90 real and 20 retest labels is not implemented.

## Independent verifier

`independent_verify_hc1h.py` is standard-library only: AST, hashlib, json, and pathlib. It does not import Pillow, cryptography, NumPy, SciPy, torch, or `nm_handcheck`.

It verifies 82 structural and receipt claims, including hard-pinned authority hashes, one-human preparation, accepted counts, constrained Neyman formula, common real-population |chi| cutpoints, distinct repeat reserves, adopted power-bound N, private server control and event HMAC, enforced 50-presentation breaks, UI flag events and reserve exhaustion, published hard-inconclusive voids without key opening, checker inability to unseal, complete-before-unseal ordering, corrected-rate formula, shared-epsilon term, committee and session-drift diagnostics, pilot non-production of `a`, mandatory pilot policy, fresh full-injection exclusion, thresholds, F-10 masking without failing-stratum leakage, full/pilot receipts, and artifact hashes.

Final independent result: `PASS_INDEPENDENT_HC1H_VERIFICATION 82 / 82`.

## Honest limits of this PASS

This PASS does not prove that generated injections are perceptually indistinguishable from real survey cutouts. The harness equalizes package schema, image mode, dimensions, rendering path, and UI treatment; realism is an input-production and human-detection question.

It does not prove Duho will be free of fatigue, learning, memory, automation, external assistance, or bias. One human has no second-human independence.

It does not make the checker path an OS sandbox. A checker with custodian-account shell access can inspect opaque package relationships, copy assets, tamper with files, or search externally. Browser-only or separate-account/device operation remains required.

HC-7 replacement capacity is finite and predeclared. Reserve exhaustion fails closed. A sufficiently determined checker can intentionally exhaust it and force inconclusive.

The hash chain detects unsupported mutation; it does not stop a party with write access and enough knowledge from rebuilding a different internally consistent chain. External timestamping is not provided.

The independent verifier is structural and receipt-based, not an external security audit or independent scientific replication.

No real data run, human pilot, HC-6 power calculation, release, freeze, publication, database operation, commit, or push occurred.