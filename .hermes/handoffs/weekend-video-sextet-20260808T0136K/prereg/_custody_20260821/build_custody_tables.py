#!/usr/bin/env python3
"""Custody tables, v2. Reports only what it can prove, and names what it cannot see.

v1 defects, all found by GATE_DECISION_MEMO_R3_20260821.md and all removed here:
  - it called every revision hash appearing anywhere in a gate "reviewed", conflating an
    evidence-ledger citation with the artifact under review;
  - it PRINTED "each revision appears at most once" without computing it;
  - it globbed narration .txt only, so it could not see chi disclosures living in deck JSON,
    SVG or HTML, yet was credited with covering them.

Never opens /Users/duhokim/NebulaMindData/chi_dr10_south/.
"""
import glob, hashlib, html, json, os, re

PREREG   = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg"
REPORTS  = "/Users/duhokim/HermesOps/reports/status-audio"
CROSSING = "20260820T2220"

sha  = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
flat = lambda s: re.sub(r"\s+", " ", s).strip()

def detect(text):
    """Return the kinds of chi disclosure present. Detectors are semantic, not numeric-only:
    spoken numbers are rendered as words and no numeric regex can see them."""
    pats = {
        "VALUE(words)": r"(?i)(zero point|minus zero|real values?:)",
        "VALUE(num)":   r"(?:\u03c7|&#967;|\\u03c7|\bchi\b)\s*=\s*[-+]?[0-9]",
        "SIGN":         r"(?i)(leaning each way|one leaning|leans? (?:positive|negative))",
        "COUNT":        r"(?i)galax(?:y|ies)[^.]{0,40}(?:carry|carries|were read|measured)",
    }
    return [k for k, rx in pats.items() if re.search(rx, text)]

def gate_history():
    revs = {}
    for p in sorted(glob.glob(f"{PREREG}/HWAO_FOOTPRINT_GEOMETRY_FINDING_*.md")):
        n = os.path.basename(p)
        revs[sha(p)] = "Rev1" if "REV1" in n else "Rev2" if "REV2" in n else "Rev3(current)"
    rows, referenced = [], set()
    for p in sorted(glob.glob(f"{PREREG}/GATE_*.md")):
        body = open(p, encoding="utf-8", errors="replace").read()
        hits = sorted({revs[h] for h in re.findall(r"\b[0-9a-f]{64}\b", body) if h in revs})
        referenced |= set(hits)
        rows.append((os.path.basename(p), body.splitlines()[0].strip(), hits))
    never = sorted(set(revs.values()) - referenced)
    return rows, never

def ledger():
    # queue.json is a ROLLING WINDOW (QUEUE_KEEP=50) and rows have been deleted from it in the
    # past. queue_ledger.jsonl is the append-only record. Join through the ledger. (Blanc,
    # PUBLICATION_LEDGER.md, 2026-08-21.)
    pubs = {}
    try:
        for line in open(f"{REPORTS}/queue_ledger.jsonl"):
            r = json.loads(line)
            f = str(r.get("file", ""))
            if not f:
                continue
            stamp = f.split("-")[0]
            ev = r.get("event", "?")
            if ev in ("publish", "withdraw", "restored", "discovered"):
                pubs.setdefault(stamp, []).append((ev, r.get("seq"), r.get("stamp_kst", "")))
    except Exception as e:
        pubs = {"(LEDGER UNREADABLE)": [("error", str(e), "")]}

    found = {}   # stamp -> {source-class -> set(kinds)}
    def note(stamp, cls, kinds):
        if kinds: found.setdefault(stamp, {}).setdefault(cls, set()).update(kinds)

    for f in glob.glob(f"{REPORTS}/2026*-*.txt"):
        st = os.path.basename(f).split("-")[0]
        if st >= CROSSING: note(st, "narration", detect(open(f, encoding="utf-8", errors="replace").read()))
    for f in glob.glob(f"{REPORTS}/*.deck.json"):
        st = os.path.basename(f).split("-")[0]
        if st >= CROSSING: note(st, "deck+svg", detect(open(f, encoding="utf-8", errors="replace").read()))
    for f in glob.glob(f"{REPORTS}/report-2026*.html"):
        st = os.path.basename(f).replace("report-", "").split("-")[0]
        if st >= CROSSING:
            note(st, "report html", detect(html.unescape(open(f, encoding="utf-8", errors="replace").read())))
    for f in glob.glob(f"{REPORTS}/_drafts/*"):
        if f.endswith((".mp3", ".times.json")):
            continue
        st = os.path.basename(f).split("-")[0]
        if st >= CROSSING:
            note(st, "_drafts", detect(open(f, encoding="utf-8", errors="replace").read()))
    for f in glob.glob(f"{REPORTS}/archive*.html"):
        k = detect(html.unescape(open(f, encoding="utf-8", errors="replace").read()))
        body = html.unescape(open(f, encoding="utf-8", errors="replace").read())
        stems = sorted({m for m in re.findall(r"report-(2026[0-9T]+)-", body) if m >= CROSSING})
        note("(archive pages — attributable via data-src/href)",
             f"{os.path.basename(f)} [post-crossing reports: {', '.join(stems) if stems else 'none'}]", k)
    return found, pubs

def self_sha():
    """Self-pin: the digest travels IN the output, so an embedded table can never cite a
    generator hash that has drifted from the generator that produced it."""
    return hashlib.sha256(open(__file__, "rb").read()).hexdigest()

if __name__ == "__main__":
    print(f"GENERATOR: {os.path.basename(__file__)} sha256 {self_sha()}\n")
    rows, never = gate_history()
    print("A. GATE HISTORY — verdicts, and which revision HASHES each gate cites\n")
    for name, verdict, hits in rows:
        print(f"  {name}\n      verdict         : {verdict}"
              f"\n      hashes cited    : {', '.join(hits) if hits else '(none)'}")
    print("\n  CITATION IS NOT REVIEW. No gate declares its subject by hash, so which revision each")
    print("  gate actually reviewed is NOT DETERMINABLE from these files. This tool makes no claim")
    print("  about how many times any revision was gated.")
    print(f"  Revisions whose hash is cited by NO gate: {', '.join(never) if never else '(none)'}\n")

    found, pubs = ledger()
    print("B. CHI DISCLOSURES — by report stamp, across every source class scanned\n")
    for st in sorted(found):
        p = pubs.get(st, [])
        print(f"  {st}")
        for cls in sorted(found[st]):
            print(f"      {cls:<14}: {', '.join(sorted(found[st][cls]))}")
        if p: print("      ledger        : " + ", ".join(f"{ev} seq {s} @ {ts}" for ev, s, ts in p))
    print("\n  SOURCES SCANNED : narration .txt, deck .json (incl. embedded SVG), report .html,\n                    archive .html, _drafts/ (withdrawn reports)\n  PUBLICATIONS    : joined through queue_ledger.jsonl (append-only), NOT queue.json,\n                    which is a rolling QUEUE_KEEP=50 window that has had rows deleted")
    print("  NOTE            : the HTML surfaces embed the deck as JSON, so the chi character\n                    appears there as a literal \\u03c7 escape; the detector matches both\n                    forms. v2 initially missed the escaped form.\n  BLIND SPOTS     : rendered .mp3 audio (never transcribed here); any artifact published")
    print("                    outside queue.json; anything deleted before this run; any surface")
    print("                    not on this machine. Absence below is not proof of absence.")
