# CODE GATE — BS-2a, the catalogue-quality exclusion predicate

Subject: **`../ref/bs2a_quality_gate.py`**, sha256 `4e205c67d7efc72a0432b8ac4d7ddeb0f6514d01c21f791011eb6427ab2d2c62`. **Verify and state the comparison.**

This is a **code review**, not a document review. The closure mechanism went v5→v9 under this kind of
scrutiny and cleared; this file has had none.

## What it is for

V29 §7 has **BS-2a as DESIGN, CLASS P — UNFILLED**, gated as **text AND code before any image byte**,
blocking **BS-2f and BS-6**. The text is cleared — both seats returned CLEAR on V29. **This file is
the code half.** If it holds, BS-2a can be filled; until then it cannot.

## The frozen contract it must implement

From V29 §2.7(7) and Row E:

    flux_ivar_r  >  8.4000532
    psfsize_r    <  1.5699703
    nobs_r       >= 3

    quality source sha256  61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3
    parent source  sha256  425a42c3ea2a6004a08b52c27201dbf59546e88fef4f3d3ba6d2ffb5a3f70831
    parent rows            65,060 (identity unchanged)
    join                   one-to-one on (brickid, objid)
    realised partition     49,211 retained

**Check the constants against the document, not against this brief.**

## What it claims

Run it yourself:

    python3 ref/bs2a_quality_gate.py --self-test
    python3 ref/bs2a_quality_gate.py --acquire acquire

It reports 7 controls / 0 failures, and `n_retained 49,211 … MATCH`. **Do not take that from me** —
my account of a tool's output has been wrong twice today and both of you caught it.

## Attack it

1. **Can the verifier be made to accept a receipt it should reject?** Every control is a rejection I
   thought of. Find one I did not. Specifically: can a receipt assert a partition the evidence does
   not support, or carry a field that leaks χ, and still pass?
2. **Is any check vacuous?** Three guards I wrote today reported clean while unable to fail. Disable
   a check and confirm `self_test()` notices. If a control passes for the wrong reason, that is the
   finding.
3. **Is the join actually exact?** Duplicates, orphans on either side, and missing parents are meant
   to be refusals rather than silent drops. Construct each.
4. **Is `verified_bytes()` a real custody boundary**, or does it verify a path and then read
   something else? Compare against the v9 pattern it borrows from.
5. **Does `evidence_digest()` actually bind the evidence?** Reorder rows; mutate a float; check the
   digest moves when it must and does not when it must not.
6. **Does the module claim more than it establishes?** Its docstring says the predicate is
   outcome-blind with respect to unobserved χ and **explicitly disclaims statistical independence
   from handedness**, per your own V25 refutation. **If any code path or comment implies the stronger
   claim, that is a finding.**
7. **Does anything here touch `successor_ref_v9.py`?** It must not. v9 is frozen.

## What it does not do, and must not be read as doing

It does **not** fill BS-2a. It does not authorise a fetch. It does not resolve whether the predicate
is independent of handedness *conditional on position* — V29 records that as **not established**, and
nothing in this file changes that.

## Standing state

BS-2a **UNFILLED**; one of fifteen class-P slots filled; BS-2v UNRESOLVED; Stage P superseded; **BS-6
and the first image byte blocked.** No image byte fetched or authorised.

Do not read `/Users/duhokim/NebulaMindData/`. No deadline.

## Verdict

`BS2A_CODE_GATE_<YOURSEAT>.md`. Numbered findings with severity, file and line, why it fails, and the
smallest sufficient repair. Anything asserted but not executed goes under `Testimony`. Final line
exactly `**CLEAR**` or `**NOT CLEAR**`.

**A refusal you can demonstrate is worth more than a pass you can argue.** Judge independently.
