#!/usr/bin/env python3
"""H5 hard-burn: value-level verification of the seven not-yet-verified topic
artifacts against the cycle-05 supplement prose snapshot.

Precedent: P1 tools/build_manifest.py (scripted matchers) and P4 scripted
numerals audit. Reads ONLY hash-verified snapshot copies. Writes ONLY inside
the H5 own dir (RESULTS_RAW.json next to this script's parent).

Per artifact value -> classify:
  PASS   : exact string, correct nearest-rounding at the prose token's dp,
           grouping variant (60,000 / 60000 / 60{,}000), or x100 percent form
  DRIFT  : an in-scope prose token is numerically adjacent (<= 2 ulp at its dp)
           but is NOT a correct rounding of the artifact value
  ABSENT : no occurrence anywhere in the supplement
Cross-check every PASS occurrence against INVARIANT_MANIFEST.json coverage and
emit manifest add-candidates.
"""
import json
import re
import sys
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
from pathlib import Path

OWN = Path(__file__).resolve().parent.parent
SNAP = OWN / "sources-snapshot"
P1 = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/"
    "mastermind/fable-weekly-burn-20260711T010503Z/p1-rp1-invariants"
)
SUPP_PATH = (
    P1 / "sources-snapshot/candidates/cycle_05_package/"
    "supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex"
)
FLAG_PATH = (
    P1 / "sources-snapshot/candidates/cycle_05_package/"
    "flagship_rp1/aastex/rp1_flagship_polished.tex"
)
MANIFEST_PATH = P1 / "INVARIANT_MANIFEST.json"
SUPP_REL = "supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex"
FLAG_REL = "flagship_rp1/aastex/rp1_flagship_polished.tex"

TOPICS = [
    "m1_rp2_environment_quenching",
    "m1_rp3_maintenance_heating",
    "m2_p1_outflow_escape_recycling",
    "m2_p2_radio_jet_environment",
    "m2_p3_feedback_transition_mass",
    "m3_p1_multiphase_census",
    "m3_p2_gas_depletion_efficiency",
]
# identifier/path fields: numerals there are IDs, not measured values
SKIP_FIELDS = {"figure_pdf", "source_sample", "slug", "card_id", "run_id", "method"}

NUM_RE = re.compile(r"\d{1,3}(?:(?:,|\{,\})\d{3})+(?:\.\d+)?|\d+\.\d+|\d+")
WORDLIKE = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_")


def extract_tokens(text):
    """Yield dicts for standalone numeric tokens in text (LaTeX-aware guards)."""
    out = []
    for m in NUM_RE.finditer(text):
        s, e = m.span()
        raw = m.group(0)
        prev = text[s - 1] if s > 0 else ""
        nxt = text[e] if e < len(text) else ""
        if prev in WORDLIKE or prev == ".":
            continue  # inside identifier/hash/decimal tail
        if nxt in WORDLIKE:
            continue  # 10th, 4e1f..., 20260708T...
        if nxt == "." and e + 1 < len(text) and text[e + 1].isdigit():
            continue  # mid-decimal (shouldn't happen)
        neg = False
        if prev == "-":
            before = text[s - 2] if s >= 2 else ""
            if before != "-" and not before.isdigit():
                neg = True  # a sign, not a LaTeX -- range dash
        norm = raw.replace("{,}", "").replace(",", "")
        grouped = norm != raw
        dp = len(norm.split(".", 1)[1]) if "." in norm else 0
        val = float(norm) * (-1 if neg else 1)
        tail = text[e : e + 12]
        pct = bool(re.match(r"\s*\\?%", tail)) or "percent" in text[e : e + 30]
        out.append(
            dict(raw=raw, norm=("-" if neg else "") + norm, val=val, dp=dp,
                 grouped=grouped, pct=pct, start=s)
        )
    return out


def walk(obj, path, sink):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in SKIP_FIELDS:
                continue
            walk(v, f"{path}.{k}" if path else k, sink)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            walk(v, f"{path}[{i}]", sink)
    elif isinstance(obj, bool):
        return
    elif isinstance(obj, (int, float)):
        sink.append(dict(path=path, kind="leaf", val=float(obj),
                         canon=repr(obj), dp=None))
    elif isinstance(obj, str):
        for t in extract_tokens(obj):
            sink.append(dict(path=f"{path}<text>", kind="embedded",
                             val=t["val"], canon=t["norm"], dp=t["dp"]))


def rounds(v, d):
    """Nearest-roundings of v at d decimals (HALF_UP and HALF_EVEN)."""
    q = Decimal(1).scaleb(-d)
    dv = Decimal(repr(v))
    return {str(dv.quantize(q, rounding=ROUND_HALF_UP)),
            str(dv.quantize(q, rounding=ROUND_HALF_EVEN))}


def canon_int(v):
    return str(int(v)) if float(v).is_integer() else None


def classify(av, tok):
    """Return (match_kind or None, is_near_miss)."""
    tv, td, tnorm = tok["val"], tok["dp"], tok["norm"]
    v = av["val"]
    # exact numeric / exact string
    if tv == v:
        return ("exact", False)
    if td > 0:
        r = rounds(v, td)
        if tnorm in r:
            return ("rounded", False)
        if abs(v) <= 1.5 and tnorm in rounds(v * 100, td):
            return ("percent_x100", False)
        if v < 0 and tnorm in rounds(-v, td):
            return ("abs_magnitude", False)
        # near-miss: adjacent at token dp but not a correct rounding
        step = 10 ** -td
        try:
            nearest = float(sorted(r)[0])
        except ValueError:
            nearest = v
        if abs(tv - nearest) <= 2 * step + 1e-12 and abs(tv - v) > 1e-12:
            return (None, True)
    else:
        ci = canon_int(v)
        if ci is not None and tnorm == ci:
            return ("int", False)
        if abs(v) <= 1.5 and v != 0 and tnorm in rounds(v * 100, 0):
            return ("percent_x100", False)
        if ci is not None and abs(v) >= 100 and abs(tv - v) <= 2 and tv != v:
            return (None, True)
    return (None, False)


def scan_doc(path):
    lines = path.read_text().splitlines()
    toks = []
    for ln, text in enumerate(lines, 1):
        for t in extract_tokens(text):
            t["line"] = ln
            toks.append(t)
    return lines, toks


def topic_scope(lines, slug):
    """Line numbers attributed to this topic: its Atlas-notes subsection plus
    any line mentioning the (LaTeX-escaped) slug or its short form."""
    esc = slug.replace("_", r"\_")
    short = "_".join(slug.split("_")[:2])
    esc_short = short.replace("_", r"\_")
    scope = set()
    anchor = None
    for i, text in enumerate(lines, 1):
        if esc in text or esc_short in text:
            scope.add(i)
            if anchor is None and esc in text and i > 88:
                anchor = i
    if anchor:
        start = end = anchor
        for i in range(anchor, 0, -1):
            if "\\subsection" in lines[i - 1]:
                start = i
                break
        for i in range(anchor + 1, len(lines) + 1):
            if "\\subsection" in lines[i - 1] or "\\section" in lines[i - 1]:
                end = i - 1
                break
        else:
            end = len(lines)
        scope.update(range(start, end + 1))
    return scope


def manifest_cover(entries, rel, line, surface):
    ids = []
    for e in entries:
        if e.get("file") != rel:
            continue
        if line in set(e.get("lines", [])) and surface.replace("{,}", ",") in \
                e.get("exact_string", "").replace("{,}", ","):
            ids.append(e["id"])
    return ids


def run(doc_path, doc_rel, label):
    lines, toks = scan_doc(doc_path)
    manifest = json.load(open(MANIFEST_PATH))["entries"]
    report = {}
    for slug in TOPICS:
        art = json.load(open(SNAP / slug / "analysis_results.json"))
        values = []
        walk(art, "", values)
        scope = topic_scope(lines, slug)
        tv = []
        for av in values:
            occ, near = [], []
            for t in toks:
                kind, miss = classify(av, t)
                if kind:
                    occ.append(dict(line=t["line"], raw=t["raw"], kind=kind,
                                    in_scope=t["line"] in scope,
                                    manifest=manifest_cover(
                                        manifest, doc_rel, t["line"], t["raw"])))
                elif miss and t["line"] in scope:
                    near.append(dict(line=t["line"], raw=t["raw"],
                                     text=lines[t["line"] - 1].strip()[:200]))
            if occ:
                cls = "PASS"
            elif near:
                cls = "DRIFT?"
            else:
                cls = "ABSENT"
            expected_absent = av["path"].endswith(".se") or av["kind"] == "leaf" and any(
                o for o in ()  # placeholder; annotated in review
            )
            tv.append(dict(path=av["path"], kind=av["kind"], canon=av["canon"],
                           val=av["val"], cls=cls, occ=occ, near=near,
                           se=av["path"].endswith(".se")))
        report[slug] = dict(scope=sorted(scope), values=tv)
    return report


def main():
    out = {"supplement": run(SUPP_PATH, SUPP_REL, "supplement")}
    if "--flagship" in sys.argv:
        out["flagship"] = run(FLAG_PATH, FLAG_REL, "flagship")
    dest = OWN / "RESULTS_RAW.json"
    dest.write_text(json.dumps(out, indent=1))
    # console summary
    for doc, rep in out.items():
        print(f"=== {doc} ===")
        for slug, r in rep.items():
            vs = r["values"]
            n = len(vs)
            p = sum(1 for v in vs if v["cls"] == "PASS")
            d = sum(1 for v in vs if v["cls"] == "DRIFT?")
            a = sum(1 for v in vs if v["cls"] == "ABSENT")
            cov = sum(1 for v in vs if any(o["manifest"] for o in v["occ"]))
            print(f"{slug}: n={n} PASS={p} DRIFT?={d} ABSENT={a} manifest-covered={cov}")
            for v in vs:
                if v["cls"] == "DRIFT?":
                    print(f"  DRIFT? {v['path']} canon={v['canon']} near={v['near']}")
    print(f"written: {dest}")


if __name__ == "__main__":
    main()
