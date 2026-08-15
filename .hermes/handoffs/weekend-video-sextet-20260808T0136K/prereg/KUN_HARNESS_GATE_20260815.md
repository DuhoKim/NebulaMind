# KUN HC-1H HARNESS GATE

Recorded: 2026-08-15T11:20:12+09:00

Verdict: PASS_HC1H_HARNESS_WITH_OPERATING_BOUNDARIES

Plain answer: the reworked HC-1H harness passes as an implementation/custody harness on exact source hash `cc88fa5ee6e7d7f2ab32ad4b7b0d7d843f9a77ed777c11d259755197eda03bbc`; nothing in this gate authorizes an actual hand-check, real-sky run, publication, acceptance, commit, or push.

## Exact Artifacts Checked

| Artifact | SHA-256 |
|---|---|
| `prereg/_tmp_KUN_HARNESS_GATE_BRIEF.md` | `b37fd9852a491e5a64387e8bb7d73ddef9fdfd4f2d2015f4b7c44ea2e837b98e` |
| `prereg/handcheck/nm_handcheck.py` | `cc88fa5ee6e7d7f2ab32ad4b7b0d7d843f9a77ed777c11d259755197eda03bbc` |
| `prereg/handcheck/test_nm_handcheck.py` | `2512d01220196441a4da28d5bac5268399cb38dc68fe2d6e9fbaf9fc2e344788` |
| `prereg/handcheck/SELFTEST.md` | `ccb217287424bbac06e4bc6f3c6e3c8f54a300c5e2f0ed42e64896cca8bd8d18` |
| `prereg/handcheck/YUI_HANDCHECK_HARNESS_20260814.md` | `d5b2ce3a2d938d8baa88861f4f2983d8fcfedd7582d25ec9f7225835d2381697` |
| `prereg/handcheck/OPERATING_INSTRUCTIONS.md` | `db0623854c3cbc837d91499cf578ddbf974507079df623c5ad78ac001a5eba8f` |
| `prereg/handcheck/independent_verify_hc1h.py` | `15f48274ccf81d476a3a92c2241a279dfe4b098d018a83e68368d2ad0000936e` |
| `prereg/handcheck/hc1h_independent_verification.json` | `19a6881f8258e064d848968984a650ea3e97cc6ecc59ad5100ed3d2d475a87a8` |
| `prereg/handcheck/hc1h_synthetic_selftest_receipt.json` | `25d02f109aba05d8a200a540e126ecba3c3c3607c0a6c9df2371566cafe2eb40` |

## Verification Run

I ran the synthetic test suite. In the normal sandbox it reached 27/28 tests, with the only error being `PermissionError: [Errno 1] Operation not permitted` while binding a local `127.0.0.1` HTTP test server. Because that test is directly relevant to checker-path exposure, I reran the suite with local-loopback permission.

Final observed result:

```text
Ran 28 tests in 4.513s
OK
```

I also reran:

```text
PYTHONDONTWRITEBYTECODE=1 python3 run_hc1h_synthetic_selftest.py
PYTHONDONTWRITEBYTECODE=1 python3 independent_verify_hc1h.py
```

Observed:

```text
PASS_HC1H_SYNTHETIC_SELFTEST
PASS_INDEPENDENT_HC1H_VERIFICATION 82 / 82
```

All of these runs used synthetic fixtures. No real hand-check and no real-sky statistic occurred.

## Source Gate Findings

### 1. Sealed-Key Unreachability

PASS under the operating boundary "checker receives browser-only access, not the custodian shell."

Source facts:

- `prepare_hc1h_experiment` writes the encrypted sealed key only to `private_root / "sealed_key.nmhc"` with mode `0600`.
- The checker package under `checking_root/checker_H` receives only `sequence`, opaque `item_id`, `asset`, and `asset_sha256`.
- Truth-bearing fields are explicitly forbidden in checker packages: `root_secret_hex`, `object_id`, `image_path`, `instrument_sign`, `abs_chi`, `committee_state`, `category`, `synthetic_id`, `truth_sign`, `stratum`, `mirrored`, and `sealed_key`.
- `load_checker_package` rejects any checker package containing those forbidden keys and verifies the package hash against the public commitment.
- HC-1H private server control is separate: `checker_H_control.json` stays in `private_root`, mode `0600`. It contains replacement/repeat control and the event-MAC key, not the sealed parity/truth key.
- `public_state()` returns status, role, instructions, progress, flag count, ergonomics status, one presentation token, one asset URL, and allowed keys. It does not return item type, source identity, truth, instrument sign, stratum, mirror parity, replacement group, parent/dependent links, or the event-MAC key.
- `current_asset()` serves only the current PNG for a matching one-use token.
- The HTTP handler exposes only `/`, `/api/state`, `/asset?token=...`, and `/api/answer`; arbitrary paths such as `package.json`, `answers.jsonl`, or `sealed_key.nmhc` fall through to 404.
- Reduction reaches `unseal_key()` only after commitment/source/authority checks, complete label stream, chronology check, and no terminal HC-7 systematic exposure. For a terminal HC-7 event it writes a hard-inconclusive integrity event with `sealed_key_opened: False`.

That is enough for browser-only custody. It is not an OS sandbox: if the checker has shell access to the custodian account, or can read `private_root` / `checker_H_control.json`, the operating assumption is broken. The operating instructions say this plainly, and I agree it is load-bearing.

### 2. Synthetic Indistinguishability

PASS as a structural harness gate; not a perceptual-validity proof.

The source enforces equal technical representation by reading rows through the same schemas, rendering through the same PNG path, requiring all generated assets to share one image mode and pixel size, and presenting every item through the same package/UI/progress path. It does not and cannot prove that synthetic injections are visually indistinguishable from real images.

That gap is acceptable only because HC-7 clause (v) is implemented as a hard operational trigger: the checker can flag a suspected specific exposure or a systematic exposure before key opening. If synthetics are perceptually obvious, the correct result is INCONCLUSIVE, not a forced measurement.

### 3. Borderline `a = 0.849`

PASS. The HC-1H verdict path uses `Decimal` values and compares unrounded lower bound to exact thresholds. The tested borderline `attenuation=Decimal("0.849"), sigma=0` returns `INCONCLUSIVE-BY-POWER`; `0.850` is the exact edge for the quality floor when all other gates pass.

### 4. Neyman Allocation

PASS. The unit test confirms the HC-1H allocation with floor 30 closes to exactly 500 real labels and respects capacity. The implementation computes constrained Neyman allocation from all nine `committee_state|chi_tertile` cells rather than treating the floor as an extra base tranche.

### 5. Shared-`epsilon_hat` Variance

PASS. `hc1h_statistics()` computes each stratum's epsilon derivative, sums the weighted derivatives across strata, and squares only after summing:

```text
shared_component = shared_derivative * shared_derivative * epsilon_variance
```

It is not the withdrawn diagonal approximation. The tests exercise this and verify the shared component is nonzero and contributes to total variance.

### 6. Replacement-Reserve Exhaustion

Ruling: acceptable fail-closed behavior, not a blocker, and not fixable by pretending the checker cannot force INCONCLUSIVE.

Yui's disclosed weakness is real: a checker can force hard INCONCLUSIVE by pressing `X`, or by repeatedly pressing `F` until the same opaque replacement group exhausts its finite reserve. The source handles that correctly: `flag_exposure()` records `REPLACEMENT_RESERVE_EXHAUSTED_HC7`, `public_state()` becomes `INCONCLUSIVE_HC7_SYSTEMATIC_EXPOSURE`, and reduction publishes a hard-inconclusive integrity event without opening the key.

This does not need a statistical bound to pass the harness gate. A larger reserve would reduce accidental exhaustion but cannot eliminate intentional denial of service, because `X` must remain available if the checker genuinely detects systematic leakage. The right operating rule is: reserve depth is pre-check and finite; exhaustion is a valid fail-closed outcome; no one may pressure the checker to answer an item they believe violates HC-7.

### 7. Real-Data Boundary

This harness can operate on `authorized_measurement` inputs if invoked later under authorization. It is therefore not a build-only no-real-data artifact like the acquisition harness.

The source does enforce production constraints before such use:

- authorized full preparation requires 500/200/150 labels and floor 30;
- authorized pilot requires 90/40/20 and floor 10;
- authorized full preparation refuses to start without a separately approved non-negative `additional_covariance`;
- passphrase file must be private (`chmod 600`);
- private/checking/output roots must be disjoint;
- existing roots are not overwritten.

This gate only says the harness is acceptable as a prepared implementation. It does not start or authorize a real run.

## Weakest Thing

The weakest thing is operational custody, not the math: browser-only access is required for the "sealed key unreachable from the checker" claim. The code keeps truth/parity out of the HTTP and package path, but a checker with shell access to the checking assets can compare PNGs, and a checker with access to `checker_H_control.json` can see opaque replacement/repeat relations and forge event MACs. The operating instructions state this, and the gate depends on it being followed.

## Final Ruling

PASS for the reworked HC-1H harness as an implementation/custody artifact, with the operating boundaries above.

No real hand-check, real-sky run, publication, acceptance, commit, or push is authorized by this report. Duho owns acceptance.
