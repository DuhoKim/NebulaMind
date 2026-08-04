#!/usr/bin/env python3
# H9 mechanical verifier — read-only on all inputs; writes nothing (stdout only).
import json, re, sys

PRIOR = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z"
CAND = PRIOR + "/p4-derived-claims/CLAIM_EVIDENCE_CANDIDATES.md"
FLG = PRIOR + "/p4-derived-claims/sources-snapshot/rp1_flagship_polished.tex"
SUP = PRIOR + "/p4-derived-claims/sources-snapshot/supplementary_denominator_atlas.tex"
MAN = PRIOR + "/p1-rp1-invariants/INVARIANT_MANIFEST.json"

cand = open(CAND, encoding="utf-8").read()
flg_lines = open(FLG, encoding="utf-8").read().split("\n")
sup_lines = open(SUP, encoding="utf-8").read().split("\n")
man = json.load(open(MAN, encoding="utf-8"))

fails = []
def report(tag, ok, detail=""):
    print(("PASS" if ok else "FAIL"), tag, detail)
    if not ok:
        fails.append((tag, detail))

# ---------- split candidates ----------
blocks = re.split(r"\n## (P4-C\d\d) ", cand)
cands = {}
for i in range(1, len(blocks), 2):
    cands[blocks[i]] = blocks[i + 1]
report("census.ids", sorted(cands) == ["P4-C%02d" % i for i in range(1, 14)], str(sorted(cands)))

# ---------- 1. evidence quote extraction + byte-exact check ----------
ev_re = re.compile(r"^\d+\.\s+`([^`]+)`, snapshot line (\d+)[^:]*: (.*)$")
total_q = 0
for cid in sorted(cands):
    body = cands[cid]
    m = re.search(r"\*\*evidence:\*\*\n(.*?)\n\n\*\*numerals_check", body, re.S)
    if not m:
        report(f"{cid}.evidence-block", False, "no evidence block"); continue
    for line in m.group(1).split("\n"):
        line = line.strip()
        if not line or not line[0].isdigit():
            continue
        em = ev_re.match(line)
        if not em:
            report(f"{cid}.evidence-parse", False, line[:80]); continue
        path, lineno, payload = em.group(1), int(em.group(2)), em.group(3)
        src = flg_lines if "flagship" in path else sup_lines
        srcname = "FLG" if "flagship" in path else "SUP"
        payload = payload.split(" — manifest:")[0].split(" — (no numerals")[0].strip()
        quotes = re.findall(r'"([^"]+)"', payload)
        if not quotes and payload.startswith("`"):
            quotes = re.findall(r"`([^`]+)`", payload)
        if not quotes:
            report(f"{cid}.quote-extract@{srcname}:{lineno}", False, payload[:60]); continue
        for q in quotes:
            total_q += 1
            ok = lineno <= len(src) and q in src[lineno - 1]
            where = ""
            if not ok:
                hits = [j + 1 for j, l in enumerate(src) if q in l]
                where = f"actual-lines={hits}"
            report(f"{cid}.quote@{srcname}:{lineno}", ok, where or f"len={len(q)}")
print(f"INFO total quoted spans checked: {total_q}")

# ---------- 2. claim_text digit-run support on cited lines ----------
for cid in sorted(cands):
    body = cands[cid]
    ct = re.search(r"\*\*claim_text:\*\* (.*?)\n\n\*\*evidence", body, re.S).group(1)
    cited = []
    for em in re.finditer(r"`([^`]+)`, snapshot line (\d+)", body):
        src = flg_lines if "flagship" in em.group(1) else sup_lines
        cited.append(src[int(em.group(2)) - 1])
    hay = "\n".join(cited)
    runs = set(re.findall(r"\d[\d,.−]*\d|\d", ct))
    missing = []
    for r in runs:
        r2 = r.rstrip(".,")
        if r2 in hay or r2.replace(",", "") in hay.replace(",", ""):
            continue
        missing.append(r2)
    report(f"{cid}.claim-digit-support", not missing, "unsupported-on-cited-lines=" + ",".join(missing) if missing else f"{len(runs)} runs ok")

# ---------- 3. manifest cross-check ----------
entries = None
for k, v in man.items():
    if isinstance(v, list) and v and isinstance(v[0], dict) and any("id" in e for e in v[:3]):
        entries = v; ekey = k; break
if entries is None:
    for k, v in man.items():
        if isinstance(v, dict) and len(v) > 20:
            entries = [dict(id=i, **(e if isinstance(e, dict) else {"value": e})) for i, e in v.items()]; ekey = k; break
print(f"INFO manifest entry container: {ekey}, count={len(entries)}")
report("manifest.count-105", len(entries) == 105, f"count={len(entries)}")
by_id = {e.get("id"): e for e in entries}
used_ids = sorted(set(re.findall(r"\b(?:FLG|SUP)-[A-Z0-9/-]+\b", cand)) - {"FLG-", "SUP-"})
used_ids = [u for u in used_ids if not u.startswith("SUP-ROW-") or u in by_id]
print(f"INFO manifest ids referenced in candidates: {len(used_ids)}")
flg_txt = "\n".join(flg_lines); sup_txt = "\n".join(sup_lines)
unknown = [u for u in used_ids if u not in by_id]
report("manifest.all-referenced-ids-exist", not unknown, "unknown=" + ",".join(unknown) if unknown else "")
def count_occ(txt, s):
    n = c = 0
    while True:
        j = txt.find(s, c)
        if j < 0: return n
        n += 1; c = j + 1
for u in used_ids:
    e = by_id.get(u)
    if not e: continue
    s = e.get("string") or e.get("canonical_string") or e.get("value") or e.get("text")
    exp = e.get("occurrences_expected") or e.get("expected_occurrences") or e.get("count")
    scope = e.get("file") or e.get("scope") or ("flagship" if u.startswith("FLG") else "supplement")
    if s is None:
        print("INFO", u, "no-string-field", sorted(e.keys())); continue
    txt = flg_txt if "flag" in str(scope) else sup_txt
    got = count_occ(txt, s)
    if exp is None:
        report(f"manifest.{u}.present", got >= 1, f"string={s!r} got={got}")
    else:
        report(f"manifest.{u}.occurrences", got == exp, f"string={s!r} exp={exp} got={got}")

# ---------- 4. receipt-claimed counts + corruption signatures ----------
for s, exp in [("[-1.334,-1.283]", 4), ("-1.309", 6), ("8,146", 9), ("60,000", 11),
               ("249,917", 1), ("24.0\\%", 1), ("39,553", 1), ("12,234", 1),
               ("0.0045", 1), ("0.00021", 1), ("1.2--6.5", 2), ("0.02<z<0.12", 2)]:
    got = count_occ(flg_txt, s)
    report(f"receipt-count.FLG.{s}", got == exp, f"exp={exp} got={got}")
for s in ["0.001-0.856", "0.001-0.610", "2.831"]:
    report(f"corruption.absent.{s}", count_occ(flg_txt, s) + count_occ(sup_txt, s) + count_occ(cand, s) == 0)
report("corruption.absent.re-rounded-CI", not re.search(r"-1\.28(?![0-9])[^\d]?", flg_txt + sup_txt + cand) or not re.search(r"1\.28(?!3)", flg_txt + sup_txt + cand), "")
report("anomaly.line188-2.830-present", "2.830" in sup_lines[187], sup_lines[187][:80])
kra = json.dumps(man.get("known_rounding_anomalies", ""))
report("manifest.anomaly-mentions-1.283", "-1.283" in kra, kra[:200])
print("INFO known_rounding_anomalies:", kra[:600])

# ---------- 5. arithmetic / contradiction sweep ----------
report("sum.denominator", 39553 + 12234 + 8146 + 67 == 60000)
report("ratio.hiexc", abs(4440 / 60000 - 0.074) < 5e-4, f"{4440/60000:.5f}")
report("ratio.env-hi", abs(3456 / 15000 - 0.230) < 5e-4, f"{3456/15000:.5f}")
report("ratio.env-lo", abs(2710 / 15000 - 0.181) < 5e-4, f"{2710/15000:.5f}")
report("ci.env-diff-in-interval", 0.041 <= 0.230 - 0.181 <= 0.059, f"{0.230-0.181:.3f}")
report("ci.jet-diff-in-interval", 0.112 <= 0.509 - 0.367 <= 0.170, f"{0.509-0.367:.3f}")
report("coef.3.2pp", abs(0.032 * 100 - 3.2) < 1e-9)
report("ratio.tracer", abs(0.418 / 0.136 - 3.1) < 0.05, f"{0.418/0.136:.4f}")
report("ratio.parent-coverage", abs(60000 / 249917 - 0.240) < 5e-4, f"{60000/249917:.5f}")
report("prevalence.bpt-vs-tracer-lo", abs(8146 / 60000 - 0.136) < 5e-4, f"{8146/60000:.5f}")
report("order.c07-subset", 0.607 * 5695 <= 0.430 * 9298, f"{0.607*5695:.0f}<={0.430*9298:.0f}")
report("order.c09-brackets-c07", 0.367 <= 0.430 <= 0.509)
rows = []
for l in sup_lines[175:190]:
    p = [x.strip() for x in l.replace("\\\\", "").split("&")]
    rows.append((p[0], p[1], int(p[2].replace(",", "")), float(p[3]), float(p[4]), float(p[5])))
report("table4.rows-15", len(rows) == 15, str(len(rows)))
report("table4.N-sum-60000", sum(r[2] for r in rows) == 60000, str(sum(r[2] for r in rows)))
mb = {}
for b, z, n, lo, bpt, ur in rows:
    a = mb.setdefault(b, [0, 0.0, 0.0]); a[0] += n; a[1] += n * lo; a[2] += n * bpt
lospans = sorted(a[1] / a[0] for a in mb.values()); bpspans = sorted(a[2] / a[0] for a in mb.values())
report("table4.massbin-lo-span", abs(lospans[0] - 0.005) < 2e-3 and abs(lospans[-1] - 0.729) < 2e-3, f"[{lospans[0]:.4f},{lospans[-1]:.4f}] vs 0.005-0.729")
report("table4.massbin-bpt-span", abs(bpspans[0] - 0.003) < 2e-3 and abs(bpspans[-1] - 0.520) < 2e-3, f"[{bpspans[0]:.4f},{bpspans[-1]:.4f}] vs 0.003-0.520")
mb_lo = {b: a[1] / a[0] for b, a in mb.items()}
first_above = [b for b in ["8.0--9.5", "9.5--10.0", "10.0--10.5", "10.5--11.0", "11.0--12.5"] if mb_lo.get(b, 0) > 0.5]
report("table4.first-bin-above-0.5", first_above and first_above[0] == "11.0--12.5", str({k: round(v, 3) for k, v in mb_lo.items()}))
mb_bpt = {b: a[2] / a[0] for b, a in mb.items()}
report("table4.bpt-peak-0.520-in-11.0-12.5", max(mb_bpt, key=mb_bpt.get) == "11.0--12.5" and abs(max(mb_bpt.values()) - 0.520) < 2e-3, str({k: round(v, 3) for k, v in mb_bpt.items()}))

# ---------- 6. wiki-shape / schema field checks ----------
LEGAL_SECTIONS = {"Overview", "Discovery & History", "Physical Properties", "Current Research", "Open Questions", "See Also", "References"}
COVERED = {"active-galactic-nuclei","asteroid-belt","binary-stars","black-hole-mergers","cosmic-inflation","cosmic-microwave-background","dark-energy","dark-matter","exoplanet-detection-methods","exoplanets","fast-radio-bursts","galaxy-clusters","galaxy-formation","gamma-ray-bursts","gravitational-waves","habitable-zone","hawking-radiation","hubble-constant","kuiper-belt","magnetars","milky-way","nebulae","neutron-stars","oort-cloud","planetary-nebulae","pulsars","quasars","spacetime","stellar-evolution","supernovae","tidal-forces","white-dwarfs","wormholes"}
for cid in sorted(cands):
    body = cands[cid]
    ws = re.search(r"```\n(candidate_id:.*?)```", body, re.S).group(1)
    fields = dict(re.findall(r"^\s*([a-z_]+): (.*)$", ws, re.M))
    need = ["page_id", "claim_id", "evidence_ids", "page_version_fk", "publish_state", "category", "proposed_page_slug", "proposed_section", "see_also", "references"]
    missing = [f for f in need if f not in fields]
    report(f"{cid}.wiki-shape-fields", not missing, "missing=" + ",".join(missing) if missing else "all 10 present")
    report(f"{cid}.category-galaxy", fields.get("category") == "galaxy", fields.get("category", ""))
    for f in ["page_id", "claim_id", "evidence_ids", "page_version_fk", "publish_state"]:
        if fields.get(f) != "OFFLINE_PLACEHOLDER":
            report(f"{cid}.placeholder.{f}", False, fields.get(f, ""))
    sec = fields.get("proposed_section", "")
    report(f"{cid}.section-legal", sec in LEGAL_SECTIONS, sec)
    slug = fields.get("proposed_page_slug", "")
    report(f"{cid}.slug-format", bool(re.fullmatch(r"/wiki/[a-z0-9-]+", slug)), slug)
    sa = re.findall(r"/wiki/([a-z0-9-]+)", fields.get("see_also", ""))
    report(f"{cid}.see-also-3", len(sa) >= 3, str(sa))
    allslugs = sa + [slug.split("/")[-1]]
    not_cov = [s for s in allslugs if s not in COVERED]
    if not_cov:
        print(f"NOTE {cid} slugs not on schema coverage-map covered list: {not_cov}")
    refs = fields.get("references", "")
    report(f"{cid}.references-s1s2", refs in ("[S1]", "[S2]"), refs)
    vf = re.search(r"\*\*verification:\*\* (\S+)", body)
    report(f"{cid}.verification-LOCAL_ONLY", vf and vf.group(1) == "LOCAL_ONLY", vf.group(1) if vf else "absent")

print("\n==== SUMMARY ====")
print("FAILS:", len(fails))
for t, d in fails:
    print("  FAIL", t, d)
