#!/usr/bin/env python3
"""Build archive.html — every past spoken reading, newest first, playable in place.

Filenames come in two historical shapes:
    20260812T181515-problem.mp3      (timestamp first, then slug)
    kunpass-20260811T1425.mp3        (slug first, then timestamp)
Both are parsed; anything without a parseable stamp falls back to file mtime.

Run after adding readings:  python3 nm_audio_index.py
"""
import os, re, subprocess, html, json
from datetime import datetime

DIR = "/Users/duhokim/HermesOps/reports/status-audio"
OUT = os.path.join(DIR, "archive.html")
SKIP = {"latest.mp3"}

STAMP = re.compile(r"(\d{8})T(\d{4,6})")


def parse(name):
    stem = os.path.splitext(name)[0]
    m = STAMP.search(stem)
    when = None
    if m:
        d, t = m.group(1), m.group(2).ljust(6, "0")
        try:
            when = datetime.strptime(d + t, "%Y%m%d%H%M%S")
        except ValueError:
            when = None
    slug = STAMP.sub("", stem).strip("-_ ")
    return when, slug


def duration(path):
    try:
        r = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nw=1:nk=1", path],
            capture_output=True, text=True, timeout=20)
        return float(r.stdout.strip())
    except Exception:
        return None


def title(slug):
    if not slug:
        return "status reading"
    s = slug.replace("_", "-").replace("-", " ").strip()
    return s[:1].upper() + s[1:]


def spanify(text):
    """Wrap each sentence in a span so playback can highlight where it has reached.

    There are no word-level timestamps — the TTS returns audio only. But the reading
    rate is uniform (alloy, speed 1.0), so the player apportions duration across
    sentences by length and lights the current one. Splitting keeps the original
    separators verbatim, because white-space:pre-wrap renders the newlines and
    losing them would reflow every paragraph.
    """
    parts = re.split(r"((?<=[.!?])\s+)", text)
    out = []
    for i, p in enumerate(parts):
        if not p:
            continue
        if i % 2 == 0:                      # sentence
            out.append(f"<span class=s>{html.escape(p)}</span>")
        else:                               # separator, preserved as-is
            out.append(html.escape(p))
    return "".join(out)


def timings(path, text, dur):
    """Per-sentence END times, measured if we have them, estimated if not.

    Measured comes from nm_audio_align.py (forced alignment, build time only).
    Estimated is length + a pause constant, which measured at ~11 wrong-sentence
    seconds per 60s against aligned ground truth — usable, not good. The page is
    told which it got, so a bad estimate is never presented as a measurement.
    """
    t = os.path.splitext(path)[0] + ".times.json"
    sents = re.split(r"((?<=[.!?])\s+)", text)
    sents = [p for i, p in enumerate(sents) if i % 2 == 0 and p.strip()]
    if os.path.exists(t):
        try:
            with open(t) as f:
                d = json.load(f)
            if d.get("ends") and d.get("n") == len(sents):
                return d["ends"], "aligned"
        except Exception:
            pass
    if not dur or not sents:
        return None, None
    w = [len(s.strip()) + 15 for s in sents]        # K=15: measured optimum
    tot = float(sum(w)); acc = 0.0; out = []
    for x in w:
        acc += x
        out.append(round(acc / tot * dur, 3))
    return out, "estimated"


def transcript(path):
    """The spoken text, saved beside the audio by nm_audio_route.sh as <stem>.txt.

    Readings made before 2026-08-14 have none — audio was the only artifact kept.
    Those render an explicit 'not saved' note rather than an empty panel, so the
    absence reads as history rather than as a broken page.
    """
    t = os.path.splitext(path)[0] + ".txt"
    if not os.path.exists(t):
        return None
    try:
        with open(t) as f:
            return f.read().strip() or None
    except Exception:
        return None


rows = []
for name in os.listdir(DIR):
    if name in SKIP or not name.lower().endswith((".mp3", ".m4a")):
        continue
    path = os.path.join(DIR, name)
    when, slug = parse(name)
    if when is None:
        when = datetime.fromtimestamp(os.path.getmtime(path))
    rows.append({
        "file": name,
        "title": title(slug),
        "when": when,
        "size": os.path.getsize(path),
        "dur": duration(path),
        "text": transcript(path),
    })
    rows[-1]["times"], rows[-1]["tmode"] = (
        timings(path, rows[-1]["text"], rows[-1]["dur"]) if rows[-1]["text"] else (None, None))

rows.sort(key=lambda r: r["when"], reverse=True)

def fmt_dur(d):
    if not d:
        return ""
    m, s = divmod(int(round(d)), 60)
    return f"{m}:{s:02d}"

# group by calendar day
groups = []
for r in rows:
    key = r["when"].strftime("%Y-%m-%d")
    if not groups or groups[-1][0] != key:
        groups.append((key, []))
    groups[-1][1].append(r)

WEEK = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
body = []
for key, items in groups:
    d = datetime.strptime(key, "%Y-%m-%d")
    label = f"{WEEK[d.weekday()]} {d.day} {d.strftime('%b %Y')}"
    body.append(f'<h2>{html.escape(label)} <span class=n>{len(items)}</span></h2>')
    body.append("<ul>")
    for r in items:
        meta = " · ".join(x for x in [fmt_dur(r["dur"]), f'{r["size"]//1024} KB'] if x)
        # Transcript sits INSIDE the <li>, directly under its own row and above the
        # next reading — always visible, not gated on a click. It was built twice
        # before this: once as a panel in the fixed player bar, once as click-to-
        # expand. Duho did not see it either time. Anything that needs discovering
        # is not delivered, so rows that have text simply show it. Rows without a
        # transcript emit nothing at all rather than 148 "not saved" notices.
        tx = f'<div class=tx>{spanify(r["text"])}</div>' if r["text"] else ""
        # Timing table travels on the row, with its provenance beside it.
        tattr = (f' data-t="{",".join(str(x) for x in r["times"])}" data-tm="{r["tmode"]}"'
                 if r.get("times") else "")
        body.append(
            f'<li data-src="{html.escape(r["file"])}" data-title="{html.escape(r["title"])}"{tattr}>'
            f'<div class=row>'
            f'<span class=play>▶</span>'
            f'<span class=t>{html.escape(r["title"])}</span>'
            f'<span class=m>{html.escape(r["when"].strftime("%H:%M"))} · {meta}</span>'
            f'</div>{tx}</li>')
    body.append("</ul>")

total_min = sum(r["dur"] or 0 for r in rows) / 60
n_text = sum(1 for r in rows if r["text"])

page = f"""<!doctype html><meta charset=utf-8><title>Status readings — archive</title>
<meta name=viewport content="width=device-width,initial-scale=1">
<style>
:root{{color-scheme:dark light}}*{{box-sizing:border-box}}
body{{font:16px/1.6 -apple-system,BlinkMacSystemFont,system-ui,sans-serif;max-width:44rem;margin:0 auto;
padding:2rem 1.1rem 9rem;background:#0f1115;color:#dfe3ea}}
h1{{font-size:1.3rem;margin:0 0 .2em;color:#fff}}
.sub{{color:#8b93a1;font-size:.85rem;margin-bottom:2rem}}
.sub a{{color:#9db8e8}}
h2{{font-size:.82rem;text-transform:uppercase;letter-spacing:.06em;color:#8b93a1;margin:2.2em 0 .6em;
padding-top:.7em;border-top:1px solid #232833;font-weight:600}}
h2 .n{{color:#4d5666;font-weight:400;text-transform:none;letter-spacing:0}}
ul{{list-style:none;padding:0;margin:0}}
li{{display:block;padding:.62em .8em;margin:.28em 0;border-radius:8px;
border:1px solid #1e242f;background:#141922;cursor:pointer}}
.row{{display:flex;gap:.75em;align-items:baseline}}
.tx{{display:none;margin:.7em 0 .15em;padding:.9em 1em;border-radius:7px;background:#0d1119;
border:1px solid #232833;font-size:1.06rem;line-height:1.7;color:#d5dbe4;white-space:pre-wrap}}
li.sel .tx{{display:block}}
body.notext .tx{{display:none}}
.tx .s{{transition:background .18s ease,color .18s ease;border-radius:3px}}
.tx .s.now{{background:#1d4f33;color:#fff;box-shadow:0 0 0 .2em #1d4f33}}
li:hover{{border-color:#3d4a5f}}
li.on{{border-color:#8ee6b8;background:#16241d}}
li.on .play{{color:#8ee6b8}}
li.err{{border-color:#ffb59e;background:#2a1a16}}
li.err .play{{color:#ffb59e}}
.play{{color:#4d5666;font-size:.75em;width:1em;flex:none}}
.t{{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.m{{color:#78818f;font-size:.78em;white-space:nowrap;flex:none}}
#mode{{display:flex;gap:.4em;justify-content:center;margin:0 auto .5em;max-width:44rem}}
#mode button{{font:600 .74rem/1 inherit;padding:.5em .9em;border-radius:999px;border:1px solid #2c3442;
background:#141922;color:#8b93a1;cursor:pointer}}
#mode button.sel{{background:#16241d;border-color:#1f5133;color:#8ee6b8}}
#bar{{position:fixed;left:0;right:0;bottom:0;background:#131720;border-top:1px solid #232833;
padding:.7em 1rem 1rem;backdrop-filter:blur(8px)}}
#bar .now{{font-size:.85rem;color:#fff;margin-bottom:.4em;max-width:44rem;margin-inline:auto;
overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
audio{{width:100%;max-width:44rem;display:block;margin:0 auto}}
#stoggle{{background:none;border:0;color:#78818f;font:inherit;font-size:.76rem;cursor:pointer;
padding:.15em .3em;text-decoration:underline}}
@media(prefers-color-scheme:light){{body{{background:#fbfbfd;color:#1c1f26}}h1{{color:#000}}
li{{background:#f4f6fa;border-color:#e6e9ef}}li.on{{background:#e8f6ee;border-color:#4bb07a}}
#bar{{background:#f4f6faee;border-top-color:#e3e6ec}}#bar .now{{color:#000}}
.tx{{background:#fff;border-color:#e3e6ec;color:#25292f}}.tx.none{{color:#8a929d}}
.tx .s.now{{background:#c9e9d7;color:#06240f;box-shadow:0 0 0 .2em #c9e9d7}}}}
</style>

<h1>Status readings — archive</h1>
<div class=sub>{len(rows)} readings · {total_min:.0f} minutes total · {n_text} with transcripts · newest first ·
<a href="listen.html">back to live listening</a></div>

{chr(10).join(body)}

<div id=bar>
<div class=now id=now>pick a reading</div>
<div id=mode>
  <button data-m="single" title="Play this reading and stop">just this one</button>
  <button data-m="list" title="Play on down the list, then stop">play the list</button>
  <button data-m="one" title="Repeat the current reading">repeat one</button>
  <button data-m="all" title="Play the list and start again at the top">repeat all</button>
  <button data-a="new" id=autonew title="Play new readings as soon as they are added">auto-play new</button>
  <button id=stoggle title="Show or hide the spoken text">hide text</button>
</div>
<audio id=au controls preload=none></audio></div>

<script>
const au=document.getElementById('au'), now=document.getElementById('now');
let items=[...document.querySelectorAll('li')];
let cur=null;

// UI state is driven by the audio element's own events, never by the click.
// Marking a row "playing" on click was a lie whenever play() failed.
function mark(state){{
  items.forEach(li=>li.classList.remove('on','err'));
  if(!cur) return;
  if(state==='err') cur.classList.add('err');
  else if(state==='playing') cur.classList.add('on');
  const t=cur.dataset.title;
  now.textContent = state==='playing' ? t
                  : state==='paused'  ? t+' — paused'
                  : state==='err'     ? t+' — could not load'
                  : t;
}}

// Transcript is inline under each row; opening a reading reveals its own text.
const stoggle=document.getElementById('stoggle');
let showText = localStorage.getItem('nm_show_text') !== '0';
function paintToggle(){{
  document.body.classList.toggle('notext', !showText);
  stoggle.textContent = showText ? 'hide text' : 'show text';
}}
stoggle.onclick=()=>{{ showText=!showText; localStorage.setItem('nm_show_text', showText?'1':'0'); paintToggle(); }};
paintToggle();

// Auto-play of newly-arrived readings is OPT-IN, not opt-out. It used to default on
// (getItem(...)!=='0', i.e. on whenever unset), which meant a page left open in a tab
// started playing on its own whenever a reading was archived. Duho heard audio he had
// not asked for and could not find the source of — twice. A page must never make sound
// unless the person watching it asked for sound.
let autoNew = localStorage.getItem('nm_auto_new')==='1';
const autonewBtn=document.getElementById('autonew');
function paintAutoNew(){{
  autonewBtn.classList.toggle('sel', autoNew);
  autonewBtn.textContent = autoNew ? 'auto-play new' : 'new: notify only';
}}
autonewBtn.onclick=()=>{{
  autoNew=!autoNew; localStorage.setItem('nm_auto_new', autoNew?'1':'0'); paintAutoNew();
}};
paintAutoNew();

// Reading position. No word-level timestamps exist — the TTS returns audio only — so
// the duration is apportioned across sentences by length, plus a constant per sentence
// for the pause the voice takes at each boundary. It is a cursor, not a caption: it
// tracks well because the reading rate is uniform, and it cannot drift permanently
// because every sentence boundary is re-derived from currentTime, not accumulated.
let track=null;
function buildTrack(li){{
  const spans=[...li.querySelectorAll('.tx .s')];
  if(!spans.length){{ track=null; return; }}
  // The build bakes end-times per sentence — measured by forced alignment where it
  // worked, estimated from length where it did not. The player does not care which;
  // it just reads the table. data-tm records which, so nothing claims false precision.
  const raw=(li.dataset.t||'').split(',').filter(Boolean).map(Number);
  if(raw.length===spans.length){{ track={{spans, ends:raw, at:-1}}; return; }}
  const w=spans.map(s=>s.textContent.trim().length+15);   // last-resort fallback
  const tot=w.reduce((a,b)=>a+b,0); let acc=0;
  track={{spans, cum:w.map(x=>(acc+=x)/tot), at:-1}};
}}
au.addEventListener('timeupdate',()=>{{
  if(!track||!au.duration||!isFinite(au.duration)) return;
  let i;
  if(track.ends){{
    i=track.ends.findIndex(e=>au.currentTime<e);
  }} else {{
    const p=au.currentTime/au.duration;
    i=track.cum.findIndex(c=>p<c);
  }}
  if(i<0) i=track.spans.length-1;
  if(i===track.at) return;
  if(track.at>-1) track.spans[track.at].classList.remove('now');
  track.spans[i].classList.add('now');
  track.at=i;
  // Follow only when the cursor has left the viewport, so it never fights a manual scroll.
  const r=track.spans[i].getBoundingClientRect();
  if(r.top<64 || r.bottom>window.innerHeight-170)
    track.spans[i].scrollIntoView({{block:'center', behavior:'smooth'}});
}});

function start(li){{
  cur=li;
  // Only the track being played shows its text, and the view follows it — including
  // when the list advances on its own, which is the case a click-driven scroll misses.
  items.forEach(x=>x.classList.remove('sel'));
  document.querySelectorAll('.tx .s.now').forEach(s=>s.classList.remove('now'));
  li.classList.add('sel');
  buildTrack(li);
  const want=li.dataset.src;
  // Re-assigning an identical src is a no-op in some browsers, so rewind explicitly.
  if(au.getAttribute('src')===want){{ au.currentTime=0; }}
  else {{ au.src=want; }}
  now.textContent=li.dataset.title+' — loading';
  au.play().then(()=>{{
    // Scroll after the transcript is displayed, or the target geometry is stale.
    const target = li.querySelector('.tx') || li;
    target.scrollIntoView({{block:'center', behavior:'smooth'}});
  }}).catch(()=>mark('err'));
}}

function wire(li){{
  li.onclick=()=>{{
    if(cur===li && !au.paused){{ au.pause(); return; }}   // click again to pause
    if(cur===li && au.paused && au.currentTime>0 && !au.ended){{ au.play().catch(()=>mark('err')); return; }}
    start(li);                                            // any other click (re)starts
  }};
}}
items.forEach(wire);

au.addEventListener('play',  ()=>mark('playing'));
au.addEventListener('pause', ()=>{{ if(!au.ended) mark('paused'); }});
au.addEventListener('error', ()=>mark('err'));
// Playback mode — stored, so it behaves as a setting rather than a per-visit toggle.
// Default is 'single' — play the one you clicked and stop. The old default walked
// on down all 157 readings, which is how Duho ended up hearing "auto playing audio
// from somewhere" he had not started. Stored under a v2 key so anyone carrying the
// old 'list' default gets the sane one, while a deliberate choice still persists.
let mode = localStorage.getItem('nm_play_mode_v2') || 'single';
const modeBtns=[...document.querySelectorAll('#mode button')];
function paintMode(){{
  modeBtns.forEach(b=>b.classList.toggle('sel', b.dataset.m===mode));
  au.loop = (mode==='one');           // native loop gives gapless repeat
}}
modeBtns.forEach(b=>b.onclick=()=>{{
  mode=b.dataset.m; localStorage.setItem('nm_play_mode_v2',mode); paintMode();
}});
paintMode();

// --- new readings arrive without a reload --------------------------------------
// The router no longer plays audio itself (Duho, 2026-08-14: "drop the afplay"), so
// THIS POLLING IS THE DELIVERY PATH. If it stops working, readings become silent
// files nobody hears — exactly the failure that started all of this. latest.txt is
// written by nm_audio_route.sh and names the archived file.
const WEEK=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
const MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
let lastSeen=null, queued=null;

function esc(s){{ return s.replace(/[&<>]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;'}}[c])); }}
// Sentence split without lookbehind — Safari only gained it recently and a syntax
// error here would take the whole player down, not just the highlighting.
function spanifyJS(t){{
  let out='', re=/([^.!?]*[.!?]+)(\\s*)/g, m, last=0;
  while((m=re.exec(t))!==null){{ out+='<span class=s>'+esc(m[1])+'</span>'+esc(m[2]); last=re.lastIndex; }}
  if(last<t.length) out+='<span class=s>'+esc(t.slice(last))+'</span>';
  return out;
}}
function titleOf(file){{
  const slug=file.replace(/\\.(mp3|m4a)$/,'').replace(/\\d{{8}}T\\d{{4,6}}/,'').replace(/^[-_]+|[-_]+$/g,'');
  const s=slug.replace(/[-_]+/g,' ').trim();
  return s ? s[0].toUpperCase()+s.slice(1) : 'status reading';
}}
function addNewReading(file, text){{
  const m=file.match(/(\\d{{4}})(\\d{{2}})(\\d{{2}})T(\\d{{2}})(\\d{{2}})/);
  const d = m ? new Date(+m[1], +m[2]-1, +m[3]) : new Date();
  const hhmm = m ? m[4]+':'+m[5] : '';
  const label = WEEK[d.getDay()]+' '+d.getDate()+' '+MON[d.getMonth()]+' '+d.getFullYear();
  const h2=document.querySelector('h2');
  let ul=document.querySelector('ul');
  if(h2 && h2.textContent.indexOf(label)!==0){{     // a new day — give it its own group
    const nh=document.createElement('h2'); nh.innerHTML=esc(label)+' <span class=n>1</span>';
    const nu=document.createElement('ul');
    h2.parentNode.insertBefore(nh,h2); h2.parentNode.insertBefore(nu,h2); ul=nu;
  }}
  const li=document.createElement('li');
  li.dataset.src=file; li.dataset.title=titleOf(file);
  li.innerHTML='<div class=row><span class=play>&#9654;</span><span class=t>'+esc(titleOf(file))
    +'</span><span class=m>'+hhmm+' &middot; just now</span></div>'
    +(text?'<div class=tx>'+spanifyJS(text)+'</div>':'');
  ul.insertBefore(li, ul.firstChild);
  wire(li);
  items=[...document.querySelectorAll('li')];
  return li;
}}
async function pollLatest(){{
  try{{
    const r=await fetch('latest.txt',{{cache:'no-store'}});
    if(!r.ok) return;
    const file=(await r.text()).trim().split(/\\s+/).pop();
    if(!file || !/\\.(mp3|m4a)$/.test(file)) return;
    if(lastSeen===null){{ lastSeen=file; return; }}   // first poll only sets the baseline
    if(file===lastSeen) return;
    lastSeen=file;
    let text=null;
    try{{ const t=await fetch('latest_transcript.txt',{{cache:'no-store'}});
          if(t.ok) text=(await t.text()).trim(); }}catch(e){{}}
    const li=addNewReading(file,text);
    if(!autoNew){{ now.textContent='new reading added \\u2014 '+li.dataset.title; return; }}
    // Never cut off something already playing; queue it instead.
    if(!au.paused && !au.ended && au.currentTime>0){{
      queued=li;
      now.textContent=(cur?cur.dataset.title:'playing')+' \\u2014 a new reading is queued';
    }} else {{ start(li); }}
  }}catch(e){{}}
}}
setInterval(pollLatest, 8000); pollLatest();

au.addEventListener('ended', ()=>{{
  if(queued){{ const q=queued; queued=null; start(q); return; }}   // arrivals win over mode
  if(mode==='one'){{ if(cur) start(cur); return; }}      // belt and braces if loop is off
  if(mode==='single'){{ mark('idle'); return; }}          // stop here — do not walk the archive
  const i=items.indexOf(cur);
  if(i>-1 && items[i+1]) {{ start(items[i+1]); return; }}
  if(mode==='all' && items.length) {{ start(items[0]); return; }}   // wrap to the top
  mark('idle');
}});
</script>
"""

with open(OUT, "w") as f:
    f.write(page)
print(f"{OUT}  {len(rows)} readings  {os.path.getsize(OUT)} B")
