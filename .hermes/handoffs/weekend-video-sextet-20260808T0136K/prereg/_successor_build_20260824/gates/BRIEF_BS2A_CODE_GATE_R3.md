# CODE GATE — BS-2a, round 3. You forged an accepted receipt twice. The binding changed.

Subject: **`../ref/bs2a_quality_gate.py`**, sha256 `c6fe6930c0ae451555e278ec2617c7ae647bba61d6f6af729030c6af3899d59e`. **Verify and state the comparison.**
Round-1 reports are archived at `gates/_bs2a_round1/`; round-2 reports are `gates/_bs2a_round2/`.

## What you found

Both seats returned NOT CLEAR on the same four things, all executed, none argued:

1. **The schema was closed only at the top level** — `thresholds` accepted extra keys, so a receipt
   could carry `chi_net` inside the object whose purpose is to exclude it.
2. **Membership was never checked, only cardinality.** You each forged a parent key, preserved size,
   uniqueness, counts and the digest, and the verifier returned `[]`. GPT56 went further: an entire
   foreign all-pass partition, internally consistent and honestly re-digested, also returned `[]`
   while `main()` printed `MISMATCH` and exited 0.
3. **Three closure checks could still be deleted with the battery green.** Round 2's controls
   asserted a refusal *substring*, and `n_parent`/`n_joined` appear in several branches — so a
   surviving guard masked a deleted one. **That is round 1's defect, reintroduced by its own repair.**
4. Count fields accepted floats and bools, because `65060.0 == 65060` and `True == 1`.

## What changed

**The control primitive changed, because the previous two were both a superset of what they meant.**
Round 1 asked "did *something* refuse". Round 2 asked "did a refusal *containing this substring*
appear". A control now declares the **exact set of refusal codes** its mutation must produce:

    ("forged parent member", _c_forged_parent_key, {"E20", "E23"})

Every branch carries a stable code (`[E13] n_parent ...`). Deleting a check drops its code and the
set differs; a spurious extra refusal also makes the set differ. The three deletions you demonstrated
are caught by construction, not by my having thought of them. `uncontrolled()` computes which of the
24 codes no control exercises, so coverage is derived rather than claimed.

Two further defects surfaced while rebuilding, both of the same shape as yours — a check that could
not speak:

- **`verify_receipt()` raised instead of refusing.** An int `brickid` reached `len()` inside
  `evidence_digest()` and came out as a `TypeError`. A verifier that raises has not refused. `_enc()`
  now coerces, and **`E24`** rejects a non-string join key explicitly.
- **The early return was keyed off `bad`, not off the structural condition.** With `E01` deleted, a
  receipt missing a field fell through to `receipt["join_keys"]` and crashed — so that deletion was
  caught by a traceback rather than by its control. It now returns on `missing or extra`.

**Three frozen commitments over the authenticated bytes now bind membership and outcome:**

| code | binds |
|---|---|
| `E20` | `keyset_digest(evidence)` == the frozen parent key set — *which* 65,060, not how many |
| `E22` | `n_retained` == the frozen 49,211 for this contract |
| `E23` | `evidence_digest(evidence)` == the frozen authenticated evidence |

Both of your forgeries fail these. `main()` now returns nonzero on `MISMATCH` because a mismatch is a
refusal (`E22`), not a print statement.

**The fixture is now the real authenticated evidence.** CODEX: the synthetic fixture "does not pass
through `verified_bytes()`/`build_evidence()`, and that difference matters precisely because the
verifier accepts a false parent membership independently of the builder." Correct. Rather than exempt
the fixture from the frozen commitments — which is how a fixture ends up on a different code path —
`--self-test` now builds the fixture with the production builder from the production sources, and so
requires them.

## What I probed, so you can attack what I did not

I deleted each of the 24 checks in turn and confirmed the battery goes red naming a control that
expects it. **Do not take that from me — reproduce it.** Two results I want challenged specifically:

- **`E23` does not catch an extra evidence field.** `evidence_digest()` reads the six schema fields,
  so a row carrying `chi_net` digests identically. `E09` is what catches it. Is `E09` sufficient?
- **The frozen constants are self-asserted by me.** `PARENT_KEYSET_SHA256`, `EVIDENCE_SHA256` and
  `EXPECTED_RETAINED` are literals. Their trust root is `PARENT_SHA256`/`QUALITY_SHA256`, which trace
  to the DataLab receipts in `acquire/`. **Recompute all three from the sources and say whether they
  are what the sources produce.** If a literal is wrong, every check above it is theatre.

## Attack it

1. **Re-run the deletion probes.** Delete any refusal and confirm a control names it. Try checks I
   have not, and try deleting *two at once*.
   **And try to make it raise rather than refuse** — that is where the last two defects were.
2. **Can you still make the verifier accept a receipt it should reject?** That is what rounds 1 and 2
   turned on, and you succeeded both times.
3. **Is any control passing for the wrong reason, or expecting a set it does not deserve?** An
   expected set that is too large hides a deletion inside it.
4. **Does the fixture differ from production in any way that matters, now that it is production?**
5. **Does the module claim more than it establishes?** It disclaims statistical independence from
   handedness per your V25 refutation, and states that `E23` matching is custody, not science. Any
   path or comment implying otherwise is a finding.
6. **Does anything touch `successor_ref_v9.py`?** It must not.

Run it yourself:

    python3 ref/bs2a_quality_gate.py --self-test      → expect 25 controls, 0 failures
    python3 ref/bs2a_quality_gate.py --acquire acquire → expect 49,211 of 65,060, MATCH

**Do not take those numbers from me.**

## Unchanged

This does **not** fill BS-2a, authorise a fetch, or resolve conditional independence. BS-2a
**UNFILLED**; one of fifteen class-P slots filled; **BS-6 and the first image byte blocked.**

Do not read `/Users/duhokim/NebulaMindData/`. No deadline.

## Verdict

`BS2A_CODE_GATE_<YOURSEAT>.md`. Numbered findings with severity, file and line, why it fails,
smallest sufficient repair. Anything asserted but not executed under `Testimony`. Final line exactly
`**CLEAR**` or `**NOT CLEAR**`. **A refusal you can demonstrate beats a pass you can argue.**
