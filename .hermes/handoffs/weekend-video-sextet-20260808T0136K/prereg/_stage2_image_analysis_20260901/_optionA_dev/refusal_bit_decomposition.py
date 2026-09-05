#!/usr/bin/env python3
"""OPTION (A) CHARACTERISATION — which maskbits drive the 159 pixel-decided §9B refusals, and what the
48 coverage refusals look like. Reads ONLY validation bricks already on disk (sealed-manifest verified),
re-renders the refused rasters with the pinned components, and records per-bit flagged-output-pixel counts.
It never reads a frozen-sample pixel, never reads GZ1 labels, and writes no score. Output has no `g`.
"""
import sys, json, csv, time
from pathlib import Path
import numpy as np
LANE = Path(__file__).resolve().parent.parent
import os; os.chdir(LANE); sys.path.insert(0, "."); sys.path.insert(0, "miniprereg_pins")
from astropy.io import fits
from astropy.wcs import WCS
import validation_resolver as vr, protected_region as pr
from study_renderer import pixel_rejection as prj
from study_renderer.renderer_v3 import render_cutout, RenderTarget
BR = LANE / "validation_bricks"; OUT = LANE / "_optionA_dev" / "refusal_bit_decomposition_20260905.jsonl"
def utc(): return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
manifest = vr.load_manifest()
refused = {}
for l in open("validation_render_journal_20260905.jsonl"):
    r = json.loads(l)
    if r.get("status") == "REFUSED" and r.get("brick") not in (None, "UNRESOLVED") and "NO-" not in r.get("reason", ""):
        refused[r["gz1_objid"]] = r["reason"]
sel = {row["GZ1_OBJID"]: row for row in csv.DictReader(open("VALIDATION_SELECTION_V29_20260905.csv"))}
print(utc(), "pixel-decided refusals to decompose:", len(refused), flush=True)
cache = {}
def load_brick(b):
    if b in cache: return cache[b]
    planes = {}
    for plane in ("image-r", "maskbits", "nexp-r"):
        p = BR / b / f"legacysurvey-{b}-{plane}.fits.fz"
        if vr.verify_plane(p, b, plane, manifest) != "OK": raise ValueError("PLANE-NOT-VERIFIED:" + plane)
        planes[plane] = p
    img_h = fits.open(planes["image-r"]); image = np.asarray(img_h[1].data, dtype=np.float64); wcs = WCS(img_h[1].header)
    mb_h = fits.open(planes["maskbits"]); mb_hdu = [x for x in mb_h if x.header.get("EXTNAME") == "MASKBITS"][0]
    maskbits = np.asarray(mb_hdu.data).astype(np.int32)
    nexp = np.asarray(fits.open(planes["nexp-r"])[1].data).astype(np.int32)
    cleaned, fill, n_rej = prj.clean_source(image, maskbits)
    cache[b] = (cleaned, maskbits, nexp, wcs)
    if len(cache) > 4: cache.pop(next(iter(cache)))
    return cache[b]
yy, xx = np.mgrid[0:128, 0:128]; rr = np.hypot(xx - 63.5, yy - 63.5)
ALT = {"drop11": (1, 3, 6, 10, 13), "drop11_13": (1, 3, 6, 10), "drop6": (1, 3, 10, 11, 13), "drop6_11": (1, 3, 10, 13), "drop6_11_13": (1, 3, 10), "only1_3_10": (1, 3, 10)}
done = 0
with OUT.open("w") as fh:
    for oid, reason in refused.items():
        row = sel[oid]; b = row["DR9N_BRICK"]; rec = {"gz1_objid": oid, "brick": b, "reason": reason}
        try:
            cleaned, maskbits, nexp, wcs = load_brick(b)
            ras = render_cutout([(cleaned, maskbits, nexp, wcs)], RenderTarget(ra=float(row["RA"]), dec=float(row["DEC"]), primary_tile_id=b))
            mb = np.asarray(ras.maskbits).astype(np.int64); ne = np.asarray(ras.nexp)
            rec["nexp_zero_pixels"] = int((ne <= 0).sum())
            if (ne <= 0).any(): rec["nexp_zero_min_r_px"] = float(rr[ne <= 0].min())
            rec["per_bit_flagged"] = {str(bit): int(((mb >> bit) & 1).sum()) for bit in range(0, 16)}
            F = int((((mb & prj.REJECT_MASK) != 0)).sum()); rec["F"] = F
            alts = {}
            for name, bits in ALT.items():
                m = 0
                for bit in bits: m |= (1 << bit)
                fl = (mb & m) != 0; Fa = int(fl.sum())
                alts[name] = {"F": Fa, "ceiling_ok": Fa <= 819, "protected_ok": not bool(fl[rr <= 23.0].any())}
            rec["alternatives"] = alts
            # dominant single bit among rejecting bits
            rec["dominant_bit"] = max(prj.REJECT_BITS, key=lambda bit: rec["per_bit_flagged"][str(bit)])
        except Exception as e:
            rec["error"] = repr(e)[:200]
        fh.write(json.dumps(rec, sort_keys=True) + "\n"); fh.flush(); done += 1
        if done % 20 == 0: print(utc(), done, "/", len(refused), flush=True)
print(utc(), "DONE", done, flush=True)
