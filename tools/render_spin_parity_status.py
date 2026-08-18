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
from datetime import datetime, timezone

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

g = gates(); hv = harvest()
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
</style>""", "<body>",
     "<h1>Galaxy spin-parity study</h1>",
     f'<div class=sub>Generated from the lane\'s own artifacts · {now} · private review copy · '
     'nothing published, run, or accepted</div>']

P += ["<h2>What is being tested</h2>",
      "<p>Longo 2011's specific claim — a spin-handedness dipole of |A| &asymp; 0.0408 &plusmn; 0.011 "
      "at (l,b) = (52&deg;, 68.5&deg;).</p>",
      "<p class=note>Not the wider class of spin-anisotropy claims. A null result would not exclude "
      "smaller amplitudes, would not adjudicate Shamir, and would not show the sky is isotropic. It "
      "also would not identify black-hole-universe cosmology — that line closed separately on 11 Aug.</p>"]

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

# --- gates, derived --------------------------------------------------------
P += ["<h2>Independent gates</h2>",
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
P += ["<h2>Frozen artifacts</h2>", "<table><tr><th>artifact</th><th>sha256</th><th>mode</th></tr>"]
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

P += ["<h2>Pinned code and fixtures</h2>", "<table><tr><th>what</th><th>sha256</th><th>state</th></tr>"]
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

P += ["<h2>What has not happened</h2>",
      "<p>No galaxy image has been fetched. No measurement has been made on the sky. Nothing has been "
      "published and nothing accepted. The work so far touches catalogues, file listings and small "
      "checksum files — never pixels.</p>",
      '<p class=note>The checksum harvest, the image retrieval, and the measurement are three separate '
      'decisions. Each needs its own authorization.</p>',
      f'<p class=note>Regenerate: <code>python3 mkspinparity.py</code>. Derived from disk, so it cannot '
      'go stale the way its hand-written predecessor did — that version still claimed the freeze was '
      'held two days after it was granted.</p>', "</body>"]

open(OUT, "w").write("\n".join(P))
print(f"  wrote {os.path.basename(OUT)} — gates {len(g)} ({len(passes)} pass / {len(holds)} hold)"
      f" · harvest {'yes' if hv else 'no state'}")
