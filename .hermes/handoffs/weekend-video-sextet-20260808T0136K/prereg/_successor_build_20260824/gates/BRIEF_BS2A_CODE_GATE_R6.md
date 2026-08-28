# CODE GATE — BS-2a, round 6. Both your round-5 findings are fixed. This round closes it or does not.

Subject: **`../ref/bs2a_quality_gate.py`**, sha256 `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508`. **Verify and state the comparison.**
Prior rounds: `_bs2a_round1/`, `_bs2a_round2/`, `_bs2a_round3_reports/`, `_bs2a_round4_reports/`,
`_bs2a_round5_reports/`. **Write to `BS2A_CODE_GATE_<YOURSEAT>_R6.md`.**

## You both found the same two things, and they were the same shape

    E21 flags a mistyped count, then E18 adds it        -> TypeError
    E24 flags a non-string join key, then E15 hashes it -> unhashable type

A check fired and the code then used the value it had just condemned. **Both now return on the
structural condition**, which closes the class rather than the instance:

    n_retained = "49211"  ->  {E21}      brickid = []   ->  {E24}
    brickid = {}          ->  {E24}      objid = [1,2]  ->  {E24}

Two controls' expected sets legitimately shrank because the gates now return
(`{E18,E21}`->`{E21}`, `{E20,E23,E24}`->`{E24}`); E18 and E20 remain covered by other controls.

**36 controls, 0 failures, 26/26 codes covered. Digests unchanged, `--acquire` still 49,211 MATCH.**

## The probe I ran, and the one that matters

I re-probed all 26 deletions under a **strict** rule where a crash scores as **NOT detected** and
only a named control failing counts. **26/26 caught by a named control, 0 crash-only, 0 undetected.**
That check exists because my earlier probe scored `rc != 0 and (named or EXCEPTION)` — a crash
counted as detection, which is the same could-not-fail shape this gate keeps finding. **Reproduce it
strictly; do not credit a crash.**

## The standing question, which the principal has already ruled on

Five rounds have each closed one crash site and found the class one level further out: a row's
fields, the row, the containers, the join-key tuple, the condemned-value consumers. **The principal
ruled this does not block a DESIGN slot**, conditional on the fix above and on the limit being
recorded where the slot is claimed. **The module docstring now states two properties separately** —
sound against forgery (established: neither seat could make it accept a receipt it should reject,
all 26 single and 325 pairwise deletions caught, all five frozen constants recomputed without
importing the module) versus hardened against hostile input (**not** established), with the two facts
that bound it: **no crash path is reachable from the builder** (0 of 65,060 rows can produce one) and
**a crash fails closed** — `main()` exits non-zero and can never emit a PASS.

**Attack that framing, not just the code.** Specifically:

1. **Is the recorded limit honest and sufficient?** Or does it still let a reader inherit the word
   "verified" for a property that was not established?
2. **Is "unreachable from the builder" true?** I claim 0/65,060 rows can produce any crash input.
   Check it.
3. **Can a crash produce a false PASS rather than failing closed?** That is the claim the ruling
   rests on.
4. **Find another raise.** Five for five so far.
5. **Can the verifier accept a receipt it should reject?** Neither of you managed in rounds 3-5.
6. **Does anything touch `successor_ref_v9.py`?** It must not.

Run it yourself — `--self-test` (expect 36 controls, 0 failures) and `--acquire acquire` (expect
49,211 of 65,060, MATCH). **Do not take those from me.**

## Say plainly

**Does any remaining defect block FREEZING this component, or only FILLING it?** A clear here pins
the **quality-predicate component** only. BS-2a stays **DESIGN, UNFILLED**: `verify_cutout_integrity`
(Row C2), the confidence threshold, retry and failure semantics, the ledger schema, and §6.3(9)'s
adversarial producer fixtures under transformed cutouts are not built, and those fixtures need
cutouts. **BS-6 and the first image byte remain blocked.**

Do not read `/Users/duhokim/NebulaMindData/`. No deadline. **Budget your iterations so the report
file is written** — that cost a full round already.

## Verdict

Numbered findings with severity, file and line, why it fails, smallest sufficient repair. Anything
asserted but not executed under `Testimony`. Final line exactly `**CLEAR**` or `**NOT CLEAR**`.
