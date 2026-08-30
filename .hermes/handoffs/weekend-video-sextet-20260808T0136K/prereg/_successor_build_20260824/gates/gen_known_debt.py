#!/usr/bin/env python3
"""gen_known_debt v2 - THE KNOWN-DEBT APPENDIX, generated from the FULL ledger file.

v1 read only gen_repair_ledger.DISPOSITIONS (V100+) and reported an all-REPAIRED world
while the generated ledger itself carried 334 pre-convention findings "enumerated as
audit debt" and 192 MAPPED-BY-CITATION findings - the exact hidden-all-clear this
generator exists to prevent, found by both mini-round seats (GPT56-V117A F1, CODEX-V117A
F1). v2 parses gates/REPAIR_LEDGER.md itself: every population surfaced, the
pre-convention enumeration reproduced verbatim as LIVE AUDIT DEBT, the ledger's final
line quoted. Controls: a synthetic ledger's planted audit-debt line must surface; a
ledger missing its final line must refuse; population arithmetic must reconcile.
"""
import sys, re
from pathlib import Path

HERE = Path(__file__).resolve().parent

# The final round's eligibility arguments - FULL VERBATIM PARAGRAPHS
# (GPT56-V117A F2: v1 excerpted and altered punctuation). Sources:
# gates/V116_WHOLE_REVIEW_{GPT56,CODEX}.md.
V116_ELIGIBILITY = (
    ("GPT56 F1 (HIGH — count-oracle harness)",
     "**Debt eligibility: DEBT-INELIGIBLE.** This is not unfinished implementation "
     "already fenced by a correctly declared DESIGN slot. The text presently classifies "
     "BS-2c as fillable while its only claimed closure lives in unnamed, absent code. "
     "Freezing that contract would permit a self-consistent but incomplete count oracle "
     "to determine BS-2o, BS-5p, BS-2s, and the selected sample. It poisons selection "
     "integrity and therefore the freeze itself; an appendix cannot turn a missing "
     "class-P prerequisite into an enforceable prerequisite."),
    ("GPT56 F2 (HIGH — release binding)",
     "**Debt eligibility: DEBT-INELIGIBLE.** The entire count oracle, traversal order, "
     "power planning, selection, and later manifest closure are conditional on the "
     "universe identities. A wrong but self-consistent universe can change the chosen "
     "footprint while every currently named count check passes. That is direct "
     "selection/freeze poisoning, not bounded known debt."),
    ("GPT56 F3 (MEDIUM — form-echo kind binding)",
     "**Debt eligibility: appendix-SAFE.** I manually verified the four present mappings "
     "against the pinned draft/spec bytes: both successor-export tuples and both "
     "terminal-review tuples currently match their intended forms. The defect is that "
     "the checker cannot preserve that fact across a future edit, not that the signed "
     "V116 bytes leave any current form’s fields undecidable. The freeze survives if the "
     "appendix records that this echo is not a kind-binding control and requires manual "
     "pair verification for any later generator revision."),
    ("CODEX F1 (HIGH — T1 mirror sentence)",
     "**Debt eligibility: DEBT-INELIGIBLE.** T1 controls termination ordering and "
     "pass-entry legality. Freezing contradictory normative and implementation semantics "
     "would leave the gate unable to say whether the named boundary/termination "
     "execution conforms. An appendix can disclose the contradiction but cannot choose "
     "which live contract the implementation must obey."),
    ("CODEX F2 (HIGH — count-oracle complex)",
     "**Debt eligibility: DEBT-INELIGIBLE.** This is the selection chain's completeness "
     "root. A stale, null, or receipt/plan-substituted proof set can change the selected "
     "footprint and every downstream statistic while leaving a canonical BS-2c envelope. "
     "The freeze cannot survive that ambiguity merely by listing it as known debt."),
    ("CODEX F3 (MEDIUM — form-echo)",
     "**Debt eligibility: DEBT-INELIGIBLE.** These forms are the successor export and "
     "terminal-review bodies used by the completed/terminated closing ceremonies. A "
     "control that can silently detach kind from body cannot support a signed freeze or "
     "generated known-debt appendix. This is a control on an existing generator and is "
     "admissible under the scope freeze; it should be repaired rather than carried."),
)

RESIDUES = (
    ("The V116→V117→V118 folds are UN-REFEREED BY FULL ROUND",
     "the option-2 cap ended full rounds; the appendix mini-round (DEFECTIVE ×2, then "
     "repaired here) reviewed the V117 diff and this appendix's v1; sources: "
     "STOPPING_RULE_RULING_20260830.md, FINDINGS_MAP V116→V117 and V117→V118, "
     "gates/V117_APPENDIX_REVIEW_{GPT56,CODEX}.md"),
    ("Writer obligations are testimony-plus-fixture by design",
     "chain-undetectable Row-B obligations, each SAID so in place: pass-entry "
     "precondition & decoding pause, reading-at-commit-start, the indivisible "
     "receipt/termination units, T1's decoded-frame priority (violation = W0 residue, "
     "bounded); spec §3d, §3c T1, §3b"),
    ("The echo controls' exact contracts (per-echo, no blanket demotion)",
     "PREIMAGE echo: tuple-and-phrase tripwire, demoted in its own text; CLOSE-CLASS "
     "echo: exact token-set comparison over the note's domain segment; FORM echo: kind "
     "presence under real word boundaries + ≥1 exact tuple within 900 bytes of a kind "
     "mention + EVERY backticked `(kind,`-opening candidate whose opening lies within 900 "
     "UTF-8 bytes of the kind mention SPAN (nearest edge — CODEX-V122A F1: a "
     "character-offset start-anchored measure missed both edges), READ WHOLE to "
     "the nearest close-paren-backtick even across interior parentheses "
     "(GPT56-V121A F1, GPT56-V122A F1) — any length, any internal whitespace (GPT56/CODEX-V120A F2: the first grammar demanded "
     "a literal space and 10–400 interior characters) — must whitespace-normalize into "
     "the asserted-present KNOWN-TUPLE whitelist; the two named notational exemptions are the "
     "three-dot metavariable and the quoted opening-fragment (comma directly "
     "followed by the closing backtick, excluded by grammar shape) (all candidates otherwise, no shared-field threshold — "
     "GPT56-V119A F2; controls run through the one shipped function — CODEX-V119A F3) — stated NON-CLAIMS: no unique "
     "authoritative site, nothing outside kind-adjacent windows; R02: "
     "sentence-scoped literal-shape list; retired-token activation list: finite, "
     "demoted; semantic paraphrase beyond these contracts passes to the successor's "
     "freeze review; sources: each tool's own docstring "
     "(GPT56-V117A F4 killed v1's blanket-demotion wording)"),
    ("Inter-anchor rollback window",
     "no-vanish, deadline and key-uniqueness claims hold AS OF THE EXTERNAL ANCHORS; a "
     "rollback inside a window is platform-level custody failure by operator "
     "observation; spec §3b, named since V95"),
    ("Per-raise vs per-call-site classification unit",
     "the raise-site ledger classifies raise STATEMENTS; a shared raise reached from "
     "call sites of different classes is classified once; parked since ~V83, re-referred "
     "every round, never re-scored; source: ref/RAISE_SITE_CLASSIFICATION.md notes"),
    ("§10 historical section/count cells are as-written",
     "digests and row presence are tool-verified; 29 cells differ from the current "
     "generator's rendering and are labelled historical (GPT56-V114 F3); the V117 fold "
     "briefly mutated the V99→V100 row and V118 REVERTED it byte-for-byte "
     "(GPT56-V117A F6, CODEX-V117A F2)"),
    ("97 legacy lint advisories",
     "pre-blocking-era citation advisories, non-blocking by declaration; "
     "tools/prereg_lint.py output, every round"),
    ("Named channels, bounded not removed",
     "cause-token channel, position-gap residual, clock quantization channels "
     "(log2-bounded per decision/refusal), inter-object pace; each named where it lives "
     "in §6.1/§3b/§5 with its bound"),
    ("W0/W1 wire residue",
     "pre-arrival frames are outside custody by the receipt transition's scoping; spec "
     "§1c, §3 crash windows"),
)

BUILD_OPEN = (
    "gates/count_oracle_harness.py (V118 — registered in §11's inventory; class P)",
    "gates/replay_harness.py (class P)",
    "gates/enumeration_verifier.py",
    "gates/canonical_decoder.py",
    "gates/terminal_review_verifier.py + the ceremony script",
    "the executable mapping module (mapping A - ruled, unbuilt; blocks BS-6)",
    "BS-SI schema; the reviewer roster values; BS-2k constants "
    "(D, Q, budgets, g, R_max, A_max, GATE_PASS_BUDGET, PASS_RETRY_MAX; M_max committed); "
    "the BS-1 release resolution (rule date 2026-09-05)",
)

def parse_ledger(ledger_text):
    """Every population, from the ledger's own lines."""
    repaired = len(re.findall(r"^- V\d+/[A-Z0-9]+ F\d+: REPAIRED —", ledger_text, re.M))
    mapped = len(re.findall(r"^- V\d+/[A-Z0-9]+ F\d+: MAPPED-BY-CITATION", ledger_text, re.M))
    pre_lines = re.findall(r"^- V\d+/[A-Z0-9]+: PRE-CONVENTION — \d+ finding\(s\).*$",
                           ledger_text, re.M)
    pre_total = sum(int(re.search(r"— (\d+) finding", ln).group(1)) for ln in pre_lines)
    fm = re.search(r"^\*\*0 undisposed;.*$", ledger_text, re.M)
    if fm:
        cn = re.search(r"(\d+) pre-convention findings", fm.group(0))
        if not cn or int(cn.group(1)) != pre_total:
            raise SystemExit(f"REFUSED: the ledger's closing line claims "
                             f"{cn and cn.group(1)} pre-convention findings but its own "
                             f"rows sum to {pre_total} - contradictory populations "
                             f"(CODEX-V118A F4)")
    rounds = sorted({m.group(1) for m in
                     re.finditer(r"^- (V\d+)/", ledger_text, re.M)},
                    key=lambda v: int(v[1:]))
    return {"repaired": repaired, "mapped": mapped, "pre_lines": pre_lines,
            "pre_total": pre_total, "final_line": fm.group(0) if fm else None,
            "rounds": rounds}

def _norm(s):
    """Blockquote-unwrap + whitespace-collapse - the comparison form for verbatim checks."""
    s = re.sub(r"^> ?", "", s, flags=re.M)
    return re.sub(r"\s+", " ", s).strip()

def enumerate_preconv(pre_lines, read_report):
    """Per-finding enumeration (GPT56/CODEX-V118A F1: aggregate counts left the 334
    content-hidden): each era report's FINDINGS-BLOCK F-lines quoted verbatim; a count
    mismatch or an unparseable report is SAID in place, never padded."""
    out = []
    for ln in pre_lines:
        m = re.match(r"- (V\d+)/([A-Z0-9]+): PRE-CONVENTION — (\d+) finding", ln)
        ver, seat, n = m.group(1), m.group(2), int(m.group(3))
        out.append("")
        out.append(f"**{ver}/{seat} — {n} finding(s) per the ledger "
                   f"(source: gates/{ver}_WHOLE_REVIEW_{seat}.md):**")
        body = read_report(ver, seat)
        if body is None:
            out.append("  - REPORT FILE ABSENT — the count stands on the ledger's era "
                       "accounting alone, said rather than padded")
            continue
        fl = re.findall(r"^F\d+ \|.*$", body, re.M)
        if not fl:
            out.append("  - NO PARSEABLE F-LINES (pre-block-format report) — the count "
                       "stands on the ledger's era accounting; full text at the named file")
            continue
        for f in fl:
            out.append(f"  - `{f}`")
        if len(fl) != n:
            out.append(f"  - **COUNT MISMATCH, said in place: the ledger line says {n}, "
                       f"the report's block carries {len(fl)} F-line(s)**")
    return out

def verify_verbatim(quote, source_text, label):
    if _norm(quote) not in _norm(source_text):
        raise SystemExit(f"REFUSED: claimed-verbatim quote for {label} is not a "
                         f"(whitespace-normalized) substring of its source - a false "
                         f"verbatim cannot ship (GPT56-V118A F3)")

LIMIT_ANCHORS = (
    ("The unresolved pre-unblinding numerical route (§5)",
     "**A completeness argument was offered here at V46 and is RETRACTED.**",
     "**The deletion of the redundant code stands on the principal's ruling, not on this retracted argument.**"),
    ("The caller-pair-only authorization guard (§5)",
     "**Recorded limit (CODEX-V34-2),",
     "a partial run is not a smaller run, it is a different experiment."),
    ("The count-only sample guard (§5)",
     "**Recorded limit (CODEX-V63 F4),",
     "stays frozen at `6a9abbbd`."),
    ("The dual-valued Stage-P contract (§2.6)",
     "> **STAGE P REMAINS DUAL-VALUED, AND THIS TEXT CANNOT FIX IT",
     "This is a design-and-implementation slot, not a value slot."),
)

def extract_limitations(draft_text):
    """FULL passages by DECLARED ANCHORS (GPT56-V119A F1, CODEX-V119A F1: hand-selected
    substrings were faithful but incomplete; extraction from start anchor to end anchor
    makes completeness a construction, and a missing or duplicated anchor refuses)."""
    out = []
    for name, start, end in LIMIT_ANCHORS:
        if draft_text.count(start) != 1 or draft_text.count(end) != 1:
            raise SystemExit(f"REFUSED: limitation anchors for {label_or(name)} are not "
                             f"unique in the draft ({draft_text.count(start)}/"
                             f"{draft_text.count(end)}) - the passage cannot be "
                             f"extracted whole")
        a = draft_text.index(start)
        b = draft_text.index(end) + len(end)
        if b <= a:
            raise SystemExit(f"REFUSED: limitation anchors for {name} are out of order")
        out.append((name, draft_text[a:b]))
    return out

def label_or(name):
    return name


def emit(led):
    led.setdefault("preconv_enum", ["", "  (enumeration not loaded in this context)"])
    if led["final_line"] is None:
        raise SystemExit("REFUSED: the ledger carries no final population line - "
                         "cannot certify a summary of a ledger that does not state its own totals")
    total = led["repaired"] + led["mapped"] + led["pre_total"]
    lines = [
        "# KNOWN-DEBT APPENDIX — generated by gates/gen_known_debt.py (v2)",
        "",
        "**Standing:** the principal's option-2 ruling capped the text-referee loop at "
        "V116; this appendix freezes and is signed WITH the preregistration. v2 derives "
        "every population from `gates/REPAIR_LEDGER.md` itself after the appendix "
        "mini-round found v1 summarizing only the post-V100 disposition dictionary while "
        "334 older findings stood in the ledger as audit debt (GPT56-V117A F1, "
        "CODEX-V117A F1 — both verdicts DEFECTIVE, both right). Quoted, never restated.",
        "",
        "## 1. The finding populations, from the ledger's own lines",
        "",
        f"- referee rounds represented: {len(led['rounds'])} "
        f"({led['rounds'][0]}–{led['rounds'][-1]}), two seats each",
        f"- findings represented in total: {total}",
        f"- REPAIRED under the strict per-finding convention (V100+): {led['repaired']}",
        f"- MAPPED-BY-CITATION (pre-V100 rounds inside the citation convention — "
        f"resolved by map citation, not per-finding dispositions): {led['mapped']}",
        f"- **PRE-CONVENTION AUDIT DEBT — STANDING: {led['pre_total']} findings.** These "
        "were dispositioned in era prose only; the ledger enumerates them as audit debt "
        "and this appendix carries them as LIVE:",
        "",
    ]
    lines += [f"  {ln}" for ln in led["pre_lines"]]
    lines += ["",
              "**The findings themselves, enumerated per report — each F-line quoted "
              "verbatim from its era report's FINDINGS-BLOCK (GPT56/CODEX-V118A F1; a "
              "pre-block report or a count mismatch is said in place, never padded):**"]
    lines += led["preconv_enum"]
    lines += [
        "",
        "The ledger's own closing line, verbatim:",
        "",
        f"> {led['final_line']}",
        "",
        "**What this debt means at signing:** the pre-convention findings were addressed "
        "in their era's briefs and map prose and every one predates V100's stricter "
        "custody layer, but NO per-finding disposition record exists for them. The "
        "successor's freeze review inherits them by name via the ledger.",
        "",
        "## 2. The final text round's eligibility arguments, verbatim and in full",
        "",
        "All six V116 findings were folded in V117/V118 (un-refereed folds under the "
        "cap; the mini-round reviewed the V117 diff and this appendix). The seats' own "
        "debt judgments, complete paragraphs:",
        "",
    ]
    for name, quote in V116_ELIGIBILITY:
        lines.append(f"**{name}**")
        lines.append("")
        lines.append(f"> {quote}")
        lines.append("")
    lines += ["## 3. Acknowledged draft limitations, quoted in full from the draft", "",
              "The four the mini-round found omitted (GPT56-V117A F3). Each passage is "
              "EXTRACTED WHOLE from the draft between declared start and end anchors at "
              "generation time (GPT56/CODEX-V119A F1: hand-selected substrings were "
              "faithful but incomplete; anchored extraction makes completeness a "
              "construction, and a missing, duplicated or out-of-order anchor refuses "
              "the build):", ""]
    for name, passage in led.get("limitations", []):
        lines.append(f"**{name}**")
        lines.append("")
        for pl in passage.split("\n"):
            lines.append(f"> {pl}")
        lines.append("")
    lines += ["## 4. Named residues and honest limits", ""]
    for name, desc in RESIDUES:
        lines.append(f"- **{name}.** {desc}")
    lines += ["", "## 5. Open build inventory (not text debt; freeze-gating where marked)", ""]
    for item in BUILD_OPEN:
        lines.append(f"- {item}")
    lines += ["",
              "*A debt item leaves this appendix only by a superseding ruling or a "
              "repaired-and-refereed successor revision; silence never retires it.*", ""]
    return "\n".join(lines)

def selftest():
    fails = []
    synth = ("- V40/GPT56: PRE-CONVENTION — 7 finding(s) dispositioned in era prose, "
             "enumerated as audit debt\n"
             "- V100/GPT56 F1: REPAIRED — x\n"
             "- V99/CODEX F2: MAPPED-BY-CITATION\n"
             "**0 undisposed; 7 pre-convention findings enumerated as audit debt "
             "(per-round counts above).**\n")
    led = parse_ledger(synth)
    out = emit(led)
    if "STANDING: 7 findings" not in out or "V40/GPT56: PRE-CONVENTION — 7" not in out:
        fails.append("planted audit-debt line did not surface as live debt")
    if "MAPPED-BY-CITATION (pre-V100" not in out or ": 1" not in out.split("MAPPED-BY-CITATION")[1][:200]:
        fails.append("mapped population not surfaced")
    try:
        emit(parse_ledger("- V100/GPT56 F1: REPAIRED — x\n"))
        fails.append("missing final line did not refuse")
    except SystemExit:
        pass
    try:
        parse_ledger(synth.replace("7 pre-convention findings", "334 pre-convention findings"))
        fails.append("contradictory closing total did not refuse")
    except SystemExit:
        pass
    fake = {"V40": "F1 | HIGH | x | one\nF2 | LOW | y | two\n"}
    en = "\n".join(enumerate_preconv(
        ["- V40/GPT56: PRE-CONVENTION — 7 finding(s) dispositioned in era prose, "
         "enumerated as audit debt"],
        lambda v, s: fake.get(v)))
    if "`F1 | HIGH | x | one`" not in en or "COUNT MISMATCH" not in en:
        fails.append("enumeration did not quote F-lines or say the mismatch")
    try:
        verify_verbatim("this text is nowhere", "totally different source", "probe")
        fails.append("false verbatim did not refuse")
    except SystemExit:
        pass
    # anchored extraction: whole passage between anchors; duplicate anchor refuses
    demo = "AAA START mid1 mid2 END BBB"
    global LIMIT_ANCHORS
    keep = LIMIT_ANCHORS
    LIMIT_ANCHORS = (("demo", "START", "END"),)
    try:
        got = extract_limitations(demo)
        if got[0][1] != "START mid1 mid2 END":
            fails.append("anchored extraction not whole")
        try:
            extract_limitations(demo + " START again END")
            fails.append("duplicate anchors did not refuse")
        except SystemExit:
            pass
    finally:
        LIMIT_ANCHORS = keep
    return fails

if __name__ == "__main__":
    if "--selftest" in sys.argv:
        f = selftest()
        for x in f: print("SELFTEST FAIL:", x)
        print(f"selftest: {8 - len(f)}/8 controls fired correctly")
        sys.exit(1 if f else 0)
    led = parse_ledger((HERE / "REPAIR_LEDGER.md").read_text())
    def _read_report(ver, seat):
        f = HERE / f"{ver}_WHOLE_REVIEW_{seat}.md"
        return f.read_text() if f.exists() else None
    led["preconv_enum"] = enumerate_preconv(led["pre_lines"], _read_report)
    for name, quote in V116_ELIGIBILITY:
        seat = "GPT56" if name.startswith("GPT56") else "CODEX"
        verify_verbatim(quote, (HERE / f"V116_WHOLE_REVIEW_{seat}.md").read_text(), name)
    import re as _re
    drafts = sorted(HERE.parent.glob("PREREG_SUCCESSOR_DRAFT_V*_2026*.md"),
                    key=lambda f: int(_re.search(r"_V(\d+)_", f.name).group(1)))
    draft_text = drafts[-1].read_text()
    led["limitations"] = extract_limitations(draft_text)
    body = emit(led)
    target = HERE / "KNOWN_DEBT_APPENDIX.md"
    if "--check" in sys.argv:
        ok = target.exists() and target.read_text() == body
        print("known-debt --check:", "byte-equal" if ok else "STALE")
        sys.exit(0 if ok else 1)
    target.write_text(body)
    print(f"KNOWN_DEBT_APPENDIX.md written ({len(body.splitlines())} lines)")
