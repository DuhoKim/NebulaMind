#!/usr/bin/env python3
"""H6 adversarial audit of the P1 invariant packet. Read-only on all inputs;
writes nothing (stdout only). Run: python3 h6_audit.py"""
import json, hashlib, re, sys, csv
from decimal import Decimal, ROUND_HALF_EVEN
from collections import Counter

P1 = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z/p1-rp1-invariants"
SNAP = P1 + "/sources-snapshot"
S_ORIG = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z"
R_ORIG = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs"

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for ch in iter(lambda: f.read(1 << 20), b""):
            h.update(ch)
    return h.hexdigest()

def rd(p):
    with open(p, encoding="utf-8") as f:
        return f.read()

def token_count(text, s):
    """count s where neighbors are not digit/comma/dot (per manifest check_rule)"""
    bad = set("0123456789.,")
    n, i = 0, 0
    hits = []
    while True:
        j = text.find(s, i)
        if j < 0:
            break
        pre = text[j - 1] if j > 0 else ""
        post = text[j + len(s)] if j + len(s) < len(text) else ""
        if pre not in bad and post not in bad:
            n += 1
            hits.append(j)
        i = j + 1
    return n, hits

def near_miss(text, s):
    """non-overlapping matches of s with digits wildcarded, minus exact matches"""
    pat = "".join("[0-9]" if c.isdigit() else re.escape(c) for c in s)
    allm = re.findall(pat, text)
    return len(allm) - text.count(s), [m for m in allm if m != s]

def findkey(obj, key, out=None):
    if out is None:
        out = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key:
                out.append(v)
            findkey(v, key, out)
    elif isinstance(obj, list):
        for v in obj:
            findkey(v, key, out)
    return out

man = json.load(open(P1 + "/INVARIANT_MANIFEST.json"))
E = man["entries"]

print("=" * 78)
print("C1 MANIFEST STRUCTURE")
print("=" * 78)
ids = [e["id"] for e in E]
print(f"entry_count field={man['entry_count']} len(entries)={len(E)} -> {'PASS' if man['entry_count']==len(E) else 'FAIL'}")
dup = [i for i, c in Counter(ids).items() if c > 1]
print(f"unique ids -> {'PASS' if not dup else 'FAIL '+str(dup)}")
req = ["id", "file", "line", "exact_string", "kind", "allowed_context", "match_mode", "lines", "occurrences_expected"]
miss = [(e["id"], k) for e in E for k in req if k not in e]
print(f"required fields -> {'PASS' if not miss else 'FAIL '+str(miss)}")
kinds = Counter(e["kind"] for e in E)
mm = Counter(e["match_mode"] for e in E)
print("kinds:", dict(kinds))
print("match_modes:", dict(mm))
bad_anchor = [e["id"] for e in E if e["line"] not in e["lines"]]
print(f"anchor line in lines[] -> {'PASS' if not bad_anchor else 'FAIL '+str(bad_anchor)}")
bad_occ = [(e["id"], len(e["lines"]), e["occurrences_expected"]) for e in E if e["occurrences_expected"] < len(e["lines"])]
print(f"occurrences_expected >= len(lines) -> {'PASS' if not bad_occ else 'FAIL '+str(bad_occ)}")
tr = [e for e in E if e["kind"] == "table_row"]
print(f"table_row count={len(tr)} (RCA claims 32), scalars={len(E)-len(tr)} (RCA claims 73)")
pairdup = [(a, c) for (a, c), n in Counter((e["file"], e["exact_string"]) for e in E).items() if n > 1]
print(f"duplicate (file,exact_string) -> {'PASS' if not pairdup else 'CHECK '+str(pairdup)}")

print()
print("=" * 78)
print("C2/C4 RECOUNT: all 105 entries vs cycle 5/6/7 snapshots (check_rule semantics)")
print("=" * 78)
cycles = {}
for c in ("05", "06", "07"):
    cycles[c] = {
        "flagship_rp1/aastex/rp1_flagship_polished.tex": rd(f"{SNAP}/candidates/cycle_{c}_package/flagship_rp1/aastex/rp1_flagship_polished.tex"),
        "supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex": rd(f"{SNAP}/candidates/cycle_{c}_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex"),
    }
NEARKINDS = {"ci_interval", "point_estimate", "fraction", "table_row"}
summary = {}
for c in ("05", "06", "07"):
    fails = []
    nears = []
    exact_mismatch_c5 = []
    for e in E:
        text = cycles[c][e["file"]]
        if e["match_mode"] == "numeric_token":
            n, _ = token_count(text, e["exact_string"])
        else:
            n = text.count(e["exact_string"])
        ok = n >= e["occurrences_expected"]
        if not ok:
            fails.append((e["id"], n, e["occurrences_expected"]))
        if c == "05" and n != e["occurrences_expected"]:
            exact_mismatch_c5.append((e["id"], n, e["occurrences_expected"]))
        if e["kind"] in NEARKINDS:
            nm, variants = near_miss(text, e["exact_string"])
            if nm > 0:
                nears.append((e["id"], nm, sorted(set(variants))[:3]))
    summary[c] = (fails, nears, exact_mismatch_c5)
    print(f"--- cycle {c}: clause-1 failures={len(fails)}, near-miss hits={len(nears)}")
    for f in fails:
        print(f"    FAIL count {f[0]}: found {f[1]}, expected >= {f[2]}")
    for nmi in nears:
        print(f"    NEAR-MISS {nmi[0]}: {nmi[1]} variant(s) e.g. {nmi[2]}")
    if c == "05":
        print(f"    cycle-5 exact-count mismatches (found != expected): {exact_mismatch_c5 if exact_mismatch_c5 else 'NONE'}")

print()
print("=" * 78)
print("C2 PROBES: token anchors")
print("=" * 78)
sup5 = cycles["05"]["supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex"]
flg5 = cycles["05"]["flagship_rp1/aastex/rp1_flagship_polished.tex"]
sup5_lines = sup5.split("\n")
flg5_lines = flg5.split("\n")
for (fname, lines_, s, label) in [
    ("sup", sup5_lines, "15", "SUP-CELLS '15'"),
    ("sup", sup5_lines, "50", "SUP-CELL-MIN '50'"),
    ("flg", flg5_lines, "67", "FLG-UNCLASS '67'"),
]:
    per = []
    for i, ln in enumerate(lines_, 1):
        n, hits = token_count(ln, s)
        if n:
            ctxs = [ln[max(0, h - 25):h + len(s) + 25].replace("\t", " ") for h in hits]
            per.append((i, n, ctxs))
    print(f"{label}: token occurrences by line:")
    for i, n, ctxs in per:
        for ctx in ctxs:
            print(f"    line {i} (n={n}): ...{ctx}...")

print()
print("=" * 78)
print("C2 ARITHMETIC RECOMPUTES (manifest+RCA derivable numbers)")
print("=" * 78)
def r3(x): return str(Decimal(str(x)).quantize(Decimal("0.001"), ROUND_HALF_EVEN))
checks = []
checks.append(("denominator sum 39553+12234+8146+67", 39553 + 12234 + 8146 + 67, 60000))
checks.append(("coverage 60000/249917 % (1dp)", round(60000 / 249917 * 100, 1), 24.0))
checks.append(("env hi 3456/15000 (3dp)", r3(3456 / 15000), "0.230"))
checks.append(("env lo 2710/15000 (3dp)", r3(2710 / 15000), "0.181"))
checks.append(("env hi-lo 0.230-0.181 in [0.041,0.059]", 0.041 <= (0.230 - 0.181) <= 0.059, True))
checks.append(("coef 0.032 -> 3.2 pp", 0.032 * 100, 3.2))
checks.append(("hi-exc 4440/60000 (3dp)", r3(4440 / 60000), "0.074"))
checks.append(("jet hi-lo 0.509-0.367 in [0.112,0.170]", 0.112 <= round(0.509 - 0.367, 3) <= 0.170, True))
checks.append(("tracer 0.418/0.136 (1dp)", round(0.418 / 0.136, 1), 3.1))
checks.append(("reuse 2731+1508", 2731 + 1508, 4239))
checks.append(("reuse feasibility 8146-2731 uses over 1508 controls, max26", 1508 * 2 <= 8146 - 2731 <= 1508 * 26, True))
for label, got, exp in checks:
    print(f"{'PASS' if got == exp else 'FAIL'}: {label}: got {got}, expected {exp}")

print()
print("=" * 78)
print("C3 RAW ARTIFACTS vs manifest artifact_full_precision + RCA E1/E3")
print("=" * 78)
flg_art = json.load(open(f"{SNAP}/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json"))
m3_art = json.load(open(f"{SNAP}/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p3_simulation_validation/analysis_results.json"))
for fld in ["matched_delta_log_sSFR_median_dex", "matched_delta_log_sSFR_median_ci95_bootstrap",
            "match_abs_delta_logM_median", "match_abs_delta_z_median", "bpt_counts"]:
    v = findkey(flg_art, fld)
    print(f"flagship artifact {fld} = {v}")
for fld in ["quenched_fraction_range", "agn_fraction_range", "result_bullets"]:
    v = findkey(m3_art, fld)
    print(f"m3_p3 artifact {fld} = {json.dumps(v)[:300]}")
# manifest full-precision fields vs artifact
for e in E:
    if "artifact_full_precision" in e and e["id"] in ("FLG-MEDIAN-OFFSET", "FLG-CI95", "FLG-SEP-LOGM", "FLG-SEP-Z", "FLG-SF", "FLG-COMP", "FLG-UNCLASS"):
        print(f"manifest {e['id']} artifact_full_precision={e['artifact_full_precision']}")
# m3_p3 cell table: find rows and check rounding of every cell vs SUP-ROW strings
cells = findkey(m3_art, "cells") or findkey(m3_art, "table") or findkey(m3_art, "rows")
print("m3_p3 cell-table key found:", bool(cells))
if cells:
    print(json.dumps(cells)[:400])

print()
print("=" * 78)
print("C3/C4 AUDIT JSONs + custody JSON claims (RCA section 1 table)")
print("=" * 78)
a5 = json.load(open(f"{SNAP}/candidates/cycle_05_package/CYCLE_05_tables_figures_AUDIT.json"))
a6 = json.load(open(f"{SNAP}/candidates/cycle_06_package/CYCLE_06_literature_AUDIT.json"))
a7 = json.load(open(f"{SNAP}/candidates/cycle_07_package/CYCLE_07_introduction_AUDIT.json"))
for nm, a in (("c5", a5), ("c6", a6), ("c7", a7)):
    for k in ("integrity_blockers", "numeric_invariants_missing", "fatal_failures", "undefined_citations"):
        v = findkey(a, k)
        print(f"{nm} {k} = {json.dumps(v)[:200]}")
cust = rd(f"{SNAP}/candidates/cycle_05_package/provenance/REAL_DATA_SOURCE_CUSTODY.json")
for h, lbl in [("63b3920e158ba3be3a78ac0fcf771a979ccf43afe1a8759eda921e1f35ae9384", "c5 flagship hash in custody"),
               ("a4e3d66c5d4fdffe969d5520636f89d963beece6f44246dd68aa3e98673cdc71", "c5 supplement hash in custody"),
               ("668ad7a67290600ff5028ae587d32ef239a09bd8627a480539f37e1927d659df", "flagship results hash in custody"),
               ("6f289f8c68da425eb3d8005e673bf5c5c02cf917eaa2bc6feedd053535de8f52", "m3_p3 results hash in custody"),
               ("4ea53af867cccccb2b68b81557ff84fe90ec3f13e0512ffbdc977fa7216996fd", "pairs CSV hash in custody")]:
    print(f"{lbl}: {'PRESENT' if h in cust else 'ABSENT'}")

print()
print("=" * 78)
print("C4 BIBITEM claims (RCA 2.4 / INTRO_LIT bibliography rule)")
print("=" * 78)
keys = ["brinchmann2004", "kauffmann2003bpt", "heckmanbest2014", "ellison2011", "schawinski2010",
        "bluck2014", "piotrowska2022", "kewley2005", "cidfernandes2011", "stasinska2008", "belfiore2016",
        "ellison2021", "harrison2017", "strateva2001", "mendel2014", "mcnamara2007", "dawson2013", "dominguezsanchez2018"]
for k in keys:
    row = []
    for c in ("05", "06", "07"):
        f = cycles[c]["flagship_rp1/aastex/rp1_flagship_polished.tex"].count("\\bibitem[" ) and None
        nf = cycles[c]["flagship_rp1/aastex/rp1_flagship_polished.tex"].count("{" + k + "}")
        ns = cycles[c]["supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex"].count("{" + k + "}")
        row.append(f"c{c} flg={nf} sup={ns}")
    print(f"{k:24s} " + " | ".join(row))

print()
print("=" * 78)
print("C5 CUSTODY RECHECK: every file P1_RECEIPT lists")
print("=" * 78)
claims = [
    (P1 + "/P1_ACK.md", 566, "c3d072cbddf68964d9749cb6eb767555d9a1d465d61d802d9c11d02bcdeb423b"),
    (P1 + "/INVARIANT_MANIFEST.json", 51754, "f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717"),
    (P1 + "/RCA_NUMERIC_DRIFT.md", 15941, "45223b5690d33d770b6b3e2905d8f05746adec7b37e6052a6a18caed65cf0096"),
    (P1 + "/INTRODUCTION_LITERATURE_REFERENCE.md", 14196, "874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d"),
    (P1 + "/tools/build_manifest.py", 19178, "0b81226d406326f263f08b4e3b316d8d946e6d0c48f5677b539209ff5c420122"),
    (P1 + "/FABLE_BURN_P1_DONE_20260711T010503Z", 0, None),
]
import os
for p, b, h in claims:
    ab = os.path.getsize(p)
    ah = sha(p) if h else "-"
    ok = (ab == b) and (h is None or ah == h)
    print(f"{'PASS' if ok else 'FAIL'}: {os.path.basename(p)} bytes {ab} (claim {b}) sha {'match' if h and ah==h else ('n/a' if h is None else 'MISMATCH '+ah)}")
snapmap = [
    ("candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex", "63b3920e158ba3be3a78ac0fcf771a979ccf43afe1a8759eda921e1f35ae9384"),
    ("candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex", "a4e3d66c5d4fdffe969d5520636f89d963beece6f44246dd68aa3e98673cdc71"),
    ("candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex", "55c497ffcc00c56953ab84a2ebb1bc2e375c6d68523958b733cc51439fe09c80"),
    ("candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex", "38bb60c135eec8c7cecc0b39cfbd55cced65f00cdbbb00922cefa5b87c450d05"),
    ("candidates/cycle_06_package/CYCLE_06_literature_AUDIT.json", "8080d24568c089c44d9e3b821068882a1f45d87441ad45573aaf6fd33f5fa4d1"),
    ("candidates/cycle_07_package/flagship_rp1/aastex/rp1_flagship_polished.tex", "5fc4fea3fa270472f9d2885b68ac1c97c8292111b60d73f275a41adb101c963b"),
    ("candidates/cycle_07_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex", "9e99adc72d1a0b939253a8ae337ea0d620fcccc3dc8e279133a0b177689ac0fb"),
    ("candidates/cycle_07_package/CYCLE_07_introduction_AUDIT.json", "51204dd2b1027e3be25b57385a8367cd9f52bd45c0a3a3d06425c4a9e213c034"),
    ("candidates/cycle_05_package/provenance/REAL_DATA_SOURCE_CUSTODY.json", "92c0f786c6ba2ded5f7e036cc3c775c43d3f71567223bd28f5d3f1a158d50c6d"),
    ("candidates/cycle_05_package/CYCLE_05_tables_figures_AUDIT.json", "79d6dd688fedaf95101fa4ce2f164244726a1c35cf0db8443c8024512a8c0178"),
    ("runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json", "668ad7a67290600ff5028ae587d32ef239a09bd8627a480539f37e1927d659df"),
    ("runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p3_simulation_validation/analysis_results.json", "6f289f8c68da425eb3d8005e673bf5c5c02cf917eaa2bc6feedd053535de8f52"),
]
print("-- snapshot copies vs receipt-claimed original hashes:")
for rel, h in snapmap:
    ah = sha(f"{SNAP}/{rel}")
    print(f"{'PASS' if ah==h else 'FAIL'}: snapshot {rel.split('/')[-1]} ({rel.split('/')[1] if '/' in rel else rel})")
    if ah != h:
        print(f"    got {ah}")
print("-- manifest snapshot_sha256 block vs receipt table:")
for k, v in man["snapshot_sha256"].items():
    match = [h for rel, h in snapmap if rel.replace("candidates/", "candidates/") == k or k.endswith(rel)]
    exp = dict(snapmap).get(k, None)
    print(f"{'PASS' if exp==v else 'FAIL'}: {k.split('/')[-2]}/{k.split('/')[-1]} manifest={v[:12]}... receipt={'same' if exp==v else exp}")
print("-- live originals (observational; may legitimately have moved on):")
livemap = [(f"{S_ORIG}/{rel}", h) for rel, h in snapmap if rel.startswith("candidates")] + \
          [(f"{R_ORIG}/{rel[5:]}", h) for rel, h in snapmap if rel.startswith("runs/")]
for p, h in livemap:
    try:
        ah = sha(p)
        print(f"{'MATCH' if ah==h else 'CHANGED'}: {p.split('/aas-autopilot/')[-1]}")
    except FileNotFoundError:
        print(f"GONE: {p.split('/aas-autopilot/')[-1]}")
csvp = f"{R_ORIG}/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv"
try:
    ch = sha(csvp)
    okc = ch == "4ea53af867cccccb2b68b81557ff84fe90ec3f13e0512ffbdc977fa7216996fd"
    print(f"{'MATCH' if okc else 'CHANGED'}: pairs CSV live hash")
    if okc:
        with open(csvp, newline="") as f:
            rdr = csv.reader(f)
            hdr = next(rdr)
            rows = list(rdr)
        print(f"CSV header: {hdr}")
        print(f"CSV data rows: {len(rows)} (RCA claims 8,146)")
        ctl_idx = [i for i, c in enumerate(hdr) if "control" in c.lower() or c.lower().startswith("sf_")]
        print(f"candidate control-id columns: {[hdr[i] for i in ctl_idx]}")
        for i in ctl_idx[:3]:
            vals = Counter(r[i] for r in rows)
            once = sum(1 for v in vals.values() if v == 1)
            print(f"  col '{hdr[i]}': unique={len(vals)} once={once} reused={len(vals)-once} maxreuse={max(vals.values())}")
except FileNotFoundError:
    print("GONE: pairs CSV")
