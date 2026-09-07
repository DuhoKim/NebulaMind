import json, pathlib, subprocess, hashlib
K = pathlib.Path(__file__).resolve().parent
H = K.parent
W = K / "work"
D = W / "d1src"
SEAT = H / "r3c2_ledger_tools_STAGED.py"
PY = "/usr/bin/python3"

def run(*a):
    r = subprocess.run([PY, "-E", str(SEAT), *[str(x) for x in a]], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr

# source where the numeral appears but the SYMBOL appears nowhere with it
(D / "k2s_nosym.txt").write_text("K2 source\nNotes, no coupling symbol here.\nThe total is 9 on the ninth page.\n")
# add it to the manifest
mf = D / "R3C2_CORPUS_MANIFEST.md"
rows = mf.read_text()
i = 7
f = "k2s_nosym.txt"
rows += f"| {i} | `{f}` | `{hashlib.sha256((D/f).read_bytes()).hexdigest()}` | {(D/f).stat().st_size} | {sum(1 for l in (D/f).read_text().splitlines() if l.strip())} |\n"
mf.write_text(rows)

rec = {"claim_id": "k2borrow.txt#1", "input_id": "k2borrow.txt#1.g", "symbol": "g", "status": "PRINTED", "origin": "IMPORTED",
       "origin_evidence": {"reason_code": "ORIG_CITATION", "source_file": "k2borrow.txt", "source_line": 3,
                           "verbatim": "We take g from k2s_choose (2021) for the evaluation below."},
       "derived_from": [], "value": "9", "source_file": "k2s_nosym.txt", "source_line": 3}
p = W / "d1h.json"; p.write_text(json.dumps({"records": [rec]}, indent=1))
rc, out = run("validate", p, D, W / "d1_cands.json")
print("D1h: value a numeric token at the cited line but the SYMBOL absent from the whole source")
print("rc:", rc)
for l in out.splitlines():
    if l.startswith("FAIL:") or l.startswith("C3"):
        print(l)
