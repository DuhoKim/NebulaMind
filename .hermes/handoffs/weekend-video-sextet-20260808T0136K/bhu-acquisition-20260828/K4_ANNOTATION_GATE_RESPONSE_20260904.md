# K4 annotation gate — what was applied, what was declined, and why

**Tori, 2026-09-04 14:13 KST.** Response to `K4_ANNOTATION_GATE_20260904_agy.md`
(`VERDICT=ACCEPT_WITH_REPAIRS`, ten repairs). Six of the seven checks passed, including state preservation, fidelity to
the result, the "NOT RUN" honesty and no overreach into the unordered follow-up. The repairs fall into three classes.

## Applied — row selection (repairs 2, 5, 7)

The gate said rows **23 and 25 were over-broad**. A fresh adjudicator, given only that question and told not to be
agreeable to either side, agreed: `K4_ROWSCOPE_ADJUDICATION_20260904_agy.md`, `ROWS_TO_ANNOTATE=24,26,56`.

**The annotation is withdrawn from rows 23 and 25.** Two independent seats against the lane on a scope question is
decisive, and scope here is the principal's authorisation, not a matter of taste.

**One thing worth Duho's eye, recorded rather than acted on.** The adjudicator found row 23 fails the scope test but
**passes the relevance test** — its claim cell records "no perturbation prescription supplied", and K4 is precisely the
demonstration that the derived boundary cannot supply one; the adjudicator's words are that the finding "perfectly
explains and bears on this row's claim". Row 23 is therefore where this result would land hardest, and it is
unannotated because the ruling authorised the construction rows. **Extending to row 23 is Duho's call, not the lane's.**

## Declined — row 54 (repair 9)

The gate wanted row 54 added. The adjudicator disagreed and so does the lane: row 54 carries a finite spherical cloud
(scope test passes) but uses it only for "ground-state effective density used in the Friedmann equation" and makes no
perturbation or CMB claim, so a finding about `ℓ ≥ 2` perturbation modes does not bear on it (relevance test fails).
Annotating it would put noise in the record.

## Declined — the timestamps (repairs 3, 6, 8, and the timestamp half of 10)

The gate asked that `STUDY 2026-09-04 14:04 KST` be changed to `13:29 KST` on the ground that 14:04 "does not trace to
`K4_RESULT_20260904.md` (which states 13:29)". **Declined, with the receipt.**

These are three different events, and the record is meant to distinguish them:

| event | time |
|---|---|
| K4 result filed | 2026-09-04 **13:29** KST |
| Duho's ruling relayed | 2026-09-04 **14:02** KST |
| annotation applied to the table | 2026-09-04 **14:04** KST, stamped from `date` |

A `STUDY` stamp in this table is the time the annotation was applied under a ruling, not the time the result was
written. The lane's own convention confirms it: row 56 already carries `STUDY 2026-09-03 17:18 KST` for K2, while
`K2_RESULT_20260903.md` is stamped 17:11 KST. Applying the repair would date the annotation **before the ruling that
authorised it** — falsifying provenance to satisfy a tracing rule that does not apply to a clock reading.

## Declined as written, fixed better — the entry-56 reference (repairs 1, 4)

The gate was right that `entry 56` does not appear in `K4_RESULT_20260904.md`, and wrong that it therefore fails to
trace: it traces to the governing preregistration, `K4_BOUNDARY_TRANSFER_PREREG_20260904.md` §1–§2, which pins it to
`gaztanaga_mass_mnras_clean.txt` L143. Deleting the identifier, as the repair asked, would have made the record
*less* traceable. **The reference is kept and now carries its citation** in both the freedom map and the synthesis.

## State

Tier, warrant token, standing, stamp and row-id columns are byte-identical to HEAD across the whole annotation; 51 data
rows before and after. Nothing else moved.

K4_ANNOTATION_GATE_RESPONSE_COMPLETE
