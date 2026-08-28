# RESUME — DESI successor lane, 2026-08-28 17:50 KST, written for a reboot

**Everything below is on disk and committed. Trust the files. Reseed by reading paths, not by
recalling decisions.** Written for a reader with none of today in memory.

## Where the lane actually is

**The preregistration text is done being wrong.** V29 is **CLEAR from both seats** — the first
two-seat clear. V30 adds motivation on top of it and **has not been refereed**.

    V29  542ee7d93dec457a0c9ea55327040550eec530675faf849c4e07750062d99343   CLEAR ×2
    V30  e81becce1b19d88a302ce7004e930467d9b12b24828bcfe037913a2eb978fecc   NOT REFEREED

**Next action: referee V30.** Pattern to copy: `gates/BRIEF_V29_REREVIEW.md` and
`gates/_tmp_w29_round.sh`. Ask specifically whether the added null **overclaims** — a null cited as
motivation can read as the study expecting to find nothing.

## What is blocked, and it is not the text

- **BS-2a** — code exists (`ref/bs2a_quality_gate.py`) and **failed its second gate is pending**:
  round 1 NOT CLEAR ×2, hardened, **round 2 was dispatched and its verdicts were never read.**
  Check `gates/BS2A_CODE_GATE_{GPT56,CODEX}.md` — round-1 copies are in `gates/_bs2a_round1/`.
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
    ref/bs2a_quality_gate.py  --self-test   17 controls, each asserting its own refusal reason

## Nothing is mid-flight

No seat dispatched, no chain running, no watcher armed. V30 completed and was verified before this
note was written. **No artefact here is truncated.**
