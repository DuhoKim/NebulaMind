#!/usr/bin/env python3
"""OPTION (A) CHARACTERISATION, part 2 — the 48 §8.12 coverage refusals. The pinned renderer raises before
returning a raster when any output pixel has nexp-r <= 0, so this script samples nexp and maskbits itself by the
SAME nearest-neighbour rule as renderer_v3._sample_stitched (rint of all_world2pix on the single source brick) and
records: count of nexp==0 output pixels, their minimum radius from the raster centre, per-bit flagged counts, and
what the raster would meet under alternative rules IF nexp==0 pixels were treated as FLAGGED contamination.
No labels, no frozen pixels. Approximate only in that it re-implements the sampling; it does not call the renderer.
"""
import sys, json, csv, time, os
from pathlib import Path
import numpy as np
LANE = Path(__file__).resolve().parent.parent; os.chdir(LANE); sys.path.insert(0, "."); sys.path.insert(0, "miniprereg_pins")
from astropy.io import fits
from astropy.wcs import WCS
import validation_resolver as vr
from study_renderer import pixel_rejection as prj
from study_renderer import renderer_v3 as rv
BR = LANE / "validation_bricks"; OUT = LANE / "_optionA_dev" / "coverage_refusal_geometry_20260905.jsonl"
manifest = vr.load_manifest()
refused = {}
for l in open("validation_render_journal_20260905.jsonl"):
    r = json.loads(l)
    if r.get("status") == "REFUSED" and r.get("reason") == "REFUSED:DATA-INTEGRITY-FAIL": refused[r["gz1_objid"]] = r["brick"]
sel = {row["GZ1_OBJID"]: row for row in csv.DictReader(open("VALIDATION_SELECTION_V29_20260905.csv"))}
print("coverage refusals:", len(refused), flush=True)
yy, xx = np.mgrid[0:rv.HEIGHT, 0:rv.WIDTH]; rr = np.hypot(xx - (rv.WIDTH-1)/2, yy - (rv.HEIGHT-1)/2)
ALT = {"as_is": (1,3,6,10,11,13), "drop11": (1,3,6,10,13)}
def load(b):
    planes = {}
    for plane in ("maskbits", "nexp-r"):
        p = BR / b / f"legacysurvey-{b}-{plane}.fits.fz"
        if vr.verify_plane(p, b, plane, manifest) != "OK": raise ValueError("PLANE-NOT-VERIFIED:" + plane)
        planes[plane] = p
    mb_h = fits.open(planes["maskbits"]); mb_hdu = [x for x in mb_h if x.header.get("EXTNAME") == "MASKBITS"][0]
    return np.asarray(mb_hdu.data).astype(np.int64), np.asarray(fits.open(planes["nexp-r"])[1].data).astype(np.int64), WCS(mb_hdu.header)
with OUT.open("w") as fh:
    for oid, b in refused.items():
        row = sel[oid]; rec = {"gz1_objid": oid, "brick": b}
        try:
            mb_src, ne_src, wcs = load(b)
            ow = rv._output_wcs(float(row["RA"]), float(row["DEC"]))
            world = ow.all_pix2world(np.column_stack([xx.ravel(), yy.ravel()]), 0)
            xy = wcs.all_world2pix(world, 0); ix = np.rint(xy[:, 0]).astype(int); iy = np.rint(xy[:, 1]).astype(int)
            inside = (ix >= 0) & (ix < mb_src.shape[1]) & (iy >= 0) & (iy < mb_src.shape[0])
            rec["outside_brick_pixels"] = int((~inside).sum())
            ne = np.zeros(ix.shape, dtype=np.int64); mb = np.zeros(ix.shape, dtype=np.int64)
            ne[inside] = ne_src[iy[inside], ix[inside]]; mb[inside] = mb_src[iy[inside], ix[inside]]
            ne = ne.reshape(rv.HEIGHT, rv.WIDTH); mb = mb.reshape(rv.HEIGHT, rv.WIDTH)
            z = ne <= 0; rec["nexp_zero_pixels"] = int(z.sum()); rec["nexp_zero_min_r_px"] = float(rr[z].min()) if z.any() else None
            rec["nexp_zero_inside_r23"] = int((z & (rr <= 23.0)).sum())
            rec["per_bit_flagged"] = {str(bit): int(((mb >> bit) & 1).sum()) for bit in (0,1,3,6,10,11,12,13)}
            alts = {}
            for name, bits in ALT.items():
                m = 0
                for bit in bits: m |= (1 << bit)
                fl = ((mb & m) != 0) | z          # nexp==0 treated as contamination
                alts[name + "+nexp_as_flag"] = {"F": int(fl.sum()), "ceiling_ok": bool(fl.sum() <= 819), "protected_ok": not bool(fl[rr <= 23.0].any())}
            rec["alternatives"] = alts
        except Exception as e:
            rec["error"] = repr(e)[:200]
        fh.write(json.dumps(rec, sort_keys=True) + "\n"); fh.flush()
print("DONE", flush=True)
