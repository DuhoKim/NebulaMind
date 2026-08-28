# RESUME — DESI successor lane, updated 2026-08-28 19:15 KST (post-reboot, two rounds in flight)

**Everything below is on disk and committed. Trust the files. Reseed by reading paths, not by
recalling decisions.** Written for a reader with none of today in memory.

## TWO ROUNDS ARE IN FLIGHT RIGHT NOW — read their reports before doing anything else

Dispatched 19:11 and 19:20 KST, four seats. If this session died, the seats may still have written:

    gates/V31_WHOLE_REVIEW_{GPT56,CODEX}.md    V31  ce1b6914eae0d36b38d5fc77bb0a8d17c3502d4a007611ad39efe7fe78f1349c
    gates/BS2A_CODE_GATE_{GPT56,CODEX}.md      code c6fe6930c0ae451555e278ec2617c7ae647bba61d6f6af729030c6af3899d59e

**Check those four files first.** Briefs are `gates/BRIEF_V31_REVIEW.md` and
`gates/BRIEF_BS2A_CODE_GATE_R3.md`; runners are `gates/_tmp_v31_round.sh` and
`gates/_tmp_bs2acode_r3.sh`. **If `BS2A_CODE_GATE_*.md` is still dated 16:40/16:41, round 3 never
wrote and those are the round-2 reports** — round-2 copies are safe in `gates/_bs2a_round2/`.

**V30 was NOT CLEAR from both seats** (`gates/V30_WHOLE_REVIEW_*.md`) on: the §1 monopole/dipole
conflation, and `prereg_trace.py --check` failing on a missing V28→V29 §10 row and a missing
V29→V30 sidecar entry. GPT56 additionally found §1 line 122 overstated McAdam & Shamir. **V31
repairs all three** — see commit `efb2fd04f`.

**`hermes` is NOT on the agent shell's PATH after a reboot.** Use
`/Users/duhokim/.hermes/hermes-agent/venv/bin/hermes`. A bare `hermes` dies with `command not found`
and the runner log shows dispatch and done at the **same second** — that is the tell, not a fast run.

## Where the lane actually is

**The preregistration text is done being wrong.** V29 is **CLEAR from both seats** — the first
two-seat clear. V30 adds motivation on top of it and is **under review as of 19:09**.

    V29  542ee7d93dec457a0c9ea55327040550eec530675faf849c4e07750062d99343   CLEAR ×2
    V30  e81becce1b19d88a302ce7004e930467d9b12b24828bcfe037913a2eb978fecc   NOT CLEAR ×2
    V31  ce1b6914eae0d36b38d5fc77bb0a8d17c3502d4a007611ad39efe7fe78f1349c   IN REVIEW

**The V31 §1 paragraph is the thing to watch.** V30 divided a direction-independent annotation
excess by a dipole amplitude. The first repair removed the ratio and lost the argument with it; the
principal caught that. **The danger is projection, not magnitude** — a bias that large needs only
mild position-dependence to counterfeit a dipole of comparable size, and BS-3's
`antisymmetry_receipt` bounds that component by measurement rather than assumption. **No numerical
projection fraction is asserted**, because GPT56 showed the ~15% is a relative difference between
annotation counts and does not share a denominator with a normalised amplitude. The open risk is
that the paragraph has now retreated too far to motivate BS-3; the seats were asked both ways.

**Line 122 adjudication (the seats disagreed):** GPT56 said V30 overstated McAdam & Shamir; CODEX
ruled it held. **GPT56 was right** — verified from arXiv:2302.06530's body, which says of Land's
mirrored-image control "these probabilities are not considered statistically significant" (P~0.13,
P~0.21). CODEX had read only the abstract, which does not isolate that residual.

## What is blocked, and it is not the text

- **BS-2a** — code is `ref/bs2a_quality_gate.py`. **Rounds 1 and 2 were both NOT CLEAR ×2**; round 3
  is in flight. Round-1 reports in `gates/_bs2a_round1/`, round-2 in `gates/_bs2a_round2/`.
  Round 2's finding was that both seats **forged a receipt the verifier accepted** (a substituted
  parent key; a foreign all-pass partition), and that three checks could be deleted with the battery
  still green. Round 3 binds membership with three frozen commitments (E20 key set, E22 retained
  count, E23 full evidence), makes every control assert an **exact refusal-code set**, and makes the
  fixture the real production evidence. All 24 checks were deletion-probed — see the commit body of
  `7e0b327d6`. **Re-run `python3 ref/bs2a_quality_gate.py --self-test` (25 controls) before trusting
  any of that.**
- **BS-2v** VOID converter UNRESOLVED. **BS-5p** unfillable, Stage P superseded on the 49,211 mask.
- **BS-6 and the first image byte remain blocked. Nothing is authorised to fetch.**
- **One of fifteen class-P slots is filled.**

## Today's science, all computed and committed

- **`gates/BS2A_QUALITY_CUT_RECEIPT_20260828.md`** — authorised catalogue metadata query (no images).
  Frozen absolute thresholds `flux_ivar_r > 8.4000532`, `psfsize_r < 1.5699703`, `nobs_r >= 3`.
  65,060 → 49,211, `N_eq` 147,578 → **110,983** against the 100,000 floor.
- **`gates/CONDITIONAL_INDEPENDENCE_PARITY_TEST_20260828.md`** — `e2` is parity-odd, `e1` is the null
  control; no parity-odd selection (χ² 7.5 vs 4.3), **bounded under ~0.75%** by injection, and the
  Longo axis sits at the **31st percentile of 300 random axes**.
- **`gates/MIRROR_TEST_DESIGN_20260828.md`** — `d(g) = χ(g) + χ(Mg)` is **mirror-invariant, therefore
  parity-even, therefore cannot carry a parity-odd dipole.** That is the blinding proof. Its home is
  BS-3's existing `antisymmetry_receipt` field. **Needs images; blocked.**
- **`gates/GALAXY_ZOO_MIRROR_CHECKED_20260828.md`** — Land et al. 2008 verified from source.
- **`gates/FRAMING_LEVERAGE_IS_IDENTIFIABILITY_20260828.md`** — `Var(cos θ)` is slope information, so
  leverage is identifiability, not efficiency. **Read its retraction section**: my claim that the
  predecessor's decline ground was weak was WRONG and is retracted there.

## Standing corrections a fresh context would otherwise repeat

1. **`hermes -Q` does not exist** despite RESOURCE_CATALOG saying so. Use `hermes -z`.
2. **All three coordinators are `claude-opus-5[1m]`.** All-models weekly governs, not Fable.
3. **Twelve of my own checks were wrong today**, every one in verification rather than in a seat's
   work. Three shapes: a check that cannot fire, a check passing for the wrong reason, a check
   reporting on more than it covers. **Both linters now carry negative controls — run
   `--self-test` before trusting either.**
4. **CODEX finds these by constructing cases, not by reading.** Deletion probes and synthetic drafts
   found what careful reading did not, twice.

## Tools written today

    tools/prereg_lint.py      --self-test   6 controls, coverage computed not asserted
    tools/prereg_counts.py    --write       emits §7 counts from the table
    tools/prereg_trace.py     --self-test   3 scope rules; --check enforces the findings map
    ref/bs2a_quality_gate.py  --self-test   25 controls over 24 checks, each asserting an EXACT
                                            refusal-code set (needs acquire/ — the fixture is the
                                            real authenticated evidence, not a synthetic one)
    gates/_tmp_deletion_probe_r3.py         deletes each check in turn; must report 0 undetected

## State as of 19:15 KST

**Four seats ARE dispatched** (see the top of this note). No other chain running, no watcher armed.
Nothing under review may be edited until its round's POST-CHECK reports the subject unchanged —
mutating a subject mid-review is exactly what the digest pinning exists to catch.

**No artefact here is truncated.**
