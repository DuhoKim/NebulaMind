"""dev_corpus_pipeline over a synthetic DR9-north-shaped brick (FITS planes with a TAN WCS), a two-object identity, a mocked network
serving the published checksum file and the planes. Asserts: manifest built only from the published checksum file; fetch verifies
against the sealed manifest only and quarantines a mismatch; render writes the driver manifest in identity order, a real tensor for a
clean object and the canonical SENTINEL for a refused one (zero exposure at the centre), journals the refusal, and records every file read."""
import io, json, unittest, tempfile, sys, hashlib
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1]))
import dev_corpus_pipeline as dcp
from study_renderer.test_renderer_v4 import make_wcs
from astropy.io import fits

def fits_bytes(arr, header=None):
    h = fits.HDUList([fits.PrimaryHDU(), fits.ImageHDU(arr, header=header)]); b = io.BytesIO(); h.writeto(b); return b.getvalue()
def brick_planes(zero_at=None):
    w = make_wcs(ra=40.0, dec=10.0); yy, xx = np.indices((180, 180), dtype=np.float64)
    image = (1.0 + 5.0 * np.exp(-((yy - 89.5) ** 2 + (xx - 89.5) ** 2) / 72.0)).astype(np.float32)
    nexp = np.ones((180, 180), dtype=np.int16)
    if zero_at: nexp[zero_at] = 0
    hdr = w.to_header()
    return {"image-r": fits_bytes(image, hdr), "maskbits": fits_bytes(np.zeros((180, 180), dtype=np.int16), hdr), "nexp-r": fits_bytes(nexp, hdr)}

class T(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()); self.b = "0400p100"
        # two bricks: clean (object 1) and one with zero exposure at the source pixel that maps to the output centre (object 2)
        self.planes = {"0400p100": brick_planes(), "0400p101": brick_planes(zero_at=(26 + 63, 26 + 63))}
        self.published = {b: "\n".join(f"{hashlib.sha256(v).hexdigest()}  legacysurvey-{b}-{p}.fits.fz" for p, v in pl.items()) + "\n" for b, pl in self.planes.items()}
        ident = {"schema_version": "CORPUS-IDENTITY-2", "detail": {"tuning": {"objids": [1001, 1002], "bricks": ["0400p100", "0400p101"]}, "holdout": {"objids": [], "bricks": []}}}
        self.identity = self.tmp / "corpus_identity.json"; self.identity.write_text(json.dumps(ident))
        self.pool = self.tmp / "pool.csv"; self.pool.write_text("GZ1_OBJID,RA,DEC,G\n1001,40.0,10.0,1\n1002,40.0,10.0,-1\n")
        self.no_r = self.tmp / "no_r.txt"; self.no_r.write_text("9999p999\n"); self.calls = []
    def fetch(self, url, timeout=60):
        self.calls.append(url)
        for b in self.planes:
            if url == dcp.checksum_url(b): return self.published[b].encode()
            for p in dcp.PLANES:
                if url == dcp.plane_url(b, p): return self.planes[b][p]
        raise OSError("404 " + url)
    def test_manifest_fetch_render_end_to_end(self):
        out = self.tmp / "m"; rec = dcp.manifest(self.identity, self.pool, self.no_r, out, self.fetch)
        self.assertEqual((rec["bricks"], rec["objects"], rec["checksum_lines"]), (2, 2, 6)); self.assertTrue(all(u.endswith(".sha256sum") for u in self.calls))
        M = out / "dev_checksum_manifest.txt"; msha = rec["manifest_sha256"]
        j = self.tmp / "fetch.jsonl"; r = dcp.fetch_bricks(out / "dev_bricks.txt", M, msha, self.tmp / "bricks", j, self.fetch, self.tmp)
        self.assertEqual((r["ok"], r["non_ok"]), (6, 0))
        r2 = dcp.fetch_bricks(out / "dev_bricks.txt", M, msha, self.tmp / "bricks", j, self.fetch, self.tmp); self.assertEqual(r2["ok"], 6)   # resumable
        rj = self.tmp / "render.jsonl"; rr = dcp.render(self.identity, self.pool, "tuning", self.tmp / "bricks", M, msha, self.tmp / "tens", self.tmp / "ro", rj)
        self.assertEqual((rr["scored"], rr["refused_sentinel"]), (1, 1))
        rows = list(__import__("csv").DictReader(open(self.tmp / "ro" / "TUNING.csv"))); self.assertEqual([r["objid"] for r in rows], ["1001", "1002"]); self.assertEqual(rows[1]["tensor_sha256"], dcp.drv.SENTINEL_SHA256)
        self.assertEqual(hashlib.sha256((self.tmp / "tens" / "1001.ic6").read_bytes()).hexdigest(), rows[0]["tensor_sha256"]); self.assertEqual(len((self.tmp / "tens" / "1001.ic6").read_bytes()), 65536)
        J = [json.loads(l) for l in open(rj)]; ref = [x for x in J if x.get("objid") == 1002][0]; self.assertEqual(ref["status"], "REFUSED"); self.assertTrue(ref["sentinel"]); self.assertEqual(ref["r_T"], 23.0)
        rm = json.loads((self.tmp / "ro" / "tuning_read_manifest.json").read_text()); self.assertTrue(any("image-r" in e["path"] for e in rm))
    def test_fetch_verifies_only_against_sealed_manifest_and_quarantines(self):
        out = self.tmp / "m"; rec = dcp.manifest(self.identity, self.pool, self.no_r, out, self.fetch); M = out / "dev_checksum_manifest.txt"
        tampered = dict(self.planes["0400p100"]); tampered["maskbits"] = tampered["maskbits"] + b"x"
        def bad_fetch(url, timeout=60):
            if url == dcp.plane_url("0400p100", "maskbits"): return tampered["maskbits"]
            return self.fetch(url, timeout)
        r = dcp.fetch_bricks(out / "dev_bricks.txt", M, rec["manifest_sha256"], self.tmp / "b2", self.tmp / "f2.jsonl", bad_fetch, self.tmp / "b2")
        self.assertEqual(r["non_ok"], 1); self.assertTrue((self.tmp / "b2" / "0400p100" / "legacysurvey-0400p100-maskbits.fits.fz.QUARANTINE").exists())
        with self.assertRaises(SystemExit): dcp.fetch_bricks(out / "dev_bricks.txt", M, "0" * 64, self.tmp / "b3", self.tmp / "f3.jsonl", self.fetch, self.tmp / "b3")   # manifest digest moved
    def test_fresh_group_refused_and_no_r_refused(self):
        with self.assertRaises(SystemExit): dcp.dev_objects(dcp.load_identity(self.identity), "fresh_validation")
        self.no_r.write_text("0400p100\n")
        with self.assertRaises(SystemExit) as cm: dcp.manifest(self.identity, self.pool, self.no_r, self.tmp / "m2", self.fetch)
        self.assertIn("BRICK-NO-R", str(cm.exception))
if __name__ == "__main__": unittest.main()
