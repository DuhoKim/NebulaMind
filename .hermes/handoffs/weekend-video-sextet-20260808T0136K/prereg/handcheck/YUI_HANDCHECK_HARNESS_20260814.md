# YUI HC-1H one-human hand-check harness

Status: reworked to the accepted HC-1H design and verified with synthetic data only. No actual pilot or hand check has occurred.

Controlling specification: `LANA_ONE_HUMAN_ATTENUATION_20260814.md`, SHA-256 `b2590e4213e225f9869fe782cfe0f55d8d8979dcb470752836a5cd31a58453fd`, with `_tmp_YUI_HARNESS_HC1H_BRIEF.md`, `HC1H_ACCEPTANCE_20260815.md`, and `KUN_HC1H_CLOSE_20260814.md`.

## What was superseded

The active CLI no longer prepares the old HC-1 design of angular-size × |chi| strata, proportional floor-40 allocation, 500 labels, two checkers, and disagreement adjudication.

The HC-1H path instead uses:

- machine-committee state × |chi| tertile;
- Neyman allocation with a real floor of 30;
- one checker;
- 500 real items, 200 blind known-truth injections, and 150 later mirrored re-presentations;
- noise-corrected agreement and shared-global-epsilon uncertainty;
- the HC-7(v) exposure flag as a real UI action;
- a separate 150-label pilot mode.

## Design

### Accepted-population strata and allocation

The only accepted committee states are `agree-confident`, `disagree`, and `low-confidence`. The accepted real population defines global rank tertiles of `abs_chi`; their two numeric cutpoints are sealed and crossed with committee state to produce exactly nine strata. The same real-population cutpoints classify injections. Synthetic-pool ranks are never computed independently, and a real-population tie across a cutpoint fails closed.

Full real allocation solves `n_s proportional to N_s sqrt(a_s(1-a_s))` subject to `30 <= n_s <= N_s`, where the pre-check machine prior for each stratum is supplied in a separate nine-key JSON document. Cells whose unconstrained quota falls below 30 are fixed at 30; capacity-saturated cells are fixed at `N_s`; the remaining total is redistributed over active cells. Integer closure uses deterministic largest remainders. The sealed receipt must sum to 500 and every realized cell must remain at least 30. The floor is a constraint, not a base tranche followed by a second proportional allocation.

Pilot real allocation is exactly 10 per stratum, 90 total.

### Sealed preparation

Preparation creates a fresh 256-bit root secret. It HMAC-ranks accepted rows, injection rows, repeat sources, parity, opaque IDs, stream order, balanced injection remainders, and replacement groups.

The private key document records source identities and hashes, category, truth or instrument sign, committee state, stratum, mirror parity, repeat parent, stream order, Neyman inputs/allocation, checker identity, authority hashes, and harness-source hash. It is canonicalized, encrypted with Scrypt-derived AES-256-GCM, and written only as an authenticated envelope.

The plaintext-key hash is committed before checking. The private preparation receipt separately anchors the public commitment so an attacker cannot merely modify a public JSON and recompute its sidecar hash.

### One opaque presented stream

The active capability is `checker_H` only. Its public package contains only sequence, opaque item ID, asset path, and asset hash. Replacement groups, repeat parent/dependent links, and the event-MAC key live in `checker_H_control.json` under private custody. The custodian starts the server with that control file; the human receives only browser access.

The full primary stream contains exactly 850 opaque item descriptors:

- 500 real;
- 200 synthetic injections;
- 150 repeats.

Every injection uses the same rendering function, PNG mode, pixel dimensions, package schema, asset route, keyboard path, and progress counter as every other presentation. Item type, source, truth, instrument sign, stratum, and mirror parity are absent from the browser state and HTTP response.

Each repeat source is a secret-keyed random member of the selected real sample. Its image is rendered with the complement of the first presentation's parity. The keyed topological stream scheduler never makes a repeat available before its first presentation, then mixes it into later available positions.

### HC-7 clause (v)

The UI visibly exposes:

- `F`: `Flag suspected synthetic/repeat exposure`
- `X`: systematic exposure

`F` records a hash-chained `ITEM_FLAGGED_HC7` event before accepting a label. The flagged presentation is discarded. The app appends a prepackaged replacement from the same sealed category-stratum group without exposing that group in browser state.

If a flagged real presentation anchors a future repeat, the app also removes that dependent repeat and appends an opaque repeat replacement whose anchor has not been flagged. This prevents the repeat diagnostic from being orphaned after key opening.

Replacement capacity is fixed before checking. The checker cannot make the tool silently draw after seeing an item. If a requested group is exhausted, the flag action records `REPLACEMENT_RESERVE_EXHAUSTED_HC7` and terminates hard-inconclusive; it does not merely reject the flag and allow the checker to answer the exposed item. `X` records `SYSTEMATIC_EXPOSURE_HC7`. Either terminal event prevents key opening and makes reduction publish a hard-inconclusive integrity event anchored to the commitment and checker-session hash.

### Session integrity

The browser receives only current progress, instructions, allowed actions, a one-use presentation token, and the current asset URL. It does not receive answer history or sealed truth.

Each event is canonical JSON with UTC time, previous MAC, and an HMAC-SHA256 made with a 256-bit key held only in the private server-control file. Writes use append mode, an exclusive `fcntl` lock, flush, and fsync. A process records the file size and hash it opened; another process changing the session causes the stale process to fail. The presentation token binds commitment, role, cursor, current item, and current chain head. Browser key repeats, stale tokens, and too-fast submissions are rejected. A party holding only `package.json` can no longer forge a complete chain by recomputing ordinary hashes.

After every 50 viewed presentations, including specifically flagged presentations, the server stops issuing image tokens. The UI requires `P` to append a `BREAK_ACKNOWLEDGED` event before another image can be served. Full synthetic execution exercised 17 breaks because one flagged item made 851 viewed presentations; pilot execution exercised two breaks before its final 50-image block.

Stop/reopen reconstructs the queue, consumed replacement reserves, flags, answers, and chain from committed package plus events.

### Full reduction

Reduction cannot call `unseal_key` until:

- the original commitment and sidecar authenticate;
- the private preparation receipt matches;
- the encrypted envelope hash matches;
- authority and harness-source hashes match;
- the one checker session started after commitment;
- exactly the required valid labels are present;
- no systematic HC-7 terminal event exists.

After opening, reduction verifies the sealed experiment/counts against the commitment, maps any replacements, reverses mirror parity, and separates three products:

1. Real first presentations produce raw machine-human agreement by accepted-population stratum.
2. Known-truth injections produce global `epsilon` and nine diagnostic injection rates.
3. Mirrored repeats produce the presented-sign non-flip rate `epsilon_rr`.

The corrected stratum estimate is:

`a_s = (raw_s - epsilon) / (1 - 2 epsilon)`.

Overall `a` is weighted by accepted-population stratum fractions, not sample fractions.

Beside `a`, the aggregate product publishes committee-state population counts plus disagreement and low-confidence rates for each |chi| tertile. These are explicitly marked `enters_attenuation=false`; they are diagnostics and never modify an agreement, epsilon, weight, or gate.

The aggregate repeat diagnostic also reports trials, non-flips, and exact non-flip rate by enforced 50-presentation session block. Those rows expose fatigue/drift patterns but do not replace or alter the frozen global epsilon_rr compatibility gate.

Realized-count uncertainty uses Wilson-68 score variances. The epsilon contribution is shared across all strata. The implementation therefore computes each derivative, sums `w_s d(a_s)/d(epsilon)` across strata, and squares only after the sum. It does not use the withdrawn diagonal approximation.

The exact unrounded full verdict requires every gate:

- `a_LB = a - 1.645 sigma_a >= 0.7905`;
- binding quality floor `a_LB >= 0.85`;
- every corrected stratum `a_s >= 0.70`;
- global `epsilon <= 0.05`;
- `epsilon_rr` compatible with global epsilon within two combined score standard errors;
- every injection-stratum diagnostic compatible with global epsilon within two combined score standard errors;
- no systematic HC-7 exposure.

There is no rounding before a branch. A lower bound of `0.849` remains inconclusive.

The preparation commitment and sealed key pin the adopted power-bound population `N=130,076` beside `a_gate=0.7905`; reduction rejects a changed bound or gate before interpreting the labels.

Private output contains per-presentation details and all unmasked calculations. Public output is aggregate JSON plus CSV. F-10 leaves each of the nine row identities present but masks all numeric real-stratum detail when realized support is below 50. Whenever any real cell is masked, public output also withholds the all-strata gate and final HC-1H verdict as `WITHHELD_F10_MASKED_STRATA`; otherwise those fields could reveal which sole masked cell failed by elimination. The full decision and identities remain private.

### Pilot mode

Pilot preparation fixes 150 labels:

- 90 real, 10 per stratum;
- 40 blind injections;
- 20 mirrored retests.

After label 150, the checker UI requires an append-only ergonomics `Y`/`N` event. The key cannot open without it.

Pilot reduction returns only `PASS-TO-FULL-HC1H` or `INCONCLUSIVE-PILOT`. PASS requires authenticated clean execution, acceptable ergonomics, no systematic HC-7 trigger, and unrounded `epsilon < 0.10`. The pilot does not issue a full attenuation verdict.

The pilot aggregate contains epsilon, its Wilson variance, and injection-stratum diagnostics only. It deliberately emits no attenuation, corrected real stratum, or repeat-rate statistic, and records `pilot_real_and_retest_values_used_for_pass=false`. The private event table retains raw labels for custody, but the PASS decision does not inspect their agreement or retest values.

Pilot injections are excluded from full epsilon. For a post-pilot full preparation, the CLI requires the pilot private root and public PASS result together, verifies their plaintext-key commitment chain, and removes every selected or reserve pilot synthetic identity before full selection. The full key/commitment records that exclusion. This build still takes the conservative route of preparing a fresh full real/retest stream; it does not automate the optional carry-forward of the pilot's 90 real and 20 retest labels.

## Implementation choices not frozen by HC-1H authority

The accepted amendment specifies the design intent but does not freeze several algorithms. This harness makes the following explicit choices so they are reviewable rather than hidden:

- `abs_chi` tertiles are global cutpoints from the accepted real population, not within-state tertiles; a tie across a cutpoint fails.
- Neyman planning values arrive as a nine-key pre-check JSON file; constrained continuous quotas are closed by deterministic largest remainder, and infeasible floors/capacities fail.
- Full injections are balanced 22/23 across the nine crossed strata; pilot injections are balanced 4/5. The input schema and rendering are harness contracts, not a frozen generator specification.
- A repeat's parity is coupled to be exactly opposite its first presentation. Later stream order is secret-keyed, and repeat selection is capacity-constrained only enough to retain predeclared same-stratum HC-7 reserves.
- `F` is accepted only before an answer; it supplies no free-text reason. Replacement reserve depth is an explicit pre-check argument; exhaustion is hard inconclusive.
- "Wilson variance" is implemented as the squared standard-error implied by the 68% Wilson interval width. Two-sigma diagnostics use the sum of those variance estimates.
- The accepted formula leaves an additive `covariance >= 0` term unfrozen. Synthetic fixtures and the non-estimating pilot use zero mechanically. Authorized full preparation requires a separately approved non-negative value, seals it, and adds it to total variance; absent that ruling it fails before creating output roots.
- No post-hoc diagnostic-disposition override is implemented. A greater-than-two-sigma synthetic-stratum incompatibility remains inconclusive.

These choices make the code deterministic. They do not convert an unfrozen production detail into accepted authority.

## Guarantees enforced by code

Given untampered dependencies, correct OS file semantics, a private custodian root, browser-only checker access, and inputs that satisfy their declared meaning, the harness enforces:

1. The active CLI prepares one HC-1H checker, not A/B/J.
2. Preparation hard-pins all four accepted authority hashes before creating either output root.
3. Authorized full counts cannot differ from 500/200/150 with floor 30.
4. Authorized pilot counts cannot differ from 90/40/20 with 10 real per stratum.
5. The stratum vocabulary and nine-cell shape are exact, and injections use real-population |chi| cutpoints.
6. Neyman allocation closes to 500 and respects floor/capacity.
7. Full primary stream closes to 850; pilot closes to 150.
8. Repeat parity is exactly complementary, repeat order is later, and repeat reserves use distinct previously unrepeated parents.
9. Browser state and public package do not expose item type, source, truth, sign, stratum, parity, repeat links, replacement groups, MAC key, or answer history.
10. Specific exposure flags are events, not prose-only policy.
11. Successful `F` replacement preserves category and stratum counts.
12. Systematic exposure prevents ordinary completed reduction.
13. Session events require the private HMAC key in addition to append/stale-process checks.
14. The sealed key is absent from the checking root and HTTP handler.
15. The key cannot be opened through the reduction function before required completion checks.
16. Pilot ergonomics must be recorded in the UI before pilot unseal.
17. Pilot injections are not represented as full-run injections.
18. Only real first presentations enter raw attenuation.
19. Only known-truth injections enter epsilon.
20. Only repeat pairs enter epsilon_rr.
21. The shared-epsilon covariance term sums derivatives before squaring.
22. Thresholds use unrounded values.
23. F-10 masks sub-50 public cells and withholds the stratum gate, final decision, and failing identities whenever any cell is masked, while preserving private calculations.
24. Machine-committee disagreement/low-confidence rates are published as diagnostics and do not enter `a`.
25. Existing output roots are never overwritten and public/private/custody/checking roots cannot overlap.

## HONEST LIMITS

### The strongest blunt statement

This harness is not a sandbox, not a lie detector, not a perceptual-validity proof, not a guarantee of human independence, and not a scientific result. A PASS means this particular committed byte stream satisfied the implemented checks under the supplied inputs. It does not mean the inputs were honest or scientifically representative.

### A determined checker can still identify items if given shell access

The browser route and public package hide item type and relationships; replacement groups and parent/dependent links now remain in the private server-control file. A checker with shell access to the public asset directory can still compare PNG bytes, mirror-match images, cluster visual style, and identify some repeats or injections with high confidence. A checker who reaches the private control file gets the exact opaque relationships and event-MAC key. The harness cannot detect that inspection.

Therefore the claim "unmarked to the human" is only supportable under browser-only access or a separate OS account/device that cannot list all assets or read private control. Giving the checker the custodian shell destroys that claim.

### It cannot prove synthetic injections look real

The tool enforces equal technical representation: same mode, dimensions, encoder, package fields, route, controls, and counter. It does not measure morphology, noise texture, PSF, artifacts, background statistics, or perceptual realism. A bad generator can produce obviously synthetic spirals and still pass preparation.

The human can notice style leakage that every automated structural check misses. Conversely, a checker can claim to notice leakage when they did not. The harness records the flag, not the truth of the suspicion.

### A checker can deliberately force inconclusive

Replacement reserves are finite. A determined checker can press `F` repeatedly in one opaque group until the predeclared reserve is exhausted, or press `X` immediately. The harness must permit this because HC-7 gives exposure precedence over completion. It cannot distinguish sabotage from honest detection.

### One human is one correlated failure mode

There is no second independent person and no adjudicator. Synthetic truth estimates one human's error on those injections; it does not prove the same error model applies to real images. Learning, fatigue, memory, motor habit, display adaptation, criterion drift, and session timing can differ by category even when category is hidden.

The per-stratum injection and mirrored-repeat diagnostics can detect some large inconsistencies. Passing them does not prove exchangeability between injections and real objects.

### Repeat diagnostics are not a truth diagnostic

A consistent wrong answer flips correctly under mirroring and passes the repeat check. A checker using a deterministic external classifier can also be perfectly repeat-consistent. Low epsilon_rr proves repeat behavior, not scientific correctness or unaided judgment.

### The UI cannot police external tools or memory

The harness cannot detect screenshots, photography, OCR, image search, a second display, another person, an external classifier, hand notes, package copies, or communication outside the browser. It cannot prove the checker did not remember an earlier image.

### Pixel bytes do not prove perceived orientation

The committed PNG hash proves bytes. It does not prove the browser, GPU, display, remote-desktop stack, accessibility transform, or physical monitor showed those pixels without reflection, rotation, scaling artifacts, caching, or color changes. A display-side mirror can invert perception while all file hashes pass.

### Cryptographic commitments do not establish external chronology

The public and private receipts make later inconsistency detectable if an honest copy survives. There is no trusted timestamp, transparency log, witness signature, or remote notarization. A malicious custodian controlling every copy can generate an entirely different internally consistent experiment and claim it was earlier.

### HMAC chaining is not tamper-proof against the control-key holder

The private HMAC key prevents a party holding only the public package/session directory from rebuilding a valid edited chain; unkeyed rehashing is rejected. It does not stop deletion, truncation, or denial of service. A custodian, compromised server process, debugger, or attacker who obtains `checker_H_control.json` can forge events. File permissions and browser-only capability separation remain operating assumptions, not proof of who supplied a label.

### Checker identity is a declaration

The tool hashes the supplied checker identifier. It does not authenticate a person, verify that only one person acted, or prevent credential sharing. `checker_id=DUHO` is not biometric or legal proof that Duho supplied every label.

### Neyman allocation is only as honest as its priors and population

The program checks formula, floor, capacity, and closure. It cannot prove the machine prior rates were estimated only from allowed synthetics, were frozen before outcomes, or are representative. It cannot prove committee states were assigned correctly. A manipulated population, state label, |chi| value, or prior file can alter inclusion probabilities while passing syntax and hashes.

### Noise correction can be numerically valid and scientifically wrong

The correction assumes a shared symmetric error parameter and uses one global epsilon. Real errors may be asymmetric, object-dependent, state-dependent, or coupled to mirror parity. Two-sigma diagnostics have limited power, especially within roughly 22 injection trials per stratum.

Wilson-score and delta-method uncertainty quantify the implemented finite-count model. They do not include generator mismatch, population-selection error, machine-state misclassification, model misspecification, display error, human learning, or malicious behavior.

### A PASS does not prove injection-stratum compatibility in perpetuity

The diagnostics are threshold tests on one finite batch. "Compatible within 2 sigma" means "not far enough apart under this approximation," not "equal" and not "same causal mechanism."

### Pilot PASS is narrow

`PASS-TO-FULL-HC1H` proves only that the synthetic pilot met execution, UI, epsilon, and HC-7 conditions. It does not prove full-run attenuation will pass, full fatigue will be tolerable, or HC-6 power is adequate.

This build does not automate optional pilot real/retest carry-forward. A fresh full run avoids accidental pilot-injection reuse but imposes extra labels. A future carry-forward implementation would need to preserve inclusion probabilities, timing, mirror relation, and committed provenance without opening future truth.

### F-10 masks information

When a cell has fewer than 50 real labels, the public product intentionally withholds its rate and count. A public reader cannot independently reproduce every private stratum gate from public files alone. That is the accepted privacy/product boundary, not full transparency.

### Source retention is not external review

The codebase still contains retained low-level legacy HC-1 helper paths and regression tests so custody/session behavior was not rewritten blindly. The active CLI does not expose the old prepare/adjudicate workflow, but a Python programmer can import internal module functions directly. Operational authority must use the documented HC-1H CLI and receipts; this module is not a policy-enforcement sandbox for arbitrary Python callers.

The standard-library verifier checks source shape, ordering, hashes, and synthetic receipts. It is not an adversarial security audit. No external security-review pass is claimed.

## What a PASS does not prove

A full `PASS_HC1H_ATTENUATION` does not prove:

- the injection generator was survey-realistic;
- the accepted population was correct or complete;
- committee states or |chi| values were honest;
- Neyman priors were valid or frozen at the right time;
- the checker was Duho, alone, unaided, honest, or blind outside the browser;
- the display preserved physical orientation;
- the same epsilon applies to real and injected images;
- repeat consistency means correctness;
- all systematic error is inside sigma_a;
- masked public cells can be independently reconstructed;
- HC-6 has adequate power;
- the scientific hypothesis is true;
- the batch is accepted, frozen, releasable, or publishable.

Synthetic self-test PASS proves even less. It proves that generated fixtures exercised the expected code paths and produced expected receipts. It does not prove behavior on real images or under a hostile operator.

## Verification actually completed

- HC-1H contract/regression suite: passing.
- Accepted-shape synthetic full stream: 850 labels, 500/200/150, nine strata, floor at least 30, 150 later complementary repeats, one successful HC-7 replacement, epsilon `1/20`, repeat non-flips `6/150`; private synthetic fixture PASS and public F-10 verdict withheld because one realized cell is below 50.
- Accepted-shape synthetic pilot: 150 labels, 90/40/20, ergonomics recorded, `PASS-TO-FULL-HC1H`, pilot injections excluded.
- Independent stdlib-only verifier: `82 / 82`.

No real data, actual human pilot, actual hand-check run, HC-6, publication, acceptance, database action, commit, or push occurred.