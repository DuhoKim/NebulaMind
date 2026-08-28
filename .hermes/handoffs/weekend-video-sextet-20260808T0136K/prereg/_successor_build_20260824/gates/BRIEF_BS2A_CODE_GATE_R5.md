# CODE GATE — BS-2a, round 5. The containers are guarded now, not just their contents.

Subject: **`../ref/bs2a_quality_gate.py`**, sha256 `aa03d1f96f47742b1cd4863b4f0e5ebbeeac66dba787b83175d9b95f702c509f`. **Verify and state the comparison.**
Prior rounds: `gates/_bs2a_round1/`, `_bs2a_round2/`, `_bs2a_round3_reports/`, `_bs2a_round4_reports/`.

**Write your report to `BS2A_CODE_GATE_<YOURSEAT>_R5.md`** — note the `_R5` suffix. Filenames are
per-round from now on, because a round-4 seat was still running when this round was dispatched and
two rounds writing the same filename would silently overwrite each other.

## What round 4 established

**CODEX: NOT CLEAR**, one HIGH finding. Everything else it checked came back fixed: all 276 pairwise
deletion probes caught, every round-2 and round-3 forgery refused, the lying-`__eq__` accepts closed,
`OverflowError` caught, and an extensive new false-accept battery (lying `__eq__` on *correct*-typed
subclasses, `int`-subclass counts, NaN and bool thresholds, duplicated evidence lists, empty-string
join keys) all refused correctly. **It could not make the verifier accept a receipt it should
reject.**

**GPT56's round-3 pair battery completed after its seat died** — `276 pairs tested, silent
(undetected) pairs: NONE`. That independently corroborates CODEX's own 276/276. Two seats, two
implementations, no masked deletion found by either.

## The finding, and the repair

The raise-instead-of-refuse class again, **one level up from where round 3 looked** — at the
top-level parameters rather than inside a row, and reachable with fully JSON-native input:

    receipt = None       → TypeError at set(receipt)
    evidence = 42        → TypeError at enumerate(evidence)
    evidence = {"a": 1}  → KeyError: 0

The dict case is the sharp one. Iterating a dict yields its keys, so `off_schema` **correctly
flagged** index 0 — and then the line written to *report* that refusal did `evidence[i]` with `i=0`,
which is valid on a list and raises `KeyError` on a dict. **The detector fired and the reporter
crashed.**

Repair: `verify_receipt()` now type-checks both containers before anything else and returns
immediately — `E25` for a non-`dict` receipt, `E26` for a non-`list` evidence. Nothing below may
assume its container's shape. Executed here before dispatch:

    receipt=None → {E25}   receipt=42 → {E25}
    evidence=None/42/true/{"a":1}/"notalist"/{} → {E26}
    evidence=[]  → {E16,E17,E19,E20,E23}   (an empty list IS a list; refused on substance)
    34 controls, 0 failures, 26/26 codes covered
    all 26 single-check deletions caught and named by a control
    EVIDENCE_SHA256 and PARENT_KEYSET_SHA256 still reproduce exactly; --acquire still 49,211 MATCH

**And one thing I got wrong, disclosed because you would find it:** my first version of the
container guard returned on `bad` rather than on the structural condition, so deleting `E25` or
`E26` let execution fall through and the deletion was caught by a *traceback* rather than by its
control — the identical defect this module already fixed at the receipt-field level, reintroduced by
the repair for it. My own probe caught it before dispatch and it is fixed; both deletions are now
caught by a named control. **Verify that, and look for the same shape elsewhere.**

**Do not take any of that from me.**

## Attack it

1. **Find another raise.** Three rounds running, this class has been the surviving defect each time,
   each time one level further out. Where is the next level? Consider `--emit` and `main()`, not only
   `verify_receipt()`.
2. **Do `E25`/`E26` hide anything?** They return before every other check. **Construct input whose
   only other defect is below them**, and confirm the short-circuit is not laundering a second fault.
3. **Can the verifier accept a receipt it should reject?** Both seats failed at this in rounds 3
   and 4. Try what neither tried.
4. **Recompute all five frozen constants from the sources, without importing the module.**
5. **Is any control passing for the wrong reason, or expecting a set it does not deserve?**
6. **Does the module claim more than it establishes?**
7. **Does anything touch `successor_ref_v9.py`?** It must not.

Run it yourself:

    python3 ref/bs2a_quality_gate.py --self-test      → expect 34 controls, 0 failures
    python3 ref/bs2a_quality_gate.py --acquire acquire → expect 49,211 of 65,060, MATCH

**Budget your iterations so the report file is written.** A verdict that exists only in a runner log
is not a verdict — that happened in round 3 and cost a full round.

## Unchanged

A clear here pins the **quality-predicate component** only. **BS-2a stays DESIGN, UNFILLED**:
`verify_cutout_integrity` (Row C2), the confidence threshold, retry and failure semantics, the ledger
schema, and §6.3(9)'s adversarial producer fixtures under transformed cutouts are not built, and
those fixtures need cutouts. One of fifteen class-P slots filled. **BS-6 and the first image byte
remain blocked.** Do not read `/Users/duhokim/NebulaMindData/`. No deadline.

## Verdict

Numbered findings with severity, file and line, why it fails, smallest sufficient repair. Anything
asserted but not executed under `Testimony`. Final line exactly `**CLEAR**` or `**NOT CLEAR**`.
**A refusal you can demonstrate beats a pass you can argue.**
