#!/usr/bin/env python3
"""kimi's independent review probes for the R3C2 D1/D7/batch CANDIDATES (2026-09-06).
Everything is written under _review_kimi/kimi_work/ only. Prints every command and its output."""
import json, subprocess, sys, pathlib, hashlib, shutil

H = pathlib.Path(__file__).resolve().parent
KIT = H.parents[1]                                  # r3c2_staged_d1d7/
SEAT = KIT/"r3c2_ledger_tools_STAGED.py"
BATCH = KIT/"r3c2_batch_tools_STAGED.py"
PY = "/usr/bin/python3"
W = H/"out"; shutil.rmtree(W, ignore_errors=True); W.mkdir(parents=True)

def w(p, obj):
    p = W/p
    p.write_text(json.dumps(obj, indent=1, sort_keys=True) if not isinstance(obj, str) else obj)
    return str(p)

def run(tool, *a):
    cmd = [PY, "-E", str(tool), *[str(x) for x in a]]
    r = subprocess.run(cmd, capture_output=True, text=True)
    print("$ " + " ".join(cmd))
    print(r.stdout + r.stderr, end="")
    print(f"[exit {r.returncode}]\n")
    return r.returncode, r.stdout + r.stderr

# ---------------- my own sources (distinct from the kit's fixtures) ----------------
S = W/"src"; S.mkdir()
(S/"paperX.txt").write_text(
    "Paper X\n"
    "We derive q = 8.5 from our model.\n"
    "Using r = 2 we get s = 16.\n")
(S/"paperY.txt").write_text(
    "Paper Y\n"
    "Setup.\n"
    "In 2022 the survey began.\n"
    "We obtain w = 17.4 from the fit.\n")          # line 4: the REQUIRED passage
def sha_s(s): return hashlib.sha256(s.encode()).hexdigest()
(S/"R3C2_CORPUS_MANIFEST.md").write_text(
    "# manifest\n| # | file | sha256 | bytes | non-blank lines |\n|---|---|---|---|---|\n"
    f"| 1 | `paperX.txt` | `{sha_s((S/'paperX.txt').read_text())}` | 1 | 3 |\n"
    f"| 2 | `paperY.txt` | `{sha_s((S/'paperY.txt').read_text())}` | 1 | 4 |\n")

REQ = ("paperY.txt", 4, "17.4")
def cand(cid, f, ln, num, inc, outc=None, att=0, pv=None, rv=None):
    c = {"candidate_id": cid, "source_file": f, "source_line": ln, "numeral": num, "included": inc}
    if inc:
        c.update({"attempts": att, "outcome": outc})
        if pv is not None: c.update({"printed_value": pv, "reproduced_value": rv})
    return c
def cfile(cs):
    inc = sum(1 for c in cs if c["included"])
    return {"declared_candidate_count": len(cs), "declared_included_count": inc,
            "declared_excluded_count": len(cs)-inc,
            "declared_attempt_count": sum(c.get("attempts", 0) for c in cs if c["included"]),
            "candidates": cs}

# BOTH seats omit paperY.txt:4 '17.4' (unambiguous: 'We obtain w = 17.4 from the fit.' is the paper's own result)
seatA = [cand("c1","paperX.txt",2,"8.5",True,"REPRO_WITHIN_STATED_PRECISION",1,"8.5","8.5"),
         cand("c2","paperX.txt",3,"16",True,"REPRO_NOT_EVALUABLE",0),
         cand("c3","paperY.txt",3,"2022",False)]
seatB = [dict(c) for c in seatA]
assert not any((c["source_file"],c["source_line"],c["numeral"])==REQ for c in seatA+seatB)
agreed = seatA
sc  = w("k_sealed_c.json", cfile(agreed))
sx  = w("k_sealed_x.json", {"declared_exclusion_count":1,"exclusions":[{"candidate_id":"c3","kind":"DATE","source_file":"paperY.txt","source_line":3,"numeral":"2022"}]})
sl  = w("k_sealed_l.json", {"records":[{"claim_id":"c1","input_id":"i1","symbol":"r","status":"PRINTED","origin":"CHOSEN",
        "origin_evidence":{"reason_code":"ORIG_CHOICE_STATED","source_file":"paperX.txt","source_line":3,"verbatim":"Using r = 2"},
        "derived_from":[],"value":"2","source_file":"paperX.txt","source_line":3}]})

aud = [dict(c, candidate_id="a"+c["candidate_id"][1:]) for c in agreed]
aud_incl_req = aud + [cand("a4",*REQ,True,"REPRO_NO_DERIVATION_STATED",0)]
ac  = w("k_aud_c.json", cfile(aud_incl_req))
ax  = w("k_aud_x.json", {"declared_exclusion_count":1,"exclusions":[{"candidate_id":"a3","kind":"DATE","source_file":"paperY.txt","source_line":3,"numeral":"2022"}]})
seed = "abcdef0123456789"*4

print("="*30, "K1: BOTH SEATS OMIT a §1-required passage; the auditor's enumeration retains it", "="*30)
run(SEAT, "audit", "seal-enumeration", ac, ax, W/"k_stage1.txt")
run(SEAT, "audit", "select", sc, seed, W/"k_sel.json")
sel = json.loads((W/"k_sel.json").read_text())
print("selection:", sel["audited_ids"], "\n")
red = {cid: ({"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"8.5","reproduced_value":"8.5","inputs":{"i1":"CHOSEN"}}
             if cid=="c1" else {"outcome":"REPRO_NOT_EVALUABLE","inputs":{}}) for cid in sel["audited_ids"]}
rd = w("k_red.json", red)
rc,out = run(SEAT, "audit", "compare", W/"k_stage1.txt", ac, ax, sc, sx, sl, W/"k_sel.json", rd, W/"k_C6_AUDIT.json")

print("="*30, "K2: REVERSE — sealed includes the passage; the auditor's enumeration lacks it", "="*30)
sc2 = w("k2_sealed_c.json", cfile(agreed+[cand("c4",*REQ,True,"REPRO_NO_DERIVATION_STATED",0)]))
ac2 = w("k2_aud_c.json", cfile(aud))
run(SEAT, "audit", "seal-enumeration", ac2, ax, W/"k2_stage1.txt")
run(SEAT, "audit", "select", sc2, seed, W/"k2_sel.json")
sel2 = json.loads((W/"k2_sel.json").read_text())
print("selection:", sel2["audited_ids"], "\n")
red2 = {cid: ({"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"8.5","reproduced_value":"8.5","inputs":{"i1":"CHOSEN"}}
              if cid=="c1" else {"outcome":"REPRO_NOT_EVALUABLE" if cid=="c2" else "REPRO_NO_DERIVATION_STATED","inputs":{}})
        for cid in sel2["audited_ids"]}
rd2 = w("k2_red.json", red2)
run(SEAT, "audit", "compare", W/"k2_stage1.txt", ac2, ax, sc2, sx, sl, W/"k2_sel.json", rd2, W/"k2_C6_AUDIT.json")

print("="*30, "K3: sealed EXCLUDED passage absent from the auditor's whole enumeration", "="*30)
ac3 = w("k3_aud_c.json", cfile(aud[:2]))                       # auditor has a1,a2 only; never lists paperY.txt:3 at all
ax3 = w("k3_aud_x.json", {"declared_exclusion_count":0,"exclusions":[]})
run(SEAT, "audit", "seal-enumeration", ac3, ax3, W/"k3_stage1.txt")
run(SEAT, "audit", "compare", W/"k3_stage1.txt", ac3, ax3, sc, sx, sl, W/"k_sel.json", rd, W/"k3_C6_AUDIT.json")

print("="*30, "K4: auditor candidate file whose declared counts are WRONG (census would FAIL it)", "="*30)
bad = cfile(aud); bad["declared_candidate_count"]=99; bad["declared_included_count"]=88
ac4 = w("k4_aud_c_badcounts.json", bad)
run(SEAT, "audit", "seal-enumeration", ac4, ax, W/"k4_stage1.txt")
rc4,out4 = run(SEAT, "audit", "compare", W/"k4_stage1.txt", ac4, ax, sc, sx, sl, W/"k_sel.json", rd, W/"k4_C6_AUDIT.json")
print("--- and the same auditor file under the pinned census control:")
run(SEAT, "census", ac4, ax)

print("="*30, "K5: D1 — import evidence cases under validate", "="*30)
D = W/"d1src"; D.mkdir()
(D/"paperP.txt").write_text(
    "Paper P\n"
    "Intro.\n"
    "We take b = 7 from paperQ (2021).\n"
    "We take c = 3 from paperQ (2021).\n"
    "We take d = 11 from paperQ (2021).\n")
(D/"paperQ.txt").write_text(
    "Paper Q\n"
    "\n"
    "Setup.\n"
    "We fit b = 7 to the data.\n"
    "We measure c = 3 in the lab.\n"
    "We adopt d = 11 from Zee (1999).\n"
    "Recall b = 7 from above.\n")
(D/"R3C2_CORPUS_MANIFEST.md").write_text(
    "# manifest\n| # | file | sha256 | bytes | non-blank lines |\n|---|---|---|---|---|\n"
    f"| 1 | `paperP.txt` | `{sha_s((D/'paperP.txt').read_text())}` | 1 | 5 |\n"
    f"| 2 | `paperQ.txt` | `{sha_s((D/'paperQ.txt').read_text())}` | 1 | 6 |\n")
def d1rec(**k):
    r = {"claim_id":"p1","input_id":"j1","symbol":"b","status":"PRINTED","origin":"IMPORTED",
         "origin_evidence":{"reason_code":"ORIG_CITATION","source_file":"paperP.txt","source_line":3,"verbatim":"We take b = 7 from paperQ (2021)"},
         "derived_from":[],"value":"7","source_file":"paperQ.txt","source_line":4}
    for kk,v in k.items():
        if kk.startswith("ev_"): r["origin_evidence"][kk[3:]] = v
        else: r[kk] = v
    return {"records":[r]}
print("--- K5a: review-form, source line 'We fit b = 7 to the data.'")
run(SEAT, "validate", w("d1_a.json", d1rec()), D)
print("--- K5b: review-form, source line 'We measure c = 3 in the lab.'")
run(SEAT, "validate", w("d1_b.json", d1rec(symbol="c", value="3", source_line=5, ev_source_line=4, ev_verbatim="We take c = 3 from paperQ (2021)")), D)
print("--- K5c: review-form, source line 'We adopt d = 11 from Zee (1999).'")
run(SEAT, "validate", w("d1_c.json", d1rec(symbol="d", value="11", source_line=6, ev_source_line=5, ev_verbatim="We take d = 11 from paperQ (2021)")), D)
print("--- K5d: value machine-matches at TWO source lines (4 and 7); filing the second")
run(SEAT, "validate", w("d1_d.json", d1rec(source_line=7)), D)
print("--- K5e: TORI-form evidence (the source's own line quoted as the citation)")
run(SEAT, "validate", w("d1_e.json", d1rec(ev_source_file="paperQ.txt", ev_source_line=4, ev_verbatim="We fit b = 7 to the data")), D)
print("--- K5f: a seat quoting the source's line under the ORDINARY precedence files FITTED")
run(SEAT, "validate", w("d1_f.json", d1rec(origin="FITTED", ev_reason_code="ORIG_FIT_STATED", ev_source_file="paperQ.txt", ev_source_line=4, ev_verbatim="We fit b = 7 to the data")), D)
print("--- K5g: review-form but the 'citing sentence' sits in a THIRD pinned text (not the borrower)")
(D/"paperR.txt").write_text("Paper R\nWe take b = 7 from paperQ (2021).\n")
(D/"R3C2_CORPUS_MANIFEST.md").write_text((D/"R3C2_CORPUS_MANIFEST.md").read_text() +
    f"| 3 | `paperR.txt` | `{sha_s((D/'paperR.txt').read_text())}` | 1 | 2 |\n")
run(SEAT, "validate", w("d1_g.json", d1rec(ev_source_file="paperR.txt", ev_source_line=2)), D)

print("="*30, "K6: batch join — a batch-1 LEDGER record citing a batch-2 text", "="*30)
M = W/"m3.md"
(D2 := W/"m3src").mkdir()
for t in ("bt1.txt","bt2.txt","bt3.txt"): (D2/t).write_text(t+"\n")
M.write_text("# m\n| # | file | sha256 | b | n |\n|---|---|---|---|---|\n" +
    "".join(f"| {i+1} | `{t}` | `{sha_s(t+chr(10))}` | 1 | 1 |\n" for i,t in enumerate(("bt1.txt","bt2.txt","bt3.txt"))))
run(BATCH, "partition", M, 2, W/"k6_part.json")
SD = W/"k6seat"; SD.mkdir()
PK = "cd"*32
def bfiles(k, cands, excls, recs):
    (SD/f"candidates_b{k}.json").write_text(json.dumps(cfile(cands), indent=1, sort_keys=True))
    (SD/f"exclusions_b{k}.json").write_text(json.dumps({"declared_exclusion_count":len(excls),"exclusions":excls}, indent=1, sort_keys=True))
    (SD/f"ledger_b{k}.json").write_text(json.dumps({"records":recs}, indent=1, sort_keys=True))
    (SD/f"SEAT_REPORT_b{k}.md").write_text(f"ACCESS_SHA={PK}\nbatch {k}\n")
bfiles(1, [cand("k1","bt1.txt",2,"9",True,"REPRO_NOT_EVALUABLE",0)], [],
       [{"claim_id":"k1","input_id":"j1","symbol":"q","status":"PRINTED","origin":"IMPORTED",
         "origin_evidence":{"reason_code":"ORIG_CITATION","source_file":"bt1.txt","source_line":3,"verbatim":"We take q = 9 from bt3"},
         "derived_from":[],"value":"9","source_file":"bt3.txt","source_line":2}])   # external source is a BATCH-2 text
bfiles(2, [], [], [])
run(BATCH, "seal", W/"k6_part.json", 1, SD, W/"k6_seals.json")
run(BATCH, "seal", W/"k6_part.json", 2, SD, W/"k6_seals.json")
run(BATCH, "join", W/"k6_part.json", SD, W/"k6_seals.json", str(W/"k6_join_"))
print("--- per-batch validate of that batch-1 ledger in a directory holding ONLY batch-1 texts (+ the manifest):")
B1 = W/"k6_batch1_only"; B1.mkdir()
(B1/"bt1.txt").write_text("bt1.txt\nline\nWe take q = 9 from bt3\n")
(B1/"bt2.txt").write_text("bt2.txt\n")
(B1/"R3C2_CORPUS_MANIFEST.md").write_text(M.read_text())
run(SEAT, "validate", SD/"ledger_b1.json", B1)
print("--- the same ledger validated against the FULL corpus (what a post-join lane-side run would do):")
run(SEAT, "validate", SD/"ledger_b1.json", D2)

print("ALL KIMI PROBES DONE")
