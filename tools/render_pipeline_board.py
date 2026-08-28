#!/usr/bin/env python3
"""Aggregate pipeline board — the status + prospects view across ALL AI-Scientist runs.
Funnel (runs reaching each stage), gate pass/kill rates, halt-point histogram, review-verdict mix,
and a run list where honest-failure states are first-class. Also renders each run's page. File-driven."""
import glob, html, json, os, subprocess, sys, time
from collections import Counter

BASE = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution"
RUNS = os.path.join(BASE, "lab-runs")
OUT = "/Users/duhokim/HermesOps/cockpit/pipeline-board.html"
HERE = os.path.dirname(os.path.abspath(__file__))
def esc(x): return html.escape(str(x if x is not None else ""))

STAGES = ["spec", "novelty", "compute", "expected", "draft", "review", "citation", "pdf"]
STAGE_LABEL = {"spec": "Spec", "novelty": "Novelty", "compute": "Study", "expected": "Expected-value",
               "draft": "Draft", "review": "Review", "citation": "Citation", "pdf": "PDF"}

def analyze(r):
    g = r.get("gates") or {}; res = r.get("result") or {}; st = r.get("status", "?"); log = " ".join(r.get("log", []))
    reached = {"spec"}
    if g.get("novelty"): reached.add("novelty")
    if res.get("summary"): reached.add("compute")
    if g.get("expected_value"): reached.add("expected")
    if "drafted" in log or res.get("review"): reached.add("draft")
    if res.get("review_verdict"): reached.add("review")
    if g.get("citation_entailment"): reached.add("citation")
    if res.get("pdf_url"): reached.add("pdf")
    if st == "gated-novelty": halt = "halted · novelty ABORT"
    elif st == "gated-expected": halt = "killed · expected-value"
    elif st == "failed": halt = "error"
    elif res.get("pdf_url"): halt = "completed · PDF"
    else: halt = "stopped · " + STAGE_LABEL.get(sorted(reached, key=STAGES.index)[-1], "?")
    return {"reached": reached, "halt": halt, "status": st,
            "novelty": (g.get("novelty") or {}).get("verdict"),
            "expected": (g.get("expected_value") or {}).get("verdict"),
            "citation": None if not g.get("citation_entailment") else ("clean" if not g["citation_entailment"].get("n_unsupported") else "flagged"),
            "review": res.get("review_verdict")}

def bar(count, total, color="#7c86ff", w=280):
    pct = (count / total * 100) if total else 0
    return f'<div class="barwrap"><div class="bar" style="width:{max(2,pct*w/100):.0f}px;background:{color}"></div><span class="barn">{count}</span></div>'

def dist_block(title, counter, colors):
    if not counter: return ""
    tot = sum(counter.values())
    rows = ""
    for k, n in counter.most_common():
        c = colors.get(str(k).upper(), "#5b6486")
        rows += f'<div class="drow"><span class="dk" style="color:{c}">{esc(k)}</span>{bar(n, tot, c, 180)}</div>'
    return f'<div class="mini"><div class="mh">{esc(title)}</div>{rows}</div>'

VC = {"NOVEL": "#4ad6c4", "PIVOT": "#e0a458", "ABORT": "#e05a5a", "CONSISTENT": "#4ad6c4",
      "TENSION": "#e0a458", "CONTRADICTS": "#e05a5a", "CIRCULAR": "#e05a5a", "INSUFFICIENT": "#9aa3b8",
      "CLEAN": "#4ad6c4", "FLAGGED": "#e05a5a", "ACCEPT": "#4ad6c4", "MINOR": "#4ad6c4",
      "MAJOR": "#e0a458", "REJECT": "#e05a5a"}

def review_card(r):
    a = r["_a"]; rid = r.get("id", "?"); spec = r.get("spec", {}); res = r.get("result", {})
    def vchip(v):
        return "" if not v else f'<span class="chip" style="border-color:{VC.get(str(v).upper(),"#5b6486")};color:{VC.get(str(v).upper(),"#9aa3b8")}">{esc(v)}</span>'
    gates = "".join(vchip(x) for x in [a["novelty"], a["expected"], a["citation"], a["review"]])
    summ = esc((res.get("summary") or "")[:150])
    risk = esc((res.get("review") or "")[:230]) or esc(a["halt"])
    ci = (r.get("gates") or {}).get("citation_entailment") or {}
    spot = ci.get("spot_audit")
    spot_html = (f'<div class="rc-spot"><b>spot-audit</b> [{esc(spot.get("key"))}] &ldquo;{esc(spot.get("sentence"))[:90]}&hellip;&rdquo; &mdash; human: verify?</div>') if spot else ""
    return (f'<div class="rcard"><div class="rc-top"><a href="runs/{esc(rid)}.html">{esc(spec.get("topic",""))[:70]}</a>'
            f'<span class="rc-out">{esc(a["halt"])}</span></div>'
            f'<div class="rc-gates">{gates}</div><div class="rc-result">{summ}</div>'
            f'<div class="rc-risk"><span class="rl">referee &middot; biggest risk</span> {risk}</div>{spot_html}</div>')

def main():
    runs = []
    for f in sorted(glob.glob(os.path.join(RUNS, "*.json"))):
        try: r = json.load(open(f))
        except Exception: continue
        r["_a"] = analyze(r); runs.append(r)
        subprocess.run([sys.executable, os.path.join(HERE, "render_run_page.py"), f],
                       capture_output=True)  # keep per-run pages fresh
    total = len(runs)
    funnel = {s: sum(1 for r in runs if s in r["_a"]["reached"]) for s in STAGES}
    nov = Counter(r["_a"]["novelty"] for r in runs if r["_a"]["novelty"])
    exp = Counter(r["_a"]["expected"] for r in runs if r["_a"]["expected"])
    cit = Counter(r["_a"]["citation"] for r in runs if r["_a"]["citation"])
    rev = Counter(r["_a"]["review"] for r in runs if r["_a"]["review"])
    halt = Counter(r["_a"]["halt"] for r in runs)

    funnel_html = ""
    for s in STAGES:
        c = funnel[s]; drop = "" if s == "spec" else ""
        funnel_html += f'<div class="frow"><span class="fl">{STAGE_LABEL[s]}</span>{bar(c, total)}</div>'
    halt_html = "".join(f'<div class="drow"><span class="dk">{esc(k)}</span>{bar(n, total, "#e0a458" if "halt" in k or "killed" in k else "#4ad6c4", 200)}</div>'
                        for k, n in halt.most_common())
    rows = ""
    for r in sorted(runs, key=lambda r: r.get("id", "")):
        a = r["_a"]; rid = r.get("id", "?")
        def vchip(v):
            if not v: return '<span class="sub">—</span>'
            return f'<span class="chip" style="border-color:{VC.get(str(v).upper(),"#5b6486")};color:{VC.get(str(v).upper(),"#9aa3b8")}">{esc(v)}</span>'
        rows += (f'<tr><td><a href="runs/{esc(rid)}.html">{esc(rid)}</a></td>'
                 f'<td>{esc((r.get("spec") or {}).get("topic",""))[:60]}</td>'
                 f'<td>{vchip(a["novelty"])}</td><td>{vchip(a["expected"])}</td>'
                 f'<td>{vchip(a["citation"])}</td><td>{vchip(a["review"])}</td>'
                 f'<td class="sub">{esc(a["halt"])}</td></tr>')

    completed = funnel["pdf"]
    html_out = TEMPLATE.format(
        total=total, completed=completed,
        novelty_pass=sum(n for k, n in nov.items() if k != "ABORT"), novelty_total=sum(nov.values()) or 0,
        funnel=funnel_html,
        nov=dist_block("Novelty verdicts", nov, VC), exp=dist_block("Expected-value verdicts", exp, VC),
        cit=dist_block("Citation gate", cit, VC), rev=dist_block("Referee verdicts", rev, VC),
        halt=halt_html, rows=rows,
        cards="".join(review_card(r) for r in sorted(runs, key=lambda r:r.get("id","")) if (r.get("result") or {}).get("summary") or r["_a"]["status"].startswith("gated")))
    open(OUT, "w").write(html_out)
    print("wrote", OUT, "|", total, "runs,", completed, "completed to PDF")

TEMPLATE = """<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>AI-Scientist — pipeline board</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#0a0d17;color:#e8ecf5;font-family:Inter,system-ui,sans-serif}}
.wrap{{max-width:1000px;margin:0 auto;padding:1.5rem 1.25rem 4rem}}a{{color:#7c86ff;text-decoration:none}}
h1{{font-size:1.3rem;margin:.2rem 0 .1rem}}.sub{{color:#9aa3b8;font-size:.84rem}}
.sect{{font-size:.72rem;text-transform:uppercase;letter-spacing:.12em;color:#9aa3b8;margin:1.6rem 0 .7rem;font-family:ui-monospace,monospace}}
.card{{background:#111524;border:1px solid #242a3d;border-radius:12px;padding:1rem 1.1rem}}
.frow{{display:flex;align-items:center;gap:.7rem;margin:.28rem 0}}.fl{{width:110px;font-size:.85rem;color:#c9d0e0}}
.barwrap{{display:flex;align-items:center;gap:.5rem}}.bar{{height:16px;border-radius:4px;min-width:2px}}.barn{{font-family:ui-monospace,monospace;font-size:.78rem;color:#9aa3b8}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:.8rem}}
.mini{{background:#0a0d17;border:1px solid #242a3d;border-radius:10px;padding:.7rem .8rem}}.mh{{font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;color:#4ad6c4;margin-bottom:.5rem;font-family:ui-monospace,monospace}}
.drow{{display:flex;align-items:center;justify-content:space-between;gap:.5rem;margin:.2rem 0}}.dk{{font-size:.8rem;font-family:ui-monospace,monospace}}
table{{width:100%;border-collapse:collapse;font-size:.83rem;margin-top:.3rem}}th{{text-align:left;color:#9aa3b8;font-weight:500;font-size:.7rem;border-bottom:1px solid #242a3d;padding:.35rem .45rem}}
td{{padding:.4rem .45rem;border-bottom:1px solid rgba(36,42,61,.5);vertical-align:middle}}
.chip{{display:inline-block;border:1px solid;border-radius:999px;padding:.05rem .5rem;font-size:.68rem;font-family:ui-monospace,monospace}}
.kpi{{display:flex;gap:2rem;margin:.6rem 0 0}}.kpi b{{font-size:1.5rem}}.rgrid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:.7rem}}.rcard{{background:#111524;border:1px solid #242a3d;border-radius:11px;padding:.75rem .85rem}}.rc-top{{display:flex;justify-content:space-between;align-items:baseline;gap:.5rem}}.rc-top a{{font-weight:600;font-size:.92rem}}.rc-out{{font-size:.68rem;color:#9aa3b8;font-family:ui-monospace,monospace;white-space:nowrap}}.rc-gates{{display:flex;gap:.25rem;flex-wrap:wrap;margin:.4rem 0}}.rc-result{{font-size:.8rem;color:#c9d0e0;margin:.2rem 0}}.rc-risk{{font-size:.76rem;color:#9aa3b8;background:#0a0d17;border:1px solid #242a3d;border-radius:7px;padding:.4rem .5rem;margin-top:.4rem}}.rl{{display:block;font-size:.62rem;text-transform:uppercase;letter-spacing:.08em;color:#e0a458;margin-bottom:.2rem;font-family:ui-monospace,monospace}}.rc-spot{{font-size:.72rem;color:#7c86ff;margin-top:.35rem}}
</style></head><body><div class=wrap>
<div class=sub>NebulaMind · AI-Scientist</div><h1>Pipeline board — status &amp; prospects</h1>
<div class=kpi><div><b>{total}</b><div class=sub>runs</div></div><div><b>{completed}</b><div class=sub>reached PDF</div></div><div><b>{novelty_pass}/{novelty_total}</b><div class=sub>passed novelty</div></div></div>
<div class=sect>Funnel — runs reaching each stage</div><div class=card>{funnel}</div>
<div class=sect>Gate &amp; referee verdicts</div><div class=grid>{nov}{exp}{cit}{rev}</div>
<div class=sect>Where runs stop (halt-point)</div><div class=card>{halt}</div>
<div class=sect>Review queue &mdash; 2-minute cards</div><div class="rgrid">{cards}</div>
<div class=sect>Runs</div><div class=card><table>
<tr><th>run</th><th>topic</th><th>novelty</th><th>exp-value</th><th>citation</th><th>referee</th><th>outcome</th></tr>
{rows}</table></div>
</div></body></html>"""

if __name__ == "__main__":
    if "--watch" in sys.argv:
        while True:
            try: main()
            except Exception as e: print("board render error:", e)
            time.sleep(30)
    else:
        main()
