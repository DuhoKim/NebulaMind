# BS-3g fill plan — read-only survey, 2026-09-03

## Scope and bottom line

This is a SURVEY and fill plan only.  No executable was changed or run, no receipt was emitted,
no V137 text was drafted, and no pixel or real-data path was opened.  The surveyed V136 bytes are
`PREREG_SUCCESSOR_DRAFT_V136_20260903.md`, recomputed sha256
`90ee001ae3b0828843c1efd91154834a431de055c6e3b0c974e8f63367398ecd`.

Two entries on the older decision-board blocker line are already closed in V136.  Contrary to the
literal older wording “`gates/replay_harness.py` digest (set when built)”, the harness is BUILT and
pinned.  Contrary to any reading that the BS-3g schema entry is still absent, `BS3G-V1` is already
in the successor layer and its entry digest is pinned.  What is not present is a fixture-scoped,
twenty-field BS-3g candidate plus an independent verifier which proves every value from the frozen
fixture bytes.  The existing `run/bs3g_sweep_runner.py` is a self-check/refusal scaffold, not that
producer.

## 1. What exists

### Operative pins and clearance

All hashes below were recomputed from the files currently on disk.

| artifact | recomputed sha256 | status and authority |
|---|---|---|
| `ref/successor_ref_v9.py` | `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` | FROZEN v9; the replay manifest pins these exact bytes.  It intentionally has no BS-3g schema entry. |
| `gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md` | `1c3ced94086be0f1995a71435ee59dff8a0d84633c44593adcc73d6c434b1f20` | gain-v6 scoped CLEAR by CODEX and GPT56; the reports explicitly do not turn the unmeasured control into a result. |
| `ref/gain_gradient_estimator.py` | `e227029713396a920f76d33eed2383339dd0e566e1cdbb6818092ec4403727fd` | CLEAR for gain-v6 scoped repairs by CODEX and GPT56 (`gates/GAIN_V6_REVIEW_CODEX.md` sha `8900463c555d4ee2c354d16784d3ffbcef524dc50594a2192f1512454c12616f`; GPT56 report sha `6db2707859272812ab2174892687b20c451a4858aa62d3939b7327793c275bf1`). |
| `gates/verify_mu_gamma.py` | `e33d9275d80787437429af7aa5989f3b886a8d1a477eddd55459e2270e046d04` | same two-seat gain-v6 scoped CLEAR. |
| `ref/gain_gradient_kernel.py` | `10dd6f62074f30a3d98ff3838c98463eb2574e99012b6db00d8454b1f25978ab` | frozen vector kernel named by V136.  It was part of the gain-control chain, but the gain-v6 subject list did not independently grant these current bytes a fresh two-seat CLEAR; treat the pin as inherited, and require the fill verifier to recompute it. |
| `ref/gain_counterfactual_path.py` | `92cbbdf89bd2a494c9cfb9f19fb12a46cf59a16731246cea2e74c56d2454a9b7` | ACTIVE root in the replay harness and compiled from its verified buffer. |
| `ref/gain_mapping_a.py` | `8bc693ffae7009e0967a0b433b9bc7787494da8742457ad381443d4b210b4aa1` | AGY MAPA-V2 SOUND (`gates/AGY_MAPPING_REVERIFY_20260831.md`, sha `58167d0f3fec2a67a30c1cf88c959ca69a948473812e194e8b235cea741c31ee`); principal-confirmed; confirmation-flip check AGY SOUND (`gates/AGY_FLIP_VERIFY_20260831.md`, sha `dc25967b494f232a2a4d8d2680ec7595b36a31dc27175b06f6617c3eb19ef413`). |
| `ref/MAPPING_CONVENTION_COMMIT_20260831.md` | `ff7b2cdb0441702ae471530b794ec43b62d0f9c07e776e308a26a76984fe0ebc` | blind commitment, then confirmed by the principal. |
| `ref/DRAW_MECHANICS_COMMIT_20260830.md` | `32673bd05f988b757a51eb445ae10d5e6a0dbe3d3a7593459db295917192790f` | COMMITTED before a verdict; Amendment 1 fixes zero-based child addressing and Amendment 2 fixes the 50-step endpoint-inclusive grid. |
| `gates/replay_harness.py` | `b6a0592bf881ca9b8b65d1fd6e716e2e845dd47c0f5c763799a40dec9966e4ac` | BUILT V126, re-pinned V132 after confirmation.  AGY flip check SOUND and 7/7; V136 says PIN-READY.  The predecessor K-gate report (`gates/KGATE_REPLAY_20260831.md`, sha `1ea0c0f6c530c9ac92cae1d9a77397f9339ec2240a90bbc7f6e6c8d64c9b3982`) concerns the pre-flip digest, so the narrow flip report is the authority for the current bytes. |
| `run/receipt_strict.py` | `c3cea71615c33ea57780872e47619b6763dad4b6aa2fb6787203dda9ec6d074c` | current successor-layer constructor; V136 referee round 2 recomputed all three entry digests, ran 10/10, and declared F1/F2 closed. |
| `run/bs3g_sweep_runner.py` | `d1b87918e09efa9cfe42cf79c9a9ff68de5ae444ec0765e0d621762b9ea5b387` | EXISTS, but NOT a fill artifact and not cleared for emission.  Its own record (`run/CODEX_BS3G_BUILD_20260901.md`, sha `ac8e8e3d3a0e64f843c2d325f659c676a634ac977213e67a2577884446d12048`) says 14/14 then BLOCKED and “No receipt candidate”.  It hard-refuses production and uses zero-digest skeleton values only to test schema shape. |

The kernel caveat is deliberate: “pinned file” and “two-seat CLEAR on these exact bytes” are not
synonyms.  A V137 fill must not silently promote an inherited pin into a clearance it never received.

### Exact successor-layer receipt path

The mandated path is not v9's permissive `receipt()`.  V136 says: “this entry is
`SLOT_SCHEMA['BS-3g']` **in the successor layer's pinned schema**, with `BS3G-V1` entry digest
`eb8589f5f70656b16dc8ba16e7d78677a0ab0da7b92cb54eddd22fef14e20102`, the one
`receipt_strict()` reads,” and “**BS-3g's producer is bound to `receipt_strict()` and to nothing
else**.”  The entry already exists at `run/receipt_strict.py:SLOT_SCHEMA_SUCCESSOR['BS-3g']`.
Recomputation under its canonical sorted-key JSON entry rule gives the same
`eb8589f5f70656b16dc8ba16e7d78677a0ab0da7b92cb54eddd22fef14e20102`.

The twenty fields, verbatim and in schema order, are:

`mask_sha256` · `calibration_sha256` · `perturbation_manifest_sha256` · `kernel_sha256` ·
`estimator_sha256` · `verifier_sha256` · `mapping_id` · `gamma_hat` · `sigma_gamma` ·
`gamma_bound` · `invariance_outcome` · `n_perturbations` · `n_draws` · `draw_generator_id` ·
`draw_master_seed` · `draw_verdict_digest` · `baseline_verdict` · `delta_gamma_max` ·
`counterfactual_path_sha256` · `replay_harness_sha256`.

No `run/classp_candidates/BS-3g.json` exists.  Therefore the entry is specified and enforced, but
the slot is not filled.

### Replay obligations already carried by the harness

V136 defines `replay_harness_sha256` as “**the digest of the replay harness that carries every
no-caller/type-exact/compile-from-buffer/flags/load-census obligation this section states**.”  The
same section's compact inventory says it carries: “no-caller-objects, type-exact mask construction,
compile-from-verified-buffer with pre-binding, optimize=0, flags and pycache checks, the loaded-object
census, root re-verification.”  The built file spells those out:

- “**NO-CALLER-OBJECTS** — no module, path, or callback crosses the call boundary”; executable
  roots enter through the source-pinned manifest.
- “**COMPILE-FROM-VERIFIED-BUFFER WITH PRE-BINDING**” — each root is read once, those bytes are
  hashed, and `compile(buffer, optimize=0)` executes fresh namespaces in order, with v9 installed in
  `sys.modules` before the counterfactual-path import.
- “**TYPE-EXACT MASK CONSTRUCTION**” — `type(m) is` the loaded namespace's exact mask class, never
  `isinstance`.
- The flag belt requires the cleared environment, `-B`, `sys.pycache_prefix is None`,
  `sys.flags.optimize == 0`, and compile `optimize=0`; the source also sets
  `sys.dont_write_bytecode`.
- “**LOADED-OBJECT CENSUS**” opens after verified load and closes at result acceptance; a Python
  import or `ctypes.dlopen` first occurring during computation outside the manifest refuses.
- “**ROOT RE-VERIFICATION**” re-reads on-disk roots before receipt assembly.  The stated residue is
  pre-hook startup payloads; V136 routes that to BS-2k's clean `-S/-E` launch transcript.

Thus building `gates/replay_harness.py` is not work remaining.  Integrating its shipped machinery
into the fixture-scoped producer, and independently verifying its exact digest, is remaining work.

## 2. What is missing to fill BS-3g

### A. Replace/extend the refusal scaffold with a fixture-scoped producer — medium (about 1 seat round)

Inputs: only frozen fixture objects already inside the pinned estimator, counterfactual-path,
mapping, v9 and verifier modules; the exact 51-value decimal grid; and the 99 committed child
streams.  The producer must not touch `acquire/`, `/Users/duhokim/NebulaMindData/`, cutouts, or any
real BS-2f/BS-8f record.

Constrained bytes: v9 `6a9abbbd…`; estimator `e2270297…`; kernel `10dd6f62…`; path `92cbbdf8…`;
mapping `8bc693ff…`; harness `b6a0592b…`; draw commit `32673bd0…`; strict constructor
`c3cea716…`; the fixture definitions within those exact files.  The existing runner's own comment
“Production is 99x51; --selfcheck is only 2x5” proves it cannot merely be relabelled as the fill.

Required behavior: run 99 × 51 through the replay path with CRN; derive rather than type the grid;
compute the estimator/Jacobian result from the frozen calibration fixture; reduce each draw against
its own `j0=25` baseline; serialize and hash the complete verdict matrix; create all twenty fields;
call `receipt_strict('BS-3g', fields)` exactly once; write a candidate only after every check passes.
The candidate must be visibly classified in surrounding text as **FROZEN-FIXTURE evidence, not a
real-data measurement**.  `gamma_hat`/`sigma_gamma`, mask and calibration digests must bind the
fixture objects actually consumed, never the real-data identities that do not exist.

### B. Independent BS-3g receipt verifier — medium (about 1 adversarial build/review round)

V136's verifier paragraph requires much more than exact field presence: it recomputes all five
module digests; recomputes `gamma_hat` and `sigma_gamma` from the frozen kernel/estimator and checks
the Jacobian path; reconstructs the exact decimal manifest and its count/endpoints/baseline;
replays exactly 99 draws with the committed generator/seed/zero-based children/CRN; recomputes the
row-major verdict digest, per-draw baselines, `delta_gamma_max`, and HELD/FAILED reduction; checks
closed tokens and digest encodings; and refuses a favorable subset.  The verifier must consume the
candidate through `receipt_strict`, not trust producer summaries or import producer helpers for the
science checks.  Add deletion/mutation fixtures for every field and for swapped draw order,
independent per-gamma randomness, 98/100 draws, omitted endpoint, binary-float grid construction,
wrong `j0`, transposed matrix serialization, mask/calibration substitution, Jacobian sign/error,
subclass masks, callback/path injection, optimize/pycache flags, census scrub and post-load root
mutation.

Constrained bytes: all pins in A, plus the exact twenty-field order and `BS3G-V1` digest
`eb8589f5…`.  This is the principal missing enforcement object; `gates/verify_mu_gamma.py` validates
the estimator relationship, but is not a complete twenty-field receipt verifier.

### C. Candidate receipt on frozen fixtures — small after A/B (about 0.25 round)

No candidate exists.  Emit `run/classp_candidates/BS-3g.json` only from A after B passes.  Record
its sha256, its body/envelope digests, the exact fixture-scope label, and whether
`invariance_outcome` is HELD or FAILED.  V136 is categorical: “**ONLY `invariance_outcome = HELD`
CAN FILL THIS SLOT**”; a valid FAILED receipt is a true blocking record and must be surfaced, not
edited or rerun with a friendlier fixture.

### D. BS-SI dependency cleanup — small text analysis; no BS-SI build needed for this fixture fill

The older `DECISIONS_FOR_DUHO.md` line says “BS-SI schema (written when filled).”  V136's actual
§11 state is later and more specific: the producer and verifier are already BUILT/PINNED at V131:
`gates/stratum_index_producer.py` sha
`4e8ee1f3512f154382c81cd505ff07abfbbabf9b19543c34bd42cd94fe5f3a22` and
`gates/stratum_index_verifier.py` sha
`3b397b1b26c3ea196fb3747c35388c94b193bee8a164c4290d3a7ef4e92a67b0`; AGY judged both SOUND and
K-gate PIN-READY (`gates/AGY_BATCH4_VERIFY_20260831.md` sha
`88e9ce786e69e6d43915b0e935a42bc79457d173fcfed24d8a5be1ce58d6edc7`,
`gates/KGATE_BATCH4_RAW.txt` sha
`6549c3289ec8f380989055e85ed7b66eed9b983fe1ec0f2c115b2167d5de5d9f`).  Its schema and sealed
artifact correctly remain SCHEMA-PENDING until P2–P3 because they are χ-derived.

The §7 dependency says BS-SI blocks BS-2f's **allocation** and BS-8p, not the fixture-only BS-3g
design receipt.  Therefore V137 should retire/correct the stale decision-board implication rather
than fabricate a BS-SI artifact pre-pixel.  If a referee finds an operative V136 clause that truly
makes BS-SI a prerequisite of fixture BS-3g (rather than of the later real execution), stop: that is
a dependency contradiction, not permission to leak χ.

### E. V137 amendment and trace products — medium (about 1–2 text/referee rounds)

After a HELD candidate exists, V137 must change the §7 DESIGN inventory/status and §11 receipt item,
pin the new producer/verifier/candidate hashes, say fixture scope in every result claim, preserve the
later real BS-3g obligation described by `run/BS6_CYCLE_RULING_20260901.md` (sha
`cbf1d1ad64c94dedc48a1296c3499aefe1abe9b5759835e7b832b23e9ad11e5b`), update generated counts,
registry provenance and findings map, and add a fill record/signing handoff.  It must use V135/V136's
append-only amendment mechanism: P0-signed V134 remains unchanged; blank signature lines are hashed;
Duho states digest plus UTC in chat; mismatch is not a signature; Hwao records the verbatim relay.

## 3. Decisions

No remaining parameter, roster or design fork for the **fixture-scoped BS-3g fill** belongs to the
principal.  The implementation must faithfully derive the already ruled values:

- Gate semantics: `OPEN_QUESTION_T_COMPLETENESS.md` opens “**STATUS: RULED — option (b), ‘real
  gate’, 2026-08-29. Option (a) is dead.**”  Thus holding observed `p` fixed is not available.
- Mapping: `OPEN_QUESTION_GAIN_SIGN_MAPPING.md` says “**STATUS: RULED — option A
  (position-dependent accuracy, redrawn), with WORST CASE OVER DRAWS**” and defines
  `a(c) = a0 + gamma*(c-cbar)` with signs redrawn.
- Architecture: the principal's verbatim selection is “**Sweep runner owns it (Recommended)**”;
  MappingA remains a one-draw primitive and the runner owns the 99 × 51 matrix/reduction.
- Four conventions: the verbatim selection is “**Confirmed as committed (Recommended)**”: fixture
  `a_hat`, mask mean `cbar`, physical clamp `[0.5+1e-9,1.0]`, and per-bin-means calibration transform.
- Draw count/CRN/bound: V136 quotes the 2026-08-30 sitting as `n_draws = 99`, common random variates,
  and an a-priori frozen range (`k_gamma` moot).
- Endpoints: Duho's verbatim ratification is “**γ range approved as proposed, ±0.25 in 50
  steps**” (`GAMMA_RATIFICATION_20260830.md`, sha
  `bf367191eda9d2762e2d78eac5257c390e61c3642776ba733f4f84eaa7f263a4`).
- Amendment 2: `n_steps = 50`; `delta_gamma = 2*Gamma/n_steps = 0.01`; 51 points; `j0=25`; exact
  canonical decimal zero; zero-based draw children.  Seed is `20260830`; generator is
  `numpy-1.26.4-PCG64-default_rng`.
- Failure consequence: a FAILED receipt is reported and blocks; no mapping search or rerun is
  licensed.
- Scope for this fill: the present instruction fixes FROZEN FIXTURES, not real data.  Selecting the
  already shipped fixture objects and binding their exact digests is builder work, not a new
  principal choice.  A new fixture, altered scientific value, new roster, or weakening of the later
  real-sweep obligation would be OPEN and must stop before implementation; none is presently needed.

The hand-check/reviewer rosters and BS-2k custody slot are outside this fill.  They must not be
smuggled in as reasons to delay or broaden BS-3g.

## 4. Order of work and seat-round estimate

1. **Build (1 round):** minimally replace/extend `run/bs3g_sweep_runner.py`; add an independent
   receipt verifier; reuse pinned modules, do not edit them.  Run only frozen fixtures.  Preserve a
   no-write/dry-run mode until verification is green.
2. **Verify (2 rounds):** local gates: estimator self-test, `verify_mu_gamma.py`, mapping self-test,
   replay-harness 7/7, `receipt_strict.py`, runner fixture battery, new receipt-verifier positive and
   mutation/deletion batteries, exact hash census, and a second execution comparing candidate bytes
   bit-for-bit.  Then one hostile code referee round; repair and narrow re-review if any byte moves.
3. **Candidate receipt (0.25 round):** execute the verified emitter once on frozen fixtures.  If
   FAILED, stop and report.  If HELD, independently reproduce all twenty fields and freeze the JSON
   hash.
4. **V137 (1 round plus repairs):** copy V136; amend only the signature mechanism's permitted
   BS-3g-fill surfaces: header/change scope; §7 BS-3g row/status/count; §11 strict-receipt,
   verifier/pin/inventory and stale blocker wording; generated §10/count/registry references;
   findings map; fill/amendment/signing records.  Preserve V135/V136 signed bytes by reference and
   use the identical amendment mechanism.
5. **Referee/signature (1–2 rounds):** dispatch the exact committed V137 digest via
   `nm_referee_dispatch.sh`, require access proof, hostile code+text review, minimality, trace/lint/
   counts/registry regeneration, and explicit fixture-vs-real challenge.  Repair by V137 candidate
   iteration until SIGNABLE; then hand the blank-line digest to Duho through Blanc and record the
   verbatim signature/UTC relay.

Expected total: **5.25 seat rounds if the first hostile review is clean; 6–7 rounds with one normal
repair/re-review cycle.**  A fixture outcome FAILED ends after roughly 3.25 rounds with a blocking
record rather than a fill.

## 5. Risks a hostile referee should attack

- **Fixture masquerading as measurement.**  Any use of words such as “measured”, the real
  `mask_digest`, real BS-8f calibration, or discharge of the later real-sweep obligation is false.
  The receipt must bind frozen fixture bytes and state exactly that scope.
- **Draw determinism.**  Off-by-one child indexing; calling `spawn` repeatedly; 98/100 draws;
  independent streams per gamma instead of CRN; reusing one child across draws; hidden retry after a
  bad verdict; NumPy-version drift; a matrix whose digest omits order or inadmissible cells.
- **Grid identity.**  “50 steps” means 51 endpoint-inclusive exact-decimal points, not 50 points;
  `j0=25` must be canonical string `0`; `delta_gamma_max` is derived; binary floating construction,
  negative zero, exponent notation or trailing zeros violate the committed serialization.
- **Jacobian correctness.**  The estimator is slope/intercept from the same GLS fit, with
  `J=(-g1/g0^2, 1/g0)` and the full joint covariance.  Sample-mean normalization, diagonalizing
  covariance, pseudo-inverse substitution, silent domain clamping, or producer/verifier sharing the
  same erroneous helper are direct attacks.
- **Harness self-exclusion.**  Caller-supplied module/path/callback; `isinstance` masks; disk import
  after hash; optimize drift/assert stripping; pycache; a scrubbed import; `ctypes.dlopen`; root
  mutation between execution and receipt; verifier importing the producer.  The known pre-hook
  startup-payload gap must remain disclosed and routed to the BS-2k clean-launch ceremony.
- **Subset/sample substitution.**  A digest field alone is not proof.  The verifier must derive the
  fixture mask/calibration digests from exactly the consumed buffers and prove every perturbation and
  draw is represented.
- **Verdict reduction.**  Compare `(i,j)` with that draw's `(i,25)`, not a global baseline or draw 0;
  treat out-of-calibration cells under the specified refusal semantics; never discard a flipping draw;
  only zero flips across the complete matrix yields HELD.
- **Strict-envelope bypass.**  Direct `v9.receipt()`, unknown/extra/missing/empty fields, mutated
  schema order or a changed `BS3G-V1` digest must refuse.  Preserve prior BS2V/BS2A entries with
  `assert_entries_preserved()`.
- **Chi leakage.**  No real sign vector, per-object calibration, BS-SI index, cutout, path callback,
  exception detail carrying object data, or object-indexed receipt field.  Digests must cover whole
  allowed fixture artifacts, not become covert per-object channels.  BS-SI stays sealed and absent
  pre-P2–P3.
- **Historical overclaim.**  The gain-v6 CLEAR is scoped; the current harness's authority is the
  post-confirmation flip review; the existing sweep runner is BLOCKED scaffolding.  V137 must not
  rewrite those histories into broader approvals.

SEAT: CODEX
VERSION: BS3G-FILL-PLAN-V1
OPEN_DECISIONS: 0 NONE
MISSING_PIECES: fixture-scoped 99x51 producer; independent twenty-field receipt verifier; frozen-fixture BS-3g candidate; V137 fill/amendment artifacts; hostile referee and signing closure
