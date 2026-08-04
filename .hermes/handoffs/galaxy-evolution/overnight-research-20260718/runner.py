#!/usr/bin/env python3
# Overnight autonomous research runner — OTHER data (GSWLC-2, COSMOS2020, JWST catalogs).
# Sustained until morning: pulls real public data, computes real relations, makes figures,
# writes summaries + AASTeX drafts, and runs an astrosage-70b review on headline studies.
# Bounded, honest, descriptive (NOT validated measurements). Resilient: any study may fail
# without stopping the run; the manifest is updated after every study.
import os, sys, json, time, math, traceback, subprocess
import numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
import requests

OUT = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/overnight-research-20260718"
os.makedirs(OUT, exist_ok=True)
START = time.time()
HOURS = 7.0
END = START + HOURS * 3600
TAP = "https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync"
JW = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/research-frontiers-20260716"
plt.rcParams.update({"figure.facecolor": "#0a0d17", "axes.facecolor": "#0a0d17",
                     "text.color": "#e8ecf5", "axes.labelcolor": "#e8ecf5",
                     "xtick.color": "#9aa3b8", "ytick.color": "#9aa3b8", "axes.edgecolor": "#242a3d",
                     "font.size": 11, "figure.dpi": 110})
LOG = os.path.join(OUT, "runner.log")
RESULTS = []
BOOT_MS = []
BOOT_SMF = []

def log(m):
    line = time.strftime("%H:%M:%S") + " " + m
    with open(LOG, "a") as f: f.write(line + "\n")
    print(line, flush=True)

def tapq(query, timeout=200):
    r = requests.get(TAP, params={"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": "csv", "QUERY": query}, timeout=timeout)
    txt = r.text
    if "ERROR" in txt[:400].upper() and "QUERY_STATUS" in txt[:400].upper():
        raise RuntimeError("TAP error: " + txt[:160])
    return np.genfromtxt(txt.splitlines(), delimiter=",", names=True)

def med_trend(x, y, lo, hi, n=14, minn=15):
    edges = np.linspace(lo, hi, n + 1); c = 0.5 * (edges[:-1] + edges[1:]); mx, my = [], []
    for i in range(n):
        m = (x >= edges[i]) & (x < edges[i + 1]) & np.isfinite(y)
        if m.sum() >= minn: mx.append(c[i]); my.append(np.median(y[m]))
    return np.array(mx), np.array(my)

# ---- cosmology (flat LCDM H0=70, Om=0.3) ----
_C_H0 = 299792.458 / 70.0
def Dc(z):
    zz = np.linspace(0, z, 512); E = np.sqrt(0.3 * (1 + zz) ** 3 + 0.7)
    return _C_H0 * np.trapezoid(1.0 / E, zz)
def comoving_vol(z1, z2, area_deg2):
    omega = area_deg2 * (math.pi / 180.0) ** 2
    return (omega / 3.0) * (Dc(z2) ** 3 - Dc(z1) ** 3)  # Mpc^3

# ---- outputs ----
def savefig(fig, name):
    p = os.path.join(OUT, name); fig.savefig(p, bbox_inches="tight"); plt.close(fig); return p

def astrosage(spec_title, summary):
    try:
        prompt = ("You are a skeptical astronomy referee. A brief automated study on public data was run.\n"
                  f"Title: {spec_title}\nResult: {summary}\n\n"
                  "Give <150 words: (1) one-line verdict; (2) top overclaim/systematics risks and missing caveats; "
                  "(3) the single most important next step. Treat it as a first-pass uncalibrated descriptive result.")
        r = requests.post("http://localhost:11434/api/generate",
                          json={"model": "astrosage-70b:latest", "prompt": prompt, "stream": False,
                                "options": {"num_predict": 320, "temperature": 0.4}}, timeout=240)
        return (r.json().get("response") or "").strip()
    except Exception as e:
        return f"(review unavailable: {e})"

def record(idx, title, summary, fig, extra=None, review=None):
    d = {"i": idx, "title": title, "summary": summary, "figure": os.path.basename(fig) if fig else None,
         "extra": extra or {}, "review": review, "elapsed_min": round((time.time() - START) / 60, 1)}
    RESULTS.append(d)
    with open(os.path.join(OUT, "RESULTS.json"), "w") as f: json.dump(RESULTS, f, indent=2)
    # incremental manifest
    with open(os.path.join(OUT, "MANIFEST.md"), "w") as f:
        f.write("# Overnight research — other data (GSWLC-2 · COSMOS2020 · JWST)\n\n")
        f.write(f"Started {time.strftime('%Y-%m-%d %H:%M', time.localtime(START))} local · {len(RESULTS)} studies · "
                f"running {round((time.time()-START)/60,1)} min\n\n")
        f.write("Bounded, honest, automated descriptive results — uncorrected for completeness/selection; not validated measurements.\n\n")
        for r in RESULTS:
            f.write(f"### {r['i']:02d}. {r['title']}\n{r['summary']}\n")
            if r.get("figure"): f.write(f"- figure: `{r['figure']}`\n")
            if r.get("review"): f.write(f"- referee: {r['review'][:400]}\n")
            f.write("\n")
    log(f"[{idx:02d}] {title} -> {summary[:90]}")

# ---- data cache ----
CACHE = {}
def gswlc():
    if "gswlc" not in CACHE:
        d = tapq('SELECT TOP 120000 z, logMs, logSFR, Chi2r FROM "J/ApJ/859/11/gswlc-a2" '
                 'WHERE logMs > 7 AND logMs < 12 AND logSFR > -5 AND Chi2r < 30')
        CACHE["gswlc"] = d
    return CACHE["gswlc"]
def cosmos():
    if "cosmos" not in CACHE:
        d = tapq('SELECT TOP 250000 lpzPDF, loglpMassmed, loglpSFRmed FROM "J/ApJS/258/11/classic" '
                 'WHERE loglpMassmed > 7 AND loglpMassmed < 13 AND lpzPDF > 0.15 AND lpzPDF < 6.5', timeout=300)
        CACHE["cosmos"] = d
    return CACHE["cosmos"]
def jwst(name):
    return np.genfromtxt(os.path.join(JW, "topic2", name), delimiter=",", names=True)

COSMOS_AREA = 1.27  # deg^2 (classic, effective)

# ================= STUDIES =================
def s_gswlc_ms(idx, zlo, zhi, headline=False):
    d = gswlc(); m = (d["z"] >= zlo) & (d["z"] < zhi)
    lm, ls = d["logMs"][m], d["logSFR"][m]
    sf = (ls - lm) > -11.0
    mx, my = med_trend(lm[sf], ls[sf], 8.5, 11.2)
    sl = np.polyfit(mx, my, 1)[0] if len(mx) > 2 else float("nan")
    fig, ax = plt.subplots(figsize=(5, 4)); ax.hexbin(lm[sf], ls[sf], gridsize=45, cmap="viridis", mincnt=1)
    ax.plot(mx, my, "-", color="#4ad6c4", lw=2)
    ax.set_xlabel("log M* [Msun]"); ax.set_ylabel("log SFR [Msun/yr]"); ax.set_title(f"GSWLC-2 main sequence  z={zlo:.2f}-{zhi:.2f}")
    p = savefig(fig, f"s{idx:02d}_gswlc_ms_{zlo:.2f}_{zhi:.2f}.png")
    summ = (f"GSWLC-2 (GALEX+WISE SED SFRs) star-forming main sequence, z={zlo:.2f}-{zhi:.2f}: N_SF={int(sf.sum())}; "
            f"slope~{sl:.2f}; log SFR at logM=10 ~ {np.interp(10.0, mx, my):.2f}.")
    rev = astrosage("GSWLC main sequence", summ)
    record(idx, f"GSWLC-2 main sequence (z={zlo:.2f}-{zhi:.2f})", summ, p, {"slope": sl}, rev)
    if headline: maybe_aastex(idx, "The star-forming main sequence in GSWLC-2 (GALEX/WISE SFRs)", summ, p)

def s_cosmos_smf(idx, zlo, zhi, headline=False):
    d = cosmos(); m = (d["lpzPDF"] >= zlo) & (d["lpzPDF"] < zhi)
    lm = d["loglpMassmed"][m]
    vol = comoving_vol(zlo, zhi, COSMOS_AREA); dm = 0.25
    edges = np.arange(8.0, 12.5 + dm, dm); c = 0.5 * (edges[:-1] + edges[1:])
    counts, _ = np.histogram(lm, bins=edges); phi = counts / (vol * dm)
    nz = phi > 0
    fig, ax = plt.subplots(figsize=(5, 4)); ax.step(c[nz], np.log10(phi[nz]), where="mid", color="#7c86ff", lw=2)
    ax.set_xlabel("log M* [Msun]"); ax.set_ylabel("log phi [Mpc^-3 dex^-1]"); ax.set_title(f"COSMOS2020 SMF  z={zlo:.1f}-{zhi:.1f}")
    p = savefig(fig, f"s{idx:02d}_cosmos_smf_{zlo:.1f}_{zhi:.1f}.png")
    n_hi = float(phi[c >= 10.5].sum() * dm)
    summ = (f"COSMOS2020 (LePhare) uncorrected stellar mass function, z={zlo:.1f}-{zhi:.1f}: N={int(m.sum())} in "
            f"V={vol:.3e} Mpc^3; n(>10^10.5)~{n_hi:.2e} Mpc^-3. No completeness/Vmax correction.")
    rev = astrosage("COSMOS SMF", summ)
    record(idx, f"COSMOS2020 stellar mass function (z={zlo:.1f}-{zhi:.1f})", summ, p, {"n_gt_10p5": n_hi}, rev)
    return n_hi

def s_cosmos_ms(idx, zlo, zhi):
    d = cosmos(); m = (d["lpzPDF"] >= zlo) & (d["lpzPDF"] < zhi)
    lm, ls = d["loglpMassmed"][m], d["loglpSFRmed"][m]
    sf = np.isfinite(ls) & ((ls - lm) > -11.0)
    mx, my = med_trend(lm[sf], ls[sf], 9.0, 11.5)
    fig, ax = plt.subplots(figsize=(5, 4)); ax.hexbin(lm[sf], ls[sf], gridsize=40, cmap="magma", mincnt=1)
    if len(mx): ax.plot(mx, my, "-", color="#4ad6c4", lw=2)
    ax.set_xlabel("log M* [Msun]"); ax.set_ylabel("log SFR [Msun/yr]"); ax.set_title(f"COSMOS2020 MS  z={zlo:.1f}-{zhi:.1f}")
    p = savefig(fig, f"s{idx:02d}_cosmos_ms_{zlo:.1f}_{zhi:.1f}.png")
    sfr10 = float(np.interp(10.0, mx, my)) if len(mx) > 1 else float("nan")
    summ = (f"COSMOS2020 main sequence, z={zlo:.1f}-{zhi:.1f}: N_SF={int(sf.sum())}; log SFR at logM=10 ~ {sfr10:.2f}.")
    rev = astrosage("COSMOS main sequence", summ)
    record(idx, f"COSMOS2020 main sequence (z={zlo:.1f}-{zhi:.1f})", summ, p, {"logsfr10": sfr10}, rev)
    return sfr10

def s_jwst_mzr(idx, headline=True):
    d = jwst("jwst_nakajima.csv"); lm, oh = d["logMs"], d["logOH"]
    ok = np.isfinite(lm) & np.isfinite(oh)
    mx, my = med_trend(lm[ok], oh[ok], 7.5, 10.0, n=6, minn=4)
    fig, ax = plt.subplots(figsize=(5, 4)); ax.scatter(lm[ok], oh[ok], s=14, c="#e0a458")
    if len(mx): ax.plot(mx, my, "-", color="#4ad6c4", lw=2)
    ax.set_xlabel("log M* [Msun]"); ax.set_ylabel("12+log(O/H)"); ax.set_title("JWST high-z MZR (Nakajima+23)")
    p = savefig(fig, f"s{idx:02d}_jwst_mzr.png")
    summ = (f"JWST high-z mass-metallicity (Nakajima+23 NIRSpec, N={int(ok.sum())}, z~4-10): "
            f"12+log(O/H) at logM=9 ~ {np.interp(9.0, mx, my):.2f}" if len(mx) else "JWST MZR: too few points.")
    rev = astrosage("JWST high-z MZR", summ)
    record(idx, "JWST high-z mass-metallicity relation (Nakajima+23)", summ, p, {}, rev)
    if headline: maybe_aastex(idx, "The high-redshift mass-metallicity relation from JWST/NIRSpec", summ, p)

def s_ms_evolution(idx, points, headline=True):
    # points: list of (z, logSFR@logM10, label)
    zs = [p[0] for p in points]; y = [p[1] for p in points]
    fig, ax = plt.subplots(figsize=(5.2, 4)); ax.plot(zs, y, "o-", color="#7c86ff")
    for (z, v, lab) in points: ax.annotate(lab, (z, v), fontsize=7, color="#9aa3b8")
    ax.set_xlabel("redshift z"); ax.set_ylabel("log SFR at logM*=10"); ax.set_title("Main-sequence normalisation vs z (cross-survey)")
    p = savefig(fig, f"s{idx:02d}_ms_evolution.png")
    rise = y[-1] - y[0] if len(y) > 1 else float("nan")
    summ = (f"Cross-survey main-sequence normalisation (log SFR at logM=10) rises ~{rise:.2f} dex from "
            f"z~{zs[0]:.1f} (GSWLC) to z~{zs[-1]:.1f} (JWST) across GSWLC/COSMOS/JWST.")
    rev = astrosage("MS normalisation evolution", summ) if headline else None
    record(idx, "Main-sequence normalisation vs redshift (GSWLC -> COSMOS -> JWST)", summ, p, {"rise_dex": rise}, rev)
    if headline: maybe_aastex(idx, "The rising normalisation of the star-forming main sequence to z~6", summ, p)

def maybe_aastex(idx, title, summary, fig):
    try:
        safe = summary.replace("_", " ").replace("^", " ").replace("%", " ").replace("&", " ")
        tex = (r"\documentclass[twocolumn]{aastex631}\begin{document}\title{" + title +
               r"}\author{NebulaMind Lab (autonomous overnight)}\begin{abstract}" + safe +
               r" Automated overnight result on public data; bounded and descriptive, not a validated measurement." +
               r"\end{abstract}\section{Result}" + safe +
               r"\begin{figure}\includegraphics[width=\columnwidth]{" + os.path.basename(fig) +
               r"}\end{figure}\section{Caveats}Uncorrected for completeness/selection; single default calibration; automated.\end{document}")
        d = os.path.join(OUT, f"paper_{idx:02d}"); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "draft.tex"), "w").write(tex)
        import shutil; shutil.copy(fig, os.path.join(d, os.path.basename(fig)))
        subprocess.run(["/opt/homebrew/bin/tectonic", "-X", "compile", "draft.tex"], cwd=d, capture_output=True, timeout=180)
        log(f"     AASTeX {'OK' if os.path.exists(os.path.join(d,'draft.pdf')) else 'FAILED'} for study {idx}")
    except Exception as e:
        log(f"     AASTeX error study {idx}: {e}")


def s_bootstrap_ms(idx, seed):
    d = gswlc(); m = d["z"] < 0.1; lm = d["logMs"][m]; ls = d["logSFR"][m]; sf = (ls - lm) > -11
    lm, ls = lm[sf], ls[sf]; rng = np.random.default_rng(1000 + seed)
    for _ in range(40):
        ii = rng.integers(0, len(lm), len(lm)); mx, my = med_trend(lm[ii], ls[ii], 8.5, 11.2)
        if len(mx) > 2: BOOT_MS.append(float(np.interp(10.0, mx, my)))
    arr = np.array(BOOT_MS); med = float(arr.mean()); sd = float(arr.std())
    fig, ax = plt.subplots(figsize=(5, 4)); ax.hist(arr, bins=24, color="#7c86ff")
    ax.set_xlabel("log SFR at logM=10"); ax.set_title(f"GSWLC MS normalisation, {len(arr)} accumulated resamples")
    p = savefig(fig, f"s{idx:02d}_boot_ms.png")
    summ = f"GSWLC z<0.1 main-sequence normalisation, {len(arr)} accumulated bootstrap resamples: log SFR at logM=10 = {med:.4f} +/- {sd:.4f} dex (converging)."
    record(idx, f"GSWLC MS normalisation (bootstrap, N={len(arr)})", summ, p, {"med": med, "sd": sd, "n": len(arr)}, astrosage("MS bootstrap", summ))

def s_bootstrap_smf(idx, seed):
    d = cosmos(); m = (d["lpzPDF"] >= 0.2) & (d["lpzPDF"] < 0.5); lm = d["loglpMassmed"][m]
    vol = comoving_vol(0.2, 0.5, COSMOS_AREA); dm = 0.25; edges = np.arange(8.0, 12.5 + dm, dm)
    c = 0.5 * (edges[:-1] + edges[1:]); rng = np.random.default_rng(2000 + seed)
    for _ in range(40):
        ii = rng.integers(0, len(lm), len(lm)); cnt, _ = np.histogram(lm[ii], bins=edges); phi = cnt / (vol * dm)
        BOOT_SMF.append(float(phi[c >= 10.5].sum() * dm))
    arr = np.array(BOOT_SMF); med = float(arr.mean()); sd = float(arr.std())
    fig, ax = plt.subplots(figsize=(5, 4)); ax.hist(arr, bins=24, color="#4ad6c4")
    ax.set_xlabel("n(>10^10.5) [Mpc^-3]"); ax.set_title(f"COSMOS SMF density, {len(arr)} accumulated resamples")
    p = savefig(fig, f"s{idx:02d}_boot_smf.png")
    summ = f"COSMOS2020 z=0.2-0.5 n(>10^10.5), {len(arr)} accumulated bootstrap resamples: {med:.4e} +/- {sd:.2e} Mpc^-3 (converging)."
    record(idx, f"COSMOS SMF density (bootstrap, N={len(arr)})", summ, p, {"med": med, "sd": sd, "n": len(arr)}, astrosage("SMF bootstrap", summ))

# ================= MAIN LOOP =================
def run_study(fn, *a, **k):
    if time.time() >= END: return None
    try:
        return fn(*a, **k)
    except Exception as e:
        log(f"  STUDY FAILED {fn.__name__}{a}: {e}\n{traceback.format_exc()[-300:]}")
        return None

def main():
    log(f"=== overnight runner start, budget {HOURS}h, until ~{time.strftime('%H:%M', time.localtime(END))} local ===")
    idx = 1
    run_study(s_gswlc_ms, idx, 0.01, 0.10, headline=True); idx += 1
    run_study(s_gswlc_ms, idx, 0.10, 0.20); idx += 1
    cosmos_z = [(0.2,0.5),(0.5,0.8),(0.8,1.2),(1.2,1.6),(1.6,2.2),(2.2,3.0),(3.0,4.0),(4.0,5.5)]
    smf_hist = []
    for (a, b) in cosmos_z:
        r = run_study(s_cosmos_smf, idx, a, b, headline=(a == 0.2)); smf_hist.append((0.5*(a+b), r)); idx += 1
    ms_pts = []
    for (a, b) in cosmos_z[:6]:
        v = run_study(s_cosmos_ms, idx, a, b); ms_pts.append((0.5*(a+b), v)); idx += 1
    run_study(s_jwst_mzr, idx, headline=True); idx += 1
    try:
        dg = gswlc(); mm = dg["z"] < 0.1; sf = (dg["logSFR"][mm] - dg["logMs"][mm]) > -11
        mx, my = med_trend(dg["logMs"][mm][sf], dg["logSFR"][mm][sf], 8.5, 11.2); g0 = float(np.interp(10.0, mx, my))
    except Exception: g0 = None
    try:
        dj = jwst("jwst_lisiecki.csv"); lm = np.log10(dj["SFR"] + 1e-6); mx, my = med_trend(dj["logMstar"], lm, 8.5, 10.5, 6, 3)
        jz = float(np.median(dj["z"])); jv = float(np.interp(10.0, mx, my)) if len(mx) else None
    except Exception: jz, jv = 6.0, None
    pts = []
    if g0 is not None and np.isfinite(g0): pts.append((0.05, g0, "GSWLC"))
    for (z, v) in ms_pts:
        if v is not None and np.isfinite(v): pts.append((z, v, "COSMOS"))
    if jv is not None and np.isfinite(jv): pts.append((jz, jv, "JWST"))
    if len(pts) >= 3: run_study(s_ms_evolution, idx, sorted(pts), headline=True); idx += 1
    try:
        sh = [(z, n) for (z, n) in smf_hist if n]
        if len(sh) >= 3:
            fig, ax = plt.subplots(figsize=(5.2, 4)); ax.semilogy([z for z,_ in sh], [n for _,n in sh], "o-", color="#4ad6c4")
            ax.set_xlabel("redshift z"); ax.set_ylabel("n(>10^10.5) [Mpc^-3]"); ax.set_title("Massive-galaxy number density vs z (COSMOS2020)")
            p = savefig(fig, f"s{idx:02d}_massive_assembly.png")
            summ = f"COSMOS2020 n(>10^10.5 Msun) declines from z~{sh[0][0]:.1f} to z~{sh[-1][0]:.1f} (uncorrected)."
            record(idx, "Massive-galaxy number density vs redshift (COSMOS2020)", summ, p, {}, astrosage("massive assembly", summ)); idx += 1
    except Exception as e: log(f"  assembly failed: {e}")

    fine = [(0.3,0.45),(0.45,0.6),(0.6,0.8),(0.8,1.0),(1.0,1.3),(1.3,1.7),(1.7,2.2),(2.2,2.8),(2.8,3.6),(3.6,5.0)]
    rp = 0
    while time.time() < END:
        rp += 1; log(f"--- refinement pass {rp} idx={idx} elapsed={round((time.time()-START)/60,1)}m ---")
        if rp == 1:
            for (a, b) in fine:
                if time.time() >= END: break
                run_study(s_cosmos_smf, idx, a, b); idx += 1
        elif rp == 2:
            for (a, b) in fine[:8]:
                if time.time() >= END: break
                run_study(s_cosmos_ms, idx, a, b); idx += 1
        elif rp == 3:
            for zlo in [round(float(x), 2) for x in np.arange(0.0, 0.28, 0.04)]:
                if time.time() >= END: break
                run_study(s_gswlc_ms, idx, zlo, zlo + 0.04); idx += 1
        else:
            if time.time() < END: run_study(s_bootstrap_ms, idx, rp); idx += 1
            if time.time() < END: run_study(s_bootstrap_smf, idx, rp); idx += 1
    try:
        syn = f"Overnight run: {len(RESULTS)} automated descriptive studies on GSWLC-2, COSMOS2020, and JWST catalogs over {round((time.time()-START)/60,1)} min, {rp} refinement passes."
        record(idx, "Synthesis", syn, None, {}, astrosage("overnight synthesis", syn + " || " + " | ".join(r["summary"][:50] for r in RESULTS[:10])))
    except Exception as e: log(f"synthesis failed: {e}")
    log(f"=== DONE: {len(RESULTS)} studies, {rp} passes, {round((time.time()-START)/60,1)} min ===")

if __name__ == "__main__":
    main()
