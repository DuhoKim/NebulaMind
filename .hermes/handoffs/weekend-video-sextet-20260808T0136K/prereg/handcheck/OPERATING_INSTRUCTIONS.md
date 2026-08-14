# HC-1H one-human hand-check operating instructions

Status: synthetic-only implementation and verification. No real image, real object row, or human measurement has been run through this build.

Authority:

- `_tmp_YUI_HARNESS_HC1H_BRIEF.md`
- `LANA_ONE_HUMAN_ATTENUATION_20260814.md`, SHA-256 `b2590e4213e225f9869fe782cfe0f55d8d8979dcb470752836a5cd31a58453fd`, especially §2, §2b, and HC-7
- `HC1H_ACCEPTANCE_20260815.md`
- `KUN_HC1H_CLOSE_20260814.md`

The old two-checker/adjudicator CLI is superseded. The active CLI creates one `checker_H` capability.

## Requirements

- Python 3.9+
- Pillow
- `cryptography` with AESGCM and Scrypt
- macOS or another Unix platform with `fcntl.flock`
- one private passphrase file of at least 16 bytes, mode `0600`

Never give the checker a shell in the custodian account. Serve only the localhost UI, or use a separate OS account/device. This is capability separation, not an OS sandbox.

## Inputs

The accepted population is JSONL with exactly these fields per row:

- `data_class`: `authorized_measurement` in an authorized run; `synthetic` in tests
- `object_id`
- `image_path`
- `instrument_sign`: `-1` or `1`
- `abs_chi`
- `committee_state`: exactly `agree-confident`, `disagree`, or `low-confidence`

The blind-injection pool is separate JSONL with exactly:

- `data_class`: `synthetic`
- `synthetic_id`
- `image_path`
- `truth_sign`: `-1` or `1`
- `abs_chi`
- `committee_state`: the same three-value vocabulary

All accepted and injection assets must have one common image mode and pixel size. That removes a simple technical identifier; it does not prove visual realism.

The Neyman-prior file is a JSON object with nine keys:

`agree-confident|0` through `agree-confident|2`, `disagree|0` through `disagree|2`, and `low-confidence|0` through `low-confidence|2`.

Each value is the pre-check machine estimate of the stratum agreement probability. The harness uses `N_s sqrt(a_s(1-a_s))`, applies the real floor, respects capacity, and closes the integer total deterministically. The prior file and realized allocation are sealed and receipted.

The accepted real population defines the two numeric |chi| cutpoints. The harness applies those same cutpoints to injections; it does not rank the synthetic pool independently. A tie across a real-population cutpoint fails preparation.

## Prepare a full 850-label stream

```text
python3 nm_handcheck.py prepare \
  --mode full \
  --real-population /private/accepted_population.jsonl \
  --synthetic-pool /private/blind_injections.jsonl \
  --neyman-priors /private/neyman_priors.json \
  --private-root /private/hc1h_key_custody \
  --checking-root /capability/hc1h_checking \
  --passphrase-file /private/hc1h.passphrase \
  --checker-id DUHO \
  --pilot-policy no-pilot-run \
  --additional-covariance <SEPARATELY_APPROVED_NONNEGATIVE_VARIANCE_TERM> \
  --replacement-reserve-per-group 1
```

For `authorized_measurement`, the tool rejects any full design other than:

- 500 real items;
- nine machine-state × |χ| tertile strata;
- Neyman allocation with at least 30 real items per stratum;
- 200 unmarked known-truth injections, balanced 22/23 across the nine strata;
- 150 randomly selected real items re-presented later with opposite mirror parity;
- 850 valid labels from one checker.

The reserve argument prepackages that many same-category, same-stratum replacements for each of the 27 category-stratum groups. Reserve exhaustion fails closed. Increasing it packages more otherwise-unseen assets and consumes more input capacity.

The accepted HC-1H text leaves an additive `covariance >= 0` term without a formula or frozen value. Therefore an authorized full preparation refuses to start unless `--additional-covariance` is supplied from a separate approved ruling. The tool seals that value and adds it directly to `sigma_a^2`. Do not enter zero merely to make the command run. Synthetic fixtures default to zero only to exercise mechanics, not to authorize production inference.

## Prepare the 150-label pilot

Use the same command with `--mode pilot`. For an authorized input, the harness fixes:

- 90 real: exactly 10 per stratum;
- 40 blind injections;
- 20 mirrored retests;
- 150 labels total.

After label 150, the UI requires `Y` or `N` for interface ergonomics. Pilot reduction returns only `PASS-TO-FULL-HC1H` or `INCONCLUSIVE-PILOT`. PASS requires an authenticated complete execution, acceptable UI ergonomics, no systematic HC-7 trigger, and unrounded global synthetic error `epsilon < 0.10`.

The pilot's 40 injections are marked excluded from final epsilon. If a pilot was run, replace the policy and add the two artifact arguments to the later full `prepare` command:

```text
  --pilot-policy exclude-completed-pilot \
  --pilot-private-root /private/hc1h_pilot_key_custody \
  --pilot-public-result /public/hc1h_pilot/hc1h_aggregates.json
```

The harness verifies a committed `PASS-TO-FULL-HC1H` result that emitted no attenuation, opens the completed pilot key, and excludes every pilot injection identity that was selected or prepackaged as a replacement. The full key and commitment record the pilot-chain hashes, excluded count, and `pilot_synthetics_reused=false`. Insufficient fresh pool capacity fails closed.

Important current boundary: the CLI automates fresh-injection exclusion but does not automate the optional carry-forward of the pilot's 90 real and 20 retest labels. A full run prepared by this version starts a fresh 850-label stream. This is conservative but costs the checker 110 labels that the accepted design permits carrying under its stated conditions.

## Run or resume the checker UI

```text
python3 nm_handcheck.py check \
  --package /capability/hc1h_checking/checker_H \
  --control-file /private/hc1h_key_custody/checker_H_control.json \
  --host 127.0.0.1 \
  --port 8765 \
  --open-browser
```

Run the server as the custodian and give the human only the localhost browser. The control file contains opaque replacement/repeat relations and the 256-bit event-MAC key. It must never be copied into the checking capability or human-readable account. The public package contains only sequence, opaque item ID, asset path, and asset hash.

Keys:

- `C`: counter-clockwise
- `W`: clockwise
- `F`: flag this specific item as suspected synthetic/repeat exposure before answering
- `X`: report systematic synthetic/repeat exposure and stop with hard inconclusive
- `P`: pause; after every 50 viewed presentations, acknowledge the mandatory break before continuing
- pilot only after all labels: `Y` acceptable ergonomics, `N` unacceptable

The `F` path records an append-only `ITEM_FLAGGED_HC7` event, discards the item, and appends a predeclared opaque replacement from the same sealed category-stratum group. It does not reveal the category. A specific flag is not itself a hard failure when replacement succeeds. If the group reserve is exhausted, the same action records `REPLACEMENT_RESERVE_EXHAUSTED_HC7`, terminates hard-inconclusive, and cannot be followed by an answer to the exposed item.

The server enforces no more than 50 viewed presentations per session block. It then withholds the next image and token until `P` appends a `BREAK_ACKNOWLEDGED` event. A specifically flagged item counts as viewed. Closing the browser or server does not lose completed events; rerun the same command to resume. The session is HMAC-chained with the private control key, fsynced, append-only, stale-token protected, debounced, and guarded by an inter-process file lock. Recomputing ordinary SHA-256 hashes from the public package cannot forge a valid label chain.

If `X` records systematic identity exposure, run `reduce` once. It does not open the key; it writes a public `hc1h_integrity_event.json` and a private receipt with hard-inconclusive status and the commitment/session hashes.

## Reduce

Only after the UI says complete:

```text
python3 nm_handcheck.py reduce \
  --private-root /private/hc1h_key_custody \
  --checking-root /capability/hc1h_checking \
  --passphrase-file /private/hc1h.passphrase \
  --private-output-root /private/hc1h_reduction \
  --public-output-root /public/hc1h_aggregates
```

Before decrypting, reduction authenticates the public commitment, private preparation receipt, sealed envelope, authority hashes, harness-source hash, session chronology, and exact completion of the sole required label stream. Pilot ergonomics must also be recorded before the pilot key can open.

Private output contains per-presentation identities, types, parity, labels, truth/sign, flags, and unmasked stratum calculations. Public output contains one aggregate JSON and CSV; F-10 masks any real stratum with realized `k < 50`. If any cell is masked, public output also withholds the all-strata gate and final decision as `WITHHELD_F10_MASKED_STRATA`, because otherwise a sole hidden failure could be deduced by elimination. The exact decision remains private.

Full reduction computes:

- raw real agreement by accepted-population stratum;
- global injection error `epsilon` from all 200 full-run injections only;
- corrected `a_s = (raw_s - epsilon)/(1 - 2 epsilon)`;
- accepted-population weighted `a`;
- Wilson-68 score variances at realized counts;
- the shared-epsilon delta term by summing weighted epsilon derivatives before squaring;
- committee-state counts and disagreement/low-confidence rates by |chi| tertile as `enters_attenuation=false` diagnostics;
- mirrored-repeat non-flip rate and its 2-sigma compatibility with epsilon;
- repeat trials/non-flips by enforced 50-presentation session block as a drift diagnostic only;
- per-injection-stratum 2-sigma diagnostics;
- exact, unrounded HC-1H gates: `a_LB = a - 1.645 sigma_a >= 0.7905`, binding quality floor `a_LB >= 0.85`, every corrected stratum at least `0.70`, `epsilon <= 0.05`, compatible repeat/injection diagnostics, and no systematic HC-7 exposure.

Preparation pins the adopted power-bound population `N=130,076` with `a_gate=0.7905` in both the public commitment and sealed key. Reduction rejects a changed pair.

## Synthetic verification

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_nm_handcheck
PYTHONDONTWRITEBYTECODE=1 python3 run_hc1h_synthetic_selftest.py
PYTHONDONTWRITEBYTECODE=1 python3 independent_verify_hc1h.py
```

These commands use generated images and rows only. They do not authorize real data, publication, HC-6, acceptance, commit, or push.