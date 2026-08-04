#!/usr/bin/env python3
"""Derive the proposed runner-audit numeric_invariants extension from INVARIANT_MANIFEST.json,
cross-validate it against the cycle-5 snapshot TeX, and emit the section-(a) fragments.

Read-only everywhere except OUTDIR (must be inside the H3 packet dir).
Usage: python3 derive_audit_extension.py MANIFEST FLAGSHIP_TEX SUPPLEMENT_TEX OUTDIR
Burn: fable-weekly-hard-burn-20260711T035354Z / lane H3.
"""
import json
import sys
from pathlib import Path

# Live audit list, verbatim from run_weekend_journal_sprint.py line 109
# (sha256 b6795c05f3b790cc22644addcf2c42f7da33387d986f683c7193ccf94450efa2).
CURRENT_NUMERIC_INVARIANTS = ["8,146", "-1.309", "[-1.334,-1.283]", "249,917", "60,000", "24.0"]

FLG_FILE = "flagship_rp1/aastex/rp1_flagship_polished.tex"
SUP_FILE = "supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex"


def md_escape(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", "\\n")


def main() -> int:
    manifest_path, flg_path, sup_path, outdir = (Path(a) for a in sys.argv[1:5])
    outdir.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(manifest_path.read_text())
    entries = manifest["entries"]
    flg_text = flg_path.read_text()
    sup_text = sup_path.read_text()

    problems = []
    seen = {}           # (doc, exact_string) -> first id
    flagship_new, supplement_new, token_gate = [], [], []
    rows = []
    stats = {"flagship": 0, "supplement": 0, "covered_now": 0, "new_flagship": 0,
             "new_supplement": 0, "dup": 0, "subsumed": 0, "token": 0}

    for e in entries:
        doc = "flagship" if e["file"] == FLG_FILE else ("supplement" if e["file"] == SUP_FILE else "?")
        if doc == "?":
            problems.append(f"{e['id']}: unknown file {e['file']}")
            continue
        stats[doc] += 1
        s = e["exact_string"]
        mode = e.get("match_mode")
        exp = e.get("occurrences_expected")
        text = flg_text if doc == "flagship" else sup_text
        if mode == "substring":
            n = text.count(s)
            val = "OK" if n == exp else f"MISMATCH(found {n}, expected {exp})"
            if n != exp:
                problems.append(f"{e['id']}: occurrence mismatch found={n} expected={exp}")
        else:
            # numeric_token entries are count-checked by the manifest gate's tokenizer,
            # not by naive substring counting; presence is still verifiable.
            val = "present (token mode)" if s in text else "TOKEN NOT FOUND"
            if s not in text:
                problems.append(f"{e['id']}: token string not present in cycle-5 text")

        dup_of = seen.get((doc, s))
        covered = doc == "flagship" and any(s == c or s in c for c in CURRENT_NUMERIC_INVARIANTS)
        note = []
        if covered:
            stats["covered_now"] += 1
            note.append("already covered by live list")
        if mode != "substring":
            stats["token"] += 1
            token_gate.append((e["id"], s))
            note.append("numeric_token mode -> manifest pre-audit gate only; too short/ambiguous for a bare substring check")
        elif dup_of:
            stats["dup"] += 1
            note.append(f"same string as {dup_of}")
        else:
            seen[(doc, s)] = e["id"]
            if not covered:
                (flagship_new if doc == "flagship" else supplement_new).append((e["id"], s))
                stats["new_flagship" if doc == "flagship" else "new_supplement"] += 1
        rows.append((e["id"], doc, e["kind"], s, exp, val, covered, dup_of, note))

    # subsumption among proposed new entries (presence of superstring implies substring)
    for lst in (flagship_new, supplement_new):
        strings = {i: s for i, s in lst}
        for i, s in lst:
            supers = [j for j, t in strings.items() if j != i and s in t]
            if supers:
                stats["subsumed"] += 1
                for r in rows:
                    if r[0] == i:
                        r[8].append(f"presence implied by {supers[0]}")

    # reverse check: every live entry should be a manifest string (or substring of one)
    reverse = []
    mstrings = [e["exact_string"] for e in entries if e["file"] == FLG_FILE]
    for c in CURRENT_NUMERIC_INVARIANTS:
        hit = next((e["id"] for e in entries if e["file"] == FLG_FILE and e["exact_string"] == c), None)
        sub = next((e["id"] for e in entries if e["file"] == FLG_FILE and c in e["exact_string"]), None)
        reverse.append((c, hit or (f"substring of {sub}" if sub else "NOT IN MANIFEST")))
        if not hit and not sub:
            problems.append(f"live audit entry {c!r} has no manifest counterpart")

    # ---- emit proposed lists (audit's own format: Python str-literal list) ----
    def fmt(pairs):
        return "".join(f"    {s!r},  # {i}\n" for i, s in pairs)

    kept = "".join(f"    {c!r},  # kept from live list\n" for c in CURRENT_NUMERIC_INVARIANTS)
    lists_txt = (
        "# --- proposed replacement for run_weekend_journal_sprint.py line 109 ---\n"
        "NUMERIC_INVARIANTS = [\n" + kept + fmt(flagship_new) + "]\n\n"
        "# --- proposed new constant (immediately below NUMERIC_INVARIANTS) ---\n"
        "SUPPLEMENT_NUMERIC_INVARIANTS = [\n" + fmt(supplement_new) + "]\n\n"
        "# --- NOT in the audit lists: numeric_token manifest entries (manifest gate only) ---\n"
        + "".join(f"#   {i}: {s!r}\n" for i, s in token_gate)
    )
    (outdir / "section_a_proposed_lists.py.txt").write_text(lists_txt)

    # ---- emit mapping table ----
    md = ["| manifest id | doc | kind | audit-list entry (exact string) | exp. occ. | cycle-5 check | live-list coverage | notes |",
          "|---|---|---|---|---:|---|---|---|"]
    for i, doc, kind, s, exp, val, covered, dup_of, note in rows:
        cov = "covered" if covered else "NEW"
        md.append(f"| {i} | {doc} | {kind} | `{md_escape(s)}` | {exp} | {val} | {cov} | {'; '.join(note) or '—'} |")
    (outdir / "section_a_mapping_table.md").write_text("\n".join(md) + "\n")

    # ---- stats + reverse table ----
    n_flag_list = len(CURRENT_NUMERIC_INVARIANTS) + len(flagship_new)
    n_ok = sum(1 for r in rows if r[5] in ("OK", "present (token mode)"))
    summary = [
        f"- Manifest entries: {len(entries)} total = {stats['flagship']} flagship + {stats['supplement']} supplement; "
        f"{len(entries) - stats['token']} substring-mode + {stats['token']} numeric_token-mode.",
        f"- Already covered by the live 6-entry list (presence-level, flagship only): {stats['covered_now']} manifest entries.",
        f"- Proposed NEW audit entries: {stats['new_flagship']} flagship + {stats['new_supplement']} supplement "
        f"({stats['dup']} exact-duplicate strings removed; {stats['token']} numeric_token entries routed to the manifest gate instead of the audit list; "
        f"{stats['subsumed']} of the new entries are presence-implied by a longer proposed entry and retained anyway).",
        f"- Proposed list sizes: NUMERIC_INVARIANTS {len(CURRENT_NUMERIC_INVARIANTS)} -> {n_flag_list}; SUPPLEMENT_NUMERIC_INVARIANTS 0 -> {len(supplement_new)}.",
        "- Reverse check (live entry -> manifest): " + "; ".join(f"`{c}` -> {r}" for c, r in reverse),
        f"- Cross-validation against cycle-5 snapshot TeX: {n_ok}/{len(rows)} entries verified "
        "(substring entries: exact occurrence count; numeric_token entries: presence).",
        f"- PROBLEMS: {len(problems)}" + ("".join(f"\n  - {p}" for p in problems) if problems else " (none)"),
    ]
    (outdir / "section_a_stats.md").write_text("\n".join(summary) + "\n")
    print("\n".join(summary))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
