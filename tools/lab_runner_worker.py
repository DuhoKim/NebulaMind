#!/usr/bin/env python3
"""NebulaMind Lab — run worker.
Executes real, bounded studies for SDSS and/or IllustrisTNG:
  - main sequence (scaling-relation-evolution / sim-vs-observation): logM vs logSFR
  - mass-metallicity (mass-metallicity): logM vs 12+log(O/H)
  - stellar mass function (stellar-mass-function / sf-efficiency-baryon-budget): TNG SMF
SDSS + TNG selected together -> overlaid comparison. Heavier outputs
(full AASTeX compile, DR-review loop) remain crew-queued.
"""
import json, time, sys, re
from pathlib import Path
import numpy as np, requests
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt

BASE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution")
RUNS = BASE / "lab-runs"
TNG_CACHE = RUNS / "_tng_cache"
TNG_EXISTING = BASE / "research-frontiers-20260716" / "topic3"   # reuse earlier downloads
ENV_FILE = "/Users/duhokim/NebulaMind/NebulaMind/backend/.env"
TAP = "https://skyserver.sdss.org/dr18/SkyServerWS/SearchTools/SqlSearch"
SIM = "TNG100-1"; SNAP = 99; Z = 0.0; H = 0.6774; FB = 0.1575; ZSUN = 0.0127; OHSUN = 8.69
V_TNG = (75.0 / H) ** 3

def save(rec): (RUNS / f"{rec['id']}.json").write_text(json.dumps(rec, indent=2))
def log(rec, m): rec["log"].append(f"{time.strftime('%H:%M:%S')} {m}"); save(rec)

def _envval(key):
    try:
        for line in open(ENV_FILE):
            if line.startswith(key + "="):
                return line.split("=", 1)[1].strip()
    except Exception:
        pass
    return ""

def median_rel(x, y, lo, hi, step=0.15, minn=25):
    b = np.arange(lo, hi + step, step); c = 0.5 * (b[:-1] + b[1:]); m = np.full(len(c), np.nan)
    for i in range(len(c)):
        s = (x >= b[i]) & (x < b[i + 1])
        if s.sum() > minn: m[i] = np.median(y[s])
    ok = np.isfinite(m); return c[ok], m[ok]

# ---------- TNG data ----------
try:
    import h5py
except ImportError:
    h5py = None


def _need_h5py():
    if h5py is None:
        raise RuntimeError('TNG support unavailable (h5py not installed)')


def tng_field(field, grp="Subhalo"):
    _need_h5py()
    TNG_CACHE.mkdir(parents=True, exist_ok=True)
    for cand in (TNG_CACHE / f"{SIM}_{SNAP}_{field}.hdf5", TNG_EXISTING / f"gc_{SNAP}_{field}.hdf5"):
        if cand.exists() and cand.stat().st_size > 1000:
            try:
                with h5py.File(cand, "r") as f: _ = f[grp][field][:1]
                return cand
            except Exception: pass
    fn = TNG_CACHE / f"{SIM}_{SNAP}_{field}.hdf5"
    key = _envval("NM_TNG_API_KEY")
    url = f"https://www.tng-project.org/api/{SIM}/files/groupcat-{SNAP}/?{grp}={field}"
    for _ in range(4):
        try:
            with requests.get(url, headers={"api-key": key}, stream=True, timeout=600, allow_redirects=True) as r:
                if r.status_code != 200:
                    time.sleep(5); continue
                with open(fn, "wb") as o:
                    for c in r.iter_content(1 << 20): o.write(c)
            with h5py.File(fn, "r") as f: _ = f[grp][field][:1]
            return fn
        except Exception:
            time.sleep(5)
    raise RuntimeError(f"TNG download failed for {field} (server may be busy — retry later)")

def tng_load(rec, need):
    log(rec, f"loading {SIM} z={Z:.0f} fields: {', '.join(need)} …")
    out = {}
    with h5py.File(tng_field("SubhaloMassInRadType"), "r") as f: out["mstar"] = f["Subhalo"]["SubhaloMassInRadType"][:, 4] * 1e10 / H
    with h5py.File(tng_field("SubhaloFlag"), "r") as f: out["flag"] = f["Subhalo"]["SubhaloFlag"][:]
    if "sfr" in need:
        with h5py.File(tng_field("SubhaloSFRinRad"), "r") as f: out["sfr"] = f["Subhalo"]["SubhaloSFRinRad"][:]
    if "gasZ" in need:
        with h5py.File(tng_field("SubhaloGasMetallicitySfrWeighted"), "r") as f: out["gasZ"] = f["Subhalo"]["SubhaloGasMetallicitySfrWeighted"][:]
    return out

# ---------- SDSS data ----------
def sdss_pull(cols_sql, where):
    r = requests.get(TAP, params={"cmd": f"SELECT TOP 120000 {cols_sql} FROM galSpecExtra WHERE {where}", "format": "csv"}, timeout=240)
    return np.genfromtxt(r.text.splitlines(), delimiter=",", skip_header=2)

# ---------- study ----------
def study(rec):
    spec = rec["spec"]; method = spec["method"]; data = spec["data_sources"]
    rid = rec["id"]; out = RUNS / rid; out.mkdir(exist_ok=True)
    use_tng, use_sdss = "tng" in data, "sdss" in data
    res = {"data_sources": data, "method": method}
    plt.figure(figsize=(5.6, 4.3)); made = False

    # ---- Stellar mass function (TNG only; needs a box volume) ----
    if method in ("stellar-mass-function", "sf-efficiency-baryon-budget") and use_tng:
        d = tng_load(rec, []); log(rec, "computing TNG stellar mass function…")
        ms = d["mstar"]; sel = (d["flag"] == 1) & (ms > 0); lgm = np.log10(ms[sel])
        b = np.arange(8.5, 11.8, 0.2); c = 0.5 * (b[:-1] + b[1:]); n, _ = np.histogram(lgm, bins=b)
        phi = n / (V_TNG * 0.2); ok = n > 0
        plt.plot(c[ok], phi[ok], "o-", color="#2471a3", lw=1.8, label=f"TNG100 z=0 (N={sel.sum():,})")
        plt.yscale("log"); plt.ylabel(r"$\phi\,[\mathrm{Mpc^{-3}dex^{-1}}]$"); plt.xlabel(r"$\log(M_\star/M_\odot)$")
        plt.title("TNG100 stellar mass function (z=0)", fontsize=10)
        res["summary"] = f"IllustrisTNG (TNG100-1, z=0) stellar mass function from {sel.sum():,} galaxies in a ({(75/H):.0f} Mpc)³ box; n(>10¹⁰·⁵M⊙)={(10**lgm>10**10.5).sum()/V_TNG:.2e} Mpc⁻³."
        made = True

    # ---- Main sequence or MZR (SDSS and/or TNG, overlaid) ----
    else:
        is_mzr = method == "mass-metallicity"
        ylab = r"$12+\log(\mathrm{O/H})$" if is_mzr else r"$\log(\mathrm{SFR}/M_\odot\mathrm{yr}^{-1})$"
        title = ("Mass–metallicity relation" if is_mzr else "Star-forming main sequence") + " (z≈0)"
        summ = []
        if use_tng:
            d = tng_load(rec, ["gasZ"] if is_mzr else ["sfr"])
            ms = d["mstar"]
            if is_mzr:
                z = d["gasZ"]; sf = d.get("sfr")
                sel = (d["flag"] == 1) & (ms > 10 ** 8.5) & (z > 0)
                lgm = np.log10(ms[sel]); yv = OHSUN + np.log10(z[sel] / ZSUN)
            else:
                with h5py.File(tng_field("SubhaloSFRinRad"), "r") as f: sfr = f["Subhalo"]["SubhaloSFRinRad"][:]
                sel = (d["flag"] == 1) & (ms > 10 ** 8.5) & (sfr > 0)
                lgm = np.log10(ms[sel]); yv = np.log10(sfr[sel])
            c, mrel = median_rel(lgm, yv, 8.5, 11.4)
            plt.plot(c, mrel, "-", color="#c0392b", lw=2.2, label=f"TNG100 (N={sel.sum():,})")
            summ.append(f"TNG100 ({sel.sum():,} gals)")
        if use_sdss:
            log(rec, "pulling SDSS…")
            if is_mzr:
                raw = sdss_pull("lgm_tot_p50, oh_p50", "lgm_tot_p50 BETWEEN 8.5 AND 11.5 AND bptclass IN (1,2) AND oh_p50>7.5 AND oh_p50<9.4")
                lgm, yv = raw[:, 0], raw[:, 1]
            else:
                raw = sdss_pull("lgm_tot_p50, sfr_tot_p50, specsfr_tot_p50", "lgm_tot_p50 BETWEEN 8.5 AND 11.5 AND specsfr_tot_p50>-11 AND sfr_tot_p50>-50")
                lgm, yv = raw[:, 0], raw[:, 1]
            g = np.isfinite(lgm) & np.isfinite(yv); lgm, yv = lgm[g], yv[g]
            c, mrel = median_rel(lgm, yv, 8.5, 11.4)
            plt.plot(c, mrel, "-", color="#2471a3", lw=2.2, label=f"SDSS (N={len(lgm):,})")
            summ.append(f"SDSS ({len(lgm):,} gals)")
        plt.xlabel(r"$\log(M_\star/M_\odot)$"); plt.ylabel(ylab); plt.title(title, fontsize=10); plt.legend(fontsize=9)
        res["summary"] = f"{title.split(' (')[0]} — median relations for {', '.join(summ)}." + (" TNG uses SF-weighted gas metallicity → O/H (solar-scaled)." if is_mzr and use_tng else "")
        made = summ != []

    if not made:
        raise RuntimeError("no computable data source for this method")
    plt.tight_layout(); plt.savefig(out / "result.png", dpi=110); plt.close()
    res["figure_url"] = f"/api/lab/runs/{rid}/artifact/result.png"
    rec["artifacts"] = ["result.png"]; rec["result"] = res


# ---------- outputs: AASTeX + automated review ----------
_UNI = {"M☉": "Msun", "☉": " solar", "→": " to ", "≈": "~",
        "×": "x", "·": ".", "–": "-", "≥": ">=", "≤": "<="}
_SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-")

def texsafe(s: str) -> str:
    s = s or ""
    for a, b in _UNI.items():
        s = s.replace(a, b)
    s = s.translate(_SUP)
    out = []
    for ch in s:
        if ch in "&%$#_{}":
            out.append("\\" + ch)
        elif ch == "^":
            out.append("\\^{}")
        elif ch == "~":
            out.append("\\~{}")
        elif ch == "\\":
            out.append("\\textbackslash{}")
        else:
            out.append(ch)
    return "".join(out)

MODEL = "astrosage-70b:latest"
MAX_REVISE = 3

def _ollama(prompt, n=700, model=MODEL):
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": model, "prompt": prompt, "stream": False,
                            "options": {"num_predict": n, "temperature": 0.4}},
                      timeout=300)
    j = r.json()
    return ((j.get("response") or "") or (j.get("thinking") or "")).strip()

def draft_body(rec):
    spec = rec["spec"]; summ = rec["result"].get("summary", "")
    prompt = (
        "You are an astronomer writing the body of a short research note.\n"
        f"Topic: {spec.get('topic')}. Data: {', '.join(spec.get('data_sources', []))}. "
        f"Method: {spec.get('method')}.\n"
        f"The ONLY quantitative result you may state is exactly: {summ}\n"
        "Write four short paragraphs in plain prose (NO LaTeX, NO headings), separated by blank lines, "
        "in this order: (1) Introduction/motivation, (2) Data and method, (3) Result, (4) Caveats. "
        "Do NOT invent any numbers, error bars, comparisons, or results beyond the single one given. "
        "The caveats paragraph must state the real limitations of an automated, single-selection, "
        "uncalibrated measurement. Be specific and honest."
    )
    return _ollama(prompt, 700)

def review_text(rec, body):
    spec = rec["spec"]
    prompt = (
        "You are a rigorous, skeptical astronomy referee reviewing the manuscript body below.\n"
        "Begin your reply with EXACTLY one line, one of: 'VERDICT: ACCEPT', 'VERDICT: MINOR', "
        "'VERDICT: MAJOR', or 'VERDICT: REJECT'. Then give a concise report (under 180 words) listing "
        "the top correctness/overclaim risks, missing caveats, and the single most important fix. "
        "Judge it fairly as a brief automated descriptive note (not a full paper): reserve MAJOR/REJECT "
        "for genuine overclaims or errors, and use MINOR/ACCEPT once claims are honest and well-caveated.\n\n"
        f"Topic: {spec.get('topic')} | Method: {spec.get('method')} | Data: {', '.join(spec.get('data_sources', []))}\n"
        "=== MANUSCRIPT BODY ===\n" + body
    )
    rep = _ollama(prompt, 480)
    m = re.search(r"VERDICT:\s*(ACCEPT|MINOR|MAJOR|REJECT)", rep, re.I)
    return rep, (m.group(1).upper() if m else "MAJOR")

def revise_body(rec, body, report):
    prompt = (
        "You are the author revising your manuscript body to satisfy a referee. Revise the text below to "
        "address the referee report: soften or remove overclaims, add honest caveats and explicit "
        "limitation statements, and improve framing. You may NOT invent new numbers, error bars, or "
        "comparisons — where the referee asks for analysis that is not available, add a single honest "
        "limitation/future-work sentence instead of fabricating it. Keep the one real quantitative result "
        "unchanged. Return ONLY the revised body prose (four paragraphs, blank lines between, no headings).\n\n"
        "=== REFEREE REPORT ===\n" + report + "\n\n=== CURRENT BODY ===\n" + body
    )
    return _ollama(prompt, 700)

def revise_loop(rec, body):
    rid = rec["id"]; res = rec["result"]
    cycles = []; verdict = "MAJOR"
    for i in range(1, MAX_REVISE + 1):
        rep, verdict = review_text(rec, body)
        cycles.append({"i": i, "verdict": verdict, "report": rep, "body": body})
        log(rec, f"review cycle {i}: {verdict}")
        if verdict in ("ACCEPT", "MINOR"):
            break
        if i < MAX_REVISE:
            body = revise_body(rec, body, rep)
            log(rec, f"revised draft after cycle {i}")
    # write the changelog artifact
    md = [f"# Automated review-revise loop\n",
          f"Model: {MODEL}. Converged to **{verdict}** after {len(cycles)} cycle(s).\n"]
    for c in cycles:
        md.append(f"\n## Cycle {c['i']} — VERDICT: {c['verdict']}\n\n{c['report']}\n")
        md.append(f"\n<details><summary>draft reviewed in cycle {c['i']}</summary>\n\n{c['body']}\n\n</details>\n")
    md.append(f"\n## Final manuscript body\n\n{body}\n")
    (RUNS / rid / "review_loop.md").write_text("\n".join(md))
    rec.setdefault("artifacts", []).append("review_loop.md")
    res["review"] = (cycles[-1]["report"] if cycles else "")[:1400]
    res["review_model"] = MODEL
    res["review_verdict"] = verdict
    res["review_cycles"] = len(cycles)
    res["review_url"] = f"/api/lab/runs/{rid}/artifact/review_loop.md"
    log(rec, f"review-revise loop done: {verdict} in {len(cycles)} cycle(s)")
    return body

def make_aastex(rec, body=None):
    import subprocess
    rid = rec["id"]; out = RUNS / rid; res = rec["result"]; spec = rec["spec"]
    log(rec, "compiling AASTeX manuscript (PDF)...")
    summ = res.get("summary", "")
    title = summ.split(" -- ")[0].split(" — ")[0].strip().rstrip(".") or "A galaxy-evolution study"
    data = ", ".join(spec.get("data_sources", []))
    fig = (out / "result.png").exists()
    figblock = (r"\begin{figure}\centering\includegraphics[width=\columnwidth]{result.png}\caption{"
                + texsafe(title) + r"}\end{figure}") if fig else ""
    if body:
        secs = ["Introduction", "Data and method", "Result", "Caveats"]
        paras = [p.strip() for p in body.split("\n\n") if p.strip()]
        parts = []
        for i, p in enumerate(paras):
            if i < len(secs):
                parts.append("\\section{" + secs[i] + "}\n" + texsafe(p))
            else:
                parts.append(texsafe(p))
            if i == 2 and figblock:
                parts.append(figblock)
        bodytex = "\n".join(parts)
        if len(paras) <= 2 and figblock:
            bodytex += "\n" + figblock
    else:
        bodytex = (
            "\\section{Introduction}\nThis short study was configured through the NebulaMind Lab and "
            "computed automatically. The requested analysis is a " + texsafe(spec.get("method", "")) +
            " using " + texsafe(data.upper()) + ".\n\\section{Data and method}\nData are taken directly "
            "from " + texsafe(data) + ". We form median relations in stellar-mass bins without further "
            "homogenisation of IMF or abundance calibration.\n" + figblock +
            "\n\\section{Result}\n" + texsafe(summ) +
            "\n\\section{Caveats}\nThis is an \\emph{automated} first-pass descriptive result. It uses "
            "default selections and calibrations and applies no completeness or selection modelling. It "
            "is a starting point, not a validated measurement."
        )
    tex = ("\\documentclass[twocolumn]{aastex631}\n\\begin{document}\n\\title{" + texsafe(title) +
           "}\n\\author{NebulaMind Lab (autonomous pipeline)}\n"
           "\\affiliation{NebulaMind Lab, \\url{https://lab.nebulamind.net}}\n\\begin{abstract}\n" +
           texsafe(summ) + " Generated autonomously from public data (" + texsafe(data) +
           ") via the NebulaMind Lab runner: a bounded, reproducible, descriptive study.\n"
           "\\end{abstract}\n" + bodytex + "\n\\end{document}\n")
    (out / "draft.tex").write_text(tex)
    try:
        r = subprocess.run(["/opt/homebrew/bin/tectonic", "-X", "compile", "draft.tex"],
                           cwd=str(out), capture_output=True, timeout=240)
        if (out / "draft.pdf").exists():
            rec.setdefault("artifacts", []).append("draft.pdf")
            res["pdf_url"] = f"/api/lab/runs/{rid}/artifact/draft.pdf"
            log(rec, "AASTeX PDF compiled OK")
        else:
            res["aastex_note"] = "compile failed: " + r.stderr.decode(errors="replace")[-160:]
            log(rec, "AASTeX compile failed")
    except Exception as e:
        res["aastex_note"] = f"compile error: {e}"; log(rec, f"AASTeX error: {e}")


def process(rec):
    rec["status"] = "running"; save(rec)
    try:
        study(rec)
        outs = rec["spec"].get("outputs", [])
        body = None
        if ("aastex-draft" in outs) or ("dr-review-loop" in outs):
            body = draft_body(rec); log(rec, "drafted manuscript body")
        if "dr-review-loop" in outs:
            body = revise_loop(rec, body); save(rec)
        if "aastex-draft" in outs:
            make_aastex(rec, body); save(rec)
        rec["status"] = "done"; log(rec, "done ✓")
    except Exception as e:
        rec["status"] = "failed"; rec["result"] = {"error": str(e)[:300]}; log(rec, f"failed: {e}")
    save(rec)

def sweep():
    n = 0
    for f in sorted(RUNS.glob("*.json")):
        try: rec = json.loads(f.read_text())
        except Exception: continue
        if rec.get("status") == "queued": process(rec); n += 1
    return n

if __name__ == "__main__":
    RUNS.mkdir(parents=True, exist_ok=True)
    # re-queue any runs orphaned in "running" by a previous crash/restart
    for jf in RUNS.glob("*.json"):
        try:
            r = json.loads(jf.read_text())
            if r.get("status") == "running":
                r["status"] = "queued"; r.setdefault("log", []).append("re-queued (worker restart)"); save(r)
        except Exception:
            pass
    if "--once" in sys.argv:
        print("processed", sweep(), "queued run(s)")
    else:
        while True:
            sweep(); time.sleep(5)
