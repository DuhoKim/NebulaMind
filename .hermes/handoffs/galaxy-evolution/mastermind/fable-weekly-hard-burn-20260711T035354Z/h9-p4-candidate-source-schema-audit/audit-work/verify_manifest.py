#!/usr/bin/env python3
# H9 manifest cross-check pass 2 — exact_string/occurrences_expected aware. Read-only; stdout only.
import json, re

PRIOR = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z"
cand = open(PRIOR + "/p4-derived-claims/CLAIM_EVIDENCE_CANDIDATES.md", encoding="utf-8").read()
flg = open(PRIOR + "/p4-derived-claims/sources-snapshot/rp1_flagship_polished.tex", encoding="utf-8").read()
sup = open(PRIOR + "/p4-derived-claims/sources-snapshot/supplementary_denominator_atlas.tex", encoding="utf-8").read()
flg_lines = flg.split("\n"); sup_lines = sup.split("\n")
man = json.load(open(PRIOR + "/p1-rp1-invariants/INVARIANT_MANIFEST.json", encoding="utf-8"))
entries = man["entries"]
by_id = {e["id"]: e for e in entries}
fails = []
def report(tag, ok, detail=""):
    print(("PASS" if ok else "FAIL"), tag, detail)
    if not ok: fails.append((tag, detail))

report("manifest.entries-105", len(entries) == 105, str(len(entries)))
report("manifest.ids-unique", len(by_id) == len(entries))

raw = set(re.findall(r"\b(?:FLG|SUP)-[A-Z0-9-]+(?:/[A-Z0-9-]+)*", cand))
used = set()
for r in raw:
    for part in r.split("/"):
        if not part.startswith(("FLG-", "SUP-")):
            part = ("FLG-" if r.startswith("FLG") else "SUP-") + part
        used.add(part.rstrip("-"))
used -= {"FLG-", "SUP-"}
expanded = set()
for u in sorted(used):
    if u in by_id:
        expanded.add(u)
    else:
        fam = [i for i in by_id if i.startswith(u)]
        report(f"idref.{u}.family-exists", bool(fam), f"{len(fam)} manifest ids match prefix")
print("INFO distinct manifest ids directly referenced:", len(expanded))

def count_occ(txt, s):
    n = 0; c = 0
    while True:
        j = txt.find(s, c)
        if j < 0: return n
        n += 1; c = j + 1

checked = 0
for u in sorted(expanded):
    e = by_id[u]
    s = e["exact_string"]; exp = e.get("occurrences_expected")
    txt = flg if e.get("file", "").startswith("flagship") or "flagship" in str(e.get("file", "")) else sup
    got = count_occ(txt, s)
    checked += 1
    if exp is None:
        report(f"man.{u}.present", got >= 1, f"got={got}")
    else:
        report(f"man.{u}.occ", got == exp, f"exp={exp} got={got} str={s[:40]!r}")
print("INFO entries occurrence-checked:", checked)

# whole-row invariance: FLG-ROW-057 and SUP-ROW-176..190
row_ids = ["FLG-ROW-057"] + [f"SUP-ROW-{n}" for n in range(176, 191)]
for rid in row_ids:
    e = by_id.get(rid)
    if not e:
        report(f"row.{rid}.exists", False); continue
    s = e["exact_string"]
    src = flg_lines if rid.startswith("FLG") else sup_lines
    ln = e.get("line") or int(rid.split("-")[-1])
    ok = s == src[ln - 1] or s in src[ln - 1]
    report(f"row.{rid}.byte-identical@{ln}", ok, f"mode={'exact' if s == src[ln-1] else ('substr' if ok else 'MISMATCH')}")

# corruption sweep with true artifact-rounding signatures from known_rounding_anomalies
for sig in ["-1.282", "[-1.334,-1.282]", "2.831", "0.001-0.856", "0.001-0.610"]:
    tot = count_occ(flg, sig) + count_occ(sup, sig) + count_occ(cand, sig)
    report(f"corruption.absent.{sig}", tot == 0, f"hits={tot}")
report("canonical.-1.283.in-cand", count_occ(cand, "-1.283") >= 1, str(count_occ(cand, "-1.283")))
report("canonical.2.830.at-SUP188", "2.830" in sup_lines[187])

# DR17 / OIII / NII probes
for pid in ["FLG-DR17", "SUP-DR17", "FLG-OIII", "FLG-NII"]:
    report(f"probe.{pid}.exists", pid in by_id)

print("\n==== SUMMARY2 ====")
print("FAILS:", len(fails))
for t, d in fails:
    print("  FAIL", t, d)
