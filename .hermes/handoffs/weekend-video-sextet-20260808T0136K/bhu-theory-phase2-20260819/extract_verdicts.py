import json, re, hashlib, pathlib

# Rows the mission's conclusion actually rests on, taken from the audits' own
# headline findings (A1 H1/H2; A2 "thin exactly where the mission needs them thick").
# Every other row can CHECK while the paper still fails to deliver.
LOAD_BEARING = {
 "P2":  "spin-fluid closure asserted by citation (A1 H2)",
 "D13": "bounce inserted by prescription, not derived (A1 H1/H2)",
 "A-2": "spin-fluid averaging; everything downstream is conditional on it",
 "A-17":"horizon/bounce matching is conjecture",
 "B-13":"shear-defeat argument is heuristic",
 "B-14":"R0 to pi closure contradiction; branch-inconsistent",
 "B-17":"parent inheritance beyond M is one unsupported sentence",
}
PASSING = {"CHECK", "CHECK-AS-STANDARD"}

def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

def parse(path):
    out, cur = [], None
    for line in pathlib.Path(path).read_text().splitlines():
        m = re.match(r"^#{2,3}\s*[\d.]*\s*(.*)", line)
        if m and not line.startswith("|"):
            cur = m.group(1).strip(); continue
        if not line.startswith("|"): continue
        cells = [c.strip() for c in re.sub(r"\\\|", "&#124;", line).strip().strip("|").split("|")]
        if len(cells) < 3: continue
        rid = re.sub(r"\*+", "", cells[0]).strip()
        if not re.match(r"^[A-Z]-?\d+$", rid): continue
        raw = re.sub(r"\*+", "", cells[2]).strip()
        base = re.split(r"[(/]", raw)[0].strip().rstrip(",")
        out.append({
            "id": rid, "section": cur,
            "claim": re.sub(r"\*+", "", cells[1]).strip(),
            "verdict": base, "verdict_raw": raw,
            "passing": base in PASSING,
            "load_bearing": rid in LOAD_BEARING,
            "load_bearing_why": LOAD_BEARING.get(rid),
        })
    return out

audits = {}
for f, label in [("TRACK_A1_AUDIT.md", "Track A1 — PLB 694 + PRD 85 (the bounce papers)"),
                 ("TRACK_A2_AUDIT.md", "Track A2 — ApJ 832 + IJMPA 40 (collapse / universe-in-a-black-hole)")]:
    rows = parse(f)
    tally = {}
    for r in rows: tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
    audits[f.replace("TRACK_", "").replace("_AUDIT.md", "")] = {
        "label": label, "source_file": f, "source_sha256": sha(f),
        "n_rows": len(rows),
        "tally": dict(sorted(tally.items(), key=lambda kv: -kv[1])),
        "n_load_bearing": sum(1 for r in rows if r["load_bearing"]),
        "n_load_bearing_failing": sum(1 for r in rows if r["load_bearing"] and not r["passing"]),
        "rows": rows,
    }

pathlib.Path("verdicts.json").write_text(json.dumps({
 "generated_by": "Tori / BHU lane, from the gated Phase 2 audits",
 "contract": [
  "A CHECK means the step reproduces. It does NOT mean the paper's conclusion holds.",
  "Do not render a pass percentage or a pass/total headline from this file: in both audits the "
  "arithmetic passes broadly while the load-bearing rows fail. A percentage inverts the finding.",
  "Rank or colour by load_bearing first, verdict second.",
 ],
 "audits": audits,
}, indent=1, ensure_ascii=False))

for k, a in audits.items():
    print(f"{k}: {a['n_rows']} rows | {a['n_load_bearing_failing']}/{a['n_load_bearing']} load-bearing failing")
    print("   ", a["tally"])
