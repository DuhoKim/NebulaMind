#!/usr/bin/env python3
"""Review-2 (seat kimi) independent probes for the UNADOPTED D1/D7/batch candidate revision 2.
Builds its own fixtures under _review2_kimi/work/ and runs the STAGED tools against them.
Nothing outside _review2_kimi/ is touched."""
import json, pathlib, subprocess, sys, hashlib, shutil

K = pathlib.Path(__file__).resolve().parent          # _review2_kimi/
H = K.parent                                          # r3c2_staged_d1d7/
W = K / "work"
shutil.rmtree(W, ignore_errors=True)                  # my own scratch only (first-write seals refuse re-runs)
W.mkdir(parents=True, exist_ok=True)
SEAT = H / "r3c2_ledger_tools_STAGED.py"
PY = "/usr/bin/python3"
LOG = []

def run(*a):
    r = subprocess.run([PY, "-E", str(SEAT), *[str(x) for x in a]], capture_output=True, text=True)
    LOG.append({"cmd": [str(x) for x in a], "rc": r.returncode, "stdout": r.stdout, "stderr": r.stderr})
    return r.returncode, r.stdout + r.stderr

def w(p, obj):
    p = W / p
    p.write_text(json.dumps(obj, indent=1, sort_keys=True) if not isinstance(obj, str) else obj)
    return str(p)

def manifest(path, files_dir, files):
    rows = "".join(f"| {i+1} | `{f}` | `{hashlib.sha256((files_dir/f).read_bytes()).hexdigest()}` | {(files_dir/f).stat().st_size} | {sum(1 for l in (files_dir/f).read_text().splitlines() if l.strip())} |\n" for i, f in enumerate(files))
    pathlib.Path(path).write_text("# review2 manifest\n| # | file | sha256 | bytes | non-blank lines |\n|---|---|---|---|---|\n" + rows)

def cfile(name, cs):
    inc = sum(1 for c in cs if c["included"])
    return w(name, {"declared_candidate_count": len(cs), "declared_included_count": inc,
                    "declared_excluded_count": len(cs) - inc,
                    "declared_attempt_count": sum(c.get("attempts", 0) for c in cs if c["included"]),
                    "candidates": cs})

def xfile(name, xs):
    return w(name, {"declared_exclusion_count": len(xs), "exclusions": xs})

def cand(cid, f, ln, num, inc, outc=None, att=0):
    c = {"candidate_id": cid, "source_file": f, "source_line": ln, "numeral": num, "included": inc}
    if inc:
        c.update({"attempts": att, "outcome": outc})
    return c

SEED = "deadbeef" * 8  # 64 lowercase hex, chosen by me

# ---------- synthetic source (my own §1-unambiguous passage) ----------
SRC = W / "src"; SRC.mkdir(exist_ok=True)
(SRC / "k2paper.txt").write_text(
    "K2 synthetic paper (review2 fixture, written by seat kimi)\n"
    "As an input assumption we fix the coupling lambda = 5 for the whole study.\n"
    "Our integration of the full system gives the dimensionless drift D = 0.625.\n"
    "A second independent check yields E = 42.0 for the same system.\n"
    "As figure 12 summarises, both are stable.\n")
# line 3 (D = 0.625) is unambiguously the paper's own result: §1 requires it.

REQ = ("k2paper.txt", 3, "0.625")
def stage(tag, ac, ax, sc, rd):
    s1 = W / f"{tag}_stage1.txt"; sel = W / f"{tag}_sel.json"; s2 = W / f"{tag}_stage2.txt"; ho = W / f"{tag}_handout.json"
    r1 = run("audit", "seal-enumeration", ac, ax, s1)
    r2 = run("audit", "select", sc, SEED, s1, sel)
    run("audit", "handout", sel, sc, ho)
    r3 = run("audit", "seal-rederivation", rd, s2)
    return s1, sel, s2, ho, r1, r2, r3

print("=" * 70); print("CASE 1 (forward): BOTH seats omit k2paper.txt:3 '0.625'; auditor includes it")
seat_cands = [cand("c1", "k2paper.txt", 4, "42.0", True, "REPRO_NO_DERIVATION_STATED"),
              cand("c2", "k2paper.txt", 2, "5", False)]
assert not any((c["source_file"], c["source_line"], c["numeral"]) == REQ for c in seat_cands)  # BOTH seats omit it
sc = cfile("f_sealed_c.json", seat_cands)
sx = xfile("f_sealed_x.json", [{"candidate_id": "c2", "kind": "AUTHOR_SPECIFIED_INPUT", "source_file": "k2paper.txt", "source_line": 2, "numeral": "5"}])
sl = w("f_sealed_l.json", {"records": []})
aud_cands = [cand("a1", "k2paper.txt", 4, "42.0", True, "REPRO_NO_DERIVATION_STATED"),
             cand("a2", *REQ, True, "REPRO_NO_DERIVATION_STATED"),
             cand("a3", "k2paper.txt", 2, "5", False)]
ac = cfile("f_aud_c.json", aud_cands)
ax = xfile("f_aud_x.json", [{"candidate_id": "a3", "kind": "AUTHOR_SPECIFIED_INPUT", "source_file": "k2paper.txt", "source_line": 2, "numeral": "5"}])
sel_obj = json.loads((W / "f_sel.json").read_text()) if (W / "f_sel.json").exists() else None
rd = w("f_rd.json", {"c1": {"outcome": "REPRO_NO_DERIVATION_STATED", "inputs": {}}})
s1, sel, s2, ho, r1, r2, r3 = stage("f", ac, ax, sc, rd)
print("--- seal-enumeration rc:", r1[0]); print(r1[1].strip().splitlines()[-1] if r1[1].strip() else "")
print("--- select rc:", r2[0], r2[1].strip())
print("--- handout:", (W / "f_handout.json").read_text().replace("\n", " "))
rc, out = run("audit", "compare", s1, ac, ax, sc, sx, sl, sel, s2, rd, W / "f_C6_AUDIT.json")
print("--- compare rc:", rc)
comp = [l for l in out.splitlines() if "COMPLETENESS" in l]
print("emitted completeness result:", comp)
tok = [l for l in out.splitlines() if l.startswith("C6_AUDIT_SAMPLE=")]
print("final token:", tok)
rows = json.loads((W / "f_C6_AUDIT.json").read_text())["completeness_rows"]
print("row for the omitted key:", json.dumps([r for r in rows if r["key"] == list(REQ)], sort_keys=True))

print("=" * 70); print("CASE 2 (reverse): sealed includes k2paper.txt:3 '0.625'; auditor omits it")
sc2 = cfile("r_sealed_c.json", [cand("c1", "k2paper.txt", 4, "42.0", True, "REPRO_NO_DERIVATION_STATED"),
                                cand("c2", *REQ, True, "REPRO_NO_DERIVATION_STATED"),
                                cand("c3", "k2paper.txt", 2, "5", False)])
sx2 = xfile("r_sealed_x.json", [{"candidate_id": "c3", "kind": "AUTHOR_SPECIFIED_INPUT", "source_file": "k2paper.txt", "source_line": 2, "numeral": "5"}])
ac2 = cfile("r_aud_c.json", [cand("a1", "k2paper.txt", 4, "42.0", True, "REPRO_NO_DERIVATION_STATED"),
                             cand("a2", "k2paper.txt", 2, "5", False)])
ax2 = xfile("r_aud_x.json", [{"candidate_id": "a2", "kind": "AUTHOR_SPECIFIED_INPUT", "source_file": "k2paper.txt", "source_line": 2, "numeral": "5"}])
rd2 = w("r_rd.json", {"c1": {"outcome": "REPRO_NO_DERIVATION_STATED", "inputs": {}},
                      "c2": {"outcome": "REPRO_NO_DERIVATION_STATED", "inputs": {}}})
s1b, selb, s2b, hob, r1b, r2b, r3b = stage("r", ac2, ax2, sc2, rd2)
rc, out = run("audit", "compare", s1b, ac2, ax2, sc2, sx2, sl, selb, s2b, rd2, W / "r_C6_AUDIT.json")
print("--- compare rc:", rc)
print("emitted completeness result:", [l for l in out.splitlines() if "COMPLETENESS" in l])
print("final token:", [l for l in out.splitlines() if l.startswith("C6_AUDIT_SAMPLE=")])
rows = json.loads((W / "r_C6_AUDIT.json").read_text())["completeness_rows"]
print("row for the omitted key:", json.dumps([r for r in rows if r["key"] == list(REQ)], sort_keys=True))

print("=" * 70); print("CASE 3 (baseline all-match, then the seedless-selection attack)")
bc = cfile("b_sealed_c.json", [cand("c1", "k2paper.txt", 4, "42.0", True, "REPRO_NO_DERIVATION_STATED"),
                               cand("c2", "k2paper.txt", 2, "5", False)])
bx = xfile("b_sealed_x.json", [{"candidate_id": "c2", "kind": "AUTHOR_SPECIFIED_INPUT", "source_file": "k2paper.txt", "source_line": 2, "numeral": "5"}])
bac = cfile("b_aud_c.json", [cand("a1", "k2paper.txt", 4, "42.0", True, "REPRO_NO_DERIVATION_STATED"),
                             cand("a2", "k2paper.txt", 2, "5", False)])
bax = xfile("b_aud_x.json", [{"candidate_id": "a2", "kind": "AUTHOR_SPECIFIED_INPUT", "source_file": "k2paper.txt", "source_line": 2, "numeral": "5"}])
brd = w("b_rd.json", {"c1": {"outcome": "REPRO_NO_DERIVATION_STATED", "inputs": {}}})
s1c, selc, s2c, hoc, r1c, r2c, r3c = stage("b", bac, bax, bc, brd)
rc, out = run("audit", "compare", s1c, bac, bax, bc, bx, sl, selc, s2c, brd, W / "b_C6_AUDIT.json")
print("baseline compare rc:", rc, [l for l in out.splitlines() if l.startswith("C6_AUDIT_SAMPLE=")])
# attack: same selection minus seed_hex, audited/sampled emptied, digests retained
selx = json.loads((W / "b_sel.json").read_text())
del selx["seed_hex"]; selx["audited_ids"] = []; selx["sampled_ids"] = []; selx["k"] = 0
selx_p = w("b_sel_seedless.json", selx)
brd_empty = w("b_rd_empty.json", {})
rc, out = run("audit", "compare", s1c, bac, bax, bc, bx, sl, selx_p, s2c, brd_empty, W / "b_C6_seedless.json")
print("SEEDLESS-SELECTION ATTACK rc:", rc, [l for l in out.splitlines() if l.startswith("C6_AUDIT_SAMPLE=")])
aud = json.loads((W / "b_C6_seedless.json").read_text())
print("seedless artefact: audited =", aud["audited"], " C6_AUDIT_SAMPLE =", aud["C6_AUDIT_SAMPLE"])

print("=" * 70); print("CASE 4 (D1): the two wordings over constructed source verbs")
D = W / "d1src"; D.mkdir(exist_ok=True)
(D / "k2borrow.txt").write_text(
    "K2 synthetic borrower (review2 fixture)\n"
    "We compute the growth factor from the coupling adopted in the literature.\n"
    "We take g from k2s_choose (2021) for the evaluation below.\n"
    "Our result is F = 2g = 18.\n")
(D / "k2s_choose.txt").write_text("K2 source\nNotes.\nFor this calculation we choose g = 9.\n")
(D / "k2s_fit.txt").write_text("K2 source\nNotes.\nWe fit g = 9 to the sample.\n")
(D / "k2s_measure.txt").write_text("K2 source\nNotes.\nWe measure g = 9 in the apparatus.\n")
(D / "k2s_adopt.txt").write_text("K2 source\nNotes.\nWe adopt g = 9 from Kepler (1619).\n")
(D / "k2s_two.txt").write_text("K2 source\nSetup g = 9 as chosen.\nNotes.\nLater we reuse g = 9 here.\n")
manifest(D / "R3C2_CORPUS_MANIFEST.md", D, ["k2borrow.txt", "k2s_choose.txt", "k2s_fit.txt", "k2s_measure.txt", "k2s_adopt.txt", "k2s_two.txt"])
DC = w("d1_cands.json", {"declared_candidate_count": 1, "declared_included_count": 1, "declared_excluded_count": 0, "declared_attempt_count": 1,
                          "candidates": [{"candidate_id": "k2borrow.txt#1", "source_file": "k2borrow.txt", "source_line": 4, "numeral": "18", "included": True, "attempts": 1, "outcome": "REPRO_WITHIN_STATED_PRECISION", "printed_value": "18", "reproduced_value": "18"}]})
def d1rec(src, sline, **kw):
    r = {"claim_id": "k2borrow.txt#1", "input_id": "k2borrow.txt#1.g", "symbol": "g", "status": "PRINTED", "origin": "IMPORTED",
         "origin_evidence": {"reason_code": "ORIG_CITATION", "source_file": "k2borrow.txt", "source_line": 3,
                             "verbatim": "We take g from k2s_choose (2021) for the evaluation below."},
         "derived_from": [], "value": "9", "source_file": src, "source_line": sline}
    for k, v in kw.items():
        if k.startswith("ev_"): r["origin_evidence"][k[3:]] = v
        else: r[k] = v
    return r
for name, src, ln in [("D1a 'we choose'", "k2s_choose.txt", 3), ("D1b 'we fit'", "k2s_fit.txt", 3),
                      ("D1c 'we measure'", "k2s_measure.txt", 3), ("D1d 'we adopt from X'", "k2s_adopt.txt", 3),
                      ("D1e1 two-line source, FIRST line filed", "k2s_two.txt", 2)]:
    rc, out = run("validate", w(f"{name.split()[0]}.json", {"records": [d1rec(src, ln)]}), D, DC)
    print(f"{name}: rc={rc} token={[l for l in out.splitlines() if l.startswith('C3')]} fails={[l for l in out.splitlines() if l.startswith('FAIL:')]}")
rc, out = run("validate", w("d1e2.json", {"records": [d1rec("k2s_two.txt", 4)]}), D, DC)
print(f"D1e2 two-line source, SECOND line filed: rc={rc} fails={[l for l in out.splitlines() if l.startswith('FAIL:')]}")
# D1f: Wording-A-style record (evidence at the SOURCE's own line) under the staged (B-only) tool
rc, out = run("validate", w("d1f.json", {"records": [d1rec("k2s_choose.txt", 3, ev_source_file="k2s_choose.txt", ev_source_line=3, ev_verbatim="we choose g = 9")]}), D, DC)
print(f"D1f Wording-A-style record under the staged tool: rc={rc} fails={[l for l in out.splitlines() if l.startswith('FAIL:')]}")
# D1g: CHOSEN-misfiling of the import (reason-code substitution), quoting the source's 'we choose' line
mis = {"claim_id": "k2borrow.txt#1", "input_id": "k2borrow.txt#1.g", "symbol": "g", "status": "PRINTED", "origin": "CHOSEN",
       "origin_evidence": {"reason_code": "ORIG_CHOICE_STATED", "source_file": "k2s_choose.txt", "source_line": 3, "verbatim": "we choose g = 9"},
       "derived_from": [], "value": "9", "source_file": "k2s_choose.txt", "source_line": 3}
rc, out = run("validate", w("d1g.json", {"records": [mis]}), D, DC)
print(f"D1g import misfiled CHOSEN (quotes the source's own 'we choose' line): rc={rc} token={[l for l in out.splitlines() if l.startswith('C3')]}")

(W / "command_log.json").write_text(json.dumps(LOG, indent=1))
print("=" * 70); print("log written:", W / "command_log.json")
