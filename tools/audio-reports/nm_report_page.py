#!/usr/bin/env python3
"""nm_report_page.py — render ONE status report as a self-contained page.

Duho, 2026-08-20: "overhaul audio report to just status report and combine
slides+audio+caption format like tori's recent report."

The inversion that matters: this is not an audio player with slides attached.
It is a STATUS REPORT — slides carry it, the voice narrates it, the caption
records it. It must read with the sound off.

Input beside the mp3: <stem>.txt (caption), <stem>.deck.json (slides),
<stem>.times.json (alignment). Output: report-<stamp>-<speaker>.html.
Missing deck or caption degrades gracefully — a report always renders.
"""
from __future__ import annotations
import html, json, pathlib, re, sys

R = pathlib.Path("/Users/duhokim/HermesOps/reports/status-audio")
VOICES = R / "voices.json"


def load_voices():
    try:
        return json.loads(VOICES.read_text())
    except Exception:
        return {}


def report_name(stem: str) -> str:
    return f"report-{stem}.html"


def parse_stamp(stem: str):
    m = re.match(r"(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})?", stem)
    if not m:
        return "", ""
    y, mo, d, hh, mm = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)
    MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return f"{int(d)} {MON[int(mo) - 1]} {y}", f"{hh}:{mm} KST"


def speaker_of(stem: str, voices: dict):
    slug = re.sub(r"^\d{8}T\d{4,6}-", "", stem)
    key = slug.split("-")[0].lower()
    meta = voices.get(key)
    return (key, meta) if meta else ("", None)


CSS = """
:root{color-scheme:dark light;--bg:#0b0f1a;--panel:#0c1228;--line:#26304f;--ink:#eef1fb;
--dim:#98a2c8;--cyan:#59d8ff;--amber:#ffc46b;--rose:#ff8ba0;--green:#7ee6a8}
*{box-sizing:border-box}
body{font:16px/1.6 -apple-system,BlinkMacSystemFont,system-ui,sans-serif;max-width:52rem;
margin:0 auto;padding:2rem 1.1rem 5rem;background:var(--bg);color:var(--ink)}
a{color:#9db8e8}
.top{display:flex;align-items:center;gap:.6rem;flex-wrap:wrap;margin-bottom:.4rem}
.who{display:inline-flex;align-items:center;gap:.45rem;font-weight:600}
.dot{width:.62em;height:.62em;border-radius:50%;display:inline-block}
.when{color:var(--dim);font-size:.85rem}
h1{font-size:clamp(1.4rem,4vw,2rem);line-height:1.18;margin:.1em 0 .5em;letter-spacing:-.01em}
.lede{color:var(--dim);font-size:.92rem;margin:0 0 1.4rem}
.stage{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:1.4rem 1.3rem;
min-height:15rem}
.kicker{color:var(--cyan);font-size:.68rem;letter-spacing:.17em;text-transform:uppercase;margin-bottom:.55rem}
.stage h2{font-size:clamp(1.15rem,3.2vw,1.6rem);line-height:1.22;margin:0 0 .8rem;font-weight:700}
.stage ul{margin:0;padding-left:1.15rem}
.stage li{font-size:1rem;line-height:1.55;margin-bottom:.5rem;color:#dfe4f5}
.stage figure{margin:0 0 .9rem}
.stage img{width:100%;border-radius:10px;display:block;background:#000}
.attr{color:#78818f;font-size:.7rem;margin:-.5rem 0 .9rem;line-height:1.45}
.gfx{margin:0 0 .9rem}
.num{color:var(--amber);font-variant-numeric:tabular-nums;font-weight:600}
.ok{color:var(--green)}.bad{color:var(--rose)}
.bar{position:sticky;bottom:0;background:rgba(11,15,26,.94);backdrop-filter:blur(9px);
border-top:1px solid var(--line);margin:1rem -1.1rem 0;padding:.7rem 1.1rem 1rem}
audio{width:100%;height:36px}
.marks{display:flex;flex-wrap:wrap;gap:.3rem;margin:.9rem 0 0}
.marks button{background:#141922;border:1px solid var(--line);color:var(--dim);border-radius:999px;
padding:.22em .68em;font:600 .72rem/1 inherit;cursor:pointer}
.marks button.on{background:var(--cyan);color:#04121c;border-color:var(--cyan)}
h3.sec{font-size:.72rem;text-transform:uppercase;letter-spacing:.14em;color:var(--dim);
margin:2.4rem 0 .7rem}
.caption{background:#0d1119;border:1px solid #1e2532;border-radius:12px;padding:1.1rem 1.2rem;
color:#b9c0cf;font-size:.94rem;line-height:1.72;white-space:pre-wrap}
.caption .s.now{background:rgba(126,230,168,.16);border-radius:3px}
.foot{margin-top:2.2rem;padding-top:1rem;border-top:1px solid #1c2230;color:#6f7787;font-size:.74rem;
line-height:1.65}
.badge{font-size:.68rem;color:#c9b280;border:1px solid #4a4020;border-radius:6px;padding:.08em .45em}
@media(prefers-color-scheme:light){
/* Measured 2026-08-21: cyan kickers scored 1.65:1 and amber numbers 1.57:1 on
   white. The numbers ARE the content of a status report, so they must not
   vanish in daylight; these keep the semantics at >=4.5:1. */
:root{--bg:#fbfbfd;--panel:#fff;--line:#e3e6ec;--ink:#1c1f26;--dim:#5c6472;
--cyan:#0b6b83;--amber:#8a5300;--green:#146c43;--rose:#b02a37}
.attr,.foot{color:#5c6472}
.marks button{color:#3f4757;border-color:#cfd5df}
.caption{background:#f5f6f9;border-color:#e3e6ec;color:#3c4250}
.stage li{color:#3c4250}.marks button{background:#f0f2f6}
.bar{background:rgba(251,251,253,.94)}}
"""


def render(stem: str) -> pathlib.Path | None:
    mp3 = R / f"{stem}.mp3"
    if not mp3.exists():
        return None
    voices = load_voices()
    key, meta = speaker_of(stem, voices)
    name = (meta or {}).get("name", key.title() or "Status")
    colour = (meta or {}).get("color", "#8b93a1")
    voice = (meta or {}).get("voice", "")
    role = (meta or {}).get("role", "")
    day, clock = parse_stamp(stem)

    caption = ""
    cp = R / f"{stem}.txt"
    if cp.exists():
        caption = cp.read_text().strip()
    asr = (R / f"{stem}.asr.json").exists()

    deck = None
    dp = R / f"{stem}.deck.json"
    if dp.exists():
        try:
            deck = json.loads(dp.read_text())
        except Exception:
            deck = None
    slides = (deck or {}).get("slides") or []

    # The headline is the report's first slide, or its first sentence.
    headline = slides[0]["h"] if slides and slides[0].get("h") else \
        (re.split(r"(?<=[.!?])\s+", caption)[0] if caption else "Status report")

    marks = "".join(
        f'<button data-t="{s["t"]}">{int(s["t"])//60}:{int(s["t"])%60:02d}</button>'
        for s in slides)
    first = slides[0] if slides else {"k": "", "h": headline, "b": []}
    fig = ""
    if first.get("img"):
        fig = (f'<figure><img src="{html.escape(first["img"])}" alt=""></figure>'
               f'<div class=attr>{first.get("attr","")}</div>')
    elif first.get("svg"):
        fig = f'<div class=gfx>{first["svg"]}</div>'
    stage = (f'<div class=kicker>{html.escape(first.get("k",""))}</div>'
             f'<h2>{first.get("h","")}</h2>{fig}'
             f'<ul>{"".join(f"<li>{b}</li>" for b in first.get("b", []))}</ul>')

    timing = (deck or {}).get("timing")
    note = ("Slides follow the voice by forced alignment." if timing == "aligned"
            else "Slide timing is estimated from sentence lengths, not measured."
            if timing else "")
    lede_bits = [f"{role}" if role else "", f"narrated in {voice}" if voice else ""]
    lede = " · ".join(x for x in lede_bits if x)

    page = f"""<!doctype html><meta charset=utf-8>
<title>{html.escape(name)} — status report {day} {clock}</title>
<meta name=viewport content="width=device-width,initial-scale=1">
<style>{CSS}</style>
<div class=top>
  <span class=who><span class=dot style="background:{html.escape(colour)}"></span>{html.escape(name)}</span>
  <span class=when>{day} · {clock}</span>
  {'<span class=badge>auto-transcribed</span>' if asr else ''}
</div>
<h1>{headline}</h1>
<div class=lede>{html.escape(lede)}</div>

<div class=stage id=stage>{stage}</div>
<div class=marks id=marks>{marks}</div>

<div class=bar><audio id=au controls preload=auto></audio></div>

<h3 class=sec>What was said</h3>
<div class=caption id=caption>{html.escape(caption)}</div>

<div class=foot>
  Status report from the NebulaMind crew. The slides restate the narration and
  nothing more — every number shown is a number spoken.{' ' + note if note else ''}
  <a href="status.html">live status</a> · <a href="archive.html">all reports</a>
</div>

<script>
const SLIDES = {json.dumps(slides)};
const FILE = {json.dumps(mp3.name)};
const au=document.getElementById('au'), stage=document.getElementById('stage'),
      marks=document.getElementById('marks'), cap=document.getElementById('caption');
// The host ignores Range requests, so a streamed seek snaps backwards; fetching
// the whole (small) reading makes chip seeking exact.
fetch(FILE,{{cache:'no-store'}}).then(r=>r.blob()).then(b=>{{au.src=URL.createObjectURL(b);}})
  .catch(()=>{{au.src=FILE;}});
let cur=-1;
function draw(i){{
  if(i===cur||!SLIDES[i])return; cur=i; const s=SLIDES[i];
  const fig = s.img ? '<figure><img src="'+s.img+'" alt=""></figure>'+(s.attr?'<div class=attr>'+s.attr+'</div>':'')
            : (s.svg ? '<div class=gfx>'+s.svg+'</div>' : '');
  stage.innerHTML='<div class=kicker>'+(s.k||'')+'</div><h2>'+(s.h||'')+'</h2>'+fig+
    '<ul>'+(s.b||[]).map(x=>'<li>'+x+'</li>').join('')+'</ul>';
  [...marks.children].forEach((b,j)=>b.classList.toggle('on',j===i));
}}
marks.addEventListener('click',e=>{{const b=e.target.closest('button'); if(!b)return;
  au.currentTime=parseFloat(b.dataset.t)+0.3; au.play().catch(()=>{{}});}});
au.addEventListener('timeupdate',()=>{{let i=0;
  for(let j=0;j<SLIDES.length;j++) if(au.currentTime>=SLIDES[j].t) i=j; draw(i);}});
if(SLIDES.length) draw(0);
</script>
"""
    out = R / report_name(stem)
    out.write_text(page)
    return out


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: nm_report_page.py <stem|reading.mp3>")
    st = pathlib.Path(sys.argv[1]).name
    st = re.sub(r"\.(mp3|deck\.json|txt)$", "", st)
    p = render(st)
    print(p if p else "no such reading", file=sys.stderr if not p else sys.stdout)
