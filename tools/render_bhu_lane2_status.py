#!/usr/bin/env python3
"""Generate bhu-lane2-status.html from the BHU lane's own gated artifacts.

The cockpit carried only the 12 Aug closing record, so a reader would see a line
described as closed with no sign it was reopened and settled. Everything volatile
here is derived: gate verdicts from their report files, the video's existence and
size from disk, the ledger tally from the ledger. Only narrative is curated.
"""
import glob, hashlib, html, json, os, re, subprocess
from datetime import datetime

W = ("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
     "weekend-video-sextet-20260808T0136K")
ADJ = os.path.join(W, "bhu-mass-adjudication-20260817")
EXP = os.path.join(W, "bhu-neutron-star-explainer-20260817")
EXP2 = os.path.join(W, "bhu-explainer-v2-20260818")
OUT = "/Users/duhokim/HermesOps/cockpit/bhu-lane2-status.html"

def sha12(p):
    try: return hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]
    except OSError: return None

def gates():
    out = []
    for d in (ADJ, EXP):
        for p in glob.glob(os.path.join(d, "KUN_*.md")):
            try: first = open(p, errors="ignore").readline().strip()
            except OSError: continue
            if re.match(r"^(PASS|HOLD|ASSESSED)_[A-Z0-9_]+$", first):
                out.append((os.path.basename(p), first, os.path.getmtime(p)))
    return sorted(out, key=lambda r: -r[2])

def ledger_tally():
    p = os.path.join(EXP, "CLAIM_LEDGER.md")
    if not os.path.exists(p): return None
    t = open(p, errors="ignore").read()
    m = re.search(r"(\d+) sentences ledgered, (\d+) MAPPED, (\d+) framing, (\d+) FLAG", t)
    return m.groups() if m else None

def video():
    p = os.path.join(EXP, "build", "BHU_NEUTRON_STAR_EXPLAINER_LOCAL_REVIEW.mp4")
    if not os.path.exists(p): return None
    d = {"size_mb": round(os.path.getsize(p)/1048576, 1), "sha12": sha12(p)}
    try:
        r = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                            "-of","default=nw=1:nk=1", p], capture_output=True, text=True, timeout=20)
        d["seconds"] = float(r.stdout.strip())
    except Exception: d["seconds"] = None
    fr = os.path.join(EXP, "build", "FREEZE.json")
    d["published"] = False
    if os.path.exists(fr):
        try:
            f = json.load(open(fr))
            d["published"] = "NOT_UPLOADED" not in json.dumps(f).upper()
        except Exception: pass
    return d

def first_line(p):
    try: return open(p, errors="ignore").readline().strip()
    except OSError: return None

def v2_progress():
    """Seat-by-seat state of the v2 remake, read from the lane's own marker files."""
    if not os.path.isdir(EXP2): return None
    steps = [
        ("Yui — script + storyboard", first_line(os.path.join(EXP2, "YUI_DONE.md"))),
        ("Lana — claim ledger", first_line(os.path.join(EXP2, "LANA_DONE.md"))),
        ("Goru — visual plan", first_line(os.path.join(EXP2, "GORU_DONE.md"))),
        ("Kun — packet gate", first_line(os.path.join(EXP2, "KUN_PACKET_GATE_V2.md"))),
        ("Tori — local build", first_line(os.path.join(EXP2, "TORI_DONE.md"))),
        ("Kun — render gate", first_line(os.path.join(EXP2, "KUN_RENDER_GATE_V2.md"))),
    ]
    cand = os.path.join(EXP2, "build", "BHU_EXPLAINER_V2_LOCAL_REVIEW.mp4")
    vid = None
    if os.path.exists(cand):
        vid = {"size_mb": round(os.path.getsize(cand)/1048576, 1), "sha12": sha12(cand)}
        try:
            r = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                                "-of","default=nw=1:nk=1", cand], capture_output=True, text=True, timeout=20)
            vid["seconds"] = float(r.stdout.strip())
        except Exception: vid["seconds"] = None
    return {"steps": steps, "video": vid}

THEORY = os.path.join(W, "bhu-theory-phase0-20260818")

def theory_progress():
    """Theory Phase 0 lane state, read from its own marker files."""
    if not os.path.isdir(THEORY): return None
    return [
        ("Lana — physics scoping (3 routes)", first_line(os.path.join(THEORY, "LANA_P0_DONE.md"))),
        ("Goru — prior-art sweep", first_line(os.path.join(THEORY, "GORU_P0_DONE.md"))),
        ("Kun — Phase 0 gate", first_line(os.path.join(THEORY, "KUN_PHASE0_GATE.md"))),
        ("Lana — Route A closure note", first_line(os.path.join(THEORY, "LANA_CLOSURE_DONE.md"))),
        ("Kun — closure-note gate", first_line(os.path.join(THEORY, "KUN_CLOSURE_GATE.md"))),
    ]

g, lt, v, v2, th = gates(), ledger_tally(), video(), v2_progress(), theory_progress()
now = datetime.now().strftime("%d %b %Y, %H:%M KST")
P = ['<!doctype html><meta charset=utf-8><title>BHU lane 2 — status</title>',
     '<meta name=viewport content="width=device-width,initial-scale=1">', """<style>
:root{color-scheme:dark light}*{box-sizing:border-box}
body{font:16px/1.65 -apple-system,BlinkMacSystemFont,system-ui,sans-serif;max-width:52rem;margin:0 auto;padding:2rem 1.1rem 4rem;background:#0f1115;color:#dfe3ea}
h1{font-size:1.5rem;margin:.2em 0 .1em;color:#fff}
.sub{color:#8b93a1;font-size:.9rem;margin-bottom:1.8rem}
h2{font-size:1rem;margin:2.2em 0 .7em;padding-top:.8em;border-top:1px solid #232833;color:#9db8e8}
.big{background:#141922;border:1px solid #232833;border-radius:10px;padding:1.1em 1.2em;margin:1.2em 0}
.big .q{color:#8b93a1;font-size:.82rem;text-transform:uppercase;letter-spacing:.06em}
.big .a{font-size:1.15rem;color:#fff;margin-top:.3em}
.ok{background:#12241a;border-color:#1f5133}.warn{background:#2a1f0e;border-color:#5a4415;color:#f0d9a8}
table{border-collapse:collapse;width:100%;font-size:.9em;margin:1em 0}
th,td{text-align:left;padding:.42em .6em;border-bottom:1px solid #1e232c}
th{color:#8b93a1;font-weight:500;font-size:.85em}
.y{color:#8ee6b8}.n{color:#ffb59e}.m{color:#78818f;font-size:.85em;white-space:nowrap}
.note{color:#8b93a1;font-size:.85rem;margin:.6em 0}
a{color:#9db8e8}
code{background:#1b212b;padding:.1em .35em;border-radius:4px;font-size:.85em}
</style>""", "<body>",
     "<h1>Black-hole-universe — lane 2</h1>",
     f'<div class=sub>Generated from the lane\'s own gated artifacts · {now} · '
     '<b>Duho\'s personal side-interest, not a NebulaMind research programme</b></div>']

P += ['<div class="big ok"><div class=q>The question that was left open</div>'
      '<div class=a>Settled: the chain fails by its author\'s own second test</div>'
      '<p class=note>The 12 Aug closing record deliberately left one item unadjudicated — whether the '
      'neutron-star mass evidence merely casts doubt on the chain, or falsifies it. It falsifies it, '
      'but not through the famous test everyone watched.</p></div>',
      "<h2>What was found</h2>",
      "<p>Brown–Lee–Rho named <b>two</b> ways to falsify their chain, joined by \"or\". Everyone — "
      "including our own closing video — watched the first: a neutron star heavier than about 2 suns. "
      "The heaviest well-measured star clears 2.00 at the quoted confidence but not at the strict one, "
      "so that limb reaches serious doubt and stops.</p>",
      "<p><b>The second limb had already finished.</b> The same sentence says a double neutron star "
      "whose masses differ by more than 4% also breaks the chain. PSR J1913+1102 differs by "
      "<b>19.3%</b> — nearly five times over — and has been in the refereed literature since 2020.</p>",
      '<div class="big warn"><div class=q>What this does not say</div>'
      '<div class=a>Not "the black-hole-universe idea is falsified"</div>'
      '<p class=note>At least five mutually disagreeing programmes exist. One chain fails as its author '
      'stated it. Smolin\'s hypothesis is not refuted either — it loses its flagship falsifiable '
      'prediction and can leave this route, at the price of no longer being tested by this channel. '
      'And nothing here was measured by us: the numbers are the pulsar community\'s.</p></div>']

P += ["<h2>Gates</h2>", "<table><tr><th>verdict</th><th>report</th></tr>"]
for name, verdict, _ in g:
    cl = "y" if verdict.startswith("PASS") else ("n" if verdict.startswith("HOLD") else "m")
    P.append(f'<tr><td class={cl}>{verdict}</td><td class=m>{html.escape(name)}</td></tr>')
P.append("</table>")
if lt:
    P.append(f'<p class=note>Claim ledger: <b>{lt[0]}</b> sentences, {lt[1]} mapped to gated source '
             f'lines, {lt[2]} framing, <b>{lt[3]} flagged</b> — the flagged one was cut, not softened.</p>')

if v:
    mins = f"{int(v['seconds']//60)} min {int(v['seconds']%60)} s" if v.get("seconds") else "—"
    st = "warn" if v["published"] else "ok"
    lbl = "PUBLISHED" if v["published"] else "Not published · local review only"
    P += [f'<div class="big {st}"><div class=q>Explainer video</div>'
          f'<div class=a>{mins} · {v["size_mb"]} MB · {lbl}</div>'
          f'<p class=note>SHA-256 <code>{v["sha12"]}…</code> · '
          '<a href="/reports/bhu-explainer/">watch the local review copy</a></p>'
          '<p class=note>Narration was transcribed back and diffed word-by-word against the gated '
          'script. The first render was <b>held</b> at 19 word errors — including an author\'s name '
          'misvoiced and a dropped "or" — before the final diffed to zero. Card headings were verified '
          'in the encoded pixels, not the source files.</p></div>']
else:
    P.append('<div class="big"><div class=q>Explainer video</div><div class=a>not built</div></div>')

if v2:
    P.append("<h2>v2 remake — in flight</h2>")
    P.append('<p class=note>Duho, 18 Aug: <i>"remake the video, now make it, easier to understand, '
             'explainning how it can be relataed to BHU cosmology"</i> — v2 walks the chain from the '
             'universe-inside-a-black-hole idea through cosmological natural selection to the '
             'neutron-star tests, on the same gated sources. Crew lane; seat states below are read '
             'from the lane\'s own marker files.</p>')
    P.append("<table><tr><th>seat</th><th>state</th></tr>")
    for label, token in v2["steps"]:
        if token is None:
            P.append(f'<tr><td>{html.escape(label)}</td><td class=m>pending</td></tr>')
        else:
            cl = "y" if ("PASS" in token or "COMPLETE" in token) else ("n" if "HOLD" in token else "m")
            P.append(f'<tr><td>{html.escape(label)}</td><td class={cl}>{html.escape(token)}</td></tr>')
    P.append("</table>")
    if v2["video"]:
        vv = v2["video"]
        mins = f"{int(vv['seconds']//60)} min {int(vv['seconds']%60)} s" if vv.get("seconds") else "—"
        # Published state is read from the video registry by full-hash match, never remembered.
        pub = None
        try:
            reg = json.load(open("/Users/duhokim/HermesOps/cockpit/videos/published.json"))
            cand = os.path.join(EXP2, "build", "BHU_EXPLAINER_V2_LOCAL_REVIEW.mp4")
            full = hashlib.sha256(open(cand, "rb").read()).hexdigest()
            pub = next((e for e in reg.values() if e.get("video_sha256") == full), None)
        except Exception:
            pass
        if pub:
            P.append(f'<p class=note>v2 candidate: {mins} · {vv["size_mb"]} MB · '
                     f'SHA-256 <code>{vv["sha12"]}…</code> · <b>uploaded {html.escape(pub.get("privacy","?"))}</b>: '
                     f'<a href="{html.escape(pub["url"])}">{html.escape(pub["url"])}</a> ({html.escape(pub.get("uploaded_kst",""))})</p>')
        else:
            P.append(f'<p class=note>v2 candidate: {mins} · {vv["size_mb"]} MB · '
                     f'SHA-256 <code>{vv["sha12"]}…</code> · local review only, not published.</p>')

if th:
    P.append("<h2>Theory Phase 0 — can a calibrated BHU observable be derived?</h2>")
    P.append('<p class=note>Duho, 18 Aug: <i>"go ahead with phase 0"</i>, then <i>"go ahead with the '
             'closure note if the gate passes"</i>. All three routes scoped DEAD-ON-ARRIVAL '
             '(axis-model amplitude: sample-complete kill, needs ~18× every galaxy that exists; '
             'torsion-bounce: ~66 orders below reach; birth fingerprint: causal-boundary degeneracy). '
             'One product survives: the Route A closure note — research-note class, one novel element '
             '(the bound→floor confrontation).</p>')
    P.append("<table><tr><th>step</th><th>state</th></tr>")
    for label, token in th:
        if token is None:
            P.append(f'<tr><td>{html.escape(label)}</td><td class=m>pending</td></tr>')
        else:
            cl = "y" if ("PASS" in token or "COMPLETE" in token) else ("n" if "HOLD" in token else "m")
            P.append(f'<tr><td>{html.escape(label)}</td><td class={cl}>{html.escape(token)}</td></tr>')
    P.append("</table>")

P += ["<h2>Status</h2>",
      "<p class=note>This is a <b>note, not a study</b> — the measurements are the pulsar community's, "
      "the threshold is the source's, and the analysis is arithmetic on published posteriors. It belongs "
      "as the closing annex to the BHU line, not grown into a manuscript. Publishing the video is an "
      "unspent decision and would be unlisted-only.</p>",
      f'<p class=note>Regenerate: <code>python3 mkbhu.py</code>. Derived from disk — a gate that does not '
      'exist cannot appear here, and the video\'s published state is read from its freeze record rather '
      'than remembered.</p>', "</body>"]

open(OUT, "w").write("\n".join(P))
print(f"  wrote bhu-lane2-status.html — {len(g)} gates, video {'yes' if v else 'no'}")
