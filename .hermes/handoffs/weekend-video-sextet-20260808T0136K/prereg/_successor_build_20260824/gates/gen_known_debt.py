#!/usr/bin/env python3
"""gen_known_debt - THE KNOWN-DEBT APPENDIX, generated.

The principal's option-2 ruling (STOPPING_RULE_RULING_20260830.md): the text-referee loop
is capped; after the last round the remaining findings and acknowledged limitations become
an enumerated, GENERATED appendix - quoted, never restated - frozen and signed with the
document. This generator derives the finding inventory from gates/gen_repair_ledger.py's
DISPOSITIONS (the same source the ledger prints), quotes the final round's
debt-eligibility arguments verbatim from the seats' own reports, and enumerates the named
residues with their sources. Seeded control: a disposition flipped to DEFERRED in memory
must surface as live debt - the appendix reflects the ledger, never a hardcoded all-clear.
"""
import sys, importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent

def _ledger():
    spec = importlib.util.spec_from_file_location("gen_repair_ledger",
                                                  HERE / "gen_repair_ledger.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.DISPOSITIONS

# The final round's eligibility arguments, VERBATIM from the seats' reports (quoted, never
# restated; sources: gates/V116_WHOLE_REVIEW_{GPT56,CODEX}.md).
V116_ELIGIBILITY = (
    ("GPT56 F1 (HIGH, count-oracle harness)", "DEBT-INELIGIBLE",
     "\"Freezing that contract would permit a self-consistent but incomplete count oracle "
     "to determine BS-2o, BS-5p, BS-2s, and the selected sample. It poisons selection "
     "integrity and therefore the freeze itself.\""),
    ("GPT56 F2 (HIGH, release binding)", "DEBT-INELIGIBLE",
     "\"A wrong but self-consistent universe can change the chosen footprint while every "
     "currently named count check passes. That is direct selection/freeze poisoning, not "
     "bounded known debt.\""),
    ("GPT56 F3 (MEDIUM, form-echo kind binding)", "appendix-SAFE (GPT56) / DEBT-INELIGIBLE (CODEX)",
     "GPT56: \"the defect is that the checker cannot preserve that fact across a future "
     "edit, not that the signed V116 bytes leave any current form's fields undecidable.\" "
     "CODEX: \"a control that can silently detach kind from body cannot support a signed "
     "freeze.\""),
    ("CODEX F1 (HIGH, T1 mirror sentence)", "DEBT-INELIGIBLE",
     "\"An appendix can disclose the contradiction but cannot choose which live contract "
     "the implementation must obey.\""),
    ("CODEX F2 (HIGH, count-oracle complex)", "DEBT-INELIGIBLE",
     "\"A stale, null, or receipt/plan-substituted proof set can change the selected "
     "footprint and every downstream statistic while leaving a canonical BS-2c envelope.\""),
    ("CODEX F3 (MEDIUM, form-echo)", "DEBT-INELIGIBLE",
     "\"These forms are the successor export and terminal-review bodies used by the "
     "completed/terminated closing ceremonies.\""),
)

# Named residues and honest limits, each with its source of record. Curated, append-only.
RESIDUES = (
    ("The V116→V117 fold is UN-REFEREED BY FULL ROUND",
     "the option-2 cap ended full rounds; the appendix mini-round reviewed the V117 diff "
     "and this appendix; sources: STOPPING_RULE_RULING_20260830.md, FINDINGS_MAP V116→V117"),
    ("Writer obligations are testimony-plus-fixture by design",
     "chain-undetectable Row-B obligations, each SAID so in place: pass-entry "
     "precondition & decoding pause, reading-at-commit-start, the indivisible "
     "receipt/termination units, T1's decoded-frame priority (violation = W0 residue, "
     "bounded); spec §3d, §3c T1, §3b"),
    ("The echo controls are tripwires, not semantics",
     "preimage echo (tuple-and-phrase), close-class echo (domain-segment token sets), "
     "form echo (kind co-location within 900 bytes), R02 (sentence-scoped literal list), "
     "retired-token activation list — each demoted in its own text; semantic paraphrase "
     "is assigned to referee review, which has now ended: the successor's freeze review "
     "inherits that duty; sources: the generators' docstrings and "
     "tools/refusal_vocabulary_check.py lines 129-135"),
    ("Inter-anchor rollback window",
     "no-vanish, deadline and key-uniqueness claims hold AS OF THE EXTERNAL ANCHORS; a "
     "rollback inside a window is platform-level custody failure by operator observation; "
     "spec §3b, named since V95"),
    ("Per-raise vs per-call-site classification unit",
     "the raise-site ledger classifies raise STATEMENTS; a shared raise reached from "
     "call sites of different classes is classified once; parked since ~V83, re-referred "
     "every round since, never re-scored; source: ref/RAISE_SITE_CLASSIFICATION.md notes"),
    ("§10 historical section/count cells are as-written",
     "digests and row presence are tool-verified; 29 cells differ from the current "
     "generator's rendering and are labelled historical; GPT56-V114 F3, header repaired "
     "V115"),
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

# Open BUILD inventory - not text debt, listed so the appendix cannot be read as
# claiming the build is done (sources: §11 inventory, DECISIONS file).
BUILD_OPEN = (
    "gates/count_oracle_harness.py (V117; class P)",
    "gates/replay_harness.py (class P)",
    "gates/enumeration_verifier.py",
    "gates/canonical_decoder.py",
    "gates/terminal_review_verifier.py + the ceremony script",
    "the executable mapping module (mapping A - ruled, unbuilt; blocks BS-6)",
    "BS-SI schema; the reviewer roster values; BS-2k constants "
    "(D, Q, budgets, g, R_max, A_max, M_max is committed, GATE_PASS_BUDGET, "
    "PASS_RETRY_MAX); the BS-1 release resolution (rule date 2026-09-05)",
)

def emit(dispositions):
    rounds = sorted(dispositions.keys(), key=lambda k: (int(k[0][1:]), k[1]))
    total = sum(len(v) for v in dispositions.values())
    live = [(rk, seat, n, st, note)
            for (rk, seat), v in dispositions.items()
            for n, (st, note) in sorted(v.items()) if st != "REPAIRED"]
    lines = [
        "# KNOWN-DEBT APPENDIX — generated by gates/gen_known_debt.py",
        "",
        "**Standing:** the principal's option-2 ruling capped the text-referee loop at "
        "V116; this appendix freezes and is signed WITH the preregistration. It is "
        "derived from `gates/gen_repair_ledger.py`'s dispositions, quotes the final "
        "round's debt-eligibility arguments verbatim, and enumerates the named residues. "
        "Quoted, never restated.",
        "",
        f"## 1. The finding ledger, summarized from its generator",
        "",
        f"- rounds with dispositions: {len(rounds)} (V88–V116 era entries present: "
        f"{', '.join(sorted(set(k[0] for k in dispositions), key=lambda x: int(x[1:])))})",
        f"- findings dispositioned: {total}",
        f"- NON-REPAIRED at generation: {len(live)}",
    ]
    if live:
        lines.append("")
        lines.append("**LIVE DEBT (non-repaired dispositions):**")
        for rk, seat, n, st, note in live:
            lines.append(f"- {seat}-{rk} F{n} — {st}: {note}")
    else:
        lines.append("- every dispositioned finding reads REPAIRED; the ledger's own "
                     "--check is the byte evidence")
    lines += [
        "",
        "## 2. The final round's eligibility arguments, verbatim",
        "",
        "All six V116 findings were folded in V117 (an UN-REFEREED fold under the cap — "
        "the appendix mini-round reviewed the diff). The seats' own debt judgments, "
        "quoted for the principal's signature:",
        "",
    ]
    for name, verdict, quote in V116_ELIGIBILITY:
        lines.append(f"- **{name}** — {verdict}: {quote}")
    lines += ["", "## 3. Named residues and honest limits", ""]
    for name, desc in RESIDUES:
        lines.append(f"- **{name}.** {desc}")
    lines += ["", "## 4. Open build inventory (not text debt; freeze-gating where marked)", ""]
    for item in BUILD_OPEN:
        lines.append(f"- {item}")
    lines += ["",
              "*A debt item leaves this appendix only by a superseding ruling or a "
              "repaired-and-refereed successor revision; silence never retires it.*", ""]
    return "\n".join(lines)

def selftest():
    fails = []
    d = {("V99", "GPT56"): {1: ("REPAIRED", "x")}}
    if "every dispositioned finding reads REPAIRED" not in emit(d):
        fails.append("clean ledger not reported clean")
    d2 = {("V99", "GPT56"): {1: ("DEFERRED", "left open")}}
    out = emit(d2)
    if "LIVE DEBT" not in out or "DEFERRED: left open" not in out:
        fails.append("flipped disposition did not surface as live debt")
    return fails

if __name__ == "__main__":
    if "--selftest" in sys.argv:
        f = selftest()
        for x in f: print("SELFTEST FAIL:", x)
        print(f"selftest: {2 - len(f)}/2 controls fired correctly")
        sys.exit(1 if f else 0)
    body = emit(_ledger())
    target = HERE / "KNOWN_DEBT_APPENDIX.md"
    if "--check" in sys.argv:
        ok = target.exists() and target.read_text() == body
        print("known-debt --check:", "byte-equal" if ok else "STALE")
        sys.exit(0 if ok else 1)
    target.write_text(body)
    print(f"KNOWN_DEBT_APPENDIX.md written ({len(body.splitlines())} lines)")
