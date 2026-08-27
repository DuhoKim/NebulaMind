# REPAIR BRIEF — V18. Three convergent blockers, and a clause V17 breaks by restoring it.

Base: `../PREREG_SUCCESSOR_DRAFT_V17_20260827.md`, sha256
`1a0a259a91f5a73a80fc864148e5fb6b0a2014dbf2494d243484e3948c16fce5`. **Verify before starting.**
Read `V17_WHOLE_REVIEW_GPT56.md` and `V17_WHOLE_REVIEW_CODEX.md` in full first.

**Write `../PREREG_SUCCESSOR_DRAFT_V18_20260827.md`.** Do not edit V17 in place — it is a reviewed
artifact. **Do not touch V15 or V16**; both are checked immutable before and after.

## Credited — five repairs hold, do not disturb them

Both seats confirm: the pinned digest matches, the document is structurally complete through §11,
**§6.3's restoration has operative normative bodies rather than titles**, §4 now carries Row J's
calibration gate, §10's false "§4 applied" claim is gone, §7's counts hold, and Row P no longer cites
V15 line numbers.

## Blocker 1 — §2.7's advertised deletion did not land (both seats)

Reason (d) is **still live**, and the replacement threshold sentence is defective. CODEX: *"A
pre-image frozen design must define one confidence predicate and one authority; Row P can apply that
predicate but cannot be an alternative authority."*

**Repair:** actually remove reason (d) and its contract. Define **exactly one** confidence predicate
with **exactly one** authority. Row P *applies* it; Row P is not a second place it may be defined.
Then check every cross-reference to (a)–(d) resolves.

## Blocker 2 — the canonical registry mixes two cardinalities (both seats)

§5 line 466 says `run_production_verdict()` "emits exactly one outcome from the canonical registry."
The registry then lists **per-attempt exclusions** alongside **run-level outcomes**. A run emits one
run-level outcome and *many* per-attempt exclusions, so **"exactly one" and clause 10 cannot both
hold**. It fails in both directions against §5 and Rows I/P.

**Repair:** split the registry by cardinality. **Run-level outcomes** — exactly one per run: the
numeric verdicts, the pre-statistic inconclusive halts, the accounting refusals, `VOID`. **Per-attempt
exclusions** — zero or more per run, never a run outcome. Scope §5's "exactly one" claim to the
run-level set explicitly, and re-run clause 10 against both sets in both directions.

This is the seam I predicted when asking for the registry, and it arrived. Adding a categorisation
surface creates new double-assignment and orphan risk; **build the split so the categories cannot
overlap by construction, not by assertion.**

## Blocker 3 — the scalar/profile threshold omits the calibration gate's precedence (both seats)

The new §3 sentence says `max_b |â_b − â| <= 0.03` selects scalar and **"selects the profile path
otherwise"** — with **no condition on `all a_LB_b >= 0.85`**. That contradicts §6.3 and the pinned
implementation at `../ref/successor_ref_v9.py` lines 1492–1496, and it assigns a profile path where
the calibration gate should already have halted the run.

**Repair:** state the precedence explicitly. **The calibration gate runs first**: any `a_LB_b < 0.85`
emits `INCONCLUSIVE-BY-CALIBRATION` and halts pre-unblinding. **Only on the complement** does the 0.03
spread test select scalar or profile. **Read lines 1492–1496 yourself** and conform to what the code
does, not to my description.

## Blocker 4 — restored §6.3 created an obligation V17 itself breaks (CODEX 4)

§6.3, as restored, **requires every gated revision to carry its finding→change map in §10.** V17 has
**no V16→V17 repair-trace entry.** The clause you restored is violated by the revision that restored
it.

**Repair:** add the **V16→V17** trace entry to §10, and the **V17→V18** entry for this pass. Then make
adding the trace entry part of every future revision, since the clause now demands it.

## Repair 5 — the chronology fix reached the banner but not the fold record (GPT56 4)

The three-moment chronology — instructed 21:48 before verdicts; verdicts landing during assembly at
21:52:33 and 21:53:46; final bytes after the schema repair — was applied to the banner and **not to
the fold record itself**, which still says the artifact was folded before the verdicts existed. Apply
it in both places, with the same wording.

## Repair 6 — §10 still makes the historical claim (GPT56 5)

Remove it.

## Then audit your own result

Clause 10 across §§0–11, **both directions**, against **both registry sets**. Every threshold —
value, phase, failure effect. And check that no repair here breaks something adjacent: three of the
last four rounds introduced a defect while fixing one.

## Standing state

Findings 1, 2, 2b and 3 **UNRESOLVED**; **BS-2a REFUSED**; rows C2 and E cannot run; **BS-6 and the
first image byte blocked**; `verify_lock()` and the unblinding-receipt schema required work, not
implemented.

## Deliverable

`../PREREG_SUCCESSOR_DRAFT_V18_20260827.md`, complete, single write, titled **V18**.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.
