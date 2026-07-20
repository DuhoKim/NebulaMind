#!/usr/bin/env python3
"""Per-run transparency page for the AI-Scientist pipeline. Projects a study's run JSON into a
navigable page: pipeline timeline + each gate's EVIDENCE + the grounded result + references + artifacts.
Every gate shows the raw material a human needs to disagree. Usage: render_run_page.py <run-id|path>"""
import base64, html, json, os, re, sys, datetime as dt

BASE = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution"
RUNS = os.path.join(BASE, "lab-runs")
OUT_DIR = "/Users/duhokim/HermesOps/cockpit/runs"
os.makedirs(OUT_DIR, exist_ok=True)

TONE = {  # verdict -> (color, label)
    "NOVEL": ("#4ad6c4", "NOVEL"), "PIVOT": ("#e0a458", "PIVOT"), "ABORT": ("#e05a5a", "ABORT"),
    "CONSISTENT": ("#4ad6c4", "CONSISTENT"), "TENSION": ("#e0a458", "TENSION"),
    "CONTRADICTS": ("#e05a5a", "CONTRADICTS·KILL"), "CIRCULAR": ("#e05a5a", "CIRCULAR"),
    "INSUFFICIENT": ("#9aa3b8", "INSUFFICIENT"),
    "ACCEPT": ("#4ad6c4", "ACCEPT"), "MINOR": ("#4ad6c4", "MINOR"),
    "MAJOR": ("#e0a458", "MAJOR"), "REJECT": ("#e05a5a", "REJECT"),
}
def esc(x): return html.escape(str(x or ""))
def chip(verdict):
    c, lab = TONE.get(str(verdict).upper(), ("#9aa3b8", str(verdict)))
    return f'<span class="chip" style="border-color:{c};color:{c}">{esc(lab)}</span>'

def img_data_uri(path):
    try:
        with open(path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode()
    except Exception:
        return None

def gate_card(title, subtitle, verdict, body_html):
    return (f'<section class="gate"><div class="gh"><h3>{esc(title)}</h3>{chip(verdict)}</div>'
            f'<p class="sub">{subtitle}</p>{body_html}</section>')

def render(rec, rid):
    spec = rec.get("spec", {}); res = rec.get("result", {}); gates = rec.get("gates", {})
    status = rec.get("status", "?")
    # ---- pipeline timeline (stages + verdicts) ----
    nv = gates.get("novelty", {}); ev = gates.get("expected_value", {}); ci = gates.get("citation_entailment", {})
    stages = [
        ("Spec", "done", ""), ("Novelty gate", nv.get("verdict", "—"), nv.get("verdict", "")),
        ("Study (compute)", "done" if res.get("summary") else "—", ""),
        ("Expected-value gate", ev.get("verdict", "—"), ev.get("verdict", "")),
        ("Grounded draft", "done" if res.get("review") or "drafted" in " ".join(rec.get("log", [])) else "—", ""),
        ("Review–revise", res.get("review_verdict", "—"), res.get("review_verdict", "")),
        ("Citation gate", ("clean" if ci and ci.get("n_unsupported", 1) == 0 else ("flagged" if ci else "—")),
         "CONTRADICTS" if ci.get("n_unsupported") else ""),
        ("AASTeX PDF", "done" if res.get("pdf_url") else "—", ""),
    ]
    tl = ""
    for name, state, vk in stages:
        c = TONE.get(str(state).upper(), ("#5b6486", ""))[0]
        tl += f'<div class="step"><span class="dot" style="background:{c}"></span><span class="sname">{esc(name)}</span><span class="sstate">{esc(state)}</span></div>'
    # ---- novelty evidence: nearest prior art ----
    nrows = ""
    for p in (nv.get("papers") or [])[:6]:
        nrows += (f'<tr><td class="mono">{p.get("score",0):.3f}</td><td>{esc((p.get("title") or "")[:78])}</td>'
                  f'<td class="mono">{esc(p.get("year"))}·{esc(p.get("cites"))}c</td></tr>')
    nbody = (f'<p class="reason">{esc(nv.get("reason",""))[:700]}</p>'
             f'<div class="evh">nearest prior art checked (cosine similarity vs the 120k index)</div>'
             f'<table class="ev"><tr><th>sim</th><th>title</th><th>yr·cites</th></tr>{nrows}</table>') if nv else "<p class='sub'>not run</p>"
    # ---- expected-value evidence ----
    ebody = (f'<div class="evh">compared the measured result against {esc(ev.get("n_values","?"))} structured '
             f'values extracted from the retrieved papers (calibration-aware)</div>'
             f'<p class="reason">{esc(ev.get("reason",""))[:900]}</p>') if ev else "<p class='sub'>not run</p>"
    # ---- citation evidence: per-sentence verification ----
    if ci and ci.get("all"):
        crows = ""
        for r in ci["all"][:40]:
            ok = r.get("supported"); c = "#4ad6c4" if ok else ("#e05a5a" if ok is False else "#9aa3b8")
            badge = "✓ supported" if ok else ("✗ unsupported" if ok is False else "— no full text")
            crows += (f'<div class="cite"><span class="cbadge" style="color:{c};border-color:{c}">{badge}</span> '
                      f'<span class="ckey">[{esc(r.get("key"))}]</span> {esc(r.get("sentence"))}</div>')
        cbody = f'<div class="evh">{ci.get("n_unsupported",0)} unsupported of {ci.get("checked",0)} citations checked against full text</div>{crows}'
    else:
        cbody = "<p class='sub'>not run yet</p>"
    # ---- result + references + figure ----
    fig = img_data_uri(os.path.join(RUNS, rid, "result.png"))
    figblock = f'<img class="fig" src="{fig}" alt="result figure"/>' if fig else ""
    refs = "".join(f"<li>{esc(x)}</li>" for x in (rec.get("lit_reflist") or [])[:12])
    pdf = res.get("pdf_url")
    pdflink = f'<a class="btn" href="{esc(pdf)}">AASTeX PDF ↗</a>' if pdf else '<span class="sub">PDF pending</span>'

    return TEMPLATE.format(
        rid=esc(rid), topic=esc(spec.get("topic")), status=esc(status),
        method=esc(spec.get("method")), data=esc(", ".join(spec.get("data_sources", []))),
        timeline=tl, novelty=gate_card("① Novelty gate", "has this exact study been done?", nv.get("verdict","—"), nbody),
        expected=gate_card("② Expected-value gate", "does the result agree with / contradict the literature?", ev.get("verdict","—"), ebody),
        citation=gate_card("③ Citation-entailment gate", "is every citation actually supported by its source?", ("clean" if ci and not ci.get("n_unsupported") else (ci.get("n_unsupported") and "flagged")) or "—", cbody),
        summary=esc(res.get("summary","")), review=chip(res.get("review_verdict","—")),
        cycles=esc(res.get("review_cycles","—")), fig=figblock, refs=refs or "<li class='sub'>none</li>", pdf=pdflink,
    )

TEMPLATE = """<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>Run {rid} — {topic}</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#0a0d17;color:#e8ecf5;font-family:Inter,system-ui,sans-serif;line-height:1.5}}
.wrap{{max-width:1000px;margin:0 auto;padding:1.5rem 1.25rem 4rem}}
a{{color:#7c86ff}} .mono{{font-family:ui-monospace,monospace}} .sub{{color:#9aa3b8;font-size:.85rem}}
h1{{font-size:1.35rem;margin:.2rem 0 .3rem;letter-spacing:-.01em}} .meta{{color:#9aa3b8;font-size:.85rem;margin-bottom:1.2rem}}
.chip{{display:inline-block;border:1px solid;border-radius:999px;padding:.1rem .55rem;font-size:.72rem;font-family:ui-monospace,monospace;letter-spacing:.03em}}
.timeline{{display:flex;flex-wrap:wrap;gap:.4rem;background:#111524;border:1px solid #242a3d;border-radius:12px;padding:.9rem;margin-bottom:1.4rem}}
.step{{display:flex;align-items:center;gap:.4rem;padding:.25rem .6rem;background:#0a0d17;border:1px solid #242a3d;border-radius:8px}}
.dot{{width:9px;height:9px;border-radius:50%}} .sname{{font-size:.82rem}} .sstate{{font-size:.68rem;color:#9aa3b8;font-family:ui-monospace,monospace}}
.gate{{background:#111524;border:1px solid #242a3d;border-radius:12px;padding:1rem 1.1rem;margin-bottom:1rem}}
.gh{{display:flex;justify-content:space-between;align-items:center}} .gate h3{{margin:0;font-size:1.02rem}}
.reason{{font-size:.84rem;color:#c9d0e0;white-space:pre-wrap;background:#0a0d17;border:1px solid #242a3d;border-radius:8px;padding:.6rem .7rem;margin:.5rem 0 0}}
.evh{{font-size:.7rem;text-transform:uppercase;letter-spacing:.1em;color:#4ad6c4;margin:.6rem 0 .35rem;font-family:ui-monospace,monospace}}
table.ev{{width:100%;border-collapse:collapse;font-size:.82rem}} table.ev th{{text-align:left;color:#9aa3b8;font-weight:500;font-size:.7rem;border-bottom:1px solid #242a3d;padding:.3rem .4rem}}
table.ev td{{padding:.3rem .4rem;border-bottom:1px solid rgba(36,42,61,.5);vertical-align:top}}
.cite{{font-size:.83rem;padding:.4rem 0;border-bottom:1px solid rgba(36,42,61,.5)}} .cbadge{{font-size:.66rem;border:1px solid;border-radius:6px;padding:.05rem .35rem;font-family:ui-monospace,monospace;margin-right:.4rem}} .ckey{{color:#7c86ff;font-family:ui-monospace,monospace}}
.fig{{max-width:100%;border:1px solid #242a3d;border-radius:10px;margin:.6rem 0}} .btn{{display:inline-block;background:#7c86ff;color:#0a0d17;font-weight:600;padding:.4rem .9rem;border-radius:8px;text-decoration:none;font-size:.85rem}}
ul{{margin:.4rem 0;padding-left:1.1rem}} li{{font-size:.82rem;color:#c9d0e0;margin:.2rem 0}}
.sect{{font-size:.72rem;text-transform:uppercase;letter-spacing:.12em;color:#9aa3b8;margin:1.6rem 0 .6rem;font-family:ui-monospace,monospace}}
</style></head><body><div class=wrap>
<div class=sub>NebulaMind · AI-Scientist run trace</div>
<h1>{topic}</h1>
<div class=meta>run <span class=mono>{rid}</span> · status <b>{status}</b> · method {method} · data {data}</div>
<div class=timeline>{timeline}</div>
{novelty}{expected}{citation}
<div class=sect>Result</div>
<section class=gate><p style="font-size:.9rem">{summary}</p>{fig}
<div class=meta>referee verdict {review} · {cycles} review cycle(s)</div>{pdf}</section>
<div class=sect>References (real, retrieved &amp; cited)</div><ul>{refs}</ul>
</div></body></html>"""

def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else "gated-e2e-demo"
    path = arg if os.path.exists(arg) else os.path.join(RUNS, f"{arg}.json")
    rec = json.load(open(path)); rid = rec.get("id", os.path.basename(path).replace(".json", ""))
    out = os.path.join(OUT_DIR, f"{rid}.html")
    open(out, "w").write(render(rec, rid))
    print("wrote", out)

if __name__ == "__main__":
    main()
