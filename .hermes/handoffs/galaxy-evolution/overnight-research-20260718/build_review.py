import json, base64, os, html
D = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(D, "RESULTS.json")))
byi = {r["i"]: r for r in R}

def img(fig):
    p = os.path.join(D, fig) if fig else None
    if not p or not os.path.exists(p): return None
    return "data:image/png;base64," + base64.b64encode(open(p, "rb").read()).decode()

# last converged bootstrap studies
boot_ms = [r for r in R if "MS normalisation (bootstrap" in r["title"]]
boot_smf = [r for r in R if "SMF density (bootstrap" in r["title"]]
sel = [1, 3, 15, 17, 19]  # gswlc MS, cosmos SMF, cosmos MS high-z, JWST MZR, massive assembly
hero = byi.get(18)  # MS normalisation evolution
cards = [byi[i] for i in sel if i in byi]
if boot_ms: cards.append(boot_ms[-1])
if boot_smf: cards.append(boot_smf[-1])

def review_html(r):
    rv = r.get("review") or ""
    if not rv or "stub" in rv: return ""
    return f'<div class="rev"><span class="rev-k">referee · astrosage-70b</span><p>{html.escape(rv[:520])}</p></div>'

def card(r, big=False):
    im = img(r.get("figure"))
    imh = f'<img src="{im}" alt="{html.escape(r["title"])}" loading="lazy">' if im else '<div class="noimg">figure unavailable</div>'
    return f'''<article class="card{' big' if big else ''}">
      <div class="fig">{imh}</div>
      <div class="body">
        <h3>{html.escape(r["title"])}</h3>
        <p class="summ">{html.escape(r["summary"])}</p>
        {review_html(r)}
      </div>
    </article>'''

n_total = len(R)
n_dist = len([r for r in R if "bootstrap" not in r["title"].lower() and r["title"] != "Synthesis"])
n_boot = n_total - n_dist - 1
pdfs = len([f for f in os.listdir(D) if False])  # count paper pdfs
pdfs = len([1 for root, _, fs in os.walk(D) for f in fs if f == "draft.pdf"])

style = """
<style>
:root{--bg:#0a0d17;--panel:#111524;--line:#242a3d;--ink:#e8ecf5;--soft:#9aa3b8;--acc:#7c86ff;--acc2:#4ad6c4;--warn:#e0a458;
--sans:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--mono:ui-monospace,"SF Mono",Menlo,monospace;}
*{box-sizing:border-box}
body,.wrap{background:var(--bg);color:var(--ink);font-family:var(--sans);line-height:1.6}
.wrap{max-width:1080px;margin:0 auto;padding:0 1.25rem 4rem}
.hd{padding:3rem 0 1.5rem;border-bottom:1px solid var(--line)}
.eyebrow{font-family:var(--mono);font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:var(--acc2);margin:0 0 .8rem}
h1{font-size:clamp(1.7rem,4.5vw,2.6rem);font-weight:700;letter-spacing:-.02em;margin:0 0 .5rem;text-wrap:balance}
.lede{color:var(--soft);max-width:70ch;margin:0 0 1.4rem;font-size:1.02rem}
.stats{display:flex;flex-wrap:wrap;gap:.6rem}
.stat{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:.6rem .9rem;min-width:110px}
.stat b{display:block;font-family:var(--mono);font-size:1.15rem;color:var(--acc);font-variant-numeric:tabular-nums}
.stat span{font-size:.72rem;color:var(--soft);text-transform:uppercase;letter-spacing:.06em;font-family:var(--mono)}
.sec-k{font-family:var(--mono);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--soft);margin:2.4rem 0 1rem}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1rem}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;display:flex;flex-direction:column}
.card.big{grid-column:1/-1;flex-direction:row;flex-wrap:wrap}
.card.big .fig{flex:1 1 380px}
.card.big .body{flex:1 1 360px}
.fig{background:#0a0d17;display:flex;align-items:center;justify-content:center;border-bottom:1px solid var(--line)}
.card.big .fig{border-bottom:none;border-right:1px solid var(--line)}
.fig img{width:100%;height:auto;display:block}
.noimg{padding:3rem;color:var(--soft);font-family:var(--mono);font-size:.8rem}
.body{padding:1.1rem 1.2rem}
.body h3{font-size:1.02rem;font-weight:650;margin:0 0 .5rem;line-height:1.3}
.summ{font-size:.9rem;color:var(--ink);margin:0 0 .8rem;line-height:1.55}
.rev{border-top:1px dashed var(--line);padding-top:.7rem;margin-top:.3rem}
.rev-k{font-family:var(--mono);font-size:.64rem;letter-spacing:.08em;text-transform:uppercase;color:var(--acc2)}
.rev p{font-size:.82rem;color:var(--soft);margin:.35rem 0 0;line-height:1.5}
.foot{margin-top:2.6rem;padding:1.2rem;border:1px solid var(--warn);border-radius:12px;background:rgba(224,164,88,.07);color:var(--warn);font-size:.85rem;line-height:1.6}
.foot b{color:var(--ink)}
.meta{margin-top:1.4rem;color:var(--soft);font-size:.78rem;font-family:var(--mono)}
@media(prefers-color-scheme:light){:root{--bg:#0a0d17}} /* page commits to dark instrument look */
</style>
"""

hero_html = ""
if hero:
    hero_html = f'<p class="sec-k">Headline result</p>{card(hero, big=True)}'

parts = [style,
  '<div class="wrap">',
  '<header class="hd">',
  '<p class="eyebrow">NebulaMind Lab · overnight autonomous research</p>',
  '<h1>Scaling relations from three surveys we hadn’t used</h1>',
  '<p class="lede">A 7-hour unattended run over public data — GSWLC-2 (GALEX+WISE SFRs), COSMOS2020 (photometric masses to z≈5), and JWST/NIRSpec catalogs — computing the star-forming main sequence, stellar mass function, and mass–metallicity relation across cosmic time, each with a compiled figure and an automated referee review. Bounded, uncorrected, descriptive.</p>',
  f'<div class="stats"><div class="stat"><b>{n_total:,}</b><span>studies</span></div>'
  f'<div class="stat"><b>{n_dist}</b><span>distinct</span></div>'
  f'<div class="stat"><b>{n_boot:,}</b><span>bootstrap passes</span></div>'
  f'<div class="stat"><b>3</b><span>surveys</span></div>'
  f'<div class="stat"><b>{pdfs}</b><span>AASTeX PDFs</span></div>'
  f'<div class="stat"><b>7.0h</b><span>runtime</span></div></div>',
  '</header>',
  hero_html,
  '<p class="sec-k">Results</p>',
  '<div class="grid">'] + [card(r) for r in cards] + [
  '</div>',
  '<div class="foot"><b>Read these as first-pass, automated descriptive results — not validated measurements.</b> '
  'Stellar mass functions are uncorrected for completeness/V<sub>max</sub>; COSMOS masses/SFRs carry photometric-redshift scatter; '
  'the JWST MZR and SDSS anchor sit on their native abundance scales (not homogenised); a single default selection and calibration is used throughout. '
  'The referee notes above flag the main systematics.</div>',
  '<p class="meta">Generated from overnight-research-20260718/RESULTS.json · NebulaMind Lab autonomous runner</p>',
  '</div>']
open(os.path.join(D, "overnight_review.html"), "w").write("\n".join(parts))
print("wrote overnight_review.html;", len(cards), "cards; hero:", bool(hero), "; pdfs:", pdfs)
