#!/usr/bin/env python3
"""nm_report_graphics.py — real graphics for audio-report slides.

Duho, 2026-08-20, on seeing text-only slides: "i expected more like graphics,
such as real images when it mentions image data". So a slide that talks about
galaxy cutouts shows THE ACTUAL CUTOUTS from the run being described — not
decoration, not stock art, not a generated impression of a galaxy.

Run under the hermes venv python (numpy + PIL).

Honesty rules, same family as the deck's restate-only rule:
- Images are rendered from real data files on disk. If the data is absent, no
  graphic is produced — never a placeholder that looks like data.
- Every image carries a provenance line naming its source and count.
- Charts only plot numbers that already appear in the report text.
"""
from __future__ import annotations
import hashlib, json, pathlib, sys

CUTOUTS = pathlib.Path("/Users/duhokim/NebulaMindData/cutouts_dr10_south/tensors")
OUT = pathlib.Path("/Users/duhokim/HermesOps/reports/status-audio/graphics")
SIDE = 128


def _stretch(a):
    """asinh stretch on a robust range — how astronomers actually display sky."""
    import numpy as np
    lo = float(np.percentile(a, 25))
    hi = float(np.percentile(a, 99.7))
    if hi <= lo:
        hi = lo + 1e-6
    x = (a - lo) / (hi - lo)
    x = np.clip(x, 0, 1)
    x = np.arcsinh(x * 12.0) / np.arcsinh(12.0)
    return np.clip(x, 0, 1)


def cutout_grid(n: int = 12, cols: int = 6, seed_key: str = "") -> dict | None:
    """A grid of REAL galaxy cutouts from the live run. Deterministic per key."""
    import numpy as np
    from PIL import Image
    files = sorted(CUTOUTS.glob("object-*.f32le"))
    if len(files) < n:
        return None
    # deterministic pick so a rebuilt deck shows the same galaxies
    h = int(hashlib.sha256(seed_key.encode()).hexdigest()[:8], 16) if seed_key else 0
    step = max(1, len(files) // n)
    picked = [files[(h + i * step) % len(files)] for i in range(n)]
    rows = (n + cols - 1) // cols
    pad = 3
    canvas = Image.new("L", (cols * SIDE + (cols + 1) * pad, rows * SIDE + (rows + 1) * pad), 8)
    for i, f in enumerate(picked):
        a = np.fromfile(f, dtype="<f4")
        if a.size != SIDE * SIDE:
            continue
        img = Image.fromarray((_stretch(a.reshape(SIDE, SIDE)) * 255).astype("uint8"), "L")
        r, c = divmod(i, cols)
        canvas.paste(img, (pad + c * (SIDE + pad), pad + r * (SIDE + pad)))
    OUT.mkdir(parents=True, exist_ok=True)
    name = f"cutgrid_{n}_{abs(h) % 10000}.png"
    canvas.convert("RGB").save(OUT / name, optimize=True)
    return {"img": f"graphics/{name}",
            "attr": f"{n} real r-band cutouts from this run's {len(files):,} verified tensors "
                    f"(DECaLS DR10 south, 128×128, asinh stretch)"}


def single_cutout(seed_key: str = "") -> dict | None:
    import numpy as np
    from PIL import Image
    files = sorted(CUTOUTS.glob("object-*.f32le"))
    if not files:
        return None
    h = int(hashlib.sha256(seed_key.encode()).hexdigest()[:8], 16) if seed_key else 0
    f = files[h % len(files)]
    a = np.fromfile(f, dtype="<f4")
    if a.size != SIDE * SIDE:
        return None
    img = Image.fromarray((_stretch(a.reshape(SIDE, SIDE)) * 255).astype("uint8"), "L")
    img = img.resize((SIDE * 3, SIDE * 3), Image.LANCZOS)
    OUT.mkdir(parents=True, exist_ok=True)
    name = f"cutout_{f.stem[-12:]}.png"
    img.convert("RGB").save(OUT / name, optimize=True)
    return {"img": f"graphics/{name}",
            "attr": f"real cutout {f.stem} — one of {len(files):,} verified this run"}


def progress_svg(done: float, total: float, label: str, unit: str = "") -> dict:
    """Inline SVG bar. Both numbers must come from the report text."""
    pct = 0 if not total else max(0.0, min(1.0, done / total))
    w, h = 520, 54
    fill = int(pct * (w - 4))
    return {"svg": (
        f'<svg viewBox="0 0 {w} {h}" width="100%" role="img" aria-label="{label}">'
        f'<rect x="0" y="18" width="{w}" height="18" rx="9" fill="#1b212b"/>'
        f'<rect x="2" y="20" width="{fill}" height="14" rx="7" fill="#59d8ff"/>'
        f'<text x="0" y="12" fill="#8b93a1" font-size="12" font-family="system-ui">{label}</text>'
        f'<text x="{w}" y="12" text-anchor="end" fill="#ffc46b" font-size="12" '
        f'font-family="system-ui" font-weight="600">{done:,.0f}{unit} / {total:,.0f}{unit}</text>'
        f'</svg>')}


def badge_svg(items: list[tuple[str, bool]]) -> dict:
    """Pass/fail chips — one per claim the audio actually made."""
    parts, x = [], 0
    for text, ok in items[:4]:
        wid = 14 + len(text) * 7.4
        col, fg = ("#173a26", "#7ee6a8") if ok else ("#3a1717", "#ff8ba0")
        parts.append(f'<rect x="{x}" y="0" width="{wid:.0f}" height="30" rx="15" fill="{col}"/>'
                     f'<text x="{x + wid/2:.0f}" y="20" text-anchor="middle" fill="{fg}" '
                     f'font-size="13" font-family="system-ui" font-weight="600">{text}</text>')
        x += wid + 8
    return {"svg": f'<svg viewBox="0 0 {max(x,1):.0f} 30" width="100%" role="img">{"".join(parts)}</svg>'}


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "grid"
    if what == "grid":
        print(json.dumps(cutout_grid(12, 6, "demo")))
    elif what == "one":
        print(json.dumps(single_cutout("demo")))


# ---------------------------------------------------------------------------
# DESI campaign graphics (2026-08-20). Built to Hwao's spec; the constraints
# below are HIS, and each exists because a graphic can mislead more efficiently
# than a sentence can. DESI_GRAPHICS_ANSWER_20260820.md has his reasoning.
# ---------------------------------------------------------------------------
RECEIPTS = pathlib.Path("/Users/duhokim/NebulaMindData/dr10_south_image_r/receipts.jsonl")
POSITIONS = pathlib.Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
                         "weekend-video-sextet-20260808T0136K/prereg/_positions_20260820/"
                         "positions_runner_view.csv")
WORKING_SET_BRICKS = 60308   # campaign_binding.json exact_file_count
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial.ttf"


def _font(size):
    from PIL import ImageFont
    try:
        return ImageFont.truetype(FONT_PATH, size)
    except Exception:
        return ImageFont.load_default()


def brick_to_radec(name: str):
    """0001m395 -> (RA 000.1, Dec -39.5). Position is IN the name; no sidecar."""
    try:
        ra = int(name[:4]) / 10.0
        sign = -1.0 if name[4].lower() == "m" else 1.0
        dec = sign * int(name[5:8]) / 10.0
        return ra, dec
    except Exception:
        return None


def read_receipts():
    """(accepted [(ra,dec,utc)], outcome counts, retried count, last utc)."""
    import json as _j
    accepted, outcomes, retried, last = [], {}, 0, None
    if not RECEIPTS.exists():
        return accepted, outcomes, retried, last
    for line in RECEIPTS.open(errors="replace"):
        try:
            d = _j.loads(line)
        except Exception:
            continue
        o = d.get("outcome", "?")
        outcomes[o] = outcomes.get(o, 0) + 1
        if (d.get("retry_count") or 0) > 0:
            retried += 1
        if o == "ACCEPTED":
            p = brick_to_radec(str(d.get("brickname", "")))
            if p:
                accepted.append((p[0], p[1], d.get("utc")))
            if d.get("utc"):
                last = d["utc"]
    return accepted, outcomes, retried, last


def sky_map(seed_key: str = "") -> dict | None:
    """Accepted bricks in RA/Dec over the parent-galaxy sky the sample needs.

    Hwao's traps, all addressed on the image itself:
      - it is NOT survey coverage: the backdrop is our 208,407 parent galaxies,
        and the caption says so;
      - the transfer walks bricks in RA order, so partial progress is a wedge
        that reads as a missing region — labelled as ordering, not a gap;
      - one brick != one galaxy, so brick coverage != sample completeness;
      - count and timestamp are burned in, so a screenshot cannot age silently.
    """
    import numpy as np
    from PIL import Image, ImageDraw
    accepted, _, _, last_utc = read_receipts()
    if not accepted:
        return None
    W, H = 900, 470
    PAD_L, PAD_B, PAD_T = 52, 46, 40
    plot_w, plot_h = W - PAD_L - 16, H - PAD_B - PAD_T

    # backdrop: where the parent galaxies are (the sky this study actually needs)
    dens = np.zeros((plot_h, plot_w), dtype="f4")
    ra_lo, ra_hi, dec_lo, dec_hi = 0.0, 360.0, -90.0, 40.0
    if POSITIONS.exists():
        import csv
        with POSITIONS.open() as f:
            for row in csv.DictReader(f):
                try:
                    ra, dec = float(row["ra"]), float(row["dec"])
                except Exception:
                    continue
                x = int((ra - ra_lo) / (ra_hi - ra_lo) * (plot_w - 1))
                y = int((dec_hi - dec) / (dec_hi - dec_lo) * (plot_h - 1))
                if 0 <= x < plot_w and 0 <= y < plot_h:
                    dens[y, x] += 1
    if dens.max() > 0:
        d = np.log1p(dens) / np.log1p(dens.max())
        back = (d * 135).astype("uint8")
    else:
        back = np.zeros((plot_h, plot_w), dtype="uint8")

    img = Image.new("RGB", (W, H), (12, 18, 40))
    plot = Image.merge("RGB", [Image.fromarray((back * 0.45).astype("uint8")),
                               Image.fromarray((back * 0.62).astype("uint8")),
                               Image.fromarray(back)])
    img.paste(plot, (PAD_L, PAD_T))
    dr = ImageDraw.Draw(img)

    for ra, dec, _ in accepted:
        x = PAD_L + int((ra - ra_lo) / (ra_hi - ra_lo) * (plot_w - 1))
        y = PAD_T + int((dec_hi - dec) / (dec_hi - dec_lo) * (plot_h - 1))
        dr.rectangle([x, y, x + 1, y + 1], fill=(89, 216, 255))

    # The transfer walks the manifest in RA order, so the leading edge is a
    # vertical front. Unlabelled it reads as "this region is missing"; Hwao
    # flagged it as the likeliest misreading, so it is named ON the image.
    ra_front = max(r for r, _, _ in accepted)
    xf = PAD_L + int((ra_front - ra_lo) / (ra_hi - ra_lo) * (plot_w - 1))
    for yy in range(PAD_T, PAD_T + plot_h, 6):
        dr.line([xf, yy, xf, yy + 3], fill=(255, 196, 107))
    dr.text((min(xf + 6, W - 210), PAD_T + 6), "transfer front — bricks are",
            font=_font(11), fill=(255, 196, 107))
    dr.text((min(xf + 6, W - 210), PAD_T + 20), "fetched in RA order, not skipped",
            font=_font(11), fill=(255, 196, 107))

    dr.rectangle([PAD_L, PAD_T, PAD_L + plot_w, PAD_T + plot_h], outline=(50, 62, 95))
    f9, f10, f12 = _font(11), _font(12), _font(15)
    for ra in range(0, 361, 60):
        x = PAD_L + int((ra - ra_lo) / (ra_hi - ra_lo) * (plot_w - 1))
        dr.line([x, PAD_T + plot_h, x, PAD_T + plot_h + 4], fill=(90, 104, 140))
        dr.text((x - 10, PAD_T + plot_h + 7), f"{ra}°", font=f9, fill=(139, 147, 161))
    for dec in range(-90, 41, 30):
        y = PAD_T + int((dec_hi - dec) / (dec_hi - dec_lo) * (plot_h - 1))
        dr.line([PAD_L - 4, y, PAD_L, y], fill=(90, 104, 140))
        dr.text((6, y - 7), f"{dec:+d}°", font=f9, fill=(139, 147, 161))
    dr.text((PAD_L, 10), "Bricks in hand, over the sky our sample needs",
            font=f12, fill=(238, 241, 251))
    dr.text((PAD_L, H - 30), "RA →   ·   blue haze = 208,407 parent galaxies   ·   "
                             "cyan = bricks accepted", font=f9, fill=(139, 147, 161))
    # Hwao, verified against all 208,407 positions (dec -89.6 to -39.4, median
    # -56.5): the empty north is the frozen selection, not absent data. Without
    # this line the black 82% reads as "we are missing most of the sky".
    dr.text((PAD_L, H - 16), "Parent sample is a frozen southern cap (BRICKID 1–121000); "
                             "the empty north is out of scope by design, not missing.",
            font=f9, fill=(255, 196, 107))
    stamp = (last_utc or "").replace("T", " ").replace("Z", " UTC")
    dr.text((W - 300, 12), f"{len(accepted):,} of {WORKING_SET_BRICKS:,} bricks · {stamp}",
            font=f9, fill=(255, 196, 107))

    OUT.mkdir(parents=True, exist_ok=True)
    name = f"skymap_{len(accepted)}.png"
    img.save(OUT / name, optimize=True)
    return {"img": f"graphics/{name}",
            "attr": f"{len(accepted):,} of {WORKING_SET_BRICKS:,} working-set bricks accepted as of "
                    f"{stamp}. NOT survey sky coverage — the backdrop is the 208,407 galaxies this "
                    f"study needs. The transfer walks bricks in RA order, so the leading edge is "
                    f"ordering, not a missing region; and one brick is not one galaxy, so brick "
                    f"coverage is not sample completeness. The parent sample is a frozen "
                    f"southern cap (BRICKID 1–121000, dec −89.6 to −39.4, median −56.5) — the "
                    f"empty north is out of scope by design, not missing data. A single cap can "
                    f"still constrain a dipole: count-weighted var(cos θ) = 0.445201 against a "
                    f"required 0.15 (TORI_FOOTPRINT_VARIANCE_RECEIPT.md)."}


def failure_strip() -> dict | None:
    """Outcome counts INCLUDING the zeros. An absent panel is not information."""
    _, outcomes, retried, last_utc = read_receipts()
    if not outcomes:
        return None
    quarantined = outcomes.get("QUARANTINED", 0)
    accepted = outcomes.get("ACCEPTED", 0)
    retry_sched = outcomes.get("TRANSIENT_RETRY_SCHEDULED", 0)
    items = [(f"{accepted:,} accepted", True),
             (f"{retry_sched} transient retry", retry_sched == 0),
             (f"{quarantined} quarantined", quarantined == 0)]
    g = badge_svg(items)
    stamp = (last_utc or "").replace("T", " ").replace("Z", " UTC")
    g["attr"] = (f"No digest mismatch so far — {quarantined} quarantined, {retried} object(s) "
                 f"retried, as of {stamp}. Zero quarantined means the digest check has not fired "
                 f"yet, not that the data is verified perfect.")
    return g


def throughput(hours: int = 24) -> dict | None:
    """Bricks per hour from receipt timestamps — the real history.

    Shows the window structure honestly: the transfer sleeps by frozen rule, so
    a flat stretch is compliance, not a stall. Prints no ETA (Hwao: an ETA from
    a running-window rate is wildly early, so give none).
    """
    import datetime as _dt
    accepted, _, _, last_utc = read_receipts()
    if not accepted:
        return None
    KST = _dt.timezone(_dt.timedelta(hours=9))
    buckets = {}
    for _, _, utc in accepted:
        if not utc:
            continue
        try:
            t = _dt.datetime.strptime(utc, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=_dt.timezone.utc)
        except Exception:
            continue
        buckets[t.astimezone(KST).strftime("%m-%d %H")] = \
            buckets.get(t.astimezone(KST).strftime("%m-%d %H"), 0) + 1
    if not buckets:
        return None
    keys = sorted(buckets)[-hours:]
    vals = [buckets[k] for k in keys]
    peak = max(vals) or 1
    w, h, bw = 520, 96, max(3, min(18, 500 // max(1, len(keys))))
    bars = []
    for i, v in enumerate(vals):
        bh = int((v / peak) * 62)
        x = 4 + i * bw
        col = "#59d8ff" if v else "#2a3550"      # an empty hour is the window rule, not a stall
        bars.append(f'<rect x="{x}" y="{70 - bh}" width="{bw - 2}" height="{max(bh,2)}" '
                    f'rx="2" fill="{col}"/>')
    label = f"{keys[0]} → {keys[-1]} KST · peak {peak:,}/h"
    return {"svg": (
        f'<svg viewBox="0 0 {w} {h}" width="100%" role="img" aria-label="bricks per hour">'
        f'<text x="0" y="12" fill="#8b93a1" font-size="12" font-family="system-ui">'
        f'bricks accepted per hour</text>{"".join(bars)}'
        f'<text x="0" y="88" fill="#8b93a1" font-size="11" font-family="system-ui">{label}'
        f'</text></svg>'),
        "attr": "Flat hours are the frozen transfer window (the campaign sleeps by rule), "
                "not a stall. No ETA is shown: projecting from a running-window rate lands "
                "wildly early."}


CUTOUT_DIR = pathlib.Path("/Users/duhokim/NebulaMindData/cutouts_dr10_south")
CHI_RESULTS = pathlib.Path("/Users/duhokim/NebulaMindData/chi_dr10_south/results.jsonl")
PARENT_TOTAL = 208407


def pipeline_chain() -> dict | None:
    """Where the sample is, stage by stage, and where it is piling up.

    Hwao's rule: most galaxies are WAITING ON BRICKS, which is the design
    working, not a failure — so the gap is labelled that way and never as
    "failed". COUNTS ONLY: results.jsonl carries chi_value and committee_state,
    and the measurement is blinded until the sample is complete, so nothing
    here may hint at the distribution.
    """
    import json as _j
    try:
        hb = _j.loads((RECEIPTS.parent / "heartbeat.json").read_text())
    except Exception:
        hb = {}
    bricks_ok, bricks_total = hb.get("accepted", 0), hb.get("total", WORKING_SET_BRICKS)
    try:
        wrap = _j.loads((CUTOUT_DIR / "wrapper_heartbeat.json").read_text())
    except Exception:
        wrap = {}
    ready = int(wrap.get("ready") or 0)
    tensors = len(list((CUTOUT_DIR / "tensors").glob("object-*.f32le"))) \
        if (CUTOUT_DIR / "tensors").exists() else 0
    measured = sum(1 for _ in CHI_RESULTS.open()) if CHI_RESULTS.exists() else 0
    stamp = (wrap.get("utc") or "").replace("T", " ").replace("Z", " UTC")

    stages = [("parent sample", f"{PARENT_TOTAL:,}", "galaxies"),
              ("bricks in hand", f"{bricks_ok:,}/{bricks_total:,}", "bricks"),
              ("ready to cut", f"{ready:,}", "galaxies"),
              ("cut", f"{tensors:,}", "galaxies"),
              ("measured", f"{measured:,}", "galaxies")]
    w, h, bw, gap = 620, 132, 104, 24
    parts = []
    for i, (label, value, unit) in enumerate(stages):
        x = i * (bw + gap)
        if x + bw > w:
            break
        parts.append(
            f'<rect x="{x}" y="26" width="{bw}" height="52" rx="9" fill="#141c33" stroke="#2a3550"/>'
            f'<text x="{x + bw/2:.0f}" y="20" text-anchor="middle" fill="#8b93a1" font-size="11" '
            f'font-family="system-ui">{label}</text>'
            f'<text x="{x + bw/2:.0f}" y="52" text-anchor="middle" fill="#ffc46b" font-size="15" '
            f'font-family="system-ui" font-weight="600">{value}</text>'
            f'<text x="{x + bw/2:.0f}" y="68" text-anchor="middle" fill="#78818f" font-size="10" '
            f'font-family="system-ui">{unit}</text>')
        if i < len(stages) - 1 and x + bw + gap < w:
            parts.append(f'<path d="M{x + bw + 4} 52 L{x + bw + gap - 6} 52" stroke="#59d8ff" '
                         f'stroke-width="1.5" fill="none" marker-end="url(#ar)"/>')
    waiting = max(0, PARENT_TOTAL - ready)
    queued = max(0, ready - tensors)
    parts.append(
        f'<text x="0" y="98" fill="#8b93a1" font-size="11" font-family="system-ui">'
        f'<tspan fill="#59d8ff">{waiting:,}</tspan> waiting on bricks — the design working, not a '
        f'failure   ·   <tspan fill="#59d8ff">{queued:,}</tspan> queued for the cutter</text>'
        f'<text x="0" y="118" fill="#78818f" font-size="10" font-family="system-ui">'
        f'counts only — the measurement stays blinded until the sample is complete · {stamp}</text>')
    return {"svg": (
        f'<svg viewBox="0 0 {w} {h}" width="100%" role="img" aria-label="pipeline stages">'
        f'<defs><marker id="ar" viewBox="0 0 8 8" refX="6" refY="4" markerWidth="5" '
        f'markerHeight="5" orient="auto"><path d="M0 1 L6 4 L0 7 z" fill="#59d8ff"/></marker></defs>'
        f'{"".join(parts)}</svg>'),
        "attr": f"Stage counts as of {stamp}. Galaxies waiting on bricks are waiting by design — a "
                f"brick they need has not arrived yet. Counts only: no chirality value or committee "
                f"state is shown, and none may be until the sample is complete and the labels are in."}
