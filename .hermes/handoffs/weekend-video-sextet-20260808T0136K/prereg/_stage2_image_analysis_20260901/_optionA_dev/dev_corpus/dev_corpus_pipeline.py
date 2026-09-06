#!/usr/bin/env python3
"""DEVELOPMENT-CORPUS ADAPTER (option A run sequence, gap 2; V15 §3a/§7/E5(b), Tier-C §9B.2a–c discipline, V38 pipeline identity).
Three closed modes over the SEALED corpus identity, for the tuning (400) and holdout (200) objects ONLY — never the fresh 2,000:
  manifest  identity + pool + pinned brick tables → dev_bricks.txt (sorted unique bricks) and dev_checksum_manifest.txt built from each
            brick's PUBLISHED checksum file at the pinned DR9-north URL pattern; receipt with digests. No pixel is touched.
  fetch     the three planes per brick, each verified ONLY against the sealed manifest (never a run-time checksum); mismatch → quarantined;
            resumable; every attempt journalled; a lock refuses concurrent fetchers.
  render    each identity object in identity order through render_chain_v3.render_object under r_T = 23 (V15 §6: the development
            objects are GZ1 objects with no catalogue size — the validation constant, stated); SCORED → <objid>.ic6; REFUSED → the
            canonical SENTINEL tensor (run_configurations_v2.SENTINEL_TENSOR) and the refusal journalled with its cause; the driver
            manifest <GROUP>.csv (objid,g,tensor_sha256) in identity order; a READ MANIFEST of every file opened (E5(b)).
Network access is a callable (`fetch(url) -> bytes`) so tests inject one; production uses urllib. Standard library + numpy + astropy."""
from __future__ import annotations
import csv, hashlib, json, os, sys, time, fcntl
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent; LANE = HERE.parents[1]
for p in (LANE, LANE / "miniprereg_pins", HERE.parent / "fourier_chirality"): sys.path.insert(0, str(p))
from study_renderer import render_chain_v3 as rc
import protected_region_v2 as pr
import run_configurations_v2 as drv

BASE = "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr9/north/coadd"
PLANES = ("image-r", "maskbits", "nexp-r")
R_T_DEV = float(pr.r_t_validation())          # 23.0 — V15 §6; no catalogue size for GZ1 development objects

def utc(): return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
def sha(p: Path):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""): h.update(c)
    return h.hexdigest()
def jrow(journal: Path, d: dict):
    with journal.open("a") as fh: fh.write(json.dumps(d, sort_keys=True, separators=(",", ":")) + "\n")
def checksum_url(b): return f"{BASE}/{b[:3]}/{b}/legacysurvey_dr9_north_coadd_{b[:3]}_{b}.sha256sum"
def plane_url(b, plane): return f"{BASE}/{b[:3]}/{b}/legacysurvey-{b}-{plane}.fits.fz"
def plane_name(b, plane): return f"legacysurvey-{b}-{plane}.fits.fz"

def load_identity(path: Path) -> dict:
    I = json.loads(Path(path).read_text())
    if I.get("schema_version") != "CORPUS-IDENTITY-2": raise SystemExit("IDENTITY-SCHEMA")
    return I

def dev_objects(I: dict, group: str):
    """(objid, brick) pairs for 'tuning' or 'holdout' in identity order — the fresh set is REFUSED by name."""
    if group not in ("tuning", "holdout"): raise SystemExit(f"GROUP-REFUSED: {group!r} is not a development group")
    d = I["detail"][group]; return list(zip([int(x) for x in d["objids"]], d["bricks"]))

def load_pool(pool: Path) -> dict:
    return {int(r["GZ1_OBJID"]): (float(r["RA"]), float(r["DEC"]), int(r["G"])) for r in csv.DictReader(open(pool, newline=""))}

def manifest(identity: Path, pool: Path, no_r: Path, out: Path, fetch) -> dict:
    I = load_identity(identity); out.mkdir(parents=True, exist_ok=True); P = load_pool(pool)
    nor = {l.strip() for l in open(no_r) if l.strip()}
    objs = dev_objects(I, "tuning") + dev_objects(I, "holdout")
    for oid, b in objs:
        if oid not in P: raise SystemExit(f"OBJID-NOT-IN-POOL {oid}")
        if b in ("UNRESOLVED", "", None): raise SystemExit(f"BRICK-UNRESOLVED {oid}")
        if b in nor: raise SystemExit(f"BRICK-NO-R {b} for {oid}")
    bricks = sorted({b for _, b in objs})
    (out / "dev_bricks.txt").write_text("\n".join(bricks) + "\n")
    lines = []; missing = []
    for b in bricks:
        try: body = fetch(checksum_url(b)).decode("utf-8")
        except Exception as e: missing.append({"brick": b, "error": repr(e)[:120]}); continue
        for l in body.splitlines():
            parts = l.split()
            if len(parts) >= 2: lines.append(f"{parts[0]}  {parts[1].lstrip('*')}")
    (out / "dev_checksum_manifest.txt").write_text("\n".join(lines) + "\n")
    rec = {"schema": "DEV-MANIFEST-RECEIPT-1", "utc": utc(), "identity_sha256": sha(identity), "pool_sha256": sha(pool), "bricks": len(bricks), "objects": len(objs), "checksum_lines": len(lines),
           "bricks_without_checksum_file": missing, "manifest_sha256": sha(out / "dev_checksum_manifest.txt"), "bricks_sha256": sha(out / "dev_bricks.txt"), "url_pattern": checksum_url("<brick>"), "r_T_dev": R_T_DEV}
    (out / "dev_manifest_receipt.json").write_text(json.dumps(rec, sort_keys=True, indent=1) + "\n")
    return rec

def load_manifest(path: Path, expected_sha256: str) -> dict:
    if sha(path) != expected_sha256: raise SystemExit("DATA-INTEGRITY-FAIL: sealed dev checksum manifest digest mismatch")
    out = {}
    for l in path.read_text().splitlines():
        parts = l.split()
        if len(parts) >= 2: out[parts[1]] = parts[0]
    return out

def fetch_bricks(bricks_txt: Path, manifest_path: Path, manifest_sha256: str, out: Path, journal: Path, fetch, lock_dir: Path) -> dict:
    M = load_manifest(manifest_path, manifest_sha256); out.mkdir(parents=True, exist_ok=True); lock_dir.mkdir(parents=True, exist_ok=True)
    lk = open(lock_dir / ".dev_fetch.lock", "w")
    try: fcntl.flock(lk, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError: raise SystemExit("REFUSED: another fetcher holds the lock")
    bricks = [l.strip() for l in open(bricks_txt) if l.strip()]
    jrow(journal, {"utc": utc(), "event": "fetch-start", "bricks": len(bricks), "sealed_manifest_sha256": manifest_sha256, "verification": "against sealed manifest only"})
    ok = bad = 0
    for b in bricks:
        for plane in PLANES:
            f = plane_name(b, plane); exp = M.get(f); dst = out / b / f
            if exp is None: jrow(journal, {"brick": b, "plane": plane, "verdict": "NO-PUBLISHED-SHA", "utc": utc()}); bad += 1; continue
            if dst.exists() and sha(dst) == exp: jrow(journal, {"brick": b, "plane": plane, "verdict": "OK", "resumed": True, "utc": utc()}); ok += 1; continue
            dst.parent.mkdir(parents=True, exist_ok=True); t0 = utc()
            try: body = fetch(plane_url(b, plane))
            except Exception as e: jrow(journal, {"brick": b, "plane": plane, "verdict": "FETCH-FAILED", "reason": repr(e)[:120], "utc": t0}); bad += 1; continue
            dst.write_bytes(body); got = sha(dst)
            if got != exp: dst.rename(dst.with_suffix(dst.suffix + ".QUARANTINE")); jrow(journal, {"brick": b, "plane": plane, "verdict": "SHA-MISMATCH-QUARANTINED", "computed_sha256": got, "sealed_sha256": exp, "utc": t0}); bad += 1; continue
            jrow(journal, {"brick": b, "plane": plane, "verdict": "OK", "bytes": len(body), "computed_sha256": got, "utc": t0}); ok += 1
    jrow(journal, {"utc": utc(), "event": "fetch-end", "ok": ok, "non_ok": bad}); return {"ok": ok, "non_ok": bad}

def _open_planes(bricks_dir: Path, b: str, M: dict, read_manifest: list):
    from astropy.io import fits
    from astropy.wcs import WCS
    planes = {}
    for plane in PLANES:
        p = bricks_dir / b / plane_name(b, plane)
        if not p.exists(): raise ValueError("PLANE-ABSENT:" + plane)
        d = sha(p); read_manifest.append({"path": str(p), "sha256": d})
        if M.get(plane_name(b, plane)) != d: raise ValueError("PLANE-NOT-VERIFIED:" + plane)
        planes[plane] = p
    def data_hdu(path):
        h = fits.open(path)
        for x in h:
            if x.data is not None: return x
        raise ValueError("DATA-INTEGRITY-FAIL:no data HDU")
    ih = data_hdu(planes["image-r"]); image = np.asarray(ih.data, dtype=np.float64); wcs = WCS(ih.header)
    maskbits = np.asarray(data_hdu(planes["maskbits"]).data).astype(np.int32); nexp = np.asarray(data_hdu(planes["nexp-r"]).data).astype(np.int32)
    return image, maskbits, nexp, wcs

def render(identity: Path, pool: Path, group: str, bricks_dir: Path, manifest_path: Path, manifest_sha256: str, tensors: Path, out: Path, journal: Path) -> dict:
    I = load_identity(identity); P = load_pool(pool); M = load_manifest(manifest_path, manifest_sha256); tensors.mkdir(parents=True, exist_ok=True); out.mkdir(parents=True, exist_ok=True)
    objs = dev_objects(I, group); read_manifest = [{"path": str(identity), "sha256": sha(identity)}, {"path": str(pool), "sha256": sha(pool)}, {"path": str(manifest_path), "sha256": manifest_sha256}]
    jrow(journal, {"utc": utc(), "event": "render-start", "group": group, "objects": len(objs), "r_T": R_T_DEV, "pipeline": "render_chain_v3 / renderer_v4 / pixel_rejection_v2 / protected_region_v2", "sentinel_sha256": drv.SENTINEL_SHA256})
    rows = []; scored = refused = 0; cache = {}
    for oid, b in objs:
        ra, dec, g = P[oid]; rec = {"utc": utc(), "objid": oid, "g": g, "brick": b}
        try:
            if b not in cache: cache[b] = _open_planes(bricks_dir, b, M, read_manifest)
            image, maskbits, nexp, wcs = cache[b]
            r = rc.render_object(image, maskbits, nexp, wcs, ra, dec, b, R_T_DEV)
            rec.update({k: v for k, v in r.items() if k not in ("tensor", "flagged_coords")}); rec["flag_count"] = len(r.get("flagged_coords", []))
            if r["status"] == "SCORED": payload = r["tensor"]; scored += 1
            else: payload = drv.SENTINEL_TENSOR; rec["sentinel"] = True; refused += 1
        except ValueError as e:
            rec.update({"status": "REFUSED", "reason": str(e), "sentinel": True}); payload = drv.SENTINEL_TENSOR; refused += 1
        (tensors / f"{oid}.ic6").write_bytes(payload); d = hashlib.sha256(payload).hexdigest(); rec["tensor_sha256"] = d; rows.append((oid, g, d)); jrow(journal, rec)
    mpath = out / f"{group.upper()}.csv"
    with open(mpath, "w", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n"); w.writerow(["objid", "g", "tensor_sha256"]); w.writerows(rows)
    (out / f"{group}_read_manifest.json").write_text(json.dumps(read_manifest, indent=1) + "\n")
    jrow(journal, {"utc": utc(), "event": "render-end", "group": group, "scored": scored, "refused_sentinel": refused, "manifest_sha256": sha(mpath)})
    return {"scored": scored, "refused_sentinel": refused, "manifest": str(mpath)}

def main(argv=None):
    import argparse, urllib.request
    def fetch(url, timeout=60):
        with urllib.request.urlopen(url, timeout=timeout) as r: return r.read()
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="mode", required=True)
    m = sub.add_parser("manifest"); m.add_argument("--identity", required=True); m.add_argument("--pool", required=True); m.add_argument("--no-r", required=True); m.add_argument("--out", required=True)
    f = sub.add_parser("fetch"); f.add_argument("--bricks", required=True); f.add_argument("--manifest", required=True); f.add_argument("--manifest-sha256", required=True); f.add_argument("--out", required=True); f.add_argument("--journal", required=True)
    r = sub.add_parser("render"); r.add_argument("--identity", required=True); r.add_argument("--pool", required=True); r.add_argument("--group", required=True); r.add_argument("--bricks-dir", required=True); r.add_argument("--manifest", required=True); r.add_argument("--manifest-sha256", required=True); r.add_argument("--tensors", required=True); r.add_argument("--out", required=True); r.add_argument("--journal", required=True)
    a = ap.parse_args(argv)
    if a.mode == "manifest": print(json.dumps(manifest(Path(a.identity), Path(a.pool), Path(a.no_r), Path(a.out), fetch), sort_keys=True)); return 0
    if a.mode == "fetch": print(json.dumps(fetch_bricks(Path(a.bricks), Path(a.manifest), a.manifest_sha256, Path(a.out), Path(a.journal), fetch, Path(a.out)))); return 0
    print(json.dumps(render(Path(a.identity), Path(a.pool), a.group, Path(a.bricks_dir), Path(a.manifest), a.manifest_sha256, Path(a.tensors), Path(a.out), Path(a.journal)))); return 0
if __name__ == "__main__": sys.exit(main())
