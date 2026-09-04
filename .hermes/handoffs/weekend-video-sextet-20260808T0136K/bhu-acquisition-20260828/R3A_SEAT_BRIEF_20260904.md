# R3-A — blind seat brief: is entry 59's particle-production coefficient β derived, cited, fitted, or free?

**Authority:** Duho, "run 1 and 2", relayed 2026-09-04 19:52 KST. **Governing document:**
`R3A_BETA_PRODUCTION_PREREG_20260904.md` (frozen V2) — read it in full first; it binds you.

**BLIND.** Do not open, list or grep any file whose name contains `R3A_seat`, `R3A_RESULT`, `R3A_ROUTE2`, `R3A_CHECK`
or `R3A_RECONCIL`. You MAY read the prereg, `K3S1_RESULT_20260903.md`, and the pinned source
`../bhu-reading-20260823/sources/desai_poplawski_2016_plb755_183_vor_clean.txt` (entry 59, Desai & Popławski 2016,
*Phys. Lett. B* 755, 183).

**Standing wording:** the record says **"unreproduced from the stated inputs," not "error."** Hold that line.

## The question

Entry 59 prints a particle-production law and calls its coefficient dimensionless. **Is `β` (a) DERIVED from the ECKS
field equations and spin content, (b) CITED from a named calculation you actually open, (c) FITTED to reproduce an
observable, or (d) FREE — carried as a parameter?** And do the paper's reported perturbation results depend on it?

## Mandatory mechanics — these are controls, not suggestions

1. **C5 — harness, LIVE.** At the top of your record, **execute** and print the real output of:
   `python3 -c "import sys;print(sys.version)"`, `python3 -c "import sympy;print(sympy.__version__)"`, and
   `shasum -a 256 $(command -v python3)`. **Printing expected values without running them fails C5.**
2. **C1 — source identity on RAW BYTES.** The text is PDF-extracted and does **not** contain clean strings: the epsilon
   in the production law is a raw `\x02` control byte, and "coefficient" on the next line carries the ligature `ﬃ`.
   **Print the Python `repr()` of lines 87, 126 and 128** and assert your match after normalisation (strip control
   bytes, expand ligatures). Do not match on clean strings; you will fail.
3. **C2 — dependence probe with a 120-SECOND CAP.** Show which reported results move with `β`. **Every symbolic
   operation must run under a hard 120-second wall-clock cap.** On timeout print `DEPENDENCE_SYMBOLIC_TIMEOUT` and fall
   back to numerical parameter variation. A silent hang is a failed run; a reported timeout is not.
4. **C3 — citations opened or BLOCKED.** For every link you mark "cited", either open the cited source and **print the
   exact text and line numbers containing the derivation**, or mark it `BLOCKED`. A citation may not be counted as a
   derivation unopened.
5. **C4 — free-symbol probe.** Recompute the paper's reported results with `β` replaced by a free symbol. If its
   printed numbers cannot be recovered without choosing a value, print that.

## Separating the classes — the operation, not the impression

Classes **FITTED** and **FREE** are separated by **quoting the exact text** where the author either targets a specific
observable value (fitted) or leaves the parameter arbitrary (free). Quote it or do not claim it.

## Deliverables — exactly two files

1. `R3A_beta_<seat>.py` — self-contained, runs under `python3`, prints everything it claims. **Run it.**
2. `R3A_<seat>_RESULT.md` — first line exactly one token:
   `BETA_DERIVED` · `BETA_CITED` · `BETA_FITTED` · `BETA_FREE` · `BETA_UNDETERMINED` · `R3A_NO_CLASS`

Print every control code by name with `=PASS`, `=FAIL` or `=NOT_RUN`. **NOT_RUN is honest; a false PASS is not.**
You have no authority over any tier, warrant token, standing or stamp.

R3A_SEAT_BRIEF_COMPLETE
