#!/usr/bin/env python3
"""SUPERSESSION SWEEP RECEIPT — the sweep as an enumerable list, not an assertion of coverage.

Why this exists (Blanc's directive, 2026-08-30 12:06 KST, after GPT56-V88 F3 / CODEX-V88 F2 found
the V88 sweep left the retired no-arrival regime live in five draft sentences and one spec cell):
the V88 sweep was an ASSERTION — "the old regime was grep-enumerated and killed" — whose coverage
lived in my head. A sweep whose coverage is enumerable can be checked and completed; one that is
claimed gets refound every round. Same lesson as every registry this week.

What this is: for each ruling, the superseded TOKENS searched, the FILES searched, every hit, and
every hit's DISPOSITION — computed by running the greps, not by describing them. A hit line is
DEAD when it carries a retirement marker (SWEEP/RETIRED/pre-arrival/previously/…): the token is
quoted as history. A hit line with no marker is LIVE: the old regime is still operative there, and
this tool EXITS NONZERO — an undisposed hit is a failing control, not a note.

Two stated limits, because an honest receipt names its blind spots:
1. TOKENS ARE LITERAL. A paraphrase of the old regime that avoids every token is invisible here —
   the referee round remains the control for paraphrase, exactly as the derivation checker says of
   unlabelled prose. The token list is append-only across revisions: killing a token's row because
   it went green would un-enumerate the coverage.
2. THE MARKER TEST IS LINE-LOCAL. A live sentence that happens to contain a marker word reads as
   DEAD. Every hit is therefore PRINTED with its verdict and line number so a referee can re-judge
   each one; the receipt is the worklist, not the judgement of last resort.

`gates/FINDINGS_MAP.md` is deliberately OUT of scope: it is testimony about past defects and
legitimately quotes every dead regime.
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent

DEAD = re.compile(
    r"SWEEP|sweep|RETIRED|retired|superseded|pre-arrival|pre-ruling|predecessor|previously|"
    r"WITHDRAWN|HISTORY|dissolved|DELETED|deleted|deletion|died with|form said|sentence said|wording said|clause said|line said|line listed|clause recomputed|refusal pinned|this paragraph declared|cell carried|cell said|cell spoke|summary said|row said|serialization concept|broke|SUPERSEDED|quoted dead")

# (ruling, token, scope keys, note) — scope keys resolve to files below. Append-only.
SWEEPS = [
    ("A-PRIORI RANGE SEMANTICS (CODEX-V112 F8)", "places the TRUE gradient inside", ("draft",),
     "the dead guard's confidence claim; conditional HELD replaced it"),
    ("A-PRIORI RANGE SEMANTICS (CODEX-V112 F8)", "the measurement itself plus a frozen constant", ("draft",),
     "the dead guard's origin; the origin is a-priori now"),
    ("MAP WIDENING CONFIRMED (2026-08-30 20:45)", "the widening is FILED with the coordinator", ("draft", "spec"),
     "the awaiting-confirmation posture; confirmed as filed"),
    ("EXHAUSTION ABSTAIN (2026-08-30 20:54)", "exhaustion HALTS the run pre-BS-8f", ("draft",),
     "the hard halt for the replay case; ABSTAIN continues the run"),
    ("GENERATOR-INPUT RULE (2026-08-30 21:07)", "complete framed wire unit, domain-tagged wire-frame", ("draft",),
     "the superseded preimage anywhere outside quoted history; the registry source is echo-checked separately"),
    ("GAMMA RATIFICATION (2026-08-30 20:19)", "await ratification", ("draft",),
     "the pre-ratification banner; folded V112"),
    ("GAMMA RATIFICATION (2026-08-30 20:19)", "awaiting ratification", ("draft",),
     "the open-item parentheticals; folded V112"),
    ("GAMMA RATIFICATION (2026-08-30 20:19)", "the proposed Γ", ("draft",),
     "every derived-value site now cites the ratified Γ"),
    ("TERMINAL SIGNATURE RULED (2026-08-30 20:22)",
     "machine testimony with NO closing waypoint", ("draft", "spec"),
     "the unruled suffix sentence; P9 exists now"),
    ("V111 ROUND (GPT56 F1)", "the sha256 of the complete framed wire unit", ("draft",),
     "the oracle preimage; identity is the envelope's"),
    ("V111 ROUND (GPT56 F6)",
     "the FIRST gate pass that refuses after a TERMINATED receipt", ("draft",),
     "the second export producer; deleted, T3 is the trigger"),
    ("V111 ROUND (CODEX F1)",
     "excluded BY TYPE from their own verification scope", ("draft",),
     "the bare by-type wave; exclusion is through typed joins now"),
    ("ARRIVAL CLASS (2026-08-30 10:46)", "one request never yields two events", ("draft", "spec"),
     "G4's pre-arrival form; swept V88"),
    ("ARRIVAL CLASS (2026-08-30 10:46)", "no event is neither", ("draft", "spec"),
     "G3's two-way partition; re-derived three-way at V89 (GPT56-V88 F1)"),
    ("ARRIVAL CLASS (2026-08-30 10:46)", "not written to the access log", ("draft",),
     "the pre-arrival identifier rule (GPT56-V88 F3)"),
    ("ARRIVAL CLASS (2026-08-30 10:46)", "with no binding never happened", ("draft",),
     "the pre-arrival recovery rule (GPT56-V88 F3, CODEX-V88 F2)"),
    ("ARRIVAL CLASS (2026-08-30 10:46)", "indistinguishable from a request that never arrived",
     ("draft",), "the pre-arrival residue (GPT56-V88 F3)"),
    ("ARRIVAL CLASS (2026-08-30 10:46)", "nothing above changes what the access log records",
     ("draft",), "the pre-arrival not-authorised ledger (GPT56-V88 F3, CODEX-V88 F2)"),
    ("ARRIVAL CLASS (2026-08-30 10:46)", "not authorised, REFERRED", ("spec",),
     "N2's why-cell, still refusing after the body retired (GPT56-V88 F3)"),
    ("ARRIVAL CLASS (2026-08-30 10:46)", "safe to re-process", ("spec",),
     "W1's recovery cell, pre-one-decision wording"),
    ("REBUILT PRINCIPLE (2026-08-30 10:46)", "may never describe the object", ("draft",),
     "the old principle sentence; swept V88"),
    ("REBUILT PRINCIPLE (2026-08-30 10:46)", "never the OBJECT", ("checker",),
     "the stale R03 control body; rebuilt V88 — the eighth site"),
    ("DRAW DISCIPLINE (2026-08-30 10:46)", "frozen value UNSET", ("registry",),
     "pre-commitment draw notes; swept V88"),
    ("DRAW DISCIPLINE (2026-08-30 10:46)", "currently EMPTY", ("registry",),
     "pre-commitment draw notes; swept V88"),
    ("FREEZE-TIME ENUMERATION IMPOSSIBLE (GPT56-V87 F7)", "enumerated at freeze", ("draft", "spec"),
     "the guard's impossible anchor; re-anchored V88"),
    ("ISSUANCE CUT (V89, GPT56-V88 F6 / CODEX-V88 F4)", "extends through issuance completion",
     ("draft",), "the circular half of the V88 cut; two cuts named at V89"),
    ("COUNT MOVE (GPT56-V88 F7)", "16/8 → 16/9", ("draft",),
     "the false predecessor count; quoted-as-history at V89"),
    ("DRAW MECHANICS COMMITTED (2026-08-30 sitting)", "CURRENTLY UNSET", ("draft",),
     "live pre-sitting draw prose the literal sweep missed (GPT56-V89 F4, CODEX-V89 F3)"),
    ("DRAW MECHANICS COMMITTED (2026-08-30 sitting)", "empty generator set", ("draft",),
     "same paragraph; the generator has one committed member (GPT56-V89 F4)"),
    ("DRAW MECHANICS COMMITTED (2026-08-30 sitting)", "CLASS-P, UNSET", ("draft",),
     "the common-vs-independent choice was RULED common (CODEX-V89 F3)"),
    ("GRID RE-EXPRESSED AS STEP COUNT (AMENDMENT 2)", "(i, 0)", ("draft",),
     "the baseline address outside the matrix domain (GPT56-V89 F3); compare to (i, j0)"),
    ("STRATA OPTION A (2026-08-30 10:46)", "the strata question", ("draft",),
     "the ruled question still listed undecided (GPT56-V90 F1)"),
    ("STRATA OPTION A (2026-08-30 10:46)", "NO COVENANT ROW PRODUCES THE INDEX", ("draft",),
     "Row D2 is the producer since the sitting (GPT56-V90 F1)"),
    ("GRID RE-EXPRESSED AS STEP COUNT (AMENDMENT 2)", "committed Δγ", ("draft",),
     "the verifier recomputing from an independently committed spacing (GPT56-V90 F6)"),
    ("GRID RE-EXPRESSED AS STEP COUNT (AMENDMENT 2)", "frozen class-P value", ("draft",),
     "the schema pinning a frozen spacing after the derivation (GPT56-V90 F6)"),
    ("DECIMAL GRAMMAR UNIFIED (V92)", "shortest round-trip", ("draft",),
     "binary-float serialization language in the exact-decimal grid (GPT56-V91 F4, CODEX-V91 F2)"),
    ("NOT-EVALUATED DELETED (CODEX-V72 F7)", "NOT-EVALUATED", ("draft",),
     "the dead outcome token; live use found in the BS-3g row at V91 (GPT56-V91 F5)"),
    ("ARRIVAL CLASS (2026-08-30 10:46)", "five crash windows", ("draft",),
     "the pre-W0/W1 window count (GPT56-V91 F6)"),
    ("COUNT MOVE (GPT56-V88 F7)", "stay 16/8", ("draft",),
     "the unqualified stale class count (CODEX-V91 F6)"),
    ("ARRIVAL CLASS (2026-08-30 10:46)", "never both, never neither", ("draft",),
     "the V71 two-way partition revived as live prose in a recap (CODEX-V97 F2)"),
    ("PADDED MULTIPLICITY (V93)", "single-pass, forward-only", ("draft", "spec"),
     "V92's form, broken against the restore rule (GPT56-V92 F4, CODEX-V92 F2)"),
    ("DRAW MECHANICS COMMITTED (2026-08-30 sitting)", "are not yet frozen", ("draft",),
     "the self-contradicting BS-3g clause (CODEX-V92 F4)"),
]


def files_for(draft_path):
    return {
        "draft": Path(draft_path),
        "spec": BASE / "LIFECYCLE_GUARANTEE_SPEC.md",
        "registry": HERE / "gen_string_field_registry.py",
        "checker": BASE.parents[4] / "tools" / "refusal_vocabulary_check.py",
    }


def classify(text, token):
    """Return [(lineno, verdict, line)] for every hit. Pure function; the controls exercise it."""
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        if token in line:
            out.append((i, "DEAD" if DEAD.search(line) else "LIVE", line.strip()))
    return out


def controls():
    """Exact-failure controls: a planted live token MUST read LIVE, a marked one MUST read DEAD."""
    fails = []
    live = classify("the rule is that one request never yields two events here\n",
                    "one request never yields two events")
    if [(v) for _, v, _ in live] != ["LIVE"]:
        fails.append(f"planted live token not detected LIVE: {live}")
    dead = classify("the pre-arrival form said one request never yields two events\n",
                    "one request never yields two events")
    if [(v) for _, v, _ in dead] != ["DEAD"]:
        fails.append(f"marked dead token not detected DEAD: {dead}")
    none = classify("nothing relevant\n", "one request never yields two events")
    if none:
        fails.append(f"hit manufactured from clean text: {none}")
    return fails


def main():
    args = [a for a in sys.argv[1:] if a != "--check"]
    if len(args) != 1:
        print("usage: gen_sweep_receipt.py DRAFT.md [--check]")
        return 2
    cf = controls()
    for f in cf:
        print(f"  CONTROL FAIL {f}")
    if cf:
        return 1

    fmap = files_for(args[0])
    texts = {k: p.read_text() for k, p in fmap.items()}
    rows, live_total, dead_total = [], 0, 0
    for ruling, token, scope, note in SWEEPS:
        for key in scope:
            hits = classify(texts[key], token)
            nlive = sum(1 for _, v, _ in hits if v == "LIVE")
            ndead = len(hits) - nlive
            live_total += nlive
            dead_total += ndead
            disp = ("VERIFIED-CLEAN" if not hits else
                    "DEAD-QUOTED" if nlive == 0 else "LIVE-UNDISPOSED")
            rows.append((ruling, token, fmap[key].name, hits, nlive, ndead, disp, note))

    out = ["# SUPERSESSION SWEEP RECEIPT — computed, not claimed\n",
           f"**Subject files:** {', '.join(f'`{p.name}`' for p in fmap.values())} — "
           "`gates/FINDINGS_MAP.md` is out of scope (testimony quotes dead regimes legitimately).\n",
           "**Rule:** every hit line is printed with a verdict; a LIVE hit under a swept token is "
           "a FAILING control (exit 1), not a note. Tokens are literal and the list is "
           "append-only; paraphrase is the round's to catch, and this header says so. **Scopes "
           "are DECLARED PER TOKEN in the table — this is not a cross-product sweep: a file "
           "absent from a token's row is UNSWEPT for that token** (CODEX-V89 F3: the two draw "
           "tokens were scoped to the registry while the live paraphrase sat in the draft — the "
           "scope was the blind spot, and it is now printed instead of implied).\n",
           "| ruling | superseded token | file | hits | live | disposition |",
           "|---|---|---|---|---|---|"]
    tok_show = lambda s: s.replace("|", "·")
    for ruling, token, fname, hits, nlive, ndead, disp, note in rows:
        out.append(f"| {ruling} | `{tok_show(token)}` | `{fname}` | {len(hits)} | {nlive} | "
                   f"{disp} — {note} |")
    out.append("\n## Every hit, for re-judging\n")
    for ruling, token, fname, hits, nlive, ndead, disp, note in rows:
        for ln, v, line in hits:
            out.append(f"- **{v}** `{fname}:{ln}` token `{tok_show(token)}` — "
                       f"{tok_show(line)[:160]}")
    content = "\n".join(out) + "\n"
    target = HERE / "SUPERSESSION_SWEEP_RECEIPT.md"
    if "--check" in sys.argv:
        ok = target.exists() and target.read_text() == content
        print("sweep receipt --check:", "byte-equal to generator output" if ok else "DRIFTED from generator")
        return 0 if (ok and not live_total) else 1
    target.write_text(content)
    print(f"sweep receipt: {len(SWEEPS)} token rows, per-token declared scopes; "
          f"{dead_total} dead-quoted hit(s), {live_total} LIVE")
    return 1 if live_total else 0


if __name__ == "__main__":
    sys.exit(main())
