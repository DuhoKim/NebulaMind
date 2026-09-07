#!/usr/bin/env python3
"""review3 kimi — independent probes of the revision-3 claimed repairs. Own fixtures only, under _review3_kimi/work/.
Never touches the kit's fixtures. Prints rc + relevant stdout lines per probe; full log in work/command_log.json."""
import json, subprocess, sys, pathlib, hashlib, shutil

H = pathlib.Path(__file__).resolve().parent
KIT = H.parent
SEAT = KIT/"r3c2_ledger_tools_STAGED.py"
BATCH = KIT/"r3c2_batch_tools_STAGED.py"
PY = "/usr/bin/python3"
W = H/"work"
shutil.rmtree(W, ignore_errors=True); W.mkdir(parents=True)
LOG = []

def run(tool, *a):
    cmd = [PY, "-E", str(tool), *[str(x) for x in a]]
    r = subprocess.run(cmd, capture_output=True, text=True)
    LOG.append({"cmd": " ".join(str(x) for x in cmd), "rc": r.returncode, "out": r.stdout + r.stderr})
    return r.returncode, r.stdout + r.stderr

def w(name, obj):
    p = W/name
    p.write_text(json.dumps(obj, indent=1, sort_keys=True) if not isinstance(obj, str) else obj)
    return p

def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

def manifest(path, d, files):
    rows = "".join(f"| {i+1} | `{f}` | `{sha(d/f)}` | {(d/f).stat().st_size} | {sum(1 for l in (d/f).read_text().splitlines() if l.strip())} |\n" for i, f in enumerate(files))
    pathlib.Path(path).write_text("# review3 kimi manifest\n| # | file | sha256 | bytes | non-blank lines |\n|---|---|---|---|---|\n" + rows)

def show(tag, rc, out, only=None):
    lines = [l for l in out.splitlines() if (only is None or any(s in l for s in only)) and not l.startswith(" ")]
    print(f"--- {tag} (rc={rc}) ---")
    for l in (lines if lines else out.splitlines()[-4:]): print(l)
    print()

# ============================================================ D1 fixtures (rows 2,3,4; ND1)
S = W/"d1src"; S.mkdir()
(S/"k3borrow.txt").write_text("K3 synthetic borrower (review3 kimi fixture)\nIntro.\nWe adopt q = 7 from k3src (2021).\nThen y = 2q = 14.\n")
(S/"k3src.txt").write_text("K3 synthetic source (review3 kimi fixture)\nSee appendix b = 70.\nSetup.\nFor this calculation we choose q = 7.\nLater we repeat q = 7.\n")
(S/"k3nosym.txt").write_text("K3 no-symbol source\nThe total is 7 on the seventh page.\n")
(S/"k3split.txt").write_text("K3 split source\nq is our coupling constant.\nthe answer is 7.\n")
manifest(S/"R3C2_CORPUS_MANIFEST.md", S, ["k3borrow.txt", "k3src.txt", "k3nosym.txt", "k3split.txt"])
CANDS = w("d1_cands.json", {"declared_candidate_count": 1, "declared_included_count": 1, "declared_excluded_count": 0, "declared_attempt_count": 1,
    "candidates": [{"candidate_id": "k3borrow.txt#1", "source_file": "k3borrow.txt", "source_line": 4, "numeral": "14", "included": True, "attempts": 1,
                    "outcome": "REPRO_WITHIN_STATED_PRECISION", "printed_value": "14", "reproduced_value": "14"}]})
def rec(**k):
    r = {"claim_id": "k3borrow.txt#1", "input_id": "k3borrow.txt#1.q", "symbol": "q", "status": "PRINTED", "origin": "IMPORTED",
         "origin_evidence": {"reason_code": "ORIG_CITATION", "source_file": "k3borrow.txt", "source_line": 3, "verbatim": "We adopt q = 7 from k3src (2021)"},
         "derived_from": [], "value": "7", "source_file": "k3src.txt", "source_line": 4}
    for kk, v in k.items():
        if kk.startswith("ev_"): r["origin_evidence"][kk[3:]] = v
        else: r[kk] = v
    return r

print("========== ROW 2 (T8): import re-filed under another reason code ==========")
rc, out = run(SEAT, "validate", w("d1_pos.json", {"records": [rec()]}), S, CANDS)
show("R2 sanity: honest import validates", rc, out, ["C3_NO_SUBSTITUTION"])
rc, out = run(SEAT, "validate", w("d1_refiled_chosen.json", {"records": [rec(origin="CHOSEN", ev_reason_code="ORIG_CHOICE_STATED", ev_source_file="k3src.txt", ev_source_line=4, ev_verbatim="we choose q = 7")]}), S, CANDS)
show("R2 attack: re-filed CHOSEN quoting the source's choice sentence", rc, out, ["FAIL:", "C3_NO_SUBSTITUTION"])
rc, out = run(SEAT, "validate", w("d1_refiled_fitted.json", {"records": [rec(origin="FITTED", ev_reason_code="ORIG_FIT_STATED", ev_source_file="k3src.txt", ev_source_line=4, ev_verbatim="we choose q = 7")]}), S, CANDS)
show("R2 attack variant: re-filed FITTED ('whatever reason code was submitted')", rc, out, ["FAIL:", "C3_NO_SUBSTITUTION"])

print("========== ROW 3 (T8): symbol floor — no line carries symbol and numeral ==========")
rc, out = run(SEAT, "validate", w("d1_nosym.json", {"records": [rec(source_file="k3nosym.txt", source_line=2)]}), S, CANDS)
show("R3 attack: numeral present, symbol nowhere in the source", rc, out, ["FAIL:", "C3_NO_SUBSTITUTION"])
rc, out = run(SEAT, "validate", w("d1_split.json", {"records": [rec(source_file="k3split.txt", source_line=3)]}), S, CANDS)
show("R3 attack variant: symbol on one line, numeral on another, never together", rc, out, ["FAIL:", "C3_NO_SUBSTITUTION"])

print("========== ROW 4 (T8): the landed rule is the deterministic first-line rule ==========")
rc, out = run(SEAT, "validate", w("d1_secondline.json", {"records": [rec(source_line=5)]}), S, CANDS)
show("R4: filing the SECOND matching line (seat discretion would allow it)", rc, out, ["FAIL:", "C3_NO_SUBSTITUTION"])

print("========== ND1 candidate: non-import PRINTED record, claim NOT in the candidate file, value line in another file ==========")
ghost = rec(origin="CHOSEN", ev_reason_code="ORIG_CHOICE_STATED", ev_source_file="k3src.txt", ev_source_line=4, ev_verbatim="we choose q = 7", claim_id="ghost.txt#9", input_id="ghost.txt#9.q")
rc, out = run(SEAT, "validate", w("d1_ghost.json", {"records": [ghost]}), S, CANDS)
show("ND1: unknown claim id + cross-file value line + CHOSEN", rc, out, ["FAIL:", "C3_NO_SUBSTITUTION"])
ghost_imp = rec(claim_id="ghost.txt#9", input_id="ghost.txt#9.q")
rc, out = run(SEAT, "validate", w("d1_ghost_imp.json", {"records": [ghost_imp]}), S, CANDS)
show("ND1 contrast: unknown claim id as IMPORT (the import branch does flag it)", rc, out, ["FAIL:", "C3_NO_SUBSTITUTION"])

# ============================================================ D7 fixtures (rows 1,7; ND2)
def cand(cid, f, ln, num, inc, outc=None, att=1, pv=None, rv=None):
    c = {"candidate_id": cid, "source_file": f, "source_line": ln, "numeral": num, "included": inc}
    if inc: c.update({"attempts": att, "outcome": outc})
    if pv is not None: c.update({"printed_value": pv, "reproduced_value": rv})
    return c
def cfile(name, cs):
    inc = sum(1 for c in cs if c["included"])
    return w(name, {"declared_candidate_count": len(cs), "declared_included_count": inc, "declared_excluded_count": len(cs)-inc,
                    "declared_attempt_count": sum(c.get("attempts", 0) for c in cs if c["included"]), "candidates": cs})
def xfile(name, xs): return w(name, {"declared_exclusion_count": len(xs), "exclusions": xs})

SC = [cand("c1", "r3a.txt", 4, "4", True, "REPRO_WITHIN_STATED_PRECISION", 1, "4", "4"),
      cand("c2", "r3a.txt", 9, "7", True, "REPRO_NOT_EVALUABLE", 0),
      cand("c3", "r3b.txt", 1, "2020", False)]
SX = [{"candidate_id": "c3", "kind": "DATE", "source_file": "r3b.txt", "source_line": 1, "numeral": "2020"}]
AC = [dict(c, candidate_id="a"+c["candidate_id"][1:]) for c in SC]
AX = [dict(SX[0], candidate_id="a3", kind="REFERENCE_NUMBER")]   # same passage, both excluded, KINDS DIFFER
sc = cfile("sealed_c.json", SC); sx = xfile("sealed_x.json", SX)
ac = cfile("aud_c.json", AC); ax = xfile("aud_x.json", AX)
sl = w("sealed_l.json", {"records": [rec(claim_id="c1", input_id="i1")]})
seed = "0123456789abcdef"*4
s1, sel, s2 = W/"stage1.txt", W/"sel.json", W/"stage2.txt"
rd = w("rd.json", {"c1": {"outcome": "REPRO_WITHIN_STATED_PRECISION", "printed_value": "4", "reproduced_value": "4", "inputs": {"i1": "IMPORTED"}},
                   "c2": {"outcome": "REPRO_NOT_EVALUABLE", "inputs": {}}})

print("========== ROW 1 (T6): seedless selection / zero-claim audit ==========")
rc, out = run(SEAT, "audit", "seal-enumeration", ac, ax, s1); show("R1 stage1 seal", rc, out, ["SHA256", "FAIL"])
rc, out = run(SEAT, "audit", "select", sc, seed, s1, sel); show("R1 select", rc, out, ["N=", "FAIL"])
rc, out = run(SEAT, "audit", "handout", sel, sc, W/"handout.json"); show("R1 handout", rc, out, ["handout:"])
rc, out = run(SEAT, "audit", "seal-rederivation", rd, s2); show("R1 stage2 seal", rc, out, ["SHA256", "FAIL"])
rc, out = run(SEAT, "audit", "compare", s1, ac, ax, sc, sx, sl, sel, s2, rd, W/"C6_pos.json")
show("R1 sanity: honest staged run passes", rc, out, ["C6_AUDIT_SAMPLE"])
selj = json.loads(sel.read_text())
ns = {k: v for k, v in selj.items() if k != "seed_hex"}; ns.update({"audited_ids": [], "sampled_ids": [], "k": 0})
rc, out = run(SEAT, "audit", "compare", s1, ac, ax, sc, sx, sl, w("sel_noseed.json", ns), s2, rd, W/"C6_noseed.json")
show("R1 attack: seedless selection, ids emptied, digests retained (rev-2 PASSed this)", rc, out, ["FAIL:", "C6_AUDIT_SAMPLE"])
em = dict(selj); em.update({"audited_ids": [], "sampled_ids": [], "k": 0})
rc, out = run(SEAT, "audit", "compare", s1, ac, ax, sc, sx, sl, w("sel_empty.json", em), s2, rd, W/"C6_empty.json")
show("R1 attack variant: seed retained, audit emptied -> recomputation catches it", rc, out, ["FAIL:", "C6_AUDIT_SAMPLE"])

print("========== ROW 7 (T3): vocabulary + study_files ==========")
c6p = json.loads((W/"C6_pos.json").read_text())
row = [r for r in c6p["completeness_rows"] if r["key"] == ["r3b.txt", 1, "2020"]][0]
print("both-excluded, kinds differ -> row:", json.dumps(row, sort_keys=True))
print("artefact study_files on PASS:", repr(c6p.get("study_files")))
c6n = json.loads((W/"C6_noseed.json").read_text())
print("artefact study_files on FAIL:", repr(c6n.get("study_files")))
print()

print("========== ND2 candidate: 64-char NON-hex seed in the selection ==========")
bs = dict(selj); bs["seed_hex"] = "Z"*64
rc, out = run(SEAT, "audit", "compare", s1, ac, ax, sc, sx, sl, w("sel_badseed.json", bs), s2, rd, W/"C6_badseed.json")
print(f"--- ND2: rc={rc}; token printed: {'C6_AUDIT_SAMPLE' in out}; artefact written: {(W/'C6_badseed.json').exists()} ---")
for l in out.splitlines()[-6:]: print(l)
print()

# ============================================================ batch fixtures (rows 5,6,8c)
print("========== ROWS 5/6/8c: join checks ==========")
CD = W/"corpus"; CD.mkdir()
T = ["u1.txt", "u2.txt", "u3.txt", "u4.txt", "u5.txt"]
for i, f in enumerate(T, 1):
    (CD/f).write_text(f"Paper {f}\nWe fix a = 2 here.\nResult r = {i}0.\n")
M = W/"manifest5.md"; manifest(M, CD, T)
rc, out = run(BATCH, "partition", M, 2, W/"part.json"); show("partition 5 -> 2", rc, out, ["batch"])
D = W/"seatK"; D.mkdir()
PK = "cd"*32
def bfiles(k, cands, excls, recs):
    inc = sum(1 for c in cands if c["included"]); att = sum(c.get("attempts", 0) for c in cands if c["included"])
    (D/f"candidates_b{k}.json").write_text(json.dumps({"declared_candidate_count": len(cands), "declared_included_count": inc, "declared_excluded_count": len(cands)-inc, "declared_attempt_count": att, "candidates": cands}, indent=1, sort_keys=True))
    (D/f"exclusions_b{k}.json").write_text(json.dumps({"declared_exclusion_count": len(excls), "exclusions": excls}, indent=1, sort_keys=True))
    (D/f"ledger_b{k}.json").write_text(json.dumps({"records": recs}, indent=1, sort_keys=True))
    (D/f"SEAT_REPORT_b{k}.md").write_text(f"ACCESS_SHA={PK}\nbatch {k} report\n")
r1 = {"claim_id": "u1.txt#1", "input_id": "u1.txt#1.a", "symbol": "a", "status": "PRINTED", "origin": "CHOSEN",
      "origin_evidence": {"reason_code": "ORIG_CHOICE_STATED", "source_file": "u1.txt", "source_line": 2, "verbatim": "We fix a = 2 here"},
      "derived_from": [], "value": "2", "source_file": "u1.txt", "source_line": 2}
B1C = [cand("u1.txt#1", "u1.txt", 3, "10", True, "REPRO_WITHIN_STATED_PRECISION", 1, "10", "10"), cand("u2.txt#1", "u2.txt", 2, "2", False)]
B1X = [{"candidate_id": "u2.txt#1", "kind": "AUTHOR_SPECIFIED_INPUT", "source_file": "u2.txt", "source_line": 2, "numeral": "2"}]
B2C = [cand("u4.txt#1", "u4.txt", 3, "40", True, "REPRO_NOT_EVALUABLE", 0)]
bfiles(1, B1C, B1X, [r1]); bfiles(2, B2C, [], [])
seals = W/"seals.json"
rc, out = run(BATCH, "seal", W/"part.json", 1, D, CD, seals); show("seal b1", rc, out, ["sealed", "FAIL"])
rc, out = run(BATCH, "seal", W/"part.json", 2, D, CD, seals); show("seal b2", rc, out, ["sealed", "FAIL"])
rc, out = run(BATCH, "join", W/"part.json", D, seals, M, str(W/"j_")); show("join positive", rc, out, ["JOIN", "joined:"])

import copy
base_seals = json.loads(seals.read_text())
def join_with(mut_seals=None, mut_dir=None, tag=""):
    sd = mut_seals or seals; dd = mut_dir or D
    rc, out = run(BATCH, "join", W/"part.json", dd, sd, M, str(W/f"j{tag}_"))
    show(tag, rc, out, ["FAIL:", "JOIN="])
    return rc, out

print("--- ROW 5 (T2): orphan claim and input-id form ---")
Do = W/"seatK_orphan"; shutil.copytree(D, Do)
l1 = json.loads((Do/"ledger_b1.json").read_text()); l1["records"][0]["claim_id"] = "u1.txt#77"; (Do/"ledger_b1.json").write_text(json.dumps(l1, indent=1, sort_keys=True))
s_o = W/"seals_o.json"; run(BATCH, "seal", W/"part.json", 1, Do, CD, s_o); run(BATCH, "seal", W/"part.json", 2, Do, CD, s_o)
join_with(s_o, Do, "R5a orphan claim (claim not an included candidate)")
Di = W/"seatK_inputid"; shutil.copytree(D, Di)
l1 = json.loads((Di/"ledger_b1.json").read_text()); l1["records"][0]["input_id"] = "i1"; (Di/"ledger_b1.json").write_text(json.dumps(l1, indent=1, sort_keys=True))
s_i = W/"seals_i.json"; run(BATCH, "seal", W/"part.json", 1, Di, CD, s_i); run(BATCH, "seal", W/"part.json", 2, Di, CD, s_i)
join_with(s_i, Di, "R5b input_id not of the form <claim file>#...")

print("--- ROW 6 (T11): predecessor chain, sealed ownership vs partition, extra seals ---")
sj = copy.deepcopy(base_seals); sj["seals"]["2"]["predecessor_seal_sha256"] = "0"*64
join_with(w("seals_chain.json", sj), None, "R6a batch-2 predecessor digest replaced by zeros")
sj = copy.deepcopy(base_seals); sj["seals"]["1"]["owned_files"] = ["u1.txt", "u2.txt"]
join_with(w("seals_own.json", sj), None, "R6b sealed ownership list differs from the partition")
sj = copy.deepcopy(base_seals); sj["seals"]["3"] = sj["seals"]["2"]
join_with(w("seals_extra.json", sj), None, "R6c an extra seal for a batch not in the partition")
sj = copy.deepcopy(base_seals); del sj["seals"]["2"]
join_with(w("seals_missing.json", sj), None, "R6d (bonus) a missing seal for batch 2")

print("--- ROW 8c (T13): candidate_id collision control (my own files) ---")
Dc = W/"seatK_collide"; shutil.copytree(D, Dc)
c2 = json.loads((Dc/"candidates_b2.json").read_text()); c2["candidates"].append(dict(c2["candidates"][0])); c2["declared_candidate_count"] = 2; c2["declared_included_count"] = 2
(Dc/"candidates_b2.json").write_text(json.dumps(c2, indent=1, sort_keys=True))
s_c = W/"seals_c.json"; run(BATCH, "seal", W/"part.json", 1, Dc, CD, s_c); run(BATCH, "seal", W/"part.json", 2, Dc, CD, s_c)
join_with(s_c, Dc, "R8c candidate_id collision")

(W/"command_log.json").write_text(json.dumps(LOG, indent=1))
print(f"full log: {W/'command_log.json'} ({len(LOG)} commands)")
