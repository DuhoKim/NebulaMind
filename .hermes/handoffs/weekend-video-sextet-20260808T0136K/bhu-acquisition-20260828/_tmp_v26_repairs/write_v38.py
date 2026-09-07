import io,sys,re
T,SEAT,LANE,NC,NP=sys.argv[1:]
M="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; m=io.open(M,encoding="utf-8").read()
def rep(a,b,count=1):
    global m; pat=r"\s+(?:>\s*)?".join(re.escape(t) for t in a.split()); hits=re.findall(pat,m); assert len(hits)==count,(a[:60],len(hits)); m=re.sub(pat,lambda _: b,m,count=count)
def repx(pat,b):
    global m; assert re.search(pat,m),pat[:60]; m=re.sub(pat,b,m,count=1)
rep("Version 37 — LIVING DRAFT: V36 + dependency-list order as a MOI source, origin-independent graph integrity at both C3 boundaries, and the exact-failure predicate for every negative control (§10.32);","Version 38 — LIVING DRAFT: V37 + search-inventory order as a MOI source and ONE exact-result evaluator for every judge in the kit (§10.33); V37 = V36 + dependency-list order, the C3 integrity boundaries and the exact-failure predicate (§10.32);")
repx(r"The seat's tool is `r3c2_ledger_tools.py`,\s+sha256\s+`[0-9a-f]{64}`","The seat's tool is `r3c2_ledger_tools.py`, sha256 `"+SEAT+"`")
repx(r"the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document,\s+sha256\s+`[0-9a-f]{64}`","the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document, sha256 `"+LANE+"`")
repx(r"the lane owner runs `r3c2_lane_tools.py`\s+\(sha256\s+`[0-9a-f]{64}`;","the lane owner runs `r3c2_lane_tools.py` (sha256 `"+LANE+"`;")
# --- codex V37 N1 (his exact replacement)
rep("are invariant under every ordering that carries no meaning, including dependency-list order.",
 "are invariant under every ordering that carries no meaning, including dependency-list order and the enumeration order of `origin_search.files` and `origin_search.matches`. The latter two fields record unordered evidence inventories. A shared canonical-search function sorts their entries by canonical JSON without dropping entries or changing their content; it preserves the `query` field. `merge` applies it before canonical keys, graph digests, branch selection and serialisation, and C6 applies it to both reconstructed and sealed search evidence before branch matching and comparison. Reordering an inventory alone must preserve the complete outcome; adding, removing or changing an entry must still fail, and changed-entry, added-entry and deleted-entry negatives are carried in the kit to prove that canonicalisation erases no evidence difference.")
# --- source (g)
rep("(f) dependency-list order — the order of ids inside a `derived_from` list, normalised at `merge` as stated above and exercised in the combined property.",
 "(f) dependency-list order — the order of ids inside a `derived_from` list, normalised at `merge` as stated above and exercised in the combined property; (g) search-inventory order — the order of entries inside `origin_search.files` and `origin_search.matches`, canonicalised at `merge` and on both sides of the C6 comparison as stated above, and exercised in the combined property including auditor-only permutations, which are the ones that flipped a verdict.")
# --- codex V37 C1 + kimi cosmetic 1: the run description, corrected to the DELIVERED behaviour (prospective)
i=m.index("EXHIBITION, one combined property in `r3c2_spi_exhibition.py`"); j=m.index("every construction also asserts its expected verdict and diagnostic.",i)+len("every construction also asserts its expected verdict and diagnostic.")
m=m[:i]+("EXHIBITION, one combined property in `r3c2_spi_exhibition.py`: each construction has TWELVE runs — both seat orders at each of "
 "PYTHONHASHSEED 0, 1 and 2; one reversed-record-arrival run; one reversed-rederivation-member-order run; reversed dependency lists in "
 "both seat ledgers under each seat order; one reversed-auditor-dependency-list run; and one reversed-auditor-search-inventory run. "
 "Every run asserts the construction's expected verdict and diagnostic and equality of the complete outcome. Only the rederivation-byte "
 "seal may differ in the variants that reorder the delivered auditor reconstruction — that seal is the digest of what was delivered, an "
 "identity and not an ordering; every other compared value remains invariant.")+m[j:]
# --- codex V37 F3-continued (his exact replacement)
rep("The same rule governs every other control in the kit that judges an outcome, the deletion probes included: each asserts its own diagnostic and exit code, and no traceback or launch failure can satisfy one.",
 "Every outcome-judging helper in the kit uses one common exact-result evaluator: it rejects empty output and setup, launch, import or traceback failures; requires the subcommand's completion token and exact exit code; and compares the complete ordered diagnostic rows and subcase evidence with their declared expectations, not substrings. A subcommand without a completion token must gain one before serving as control evidence. Deletion probes additionally require the targeted diagnostic to be absent; when an overlapping guard remains, they require its exact retained failure result. Relocating a deletion marker without disabling its diagnostic must fail the probe. Meta-controls exercise every helper with a real crash, an unrelated subcase failure, a wrong diagnostic and an undeleted diagnostic. Production guards are never weakened to satisfy a probe.")
m=m.rstrip("\n")+f"""

## 10.33 V38 — search-inventory order, and one exact-result evaluator for every judge ({T})

C0 on V37: codex PASS, kimi PASS. Gate on V37: codex `PREREG_UNSOUND` (N1 and F3-continued non-cosmetic, C1 cosmetic; NO_MASKED_STAGE=NO
and PRIOR_FINDINGS_CLOSED=NO, both resting on the kit accepting a crashed stage), kimi `PREREG_SOUND_WITH_REPAIRS` (no numbered findings;
two cosmetics). Reconciled BY TOPIC (`R3C2_V37_GATE_RECONCILIATION_20260907.md`, sweep none missing), which also carries the disclosure of
a pinned kit file mutated while the kimi seat was live, bounded there and not restated here.

**N1 — the fifth ordering source, and the first since V32 that changes the answer.** Reversing `origin_search.files` or
`origin_search.matches` changed merged bytes, and an AUDITOR-ONLY permutation flipped C6 from PASS to FAIL: equivalent evidence,
different verdict. Repaired with codex's exact sentence: one shared canonical-search function, applied at `merge` before keys, digests,
branch selection and serialisation, and on BOTH sides of the C6 comparison. Enumerated as source (g). The combined property gained an
auditor-only search permutation, so each construction now runs twelve times. **The guard Blanc ordered at 09:07 is carried and passes:**
changed-entry, added-entry and deleted-entry negatives still FAIL after canonicalisation, so sorting an inventory does not let two
genuinely different inventories compare equal.

**F3-continued — the exact-failure rule reached the text but not every judge.** The general `check` helper omitted the setup guard,
treated the completion token as optional and matched diagnostics by substring; the reviewer executed a real traceback and `check`
credited it. Deletion probes accepted an undeleted diagnostic when only the marker moved. Repaired with codex's exact replacement:
ONE exact-result evaluator now serves every judge — no per-helper variants, no optional fields, no substring-only matching. It rejects
empty output and setup, launch, import, syntax or traceback failures (`SyntaxError` added on kimi's request, the same class as the
credited traceback); requires the exact exit code and a completion token line; and compares the complete ordered diagnostic rows against
`r3c2_exact_rows.json`, a pinned table of the full expected text for every judged control, while still requiring each control's own
declared expectation to appear in its row. Every subcommand that lacked a completion token gained one, emitted once per run at each
tool's dispatcher, and argument errors emit `INVOCATION=REJECTED`. Deletion probes now run the tool BOTH unprobed and probed and require
the targeted diagnostic to have vanished — pinned per probe in the same table — with the remaining result and the declared exit code
retained; a probe whose effect appears only in an artefact declares the evidence that must disappear from it; and the neutraliser was
extended so that an assignment guard is genuinely deleted rather than left standing. Eight meta-controls exercise the judges with a real
crash, a missing completion token, a wrong diagnostic, an extra diagnostic row, a relocated marker that disables nothing, an unrelated
launch failure, a real failure of a different subcase, and the right subcase failing for the wrong stated reason.

**What changed status under the strict evaluator, measured:** 31 of the 201 controls then in the kit stopped passing the moment the
evaluator became exact — 17 because their subcommand printed no completion token, 12 probes because nothing actually vanished when the
marked line was neutralised or because the diagnostic text changed shape, 1 because a deliberate usage banner was read as a launch
failure, and 1 because the property's construction count had grown. Every one was repaired in the tools or the kit, none by weakening a
production guard: the kit now stands at {NC} controls and {NP} deletion probes, passing in both capture and strict modes.

**On counting:** the previous version reported 201 controls and 65 probes passing while all three of these defects were live. A control
total is not a guarantee and is not offered as one here; what each control asserts is stated where it is claimed, and the evaluator that
judges them is now itself under meta-control. **Next:** C0 and the gate on V38 — a genuinely fresh independent review; no part of V37's
round covers this package.
"""
io.open(M,"w",encoding="utf-8").write(m); print("V38 master written")
