# CODE GATE — BS-2a, round 4. You made it raise. That path is closed.

Subject: **`../ref/bs2a_quality_gate.py`**, sha256 `e9d2ce3be96e481bf6433ac4736a13b0f8b870da3f40f0cb988d1bf559a1c3c8`. **Verify and state the comparison.**
Round-1 reports: `gates/_bs2a_round1/`. Round-2: `gates/_bs2a_round2/`. Round-3: `gates/_bs2a_round3_reports/`.

## What round 3 established

**CODEX could not make the verifier accept a receipt it should reject.** All 276 pairwise deletion
probes were caught. Every round-2 forgery — forged parent key, foreign all-pass partition, χ nested
in `thresholds`, float and bool counts — is refused. All five frozen constants were recomputed
**without importing the module**, from the CSVs directly, and every one matched. The trust root
holds.

**One defect survived, and it was the other half of the challenge: making it raise instead of
refuse.**

    del ev[0]["flux_ivar_r"]   →   KeyError out of evidence_digest(), not a refusal

`E09` detected the off-schema row and then execution fell straight through into a digest computation
that assumes every row is well-formed. **A verifier that raises has not refused.**

## GPT56: you did not write a round-3 report

You ran 38 minutes and exhausted your iteration budget before writing the file, so
`BS2A_CODE_GATE_GPT56.md` still held your **round-2** report. Your findings survive only in the
runner log, preserved at `gates/_bs2a_round3_reports/GPT56_UNFINISHED_runner.log`. **All three were
reproduced independently here and all three are repaired below.** Your 150/276 pair probes found
nothing silent; CODEX completed all 276 with the same result.

**Budget your iterations so the report file gets written.** A verdict that exists only in a log is
not a verdict.

## The repair

1. **`verify_receipt()` returns on the structural condition.** Once `off_schema` is non-empty it
   returns immediately — before any digest or key computation — mirroring the receipt-level
   `if missing or extra: return bad`. **Keyed off the condition, not off `bad`**, so deleting `E09`
   cannot silently restore the fall-through.
2. **`off_schema` can no longer raise while computing itself.** `isinstance(e, dict)` short-circuits
   before `set(e)`, so a row that is `None`, a string or an int is refused rather than crashing the
   detector meant to catch it.
3. **The encoder is guarded anyway.** `evidence_digest()`'s `enc()` uses `.get()` with a sentinel for
   unconvertible values, so it cannot raise even if reached by another path. **This changes no
   digest of well-formed evidence** — `EVIDENCE_SHA256` and `PARENT_KEYSET_SHA256` both still
   reproduce exactly, which you should verify.
4. **`OverflowError` is caught** (GPT56). `float(10**400)` raised it out of the per-row loop and out
   of the digest encoder; it was not in either `except` tuple. It is now in both.
5. **A lying `__eq__` no longer buys an ACCEPT** (GPT56) — the worst of the three, because it was
   silent rather than loud. `schema_version`, both source digests and `evidence_sha256` must now be
   `str`; threshold values must be `int`/`float`; `join_keys` elements must be `str`. **Folded into
   the existing codes**, so the code count stays 24 and no control changes meaning.
6. **Six isolated controls added**: `row missing a key`, `row is not a dict`, `lying __eq__ schema`,
   `lying __eq__ threshold`, `lying __eq__ digest`, `value overflows float`.

Executed here before dispatch, and you should not take any of it from me:

    del ev[0]["flux_ivar_r"]  →  REFUSED {E09}       ev[0] = None   →  REFUSED {E09}
    ev[0] = "string"          →  REFUSED {E09}       ev[0] = 42     →  REFUSED {E09}
    flux_ivar_r = 10**400     →  REFUSED {E10,E19,E23}
    LiarEq schema_version     →  REFUSED {E03}       LiarEq thresholds  →  REFUSED {E07}
    LiarEq evidence_sha256    →  REFUSED {E19}
    31 controls, 0 failures, 24/24 codes covered
    EVIDENCE_SHA256 and PARENT_KEYSET_SHA256 both still reproduce exactly

## Attack it

1. **Find another way to make it raise rather than refuse.** That is where the last two rounds' real
   defects were. Malformed receipts, exotic types, recursive structures, NaN keys, huge inputs.
2. **Does the new early return hide anything?** It short-circuits every check below `E09`. I have
   re-probed all 24 single deletions; **the pairwise set is yours to redo.** Specifically:
   **construct a receipt whose only other defect is below `E09` and which also carries an off-schema
   row**, and check the short-circuit is not laundering the second fault.
3. **Can the verifier still accept a receipt it should reject?** CODEX failed at this in round 3.
   Try the angles it did not.
4. **Are `row missing a key` and `row is not a dict` isolated, or do they pass for the wrong
   reason?** Both expect exactly `{E09}`.
5. **Recompute all five frozen constants from the sources**, without importing the module.
6. **Does the module claim more than it establishes?** It disclaims statistical independence from
   handedness, and states that digest agreement is custody, not science.
7. **Does anything touch `successor_ref_v9.py`?** It must not.

Run it yourself:

    python3 ref/bs2a_quality_gate.py --self-test      → expect 31 controls, 0 failures
    python3 ref/bs2a_quality_gate.py --acquire acquire → expect 49,211 of 65,060, MATCH

## Unchanged

This does **not** fill BS-2a. A clear here pins the **quality-predicate component** only; the slot
stays **DESIGN, UNFILLED** because `verify_cutout_integrity` (Row C2), the confidence threshold,
retry and failure semantics, the ledger schema, and §6.3(9)'s adversarial producer fixtures under
transformed cutouts are not built — and those fixtures need cutouts, which BS-6 blocks.

One of fifteen class-P slots filled. **BS-6 and the first image byte remain blocked.**
Do not read `/Users/duhokim/NebulaMindData/`. No deadline.

## Verdict

`BS2A_CODE_GATE_<YOURSEAT>.md`. Numbered findings with severity, file and line, why it fails,
smallest sufficient repair. Anything asserted but not executed under `Testimony`. Final line exactly
`**CLEAR**` or `**NOT CLEAR**`. **A refusal you can demonstrate beats a pass you can argue.**
