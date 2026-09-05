ACCESS_SHA=6d60bb0a20519a64cb7fc83cae780822e17b830fa15d090da119ed3980e5132d
GATE=PREREG_UNSOUND

1. OUTCOME CLASSES

The six terminal classes are exhaustive and mutually exclusive as an operational decision procedure. Class 3 is selected only by the limb-A exit; classes 1, 2, and 4 are available only after limb B is entered and partition its readings through the mutually exclusive P/Z/I cases. Classes 5 and 6 are ordered by first ruling out `DYM_SOURCE_BLOCKED`, and the seat-split and persistent-control-failure rules route terminal non-scientific states. I cannot construct a conforming result that fits two classes or none.

An inconclusive result is genuinely reachable. For example, a printed size-mass relation with a completion-free reading yielding a 10 kg floor and an admissible GR-exterior completion yielding a 20 kg floor puts two distinct floors in P and files class 2, `DYM_FLOOR_UNDERDETERMINED`. An unreadable pinned source reaches class 5. This section is sound; no replacement.

2. CONTROLS

The controls generally require printed artefacts rather than assertions, give exact `PASS|FAIL|NOT_RUN` codes, and explicitly handle controls made unreached by an earlier terminal block. The literal C3 command and all three literal C5 commands are shell-executable as printed.

C3 deletion-probe execution requested by the gate:

(a) Yes. I executed the literal command exactly as printed.

(b) Working directory: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828`

(c) Exact stdout:

```
target            : M
retained (all)    : ['eq_src', 'inj_ok']
DELETED (pinned)  : ['eq_src']
injected relations: [('inj_ok', 'Eq(r0, 2*G*M/c**2)')]
§2b constants     : ['hbar', 'c', 'G']
with everything   : c**2*r0/(2*G)   (indeterminate: free in ['r0'])
pinned DELETED    : c**2*r0/(2*G)   (indeterminate: free in ['r0'])
VERDICT: no unique floor without the source-pinned equations -> not circular
C3_DELETION_PROBE=PASS
```

Exit code: `0`.

Defect 2.1 — C5 does not actually pin the interpreter used by C3. Verbatim: “The interpreter is the one C5 pins by digest.” C3 invokes `/usr/bin/python3`, but C5 hashes `$(command -v python3)`, which is PATH-dependent and is not required to resolve to `/usr/bin/python3`; moreover, no expected interpreter digest is supplied for comparison. Thus a seat can satisfy C5 with a different interpreter, and the claimed pin can be passed by printing an unbound digest rather than demonstrating identity to the C3 interpreter.

Exact replacement: “The interpreter used by C3 is `/usr/bin/python3`. Every seat executes and prints `/usr/bin/python3 --version`, `/usr/bin/python3 -c "import sympy; print(sympy.__version__)"`, and `shasum -a 256 /usr/bin/python3`; the computed digest must equal `b8763cf250e607a778bb4603cecb5b90338814d0a3dfcba0d57b1de242f610e9`, otherwise `C5_HARNESS_PINNED=FAIL`.” Replace the three C5 commands in §9 with those same three absolute-path commands.

Defect 2.2 — the C3 script digest is declared but never checked by an operative control. Verbatim: “The probe is the committed script `r3d_c3_deletion_probe.py`, pinned by sha256 `7db669313568d08dc9be7bb18d142a956db3cc3ad62a87bff9e4724c47527874`.” Executing the script and printing its output does not prove that the executed bytes have that digest; a modified script can emit the expected-looking artefact. The pin is therefore assertion-only.

Exact replacement: “Before executing the probe, the seat runs and prints `shasum -a 256 /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/r3d_c3_deletion_probe.py`. The computed digest must equal `7db669313568d08dc9be7bb18d142a956db3cc3ad62a87bff9e4724c47527874`; mismatch emits `C3_DELETION_PROBE=FAIL` and the probe is not executed. The printed digest and comparison are part of the C3 artefact.”

Defect 2.3 — the input filename is specified inconsistently. Verbatim: “— the JSON file `relations.json` carries `target`, `symbols`, the §2b `constants` list, and one record per relation with `id`, `origin` (`SOURCE_PINNED` or `INJECTED`) and `expr`.” The mandatory command reads `_c3_relations.json`, not `relations.json`; a conforming seat following the schema sentence can write the wrong file and then execute the literal command against stale or absent input.

Exact replacement: “The JSON file `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/_c3_relations.json` carries `target`, `symbols`, the §2b `constants` list, and one record per relation with `id`, `origin` (`SOURCE_PINNED` or `INJECTED`) and `expr`.”

3. CIRCULARITY

The lane pattern cannot validly select the enumerated relations, exclusions, or outcome. Every nonblank source line receives a printed disposition, every displayed equation receives its own row, exclusions use a closed reason-code set supported by source text, `UNRESOLVED` blocks rather than becoming absence, and the pattern is forbidden until C6 after a positive-floor class is selected. A contrary mass/size relation cannot quietly disappear without breaking the reconciliation or equation list. This section is sound; no replacement.

4. THE FALSIFIER

Number of declared terminal outcome classes in which `C6_BREAKER_TEST=FAIL` can be recorded: **4** — classes 1 and 2 directly, class 5 if condition 3 remains undecided after fallback, and class 6 if an engaged C6 is followed by a persistent control failure.

Condition 1: PASS is possible with a filed floor `M_min = 10 kg`. FAIL is possible only as a filing-integrity failure, e.g. filing the dimensionless ratio `r0/r_g = 2` as the floor. It cannot fail on any valid positive-floor path; it is the one condition that cannot substantively fail.

Condition 2: PASS is possible for `M_min = sqrt(ħc/G)` derived by a manifest equation, because every constant terminates in §2b or that equation. FAIL is possible for `M_min = α sqrt(ħc/G)` where `α` terminates in an unsupported “we choose α=3” premise.

Condition 3: PASS is possible for `M_min = sqrt(ħc/G)`, whose simplified expression has no non-§2b symbol. FAIL is possible for `M_min = λ sqrt(ħc/G)` with free `λ`.

Condition 4: PASS is possible for `M_min = sqrt(ħc/G)` with no held-constant non-§2b quantity. FAIL is possible for a floor `M_min = f(ρ0)` made rigid only by choosing and holding `ρ0` constant without a manifest derivation of that fixity.

Condition 5: PASS is possible for the point floor `1.0e15 kg`, which overlaps none of the three numerical comparator intervals. FAIL is possible for `2.0e11 kg`, which overlaps the Hawking-evaporation interval. Other concrete FAIL directions are `2.1764343e-8 kg` for the Planck interval and `5.0e30 kg` for the TOV interval.

Apart from the control-integrity defects under heading 2, the C6 decision rules are reachable and directional; no replacement here.

5. RE-RUN GUARD

The design explicitly says K6 may not be assumed to repeat and makes `DYM_FLOOR_DERIVED` reachable: a completion-free, consistent reading with a unique positive mass infimum and no Z or I reading reaches class 1. This section is sound; no replacement.

6. FAIRNESS

Defect 6.1 — the operative class tokens themselves assert absence, even though their definitions use the required epistemic wording. Verbatim: “3. **DYM_NO_SIZE_MASS_RELATION** — limb A's exit: **a relation binding size to mass, or bounding the mass, was unreproduced from the stated inputs** after the frozen census of §2 was completed.” A class token is carried into filenames, reports, and summaries without its qualifying definition; `NO` therefore converts “unreproduced” into a branch-level nonexistence claim.

Exact replacement: “3. **DYM_SIZE_MASS_RELATION_UNREPRODUCED** — limb A's exit: **a relation binding size to mass, or bounding the mass, was unreproduced from the stated inputs** after the frozen census of §2 was completed.” Replace every operative occurrence of `DYM_NO_SIZE_MASS_RELATION` with `DYM_SIZE_MASS_RELATION_UNREPRODUCED`.

Defect 6.2 — the second negative token has the same fault. Verbatim: “4. **DYM_NO_POSITIVE_FLOOR** — as partitioned above.”

Exact replacement: “4. **DYM_POSITIVE_FLOOR_UNREPRODUCED** — as partitioned above.” Replace every operative occurrence of `DYM_NO_POSITIVE_FLOOR` with `DYM_POSITIVE_FLOOR_UNREPRODUCED`.

The prose on the scientific negative paths otherwise consistently says “unreproduced from the stated inputs,” not “error.”

7. STALL

The run can always reach a declared terminal class. Symbolic operations have two bounded 120-second stages; an absent, timed-out, unparsable, or nondeciding fallback routes to `DYM_SOURCE_BLOCKED`. Seat disagreement is adjudicated, an unresolved three-way split routes to class 5, and persistent control failures route to class 6. I find no terminal state with no fileable class. This section is sound; no replacement.

R3D_V26_GATE_COMPLETE
