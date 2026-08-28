# REFEREE BRIEF — V31. Both of you blocked V30. Both blockers are repaired.

Subject: **`../PREREG_SUCCESSOR_DRAFT_V31_20260828.md`**, sha256
`ce1b6914eae0d36b38d5fc77bb0a8d17c3502d4a007611ad39efe7fe78f1349c`. **Verify and state the comparison.**

Predecessor: **V30**, `e81becce1b19d88a302ce7004e930467d9b12b24828bcfe037913a2eb978fecc` — **NOT CLEAR
from both of you.** Your reports are `gates/V30_WHOLE_REVIEW_{GPT56,CODEX}.md`.

`diff` V30 against V31: the delta is **four hunks** — the retitle, §1 line 120, §1 line 122, and two
rows appended to the §10 table. Nothing else moved.

## Finding 1 — the monopole/dipole conflation. Both of you raised it; both of you were right.

You independently found that "an unmeasured classification bias … was nearly four times the signal
being sought" compares a direction-independent excess with a dipole amplitude, and that this lane's
own `FRAMING_LEVERAGE_IS_IDENTIFIABILITY_20260828.md` says a constant bias is an intercept and
separable from a slope. GPT56 added that the two figures do not even share a denominator.

**The ratio is gone.** Line 120 now states the estimand distinction explicitly and says the centred
estimator absorbs the intercept. GPT56's "same survey family" point is fixed (Land is SDSS, this
study is DESI Legacy Surveys), and the denominator caveat is stated in-line.

**But my first repair was itself wrong, in the opposite direction, and the principal caught it.**
Removing the ratio also removed the argument. A 15% bias beside a 4% dipole *is* alarming — not
because 15 > 4, but because **a bias that large needs only mild position-dependence to project a
spurious dipole of comparable size.** The paragraph now says the danger is *projection, not
magnitude*, and that BS-3's `antisymmetry_receipt` bounds the position-dependent component **by
measurement instead of by assumption** — which is what makes the mirror test a prerequisite.

**Attack that reformulation.** I have deliberately not asserted a numerical projection fraction,
because the fraction depends on which denominator the ∼15% uses and GPT56 showed that is unresolved.
**Is the paragraph now making a quantitative claim it has not earned, or has it retreated so far
that it no longer motivates BS-3?** Either failure is a finding.

## Finding 2 — you disagreed with each other, and I checked the source

**GPT56 (MEDIUM/BLOCKING):** V30 overstates the reanalysis; the post-mirror residual is P≈0.13 and
P≈0.21 and the paper calls it not significant.
**CODEX (held, item 5):** the abstract reports non-randomness and 2.33σ–3.97σ, so "split" is
even-handed.

**I read arXiv:2302.06530 rather than choosing between you. GPT56 is right, and CODEX's read was
from the abstract, which does not isolate the residual.** The body says of the mirrored-image
control: *"these probabilities are not considered statistically significant, which can possibly
result from the low number of galaxies, but the direction and magnitude of the distribution also
does not conflict with the observed distribution."* The significant results (parity violation
*"lower than 0.01"*, dipole *"2.33σ to 3.97σ"*) come from its own separate analyses, not from Land's
mirrored control.

Line 122 now quotes both, states the distinction explicitly, names **Darius McAdam & Lior Shamir**
in full, and says the reanalysis does **not** establish that Land's post-mirror residual is
significant. **Check those quotations against the source — do not take them from me.** If I have
now overcorrected in the other direction, that is a finding.

## Finding 3 — the trace check

Both of you ran `prereg_trace.py --check` and got exit 1 on two missing obligations. Repaired: the
generated **V28→V29** and **V29→V30** rows are appended to §10, and `gates/FINDINGS_MAP.md` gains
both `V29→V30` and `V30→V31`.

The `V29→V30` sidecar entry names a **human instruction**, not a referee finding —
`PRINCIPAL-20260828-LAND-NULL` — because that transition answered an instruction and inventing a
finding ID for it would be a lie. GPT56 asked for exactly this. **Check that it is honest.**

The V30→V31 row is **deliberately absent** from V31's §10: a draft cannot describe the transition
that created it without changing its own digest. It appears in the next draft.

Run all four yourself and report what you get:

    python3 tools/prereg_lint.py  <V31> --gates .
    python3 tools/prereg_lint.py  <V31> --gates . --self-test
    python3 tools/prereg_trace.py .. --check <V31>
    python3 tools/prereg_trace.py .. --check <V31> --self-test

**My account of a tool result has been wrong repeatedly and both of you caught it. It carries no
weight here.**

## Everything else must still be true

**BS-2a DESIGN/UNFILLED** — its code is in a separate gate round, NOT CLEAR twice, round 3 pending;
**one of fifteen class-P slots filled**; BS-2v UNRESOLVED; findings 1, 2, 2b and 3 UNRESOLVED; rows
C2 and E cannot run; **Stage P `SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK`, BS-5p unfillable
pending rerun**; **BS-6 and the first image byte remain blocked.** No image byte fetched or
authorised. The §1 scope block and **§2.7 line 384** are byte-identical to the V30 you reviewed —
verify that rather than believe it.

A CLEAR means *this is a correct preregistration that is honest about being an unfinished
programme* — not that the study may proceed.

Do not read `/Users/duhokim/NebulaMindData/`. No deadline.

## Verdict

`V31_WHOLE_REVIEW_<YOURSEAT>.md`. Numbered findings with severity, section and line, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`. **Judge independently; do not converge.**
