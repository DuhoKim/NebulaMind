#!/usr/bin/env python3
"""Generate spin-parity-status.html from the lane's own artifacts.

The hand-written version was two days stale when it was found: it still claimed the
freeze was held and the sky run blocked on it, both untrue since 15 Aug. Prose that
has to be remembered gets forgotten, so here the volatile facts are DERIVED and only
the narrative is curated.

Derived on every run: gate verdicts (from the KUN_*.md first lines), harvest progress
(heartbeat.json), contradiction tally (receipts.jsonl), frozen-artifact hashes and
modes. If an input vanishes the page says so rather than repeating a stale claim.
"""
import glob, hashlib, html, json, os, re, stat
from datetime import datetime, timedelta, timezone

PREREG = ("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
          "weekend-video-sextet-20260808T0136K/prereg")
OUT = "/Users/duhokim/HermesOps/cockpit/spin-parity-status.html"

def sha12(p):
    try:
        return hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]
    except OSError:
        return None

def mode(p):
    try:
        return stat.filemode(os.stat(p).st_mode)
    except OSError:
        return None

def gates():
    """Every Kun verdict, newest first. Verdict is the file's first line."""
    out = []
    for p in glob.glob(os.path.join(PREREG, "KUN_*.md")):
        try:
            first = open(p, errors="ignore").readline().strip()
        except OSError:
            continue
        m = re.match(r"^(PASS_[A-Z0-9_]+|HOLD_[A-Z0-9_]+|ASSESSED_[A-Z0-9_]+)$", first)
        if m:
            out.append((os.path.basename(p), m.group(1), os.path.getmtime(p)))
    return sorted(out, key=lambda r: -r[2])

def harvest():
    h = os.path.join(PREREG, "_tori_harvest_20260817")
    hb = os.path.join(h, "heartbeat.json")
    if not os.path.exists(hb):
        return None
    try:
        d = json.load(open(hb))
    except Exception:
        return None
    d["blocked"] = os.path.exists(os.path.join(h, "BLOCK_EVENT.json"))
    d["complete_marker"] = os.path.exists(os.path.join(h, "HARVEST_COMPLETE.json"))
    # contradiction tally, streamed
    rp = os.path.join(h, "receipts.jsonl")
    ok = bad = 0; names = []
    if os.path.exists(rp):
        for line in open(rp, errors="ignore"):
            try: r = json.loads(line)
            except Exception: continue
            if r.get("image_r_listed") is True: ok += 1
            elif r.get("image_r_listed") is False:
                bad += 1
                if len(names) < 6: names.append(r.get("brickname"))
    d["confirmed"] = ok; d["contradicted"] = bad; d["contradicted_names"] = names
    return d

TRANSFER_HB = "/Users/duhokim/NebulaMindData/dr10_south_image_r/heartbeat.json"

def transfer():
    """DR10 south r-band image transfer, read from its own heartbeat (2026-08-19).

    Trust the JOB PHASE, not artifact existence; a beat older than 10 minutes is
    reported as stale instead of echoing a state the writer may no longer hold.
    """
    if not os.path.exists(TRANSFER_HB):
        return None
    try:
        d = json.load(open(TRANSFER_HB))
    except Exception:
        return None
    try:
        beat = datetime.strptime(d.get("utc", ""), "%Y-%m-%dT%H:%M:%SZ")
        d["age_s"] = (datetime.utcnow() - beat).total_seconds()
        d["beat_kst"] = (beat + timedelta(hours=9)).strftime("%d %b %H:%M KST")
    except Exception:
        d["age_s"] = None
        d["beat_kst"] = "unparsable beat time"
    return d

DECLINE = "DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md"
SUCCESSOR = "_successor_build_20260824"

def decline():
    """The decline memo's own signature block, read rather than assumed.

    The study was DECLINED by signature on 2026-08-25. A status page that still presents it as
    in flight is the failure this page exists to avoid, so the banner is derived from the memo's
    EFFECTIVE line and disappears by itself if that line ever changes.
    """
    p = os.path.join(PREREG, DECLINE)
    if not os.path.exists(p):
        return None
    head = open(p, errors="ignore").read(4000)
    m = re.search(r"\*\*EFFECTIVE BY SIGNATURE\s*[—-]\s*([0-9-]+)\.\*\*", head)
    if not m:
        return None
    return {"date": m.group(1), "sha12": sha12(p), "mode": mode(p),
            "declined": "**DECLINED**" in head or "is **DECLINED**" in head}

def successor():
    """The successor's closure gate: the verdict line of each referee report, plus the required
    brick count from the probe receipt. Nothing here is asserted -- if the files are gone, the
    section says so."""
    d = os.path.join(PREREG, SUCCESSOR, "gates")
    if not os.path.isdir(d):
        return None
    out = {"reports": [], "required": None, "objects": None, "selected": None}
    for p in sorted(glob.glob(os.path.join(d, "CLOSURE_V*_*.md"))):
        name = os.path.basename(p)
        if "PROBE" in name or "REPAIR" in name:
            continue
        try:
            last = [l.strip() for l in open(p, errors="ignore") if l.strip()][-1]
        except (OSError, IndexError):
            continue
        v = last.replace("*", "").strip()
        if v in ("CLEAR", "NOT CLEAR"):
            out["reports"].append((name, v, os.path.getmtime(p)))
    out["reports"].sort(key=lambda r: -r[2])
    rec = os.path.join(d, "CLOSURE_PROBE_V6_RECEIPT_20260826.json")
    if os.path.exists(rec):
        try:
            j = json.load(open(rec))
            dm = j.get("stable", {}).get("derived_manifest", {})
            out["required"] = dm.get("required_count")
            out["objects"] = dm.get("objects")
            out["selected"] = dm.get("selected_bricks")
            out["suite"] = j.get("stable", {}).get("summary", {})
        except Exception:
            pass
    return out


FOOTPRINT = "HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md"

def footprint():
    """The two variance numbers whose disagreement stopped the first attempt.

    The licence to proceed required var(cos theta) >= 0.15 for the sample being measured. It was
    recorded as a PASS using 0.445201 -- a number measured on a different, much larger
    population. The sample actually collected scores 0.057985. Both numbers are read out of the
    finding's own table rather than repeated here, so if that document is ever corrected this
    panel follows it.
    """
    fp = os.path.join(PREREG, FOOTPRINT)
    if not os.path.exists(fp):
        return None
    txt = open(fp, errors="ignore").read(8000)
    row = re.search(r"var\(cos theta\)[^|]*\|\s*\*\*`([0-9.]+)`\*\*[^|]*\|\s*\*\*`([0-9.]+)`\*\*", txt)
    obj = re.search(r"\| objects \|[^|]*?([0-9][0-9,]+)[^|]*\|[^|]*?([0-9][0-9,]+)[^|]*\|", txt)
    if not row:
        return None
    d = {"gated": float(row.group(1)), "measured": float(row.group(2)), "threshold": 0.15}
    if obj:
        d["objects_gated"], d["objects_measured"] = obj.group(1), obj.group(2)
    return d


FROZEN = [
    ("Preregistration (v3)", "PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md"),
    ("Route binding (successor, route B)", "TORI_ROUTE_BINDING_SUCCESSOR_20260817.md"),
    ("Route binding (predecessor, superseded)", "TORI_ROUTE_BINDING_20260815.md"),
]
PINS = [
    ("adapter", "adapter/nm_brick_cutout_adapter.py", "267b2a93d2a6"),
    ("fixtures r1", "boundary_fixtures/make_boundary_fixtures.py", "24f55943bffa"),
    ("fixtures r2", "boundary_fixtures/make_boundary_fixtures_round2.py", "60e3d662d72f"),
    ("fixtures r3", "boundary_fixtures/make_boundary_fixtures_round3.py", "6b410fb40def"),
    ("fixtures r4", "boundary_fixtures/make_boundary_fixtures_round4.py", "d6c193841ff8"),
    ("fixtures r5", "boundary_fixtures/make_boundary_fixtures_round5.py", "498659bf1798"),
]

g = gates(); hv = harvest(); tr = transfer(); dc = decline(); sc = successor()
fp = footprint()
passes = [x for x in g if x[1].startswith("PASS")]
holds  = [x for x in g if x[1].startswith("HOLD")]
now = datetime.now().strftime("%d %b %Y, %H:%M KST")

P = ['<!doctype html><meta charset=utf-8><title>Spin-parity study — status</title>',
     '<meta name=viewport content="width=device-width,initial-scale=1">', """<style>
:root{color-scheme:dark light}*{box-sizing:border-box}
body{font:16px/1.65 -apple-system,BlinkMacSystemFont,system-ui,sans-serif;max-width:52rem;margin:0 auto;padding:2rem 1.1rem 4rem;background:#0f1115;color:#dfe3ea}
h1{font-size:1.5rem;margin:.2em 0 .1em;color:#fff}
.sub{color:#8b93a1;font-size:.9rem;margin-bottom:1.8rem}
h2{font-size:1rem;margin:2.2em 0 .7em;padding-top:.8em;border-top:1px solid #232833;color:#9db8e8}
.big{background:#141922;border:1px solid #232833;border-radius:10px;padding:1.1em 1.2em;margin:1.2em 0}
.big .q{color:#8b93a1;font-size:.82rem;text-transform:uppercase;letter-spacing:.06em}
.big .a{font-size:1.15rem;color:#fff;margin-top:.3em}
.blocked{background:#2a1f0e;border-color:#5a4415;color:#f0d9a8}
.ok{background:#12241a;border-color:#1f5133}
.bad{background:#2a1414;border-color:#5a2020;color:#ffc9c9}
table{border-collapse:collapse;width:100%;font-size:.9em;margin:1em 0}
th,td{text-align:left;padding:.42em .6em;border-bottom:1px solid #1e232c}
th{color:#8b93a1;font-weight:500;font-size:.85em}
.y{color:#8ee6b8}.n{color:#ffb59e}.m{color:#78818f;font-size:.85em;white-space:nowrap}
.note{color:#8b93a1;font-size:.85rem;margin:.6em 0}
.bar{height:7px;background:#1b212b;border-radius:4px;overflow:hidden;margin:.6em 0 .3em}
.bar i{display:block;height:100%;background:#4a8f6b}
code{background:#1b212b;padding:.1em .35em;border-radius:4px;font-size:.85em}
.lede{font-size:1.06rem;color:#e8ecf3;border-left:3px solid #3a465c;padding-left:1em;margin:1.4em 0}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(13.5rem,1fr));gap:.7rem;margin:1.3em 0}
.tile{background:#141922;border:1px solid #232833;border-radius:10px;padding:.85em .95em}
.tile .k{color:#8b93a1;font-size:.76rem;text-transform:uppercase;letter-spacing:.05em}
.tile .v{font-size:1.05rem;color:#fff;margin-top:.25em;line-height:1.35}
.tile .w{font-size:.82rem;color:#8b93a1;margin-top:.35em}
.tile.stop{border-color:#5a2020}.tile.stop .v{color:#ffc9c9}
.tile.go{border-color:#1f5133}.tile.go .v{color:#8ee6b8}
.tile.hold{border-color:#5a4415}.tile.hold .v{color:#f0d9a8}
ol.story{padding-left:1.2em}ol.story li{margin:.55em 0}
.meter{margin:1em 0}
.meter .track{position:relative;height:26px;background:#1b212b;border-radius:5px;overflow:hidden}
.meter .fill{height:100%;background:#7a2b2b}
.meter .mark{position:absolute;top:0;bottom:0;width:2px;background:#e8ecf3}
.meter .lab{display:flex;justify-content:space-between;font-size:.8rem;color:#8b93a1;margin-top:.35em}
details{margin:1.4em 0;border-top:1px solid #232833;padding-top:1em}
summary{cursor:pointer;color:#9db8e8;font-size:1rem}
summary::marker{color:#4a5568}
</style>""", "<body>",
     "<h1>Galaxy spin-parity study</h1>",
     f'<div class=sub>Generated from the lane\'s own artifacts · {now} · private review copy · '
     'nothing published, run, or accepted</div>']

# --- the plain-language layer: what this is, where it stands, what happened -------------
declined = bool(dc and dc["declined"])
imgs = tr.get("accepted", 0) if tr else 0
img_gb = (tr.get("cumulative_received_bytes", 0) / 1e9) if tr else 0.0

P += ['<p class=lede>Do galaxies spin one way more often than the other, depending on which '
      'direction of the sky you look in? One 2011 paper says yes, by about 4%, along a '
      'particular axis. This page tracks an attempt to check that — and the attempt has been '
      'stopped.</p>']

first_state = "Stopped" if declined else "Running"
first_cls = "stop" if declined else "go"
succ_line = "Being designed" if sc is not None else "None yet"
succ_cls = "hold"
if sc and sc.get("reports"):
    clear = sum(1 for r in sc["reports"] if r[1] == "CLEAR")
    succ_line = f"In design — {clear} of {len(sc['reports'])} referee report(s) clear"
P += ["<div class=tiles>",
      '<div class=tile><div class=k>The question</div>'
      '<div class=v>Is there a preferred spin direction?</div>'
      '<div class=w>Longo 2011: about 4%, along one axis. Not the wider family of '
      'spin-anisotropy claims — just this one.</div></div>',
      f'<div class="tile {first_cls}"><div class=k>First attempt</div>'
      f'<div class=v>{first_state}{" — declined " + html.escape(dc["date"]) if declined else ""}</div>'
      '<div class=w>Its sample could not answer the question. It halts unrun: no measurement '
      'will be made under it.</div></div>',
      f'<div class="tile {succ_cls}"><div class=k>Replacement</div>'
      f'<div class=v>{html.escape(succ_line)}</div>'
      '<div class=w>Same question, sample chosen differently. Not approved, not running, '
      'nothing measured.</div></div>',
      f'<div class=tile><div class=k>Answer so far</div>'
      f'<div class=v>None</div>'
      f'<div class=w>{imgs:,} bricks of images were downloaded, but no measurement has ever '
      'been made on them.</div></div>',
      "</div>"]

P += ["<h2>What happened, in order</h2>", '<ol class=story>',
      '<li><b>A sample was chosen and its images fetched.</b> '
      f'{imgs:,} sky bricks, {img_gb:,.0f} GB, all of it downloaded and checked.</li>',
      '<li><b>Then someone compared two numbers that had never been put side by side.</b> '
      'The permission to proceed depended on the sample being spread out along the axis being '
      'tested. That check had been recorded as a pass — but using a measurement of a different, '
      'much larger population, not of the sample actually collected.</li>',
      '<li><b>Measured properly, the sample failed that check</b> — see below. The galaxies sat '
      'bunched near one pole, all at nearly the same angle to the axis in question. You cannot '
      'work out which way a room slopes by measuring in one corner.</li>',
      f'<li><b>The study was declined{" on " + html.escape(dc["date"]) if declined else ""}.</b> '
      'Not paused or amended — a preregistration is a promise made before seeing the data, and '
      'once the data exist you cannot edit the promise, only end it and write a new one.</li>',
      '<li><b>A replacement is being designed</b>, testing the same claim with a sample picked '
      'for the property the first one accidentally lacked. It has passed no gate yet.</li>',
      "</ol>"]

if fp:
    lo, hi, thr = fp["measured"], fp["gated"], fp["threshold"]
    scale = max(hi, thr) * 1.1
    P += ["<h2>The number that stopped it</h2>",
          '<p>The sample had to be spread out along the axis being tested. The measure of that '
          f'spread had to be at least <b>{thr}</b>.</p>',
          '<div class=meter><div class=track>'
          f'<div class=fill style="width:{100*lo/scale:.1f}%"></div>'
          f'<div class=mark style="left:{100*thr/scale:.1f}%"></div></div>'
          f'<div class=lab><span>the sample actually collected: <b>{lo}</b></span>'
          f'<span>required: {thr}</span></div></div>',
          f'<p class=note>The pass on file cited <b>{hi}</b> — correct for the {fp.get("objects_gated","larger")}'
          f'-object population it was measured on, and not a statement about the '
          f'{fp.get("objects_measured","collected")}-object sample being used. Neither document '
          'was wrong. They were never compared.</p>']

P += ["<details><summary>The receipts — harvest, transfer, gate verdicts, frozen artifacts and code pins</summary>", '<p class=note>Everything below is read off disk each time this page is built. It is here for someone checking the work rather than reading the story.</p>']

# --- harvest, derived -------------------------------------------------------
if hv:
    done, tot = hv.get("completed", 0), hv.get("total", 1)
    pct = 100.0 * done / tot if tot else 0
    if hv["blocked"]:
        cls, q, a = "big bad", "Retrieval", "STOPPED — the survey host pushed back. Needs your decision."
    elif hv["complete_marker"]:
        cls, q, a = "big ok", "Retrieval", f"Checksum harvest complete — {done:,} of {tot:,}"
    else:
        st = hv.get("state", "?")
        inw = hv.get("in_window")
        a = (f"Checksum harvest {st.lower()} — {done:,} of {tot:,} ({pct:.1f}%)"
             + ("" if inw else ", paused outside the retrieval window"))
        cls, q = "big", "Retrieval in progress"
    P += [f'<div class="{cls}"><div class=q>{q}</div><div class=a>{html.escape(a)}</div>',
          f'<div class=bar><i style="width:{pct:.2f}%"></i></div>',
          f'<p class=note>{hv.get("recent_rate_req_per_s","?")} requests/second against a 1.0 s floor · '
          f'{hv.get("window_pauses",0)} window pause(s) · checksum text only, zero image bytes.</p>']
    if hv["contradicted"]:
        P.append(f'<p class=note><b class=n>{hv["contradicted"]} contradiction(s)</b> — bricks predicted '
                 f'to carry an r-band image whose published listing lacks one: '
                 f'{html.escape(", ".join(str(n) for n in hv["contradicted_names"]))}. This falsifies the '
                 'gated coverage prediction and is a real finding.</p>')
    elif hv["confirmed"]:
        P.append(f'<p class=note><span class=y>{hv["confirmed"]:,} confirmed, 0 contradicted</span> — every '
                 'brick checked so far carries the r-band image its classification predicted.</p>')
    P.append("</div>")
else:
    P += ['<div class="big blocked"><div class=q>Retrieval</div>'
          '<div class=a>No harvest state found on disk</div>'
          '<p class=note>Either it has not started or its state directory has moved. This page reports '
          'what it can read, and says so when it cannot read anything.</p></div>']

# --- transfer, derived ------------------------------------------------------
if tr:
    acc, tot = tr.get("accepted", 0), tr.get("total", 0)
    pct = 100.0 * acc / tot if tot else 0.0
    gb = tr.get("cumulative_received_bytes", 0) / 1e9
    cap = tr.get("approved_byte_ceiling", 0) / 1e9
    st = str(tr.get("state", "?"))
    stale = tr["age_s"] is None or tr["age_s"] > 600
    if stale and st in ("COMPLETE", "COMPLETED", "DONE"):
        # A finished job stops beating; calling that "stale" reads as a fault when it is the
        # expected end state. Say which it is.
        cls, q = "big ok", "Image transfer — finished"
        a = f"{st} at its last beat, {tr['beat_kst']} — {acc:,} bricks. It has not beaten since, "
        a += "which is what a finished transfer does."
    elif stale:
        cls, q = "big blocked", "Image transfer — heartbeat stale"
        a = f"Last beat {tr['beat_kst']} said {st} — treat the state as unknown until it beats again."
    elif st in ("ERROR", "STOPPED", "ABORTED"):
        cls, q, a = "big bad", "Image transfer", f"{st} — needs a decision."
    elif st != "RUNNING":
        cls, q, a = "big ok", "Image transfer", f"{st} — {acc:,} of {tot:,} bricks"
    else:
        cls, q = "big", "Image transfer in progress"
        a = (f"{acc:,} of {tot:,} bricks accepted ({pct:.2f}%)"
             + ("" if tr.get("in_window") else " — paused outside the window"))
    P += [f'<div class="{cls}"><div class=q>{q}</div><div class=a>{html.escape(a)}</div>',
          f'<div class=bar><i style="width:{pct:.2f}%"></i></div>',
          f'<p class=note>{gb:,.1f} GB of the approved {cap:,.0f} GB ceiling · '
          f'{tr.get("bandwidth_ceiling_bytes_per_second", 0)/1e6:.0f} MB/s bandwidth cap · '
          f'{tr.get("pacing_seconds", "?")} s pacing · last brick {html.escape(str(tr.get("last_brick", "?")))} · '
          f'beat {tr["beat_kst"]}.</p></div>']

# --- gates, derived --------------------------------------------------------
P += ["<h3>Independent gates</h3>",
      f'<p class=note>{len(passes)} passed, {len(holds)} held. Every verdict below is read from the '
      'first line of its own report file — this page cannot claim a gate that does not exist.</p>',
      "<table><tr><th>verdict</th><th>report</th></tr>"]
for name, verdict, _ in g[:14]:
    cl = "y" if verdict.startswith("PASS") else ("n" if verdict.startswith("HOLD") else "m")
    P.append(f'<tr><td class={cl}>{verdict}</td><td class=m>{html.escape(name)}</td></tr>')
P.append("</table>")
if holds:
    P.append('<p class=note>Holds are kept visible on purpose. A chain that only ever agrees is not '
             'evidence of anything.</p>')

# --- frozen artifacts, derived ---------------------------------------------
P += ["<h3>Frozen artifacts</h3>", "<table><tr><th>artifact</th><th>sha256</th><th>mode</th></tr>"]
for label, rel in FROZEN:
    p = os.path.join(PREREG, rel)
    h, md = sha12(p), mode(p)
    if h is None:
        P.append(f'<tr><td>{html.escape(label)}</td><td class=n colspan=2>not found</td></tr>')
    else:
        locked = "y" if md and md.startswith("-r--r--r--") else "n"
        P.append(f'<tr><td>{html.escape(label)}</td><td class=m>{h}</td>'
                 f'<td class={locked}>{md}</td></tr>')
P.append("</table>")

P += ["<h3>Pinned code and fixtures</h3>", "<table><tr><th>what</th><th>sha256</th><th>state</th></tr>"]
for label, rel, expect in PINS:
    h = sha12(os.path.join(PREREG, rel))
    if h is None:
        st, cl = "missing", "n"
    elif h == expect:
        st, cl = "unmoved", "y"
    else:
        st, cl = f"MOVED (expected {expect})", "n"
    P.append(f'<tr><td>{html.escape(label)}</td><td class=m>{h or "—"}</td><td class={cl}>{st}</td></tr>')
P.append("</table>")
P.append('<p class=note>The adapter hash matters: the boundary gates were passed against it, so if it '
         'moves those passes no longer cover the current code.</p>')


P.append("</details>")

if sc is not None:
    P += ["<h2>Successor — closure gate</h2>"]
    if sc["required"]:
        P += [f'<div class="big"><div class=q>Required image manifest</div>'
              f'<div class=a>{sc["required"]:,} bricks, derived from {sc["objects"]:,} objects in '
              f'{sc["selected"]:,} selected bricks</div>'
              f'<p class=note>The neighbour-brick effect is {sc["required"]/sc["selected"]:.3f}x the '
              f'selection, so the transfer this implies is about '
              f'{sc["required"] * 12.2 / 1000:,.0f} GB at the predecessor\'s measured 12.2 MB/brick. '
              'Duho raised the planning ceiling to match on 26 Aug. A ceiling is not an '
              'authorization: nothing has been fetched for the successor.</p></div>']
    if sc["reports"]:
        P += ['<table><tr><th>verdict</th><th>report</th></tr>']
        for name, v, _ in sc["reports"]:
            cl = "y" if v == "CLEAR" else "n"
            P.append(f'<tr><td class={cl}>{v}</td><td class=m>{html.escape(name)}</td></tr>')
        P.append("</table>")
        clears = [r for r in sc["reports"] if r[1] == "CLEAR"]
        P.append(f'<p class=note>{len(clears)} of {len(sc["reports"])} referee report(s) CLEAR. '
                 'The panel was designed for more than one seat and returned fewer: two seats were '
                 'refused mid-analysis by their provider\'s safety filter on 26 Aug, so this is a '
                 'narrower review than a full panel, not a stronger one. Whoever makes a freeze '
                 'call downstream should know which kind they are holding.</p>')
    else:
        P.append('<p class=note>No referee verdict on disk yet.</p>')

P += ["<h2>What has and has not happened</h2>"]
if tr and tr.get("accepted"):
    P += [f'<p>Images <b>have</b> been fetched: {tr["accepted"]:,} bricks, '
          f'{tr.get("cumulative_received_bytes", 0)/1e9:,.1f} GB, under the predecessor\'s '
          f'authorization. That transfer reported {html.escape(str(tr.get("state","?")))} at its last '
          f'beat. This page said "never pixels" until 26 Aug, which was false from the moment the '
          'transfer began — the panel above was derived and the sentence was not.</p>']
else:
    P += ["<p>No galaxy image has been fetched.</p>"]
P += ["<p>What has <b>not</b> happened: no measurement has been made on the sky, nothing has been "
      "published, and nothing has been accepted. The spin-parity measurement halts unrun under the "
      "signed decline; the successor's own image transfer has not started.</p>",
      '<p class=note>The checksum harvest, the image retrieval, and the measurement are three separate '
      'decisions. Each needs its own authorization.</p>',
      f'<p class=note>Regenerate: <code>python3 tools/render_spin_parity_status.py</code> (launchd, '
      'every 600 s). Derived from disk — but only where it is actually derived: the sentence above is '
      'a standing reminder that a hand-written claim beside a derived panel is how this page last went '
      'wrong.</p>', "</body>"]

open(OUT, "w").write("\n".join(P))
print(f"  wrote {os.path.basename(OUT)} — gates {len(g)} ({len(passes)} pass / {len(holds)} hold)"
      f" · harvest {'yes' if hv else 'no state'}")
