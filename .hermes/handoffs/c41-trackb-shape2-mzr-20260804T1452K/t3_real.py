#!/usr/bin/env python3
"""t3_real.py — Shape-2 T3, REAL execution. Reviewed-script protocol:
authored by Hwao, code-reviewed by Kun BEFORE execution; no agent types a number.

Contract bindings (read as inputs, quoted in outputs):
  - T2B_CONTRACT_SEMANTICS.md + T2B_AMENDMENT_RULING.md  (Class A' accepted; seam rules)
  - APRIME components implemented HERE for review (PyNeb direct method; S/N(4363) >= 5 per
    Amendment Ruling A'-1 "as tabulated" — rows without tabulated e4363 are Class X, excluded;
    CCM89 dust via PyNeb RedCorr; ICF-fallback rows EXCLUDED from bin statistics per Kun R1),
    superseding the retired seat's mock. Kun review edits B1-B3, R1-R4 applied (KUN_SCRIPT_REVIEW.md).
  - Anchor frame (declared): Andrews & Martini (2013) Te-anchored local MZR as the z<3
    baseline scale. Single declared scale; no strong-line values enter.
  - Forecast v2 thresholds are read and REPORTED as inputs (Goru-authored; flagged for review).

Stage plan (each stage writes its receipt before the next runs):
  S1 enumerate: TAP_SCHEMA over the JADES (V/159) + CEERS-candidate series from the T1
     manifest; select tables carrying [OIII]4363-class flux columns + z; report the truth.
  S2 fetch: line-flux rows (polite, cached via nm_external_data); join masses where a
     declared join exists; every exclusion carries a per-row reason.
  S3 derive: PyNeb Te/O/H per the A' spec; per-row provenance incl. every flux and flag.
  S4 compute: per-bin offsets vs the declared anchor frame; bootstrap uncertainties;
     T2b decision rule applied verbatim; A4 FMR only if SFR-capable fluxes exist (else
     reported not-computable with the reason).
  S5 confront: numeric predictions from C41_PREDICTION_ENTRIES.jsonl; per-entry distance in
     OUR anchor frame or an explicit frame-mismatch verdict; nothing defaults to consistent.
Outputs: T3_REAL_SAMPLE.jsonl, T3_REAL_RESULTS.json, T3_REAL_LOG.txt, T3_REAL_FIGURE.png.
"""
import json, math, os, random, re, sys, time

LANE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(LANE, "..", "..", "..", "tools"))
sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/tools")
import nm_external_data as ext

LOG = open(os.path.join(LANE, "T3_REAL_LOG.txt"), "a")
def log(m):
    line = f"[{time.strftime('%Y-%m-%dT%H:%M:%S%z')}] {m}"
    print(line, flush=True); LOG.write(line + "\n"); LOG.flush()

TAP = "https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync"
SERIES = ["V/159"]  # JADES DR (T1-verified live); CEERS-class series appended from manifest
# Anchor frame (B3): PUBLISHED Andrews & Martini 2013 asymptotic form (their eq. 5),
# 12+log(O/H) = 8.798 - log10(1 + (M_TO/M)^0.640), log(M_TO)=8.901 — citable, parametrized.
# REPORTABLE DISCREPANCY (per Kun B3, not averaged away): the crew's z9-10 receipted arithmetic
# implies AM13(logM=8) ~ 8.26; this published form gives 8.12 (~0.14 dex). Recorded in results
# as anchor_frame_discrepancy_note for T4 adjudication.
AM13_ASYM, AM13_LOGMTO, AM13_GAMMA = 8.798, 8.901, 0.640
BINS = [(8.0, 9.0, "M_star_bin_8_9"), (9.0, 10.0, "M_star_bin_9_10"), (10.0, 12.0, "M_star_bin_gt_10")]
SN_FLOOR = 5.0  # B1: Amendment Ruling A'-1, uniform pre-fetch floor; 3.0 was a contract violation
TE_CLASS_FLOOR = 0.15  # R3: pure-A/A' sample scale floor per T2A_CONVERSION_TABLES §2 (Te-anchor class)
RNG = random.Random(20260804)

def anchor_oh(logm):
    return AM13_ASYM - math.log10(1.0 + (10 ** (AM13_LOGMTO - logm)) ** AM13_GAMMA)

def unq(s):
    # v4: nm_external_data's CSV parse retains BOTH quote layers on string fields
    # ("'III/203/table'"); verified live 2026-08-04. Strip uniformly everywhere.
    return str(s or "").strip().strip('"').strip("'").strip()

def tap(query):
    return ext.vizier_tap(query)  # cached + polite + resilient per module

def s1_enumerate(manifest_path):
    # v2 (post-HONEST_FAILURE): GLOBAL column-search enumeration — the first run proved the
    # T1-series scoping too narrow while VizieR globally carries many 4363-column tables.
    # The z>3 filter in S2 self-scopes the sample by DATA, not assumption. (Kun micro-delta.)
    # v4: ONE self-join query (equality on quoted names is unreliable — TAP_SCHEMA values
    # embed literal quotes); group in python with uniform unq().
    pairs = tap("SELECT c2.table_name, c2.column_name FROM TAP_SCHEMA.columns c1 "
                "JOIN TAP_SCHEMA.columns c2 ON c1.table_name = c2.table_name "
                "WHERE c1.column_name LIKE '%4363%'")
    bytab = {}
    for r in pairs:
        bytab.setdefault(unq(r.get("table_name")), []).append(unq(r.get("column_name")))
    log(f"S1-global v4: {len(bytab)} 4363-tables with full column inventories (one query)")
    found = []
    for tname, cols in sorted(bytab.items()):
        cl = [c.lower() for c in cols]
        if not any("5007" in c for c in cl):
            continue
        hasz_in = any(re.fullmatch(r"z(spec|_spec|sp)?|redshift", c) for c in cl)
        sib = None
        if not hasz_in:
            m = re.match(r"^(.+)/[^/]+$", tname)
            if m:
                sibs = tap("SELECT DISTINCT table_name, column_name FROM TAP_SCHEMA.columns "
                           f"WHERE table_name LIKE '%{m.group(1)}/%' AND "
                           "(column_name LIKE '%zsp%' OR column_name LIKE '%z_spec%' OR "
                           "column_name LIKE '%Redshift%' OR column_name LIKE '%redshift%' OR "
                           "column_name = '''z''' OR column_name = 'z')")
                for s in sibs:
                    st = unq(s.get("table_name"))
                    if st and st != tname:
                        sib = {"table": st, "zcol": unq(s.get("column_name"))}
                        break
        if hasz_in or sib:
            found.append({"table": tname, "cols": cols, "has_z": hasz_in, "z_sibling": sib})
            log(f"S1 candidate: {tname} (z: {'in-table' if hasz_in else 'sibling ' + sib['table']})")
    json.dump(found, open(os.path.join(LANE, "_s1_line_tables.json"), "w"), indent=1)
    log(f"S1 done: {len(found)} candidates (in-table or sibling z)")
    return found

def pick_col(cols, *pats):
    for p in pats:
        for c in cols:
            if re.search(p, c, re.I): return c
    return None

def pick_flux(cols, wave):
    # v6: flux columns must NEVER be error/limit/EW columns. Run-5 forensics: schema order put
    # e_F4363 before F4363, so bare-substring picks returned the ERROR column for flux AND error
    # (f==e identically on 723 rows; '5007'<'4363' impossibility). Explicit preference order:
    for p in (rf"^F{wave}$", rf"^Flux{wave}$", rf"^{wave}$", rf"^F_{wave}$"):
        for c in cols:
            if re.fullmatch(p, c, re.I): return c
    for c in cols:  # last resort: contains wave but not error/limit/EW markers
        if str(wave) in c and not re.match(r"^(e_|u_|l_|n_|q_|EW|sigma)", c, re.I):
            return c
    return None

def pick_err(cols, wave):
    for c in cols:
        if re.match(rf"^e_.*{wave}", c, re.I) or re.search(rf"{wave}.*err", c, re.I):
            return c
    return None

def s2_fetch(line_tables):
    sample = []
    for t in line_tables:
        cols = t["cols"]
        c4363 = pick_flux(cols, 4363)
        c5007 = pick_flux(cols, 5007)
        c4959 = pick_flux(cols, 4959)
        chb = pick_flux(cols, 4861) or pick_col(cols, r"^Hb$|^F?Hbeta$")
        chg = pick_flux(cols, 4340) or pick_col(cols, r"^Hg$|^F?Hgamma$")
        c3727 = pick_flux(cols, 3727) or pick_flux(cols, 3729)
        cz = pick_col(cols, r"^z(spec|_spec)?$|^redshift$") or pick_col(cols, r"^z")
        cid = pick_col(cols, r"^id$|^name$|^source|^recno$")
        cmass = pick_col(cols, r"mass|logm|lgm")
        e4363 = pick_err(cols, 4363)
        sib = t.get("z_sibling")
        if not (c4363 and c5007) or (not cz and not sib):
            log(f"S2 skip {t['table']}: missing essential columns"); continue
        want = [x for x in [cid, cz, c4363, e4363, c5007, c4959, chb, chg, c3727, cmass] if x]
        q = f"SELECT {', '.join(sorted(set(want)))} FROM \"{t['table']}\" WHERE {c4363} IS NOT NULL"
        try:
            rows = tap(q)
        except Exception as e:
            # v5: one bad table must not kill the run — log, skip, continue (fail-closed per-table).
            log(f"S2 SKIP {t['table']}: fetch failed ({str(e)[:90]})"); continue
        log(f"S2 {t['table']}: {len(rows)} rows with 4363 measured")
        zmap = {}
        if not cz and sib and cid:
            # sibling join on the shared id/recno column (v3): fetch sibling z table once.
            try:
                srows = tap(f"SELECT * FROM \"{sib['table']}\"")
            except Exception as e:
                log(f"S2 SKIP sibling {sib['table']}: fetch failed ({str(e)[:90]})"); continue
            skey = None
            if srows:
                scols = list(srows[0].keys())
                skey = next((c for c in scols if c.lower() == cid.lower()), None) or \
                       next((c for c in scols if c.lower() in ("recno", "id", "name", "seq")), None)
            if skey:
                for s in srows:
                    zmap[unq(s.get(skey, ""))] = _f(s.get(sib["zcol"]))
                log(f"S2 sibling-join {sib['table']} via {skey}: {len(zmap)} z rows")
            else:
                log(f"S2 {t['table']}: sibling {sib['table']} has no shared key — rows skipped"); continue
        # v7: sibling-MASS join (run-6: 5 derived rows all lacked in-table masses — JADES keeps
        # masses in photometry siblings). Same pattern as sibling-z: same catalog prefix,
        # mass-column table, shared id key; logged; missing mass remains per-row honest.
        massmap = {}
        if not cmass and cid:
            mm = re.match(r"^(.+)/[^/]+$", t["table"])
            if mm:
                try:
                    mtabs = tap("SELECT DISTINCT table_name, column_name FROM TAP_SCHEMA.columns "
                                f"WHERE table_name LIKE '%{mm.group(1)}/%' AND "
                                "(column_name LIKE '%logM%' OR column_name LIKE '%lgM%' OR "
                                "column_name LIKE '%Mass%' OR column_name LIKE '%mass%')")
                except Exception as e:
                    mtabs = []; log(f"S2 mass-sibling search failed for {t['table']}: {str(e)[:70]}")
                for s in mtabs:
                    st_, mcol = unq(s.get("table_name")), unq(s.get("column_name"))
                    if not st_ or st_ == t["table"]: continue
                    try:
                        mrows = tap(f"SELECT * FROM \"{st_}\"")
                    except Exception:
                        continue
                    if not mrows: continue
                    scols = list(mrows[0].keys())
                    mkey = next((c for c in scols if unq(c).lower() == cid.lower()), None) or \
                           next((c for c in scols if unq(c).lower() in ("recno", "id", "name", "seq")), None)
                    if not mkey: continue
                    for srow in mrows:
                        v = _f(srow.get(mcol))
                        if v is not None and 5.0 < v < 13.5:
                            massmap[unq(srow.get(mkey, ""))] = v
                    if massmap:
                        log(f"S2 mass-sibling {st_}.{mcol} via {unq(mkey)}: {len(massmap)} masses")
                        break
        for r in rows:
            if cz:
                try: z = float(r.get(cz, "nan"))
                except Exception: continue
            else:
                z = zmap.get(unq(r.get(cid, "")))
                if z is None: continue
            if not (z > 3.0):
                continue
            rec = {"table": t["table"], "id": r.get(cid, "?"), "z": z,
                   "f4363": _f(r.get(c4363)), "e4363": _f(r.get(e4363)) if e4363 else None,
                   "f5007": _f(r.get(c5007)), "f4959": _f(r.get(c4959)) if c4959 else None,
                   "fhb": _f(r.get(chb)) if chb else None, "fhg": _f(r.get(chg)) if chg else None,
                   "f3727": _f(r.get(c3727)) if c3727 else None,
                   "logmass": (_f(r.get(cmass)) if cmass else massmap.get(unq(r.get(cid, "")))),
                   "exclusion": None}
            sample.append(rec)
    log(f"S2 done: {len(sample)} z>3 rows with 4363 across tables")
    return sample

def _f(v):
    try:
        x = float(unq(v)); return x if math.isfinite(x) else None
    except Exception:
        return None

def s3_derive(sample):
    import pyneb as pn
    O3 = pn.Atom("O", 3); O2 = pn.Atom("O", 2)
    kept = 0
    for r in sample:
        if r["f4363"] is None or r["f5007"] is None:
            r["exclusion"] = "missing 4363/5007 flux"; continue
        sn = (r["f4363"] / r["e4363"]) if (r["e4363"] and r["e4363"] > 0) else None
        r["sn4363"] = sn
        if sn is None:
            # R4(b): Ruling A'-1 requires S/N "as tabulated"; no tabulated e4363 => Class X.
            r["exclusion"] = "Class X: no tabulated e4363 (cannot demonstrate S/N>=5)"; continue
        if sn < SN_FLOOR:
            r["exclusion"] = f"S/N(4363) {sn:.1f} < {SN_FLOOR} (Ruling A'-1 floor)"; continue
        f4959 = r["f4959"] if r["f4959"] else r["f5007"] / 2.98
        # B2: CCM89 dust correction via PyNeb RedCorr (R_V=3.1); Case B Hg/Hb intrinsic 0.468.
        cor = 1.0
        if r["fhb"] and r["fhg"] and r["fhb"] > 0 and r["fhg"] > 0:
            obs = r["fhg"] / r["fhb"]
            if 0 < obs < 0.468:
                import pyneb as _pn
                rc = _pn.RedCorr(law="CCM89", R_V=3.1)
                rc.setCorr(obs_over_theo=obs / 0.468, wave1=4340.47, wave2=4861.33)
                r["ebv"] = round(float(rc.E_BV), 3)
                # 4363-vs-5007 differential correction from the SAME law object:
                cor = float(rc.getCorr(4363.21) / rc.getCorr(5006.84))
                r["dustcorr_4363_over_5007"] = round(cor, 4)
            else:
                # B2: asymmetric silent-zero is a bias — flag it.
                r["flag_dustcorr_skipped"] = f"obs Hg/Hb {obs:.3f} >= 0.468 (no correction applied, flagged)"
        else:
            r["flag_no_dustcorr"] = True  # R4(a): Balmer pair unavailable; correction not applied, recorded
        ratio = (f4959 + r["f5007"]) / (r["f4363"] * cor)
        try:
            te = O3.getTemDen(int_ratio=ratio, den=100.0,
                              wave1=5007, wave2=4363, to_eval="(L(4959)+L(5007))/L(4363)")
        except Exception as e:
            r["exclusion"] = f"pyneb Te failed: {e}"; continue
        if not (5000 < (te or 0) < 30000):
            r["exclusion"] = f"Te out of range: {te}"; continue
        r["te"] = round(float(te), 1)
        opp = O3.getIonAbundance(int_ratio=r["f5007"] / (r["fhb"] or r["f5007"]),
                                 tem=te, den=100.0, wave=5007, Hbeta=1.0) if r["fhb"] else None
        if opp is None:
            r["exclusion"] = "no Hbeta -> abundance undefined under A' spec"; continue
        if r["f3727"]:
            te2 = 0.7 * te + 3000.0  # Izotov-class T(OII) relation (declared)
            op = O2.getIonAbundance(int_ratio=r["f3727"] / r["fhb"], tem=te2, den=100.0,
                                    wave=3727, Hbeta=1.0)
            icf_note = "O+ measured"
        else:
            # R1: fabricated-constant O+ may NOT flow into compared statistics.
            # Row completes for the record but is excluded from bin means (s4 filters the flag).
            op = opp * 0.1
            icf_note = "O+ absent: ICF-fallback row — EXCLUDED from offset statistics (Kun R1)"
            r["flag_icf_fallback"] = True
        oh = 12 + math.log10(opp + op)
        if not (6.0 < oh < 9.5):
            r["exclusion"] = f"O/H out of range: {oh:.2f}"; continue
        r["oh_direct"] = round(oh, 3); r["icf_note"] = icf_note; kept += 1
    log(f"S3 done: {kept} rows with A' direct O/H; exclusions carry reasons")
    return sample

def s4_compute(sample):
    res = {"bins": {}, "A4_FMR": {"status": "not-computable-v1",
           "reason": "no declared SFR channel in v1 fetch (Hbeta-SFR needs flux calibration review)"}}
    ok = [r for r in sample if r.get("oh_direct") and r.get("logmass")
          and not r.get("flag_icf_fallback")]  # R1: fallback rows out of statistics
    res["per_class_counts"] = {  # R4(c)
        "oh_rows_total": sum(1 for r in sample if r.get("oh_direct")),
        "icf_fallback_excluded": sum(1 for r in sample if r.get("oh_direct") and r.get("flag_icf_fallback")),
        "no_mass": sum(1 for r in sample if r.get("oh_direct") and not r.get("logmass")),
        "no_dustcorr_flagged": sum(1 for r in sample if r.get("flag_no_dustcorr")),
        "dustcorr_skipped_flagged": sum(1 for r in sample if r.get("flag_dustcorr_skipped")),
        "class_x_no_snr": sum(1 for r in sample if str(r.get("exclusion", "")).startswith("Class X")),
    }
    res["anchor_frame"] = {
        "form": "AM13 eq.5 asymptotic: 8.798 - log10(1+(10^(8.901-logM))^0.640)",
        "table": {f"{m/10:.1f}": round(anchor_oh(m / 10), 3) for m in range(80, 106, 5)},
        "anchor_frame_discrepancy_note": ("crew z9-10 receipted arithmetic implies AM13(8.0)~8.26; "
                                          "this published form gives 8.12 (~0.14 dex) — REPORTABLE, "
                                          "referred to T4; not averaged away (Kun B3)"),
    }
    for lo, hi, name in BINS:
        rows = [r for r in ok if lo <= r["logmass"] < hi]
        if len(rows) < 3:
            res["bins"][name] = {"N": len(rows), "verdict": "no-verdict-possible (too few anchors)"}
            continue
        offs = [r["oh_direct"] - anchor_oh(r["logmass"]) for r in rows]
        boots = []
        for _ in range(2000):
            b = [offs[RNG.randrange(len(offs))] for _ in offs]
            boots.append(sum(b) / len(b))
        boots.sort()
        med = sum(offs) / len(offs)
        lo16, hi84 = boots[int(0.16 * len(boots))], boots[int(0.84 * len(boots))]
        unc = (hi84 - lo16) / 2
        floor = TE_CLASS_FLOOR  # R3: pure-A' sample => Te-anchor class floor (0.15), named below
        verdict = "detection" if abs(med) > max(unc * 2, floor) else "scale-limited"
        res["bins"][name] = {"N": len(rows), "offset_dex": round(med, 3),
                             "unc_16_84_half": round(unc, 3), "verdict": verdict,
                             "scale_floor_class": "Te-anchor class 0.15 dex (T2A conversions §2; pure-A' bin)",
                             "rule": "T2b: |offset| must exceed max(2*unc, class scale floor)"}
    return res

def s5_confront(res):
    out = {}
    preds = [json.loads(l) for l in open(os.path.join(LANE, "C41_PREDICTION_ENTRIES.jsonl"))]
    bins = res["bins"]
    meas = {k: v for k, v in bins.items() if "offset_dex" in v}
    for p in preds:
        pid = p.get("entry_id"); a = p.get("assertion", "")
        m = re.search(r"(\d+\.\d+)\s*dex", a)
        if not m:
            out[pid] = {"status": "not-numeric-in-span"}
            continue
        val = float(m.group(1))
        if not meas:
            out[pid] = {"status": "no-measured-bins"}
            continue
        # R2(a): frame from the ENTRY's scope fields, never keyword-guessed from prose.
        scope = p.get("scope") or {}
        baseline = (scope.get("baseline") or p.get("baseline") or "").lower()
        if not baseline:
            out[pid] = {"status": "frame-undetermined (entry carries no scope.baseline field) — not-comparable-v1",
                        "pred_dex": val}
            continue
        if "am13" not in baseline and "te-anchor" not in baseline and "z<3" not in baseline:
            out[pid] = {"status": f"frame-mismatch (baseline '{baseline[:40]}' is not our z<3 Te-anchor frame)",
                        "pred_dex": val}
            continue
        # R2(b): sign from the entry's direction field; undeterminable => not-comparable.
        direction = (scope.get("direction") or p.get("direction") or "").lower()
        if direction in ("decline", "deficit", "below"):
            pred_off = -val
        elif direction in ("elevation", "above", "excess"):
            pred_off = +val
        else:
            out[pid] = {"status": "direction-undetermined (no direction field) — not-comparable-v1",
                        "pred_dex": val}
            continue
        # R2(c): compare against EVERY measured bin, explicitly.
        rows = {}
        for k, v in meas.items():
            d = abs(v["offset_dex"] - pred_off)
            rows[k] = {"dex_distance": round(d, 3), "combined_unc": v["unc_16_84_half"],
                       "verdict": "consistent" if d <= v["unc_16_84_half"] * 2 else "in-tension"}
        out[pid] = {"pred_offset_dex": pred_off, "per_bin": rows}
    return out

def main():
    log("=== t3_real.py START (reviewed-script protocol) ===")
    man = os.path.join(LANE, "T1_CATALOG_MANIFEST.json")
    tables = s1_enumerate(man)
    if not tables:
        json.dump({"status": "HONEST_FAILURE", "reason": "no public line tables carry 4363-class columns in enumerated series"},
                  open(os.path.join(LANE, "T3_REAL_RESULTS.json"), "w"), indent=1)
        log("S1 empty -> HONEST_FAILURE recorded"); return
    sample = s2_fetch(tables)
    sample = s3_derive(sample)
    with open(os.path.join(LANE, "T3_REAL_SAMPLE.jsonl"), "w") as f:
        for r in sample: f.write(json.dumps(r) + "\n")
    res = s4_compute(sample)
    res["predictions_confrontation"] = s5_confront(res)
    res["status"] = "REAL_COMPLETED"
    res["protocol"] = "reviewed-script; no agent-typed numbers; every row carries provenance"
    json.dump(res, open(os.path.join(LANE, "T3_REAL_RESULTS.json"), "w"), indent=1)
    try:
        import matplotlib; matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        ok = [r for r in sample if r.get("oh_direct") and r.get("logmass")]
        xs = [r["logmass"] for r in ok]; ys = [r["oh_direct"] for r in ok]
        plt.figure(figsize=(6, 4.2))
        plt.scatter(xs, ys, s=22, label=f"A' direct-Te z>3 (N={len(ok)})")
        am_x = [x / 100 for x in range(800, 1051, 5)]
        plt.plot(am_x, [anchor_oh(x) for x in am_x], "k--", lw=1, label="AM13 Te anchor (z<3 frame)")
        plt.xlabel("log M*/Msun"); plt.ylabel("12+log(O/H) [direct]")
        plt.legend(); plt.tight_layout()
        plt.savefig(os.path.join(LANE, "T3_REAL_FIGURE.png"), dpi=150)
    except Exception as e:
        log(f"figure skipped: {e}")
    log("=== t3_real.py DONE ===")

if __name__ == "__main__":
    main()
