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
