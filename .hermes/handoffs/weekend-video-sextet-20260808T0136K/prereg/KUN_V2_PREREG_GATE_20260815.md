# KUN V2 PREREGISTRATION GATE

Recorded: 2026-08-15T01:26:05+09:00

Verdict: HOLD_FREEZE_FOR_METADATA_REPAIR

Plain answer: the substantive v2 protocol is gateable, BS-1 still reads as FAILED, and the 08-14 frozen file was not modified; however, the candidate's supersession-chain self-description is not yet clean enough to freeze because it claims "all three hashes" while omitting the candidate's own hash, and the footer still says `2026-08-14`.

## Exact Bytes Checked

| Artifact | SHA-256 / mode |
|---|---|
| `prereg/PREREG_LONGO_AMPLITUDE_TEST_20260815_CANDIDATE.md` | `6ae6a58cd6d295116257f66888328f346dec2bb080b6c45056cbcab924008df8` |
| `prereg/PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260814.md` | `da2c6a21d994b9af7395347bf881075f855826ff859dd0415f15042f80ed3308`; mode `-r--r--r--` |
| `prereg/PREREG_LONGO_AMPLITUDE_TEST_20260812.md` | `ac43490054b159610385b8faac28dc4e3178161fadd97d66aa0418a1186b7590` |
| `prereg/LANA_ONE_HUMAN_ATTENUATION_20260814.md` | `b2590e4213e225f9869fe782cfe0f55d8d8979dcb470752836a5cd31a58453fd` |

The 08-14 frozen file is still byte-identical to the brief's hash and still chmod 444. I found no evidence that it was modified.

## Gate Findings

### 1. BS-1 status

PASS. The candidate does not present BS-1 as solved or passed unchanged.

It states in the preamble that old BS-1 **FAILED**, that the licence problem was routed around by redesign rather than solved, and that anything reading as a retrospective licence cure is wrong. In the binding-slot register, `BS-1 (REWRITTEN)` says the old validity text `"licence permits derived-catalogue publication"` **FAILED, stays failed as written**.

This is the correct distinction: the old licence limb remains failed; only the replacement aggregate-output validity text can be judged if this candidate passes.

### 2. Supersession chain

HOLD for repair. The chain names the 08-12 draft and the 08-14 frozen file with full hashes, and it names the HC-1H amendment hash. It does not include the candidate's own hash, despite the header saying "Supersession chain, all three hashes" and the brief asking for 08-12 draft, 08-14 frozen, and this candidate.

I understand that embedding a file's own exact hash in itself is not stable. The repair should therefore avoid a false self-description. Acceptable repair wording would be:

```text
Supersession chain: 08-12 draft and 08-14 frozen hashes are embedded here; this candidate is bound by the external Kun gate/freeze record at SHA-256 [hash].
```

or equivalent. What cannot remain is a statement that the document itself carries all three preregistration hashes when it does not.

Second metadata repair: the final signature line still says `— Lana, 2026-08-14.` on a v2 candidate whose header and amendment status are 2026-08-15. This is not a scientific defect, but in a freeze candidate it is the same class of stale self-description that has caused prior custody failures. Change it to `2026-08-15` or remove the date.

### 3. HC-1H incorporation

PASS. The HC-1H amendment is incorporated faithfully on the points I was asked to check:

- one human checker, 850 blinded labels: 500 real, 200 synthetic ground-truth injections, 150 mirrored re-presentations;
- 9 strata with machine committee only as stratifier/allocator/diagnostic, never inside `a`;
- `a` is named as the HC-1H one-human, synthetic-error-corrected attenuation estimate, not as a multi-human truth reference;
- shared-`epsilon_hat` variance is the summed-derivative-then-squared form:
  `sigma_a^2 = sum_s w_s^2 Var(a_hat_s)/(1-2epsilon_hat)^2 + [sum_s w_s(2a_hat_s-1)/(1-2epsilon_hat)^2]^2 Var(epsilon_hat) (+ covariance >= 0)`;
- `a_gate = 0.7905` at `N = 130,076`, and the text correctly says the quality floor `a_LB >= 0.85` binds separately from the power break-even;
- HC-7 includes clause `(v)` for synthetic/repeat identity exposure and makes it a hard protocol-integrity trigger, not a note.

### 4. Amendment drift

PASS. I found the requested preserved elements still present:

- F-10 output boundary and Tori's six cumulative package-wide conditions;
- BS-11 linter rule, cumulative-release registry, and "isolated-package ACCEPT is insufficient" policy;
- STOP rule;
- K-1...K-14 carried by reference, with K-8 and K-14 restated in operative sections;
- canonical sentence: `"A null here does not establish that the sky is isotropic; it rejects only Longo's published amplitude at Longo's published axis if the preregistered rejection rule is met."`;
- per-object and per-label public-release prohibitions updated from 500-row language to the 850-label HC-1H table where live, while the old 500 wording survives only as historical quoted text;
- all eleven binding-slot rows are present, with receipt references.

I also spot-checked receipt hashes named in the binding-slot register against disk for BS-1 through BS-11; the full hashes I recomputed matched the abbreviated hashes in the candidate where those hashes are shown.

## Blocking Repairs

Required before freeze:

1. Repair the supersession-chain wording so it no longer falsely claims the candidate file embeds all three preregistration hashes. Either add an external-hash binding sentence or revise the claim to distinguish embedded predecessor hashes from the external candidate hash.
2. Fix or remove the stale footer date `— Lana, 2026-08-14.`.

These are metadata/custody blockers, not substantive protocol blockers. I do not find a BS-1, HC-1H, STOP-rule, F-10, BS-11, null-boundary, or receipt-register blocker in the v2 substance.

## Release Boundary

This gate does not freeze, publish, accept, commit, push, or authorize any sky run. Duho owns acceptance.
