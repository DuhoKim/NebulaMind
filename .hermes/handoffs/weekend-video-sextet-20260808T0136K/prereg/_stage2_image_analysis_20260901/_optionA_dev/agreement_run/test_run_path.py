"""Synthetic fixtures only. No protected file is read and no network is used.

POSITIVE-REGRESSION labels denote the retained contract checks. V46 migrates
only their manifest/runtime fixture to CORE; the existing outcomes are retained.
V47 gives that synthetic ready fixture all declared obligations and a separately
bound synthetic A1 revision. The real A1/runtime obligation remains unresolved.
"""
import hashlib
import io
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from _optionA_dev.agreement_run import run_path as rp
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from _optionA_dev.fourier_chirality import fourier_chirality as fc
from _optionA_dev.drand_only import verify_drand_v2 as vd

LANE = rp.ROOT
SOURCE = getattr(rp, "_source_for_test", None)
if SOURCE is None:
    SOURCE = Path(rp.__file__).read_bytes()


def rows(n, m, k):
    return ([{"status": "SCORED", "match": True}] * k +
            [{"status": "SCORED", "match": False}] * (m-k) +
            [{"status": "RENDER-REFUSED", "reason": "synthetic"}] * (n-m))


class RunPathTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="a1-synthetic-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.code_root = self.base / "code"
        for rel in rp.CODE:
            path = self.code_root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            if rel.endswith("/run_path.py"):
                path.write_bytes(SOURCE)
            else:
                path.symlink_to(LANE / rel)
        self.root_patch = patch.object(rp, "ROOT", self.code_root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        self.network = patch.object(rp, "fetch_bytes", side_effect=AssertionError("NETWORK FORBIDDEN"))
        self.network.start()
        self.addCleanup(self.network.stop)
        coords = [{"objid": i, "ra": 40.0, "dec": 10.0, "brick": "0400p100"}
                  for i in range(2600)]
        runtime = json.loads((LANE / "_optionA_dev/agreement_run/RUNTIME_PINS_A1_CORE.json").read_text())
        config_path = self.code_root / "miniprereg_pins/render_config_v2.json"
        config_path.write_bytes((LANE / "miniprereg_pins/render_config_v2.json").read_bytes())
        inputs = {
            "eligible": self.put("eligible.txt", "".join(str(i)+"\n" for i in range(2600)).encode()),
            "exclusion": self.put("excluded.txt", b""),
            "failed": self.put("failed.txt", b""),
            "coordinates": self.put_json("coordinates.json", coords),
            "bricks": self.put("bricks.txt", b"synthetic brick metadata\n"),
            "no_r": self.put("no_r.txt", b""),
            "render_config": self.pin(config_path),
            "env_lock": self.pin(LANE / "_optionA_dev/fourier_chirality/env_lock.json"),
            "runtime": self.put_json("runtime.json", runtime),
        }
        a1_path = self.code_root / "AGREEMENT_RUN_AMENDMENT_A1_20260907.md"
        a1_text = (LANE / a1_path.name).read_text().replace(
            "Runtime representation remains current preparation work to be done.",
            "Runtime representation preparation work is resolved.").replace(
            "Runtime representation remains a current preparation obligation to be done",
            "Runtime representation is a resolved current preparation obligation")
        a1_path.write_text(a1_text)
        a1_pin = self.pin(a1_path)
        a1_patch = patch.object(rp, "A1_REVIEWED_SHA256", a1_pin["sha256"])
        a1_patch.start()
        self.addCleanup(a1_patch.stop)
        c = {"schema": "A1-INPUT-CORE-DRAFT-1",
             "code": {p: self.pin(self.code_root/p)["sha256"] for p in rp.CODE},
             "inputs": inputs, "ready_for_input_freeze": True,
             "readiness": {"checks": {"all_real_entries_rehashed_and_matched": True,
                 "input_due_placeholders_resolved": True,
                 "declared_obligation_set_complete": True,
                 "current_preparation_obligations_resolved": True,
                 "a1_manifest_obligations_agree": True}},
             "a1_obligations_source": a1_pin,
             "current_preparation_obligations": [
                 {"id": "CORE_CONSUMER_RECONCILIATION", "resolved": True},
                 {"id": "MEDIUM_CURRENT_PREPARATION", "resolved": True},
                 {"id": "RUNTIME_REPRESENTATION", "resolved": True}], "placeholders": []}
        c["files"] = [{**pin, "status": "REAL"} for pin in inputs.values()]
        c["files"].append({**a1_pin, "status": "REAL", "kind": "a1_obligation_source"})
        c["files"] += [{**self.pin(self.code_root/p), "status": "REAL", "kind": "our_source_code"}
                       for p in rp.CODE]
        for rel in rp.CODE:
            cache = Path(importlib.util.cache_from_source(str((self.code_root/rel).resolve())))
            if cache.is_file():
                c["files"].append({**self.pin(cache), "status": "REAL",
                    "kind": "our_imported_bytecode", "source": rel})
        self.C = self.put_json("C.json", c)
        self.run = rp.RunPath(self.C, self.base / "out")
        self.inputs = inputs
        self.anchor_fields = {"mechanism": "provider-chat", "external_reference": "synthetic:chat",
            "third_party": "fixture-witness", "lane_owner": "fixture-owner",
            "third_party_utc": "2020-07-22T00:00:00+00:00",
            "pushed_reference": "synthetic:push"}
        self.count = 0

    def pin(self, path):
        return {"path": str(path.resolve()), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}

    def put(self, name, raw):
        p = self.base / name
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("xb") as f:
            f.write(raw)
        return self.pin(p)

    def put_json(self, name, data):
        return self.put(name, rp.canonical(data))

    def predecessor(self, stage, **extra):
        self.count += 1
        return self.put_json("previous%d.json" % self.count, {
            "C": self.C, "stage": stage, "verdict": "PASS", "outputs": {}, **extra})

    def bad_digest(self):
        return {**self.C, "sha256": "0"*64}

    def missing_file(self):
        return {"path": str(self.base/"absent.json"), "sha256": "1"*64}

    def invoke(self, stage, predecessor):
        if stage == "designation":
            return self.run.designate(predecessor)
        if stage == "seed":
            return self.run.accept_seed(predecessor)
        if stage == "draw":
            return self.run.select_sample(predecessor)
        return {"tuning": self.run.tune, "holdout": self.run.holdout,
                "validation": self.run.validate}[stage](predecessor, None, None)

    def test_designation_digest_mismatch(self):
        """POSITIVE-REGRESSION: designation refuses mismatched predecessor bytes."""
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH"):
            self.invoke("designation", self.bad_digest())

    def test_seed_digest_mismatch(self):
        """POSITIVE-REGRESSION: seed refuses mismatched predecessor bytes."""
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH"):
            self.invoke("seed", self.bad_digest())

    def test_draw_digest_mismatch(self):
        """POSITIVE-REGRESSION: draw refuses mismatched predecessor bytes."""
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH"):
            self.invoke("draw", self.bad_digest())

    def test_tuning_digest_mismatch(self):
        """POSITIVE-REGRESSION: tuning refuses mismatched predecessor bytes."""
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH"):
            self.invoke("tuning", self.bad_digest())

    def test_holdout_digest_mismatch(self):
        """POSITIVE-REGRESSION: holdout refuses mismatched predecessor bytes."""
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH"):
            self.invoke("holdout", self.bad_digest())

    def test_validation_digest_mismatch(self):
        """POSITIVE-REGRESSION: validation refuses mismatched predecessor bytes."""
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH"):
            self.invoke("validation", self.bad_digest())

    def test_every_stage_requires_a_digest(self):
        """POSITIVE-REGRESSION: no stage accepts a path without an expected digest."""
        for stage in ("designation", "seed", "draw", "tuning", "holdout", "validation"):
            with self.subTest(stage=stage):
                with self.assertRaisesRegex(rp.Refused, "MISSING-DIGEST"):
                    self.invoke(stage, {"path": self.C["path"]})

    def test_every_stage_requires_predecessor_file(self):
        """POSITIVE-REGRESSION: a nonexistent predecessor cannot advance any stage."""
        for stage in ("designation", "seed", "draw", "tuning", "holdout", "validation"):
            with self.subTest(stage=stage):
                with self.assertRaisesRegex(rp.Refused, "MISSING-FILE"):
                    self.invoke(stage, self.missing_file())

    def test_every_stage_checks_predecessor_kind(self):
        """POSITIVE-REGRESSION: a valid digest from another stage cannot advance."""
        wrong = self.predecessor("wrong")
        for stage in ("designation", "seed", "draw", "tuning", "holdout", "validation"):
            with self.subTest(stage=stage):
                with self.assertRaisesRegex(rp.Refused, "PREDECESSOR-STAGE"):
                    self.invoke(stage, wrong)

    def test_input_digest_mismatch_before_seed(self):
        """POSITIVE-REGRESSION: changed INPUT metadata prevents seed collection."""
        Path(self.inputs["bricks"]["path"]).write_bytes(b"changed synthetic metadata")
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH"):
            self.run.accept_seed(self.predecessor("designation"))

    def test_code_digest_mismatch_before_tuning(self):
        """POSITIVE-REGRESSION: code pins are checked at a data-stage boundary."""
        Path(self.code_root/rp.CODE[0]).write_bytes(b"# synthetic corruption\n")
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH"):
            self.run.tune(self.predecessor("draw"), None, None)

    def test_closed_holdout_cannot_validate(self):
        """POSITIVE-REGRESSION: a CLOSED holdout record prevents validation."""
        pred = self.predecessor("holdout", verdict="CLOSED: holdout floor")
        with self.assertRaisesRegex(rp.Refused, "PREDECESSOR-NOT-PASS"):
            self.run.validate(pred, None, None)

    def test_anchor_schedule_uses_a1_formula(self):
        """POSITIVE-REGRESSION: anchor plus 600 uses ceil on the drand period."""
        a = vd.GENESIS + 7
        anchor = self.predecessor("input-anchor", published_sha256=self.C["sha256"],
            **{**self.anchor_fields, "third_party_utc":
               rp.datetime.fromtimestamp(a, rp.timezone.utc).isoformat()})
        with patch.object(rp, "utc", return_value=rp.datetime.fromtimestamp(a+1, rp.timezone.utc).isoformat()):
            rec = rp.json_pin(self.run.designate(anchor))
        self.assertEqual((rec["round"], rec["scheduled_unix"]), (22, vd.GENESIS+630))

    def test_missed_designation_deadline_aborts(self):
        """POSITIVE-REGRESSION: a missed prospective deadline cannot choose a replacement."""
        anchor = self.predecessor("input-anchor", published_sha256=self.C["sha256"],
                                  **self.anchor_fields)
        with self.assertRaisesRegex(rp.Refused, "DESIGNATION-DEADLINE"):
            self.run.designate(anchor)

    def seed_fixture(self):
        rnd = 100
        signature = bytes(range(96))
        raw = rp.canonical({"round": rnd, "signature": signature.hex(),
                            "previous_signature": "00"*96, "randomness": rp.sha(signature)})
        return self.predecessor("designation", round=rnd, scheduled_unix=vd.GENESIS), raw

    def test_seed_requires_bls_despite_matching_hosts(self):
        """POSITIVE-REGRESSION: two agreeing hosts never substitute for BLS."""
        pred, raw = self.seed_fixture()
        with patch.object(rp, "fetch_bytes", return_value=raw), patch.object(vd.G2Basic, "Verify", return_value=False):
            with self.assertRaisesRegex(rp.Refused, "fewer than two BLS"):
                self.run.accept_seed(pred)

    def test_seed_requires_two_distinct_hosts(self):
        """POSITIVE-REGRESSION: one authenticated refetched host is insufficient."""
        pred, raw = self.seed_fixture()
        def one(url):
            if url == vd.round_url(vd.RELAYS[0], 100):
                return raw
            raise OSError("synthetic unavailable host")
        with patch.object(rp, "fetch_bytes", side_effect=one), patch.object(vd.G2Basic, "Verify", return_value=True):
            with self.assertRaisesRegex(rp.Refused, "fewer than two BLS"):
                self.run.accept_seed(pred)

    def test_seed_refetch_is_required(self):
        """POSITIVE-REGRESSION: successful collection alone cannot accept seed."""
        pred, raw = self.seed_fixture()
        calls = [raw]*4 + [OSError("synthetic refetch unavailable")]*4
        with patch.object(rp, "fetch_bytes", side_effect=calls), patch.object(vd.G2Basic, "Verify", return_value=True):
            with self.assertRaisesRegex(rp.Refused, "fewer than two BLS"):
                self.run.accept_seed(pred)

    def test_seed_accepts_bls_and_two_refetched_hosts(self):
        """POSITIVE-REGRESSION: accepted seed retains both passes and all raw pins."""
        pred, raw = self.seed_fixture()
        with patch.object(rp, "fetch_bytes", return_value=raw), patch.object(vd.G2Basic, "Verify", return_value=True):
            rec = rp.json_pin(self.run.accept_seed(pred))
        self.assertEqual((rec["verdict"], len(rec["hosts"]), len(rec["outputs"])), ("PASS", 4, 9))

    def synthetic_draw(self):
        return self.run.select_sample(self.predecessor("seed", seed="ab"*32, round=100))

    def test_selector_exact_disjoint_synthetic_draw(self):
        """POSITIVE-REGRESSION: existing selector supplies all exact identity lists."""
        draw = rp.json_pin(self.synthetic_draw())
        groups = [rp.json_pin(draw["outputs"][s]) for s in rp.SIZES]
        self.assertEqual(([len(g) for g in groups], len({r["objid"] for g in groups for r in g})),
                         ([400, 200, 2000], 2600))

    def test_draw_cannot_be_reused(self):
        """POSITIVE-REGRESSION: an existing draw invocation is never overwritten."""
        seed = self.predecessor("seed", seed="ab"*32, round=100)
        self.run.select_sample(seed)
        with self.assertRaisesRegex(rp.Refused, "REUSE-REFUSED"):
            self.run.select_sample(seed)

    def test_tuning_floor_below(self):
        """POSITIVE-REGRESSION: m=379 cannot enter the winner comparison."""
        self.assertFalse(rp.stage_statistic("tuning", rows(400, 379, 379))["eligible"])

    def test_tuning_floor_at(self):
        """POSITIVE-REGRESSION: m=380 is eligible without shrinking the draw."""
        self.assertTrue(rp.stage_statistic("tuning", rows(400, 380, 380))["eligible"])

    def test_tuning_denominator_is_400(self):
        """POSITIVE-REGRESSION: refusals count as misses under either orientation."""
        self.assertEqual(rp.stage_statistic("tuning", rows(400, 380, 0))["p_val"], 0.95)

    def test_holdout_floor_before_wilson(self):
        """POSITIVE-REGRESSION: m=189 closes before any Wilson call."""
        with patch("miniprereg_pins.validation_gate.wilson_lower", side_effect=AssertionError("Wilson called too early")):
            result = rp.stage_statistic("holdout", rows(200, 189, 189))
        self.assertEqual(result["verdict"], "CLOSED: holdout floor")

    def test_holdout_floor_at(self):
        """POSITIVE-REGRESSION: m=190 reaches the strength gate."""
        self.assertEqual(rp.stage_statistic("holdout", rows(200, 190, 190))["verdict"], "PASS")

    def test_holdout_fixed_denominator(self):
        """POSITIVE-REGRESSION: 150/200 fails although 150/190 would pass."""
        self.assertEqual(rp.stage_statistic("holdout", rows(200, 190, 150))["verdict"],
                         "CLOSED: holdout strength")

    def test_holdout_threshold_153(self):
        """POSITIVE-REGRESSION: 153 of exact draw 200 clears the retained bar."""
        self.assertEqual(rp.stage_statistic("holdout", rows(200, 190, 153))["verdict"], "PASS")

    def test_validation_floor_before_wilson(self):
        """POSITIVE-REGRESSION: m=1899 closes before any Wilson call."""
        with patch("miniprereg_pins.validation_gate.wilson_lower", side_effect=AssertionError("Wilson called too early")):
            result = rp.stage_statistic("validation", rows(2000, 1899, 1899))
        self.assertEqual(result["verdict"], "CLOSED: validation floor")

    def test_validation_floor_at(self):
        """POSITIVE-REGRESSION: m=1900 reaches Wilson with r=100 excluded."""
        result = rp.stage_statistic("validation", rows(2000, 1900, 1400))
        self.assertEqual((result["verdict"], result["denominator"], result["r"]),
                         ("PASS", 1900, 100))

    def test_validation_scored_denominator(self):
        """POSITIVE-REGRESSION: validation computes 1400/1900, never 1400/2000."""
        self.assertAlmostEqual(rp.stage_statistic("validation", rows(2000, 1900, 1400))["p_val"], 1400/1900)

    def test_validation_reversed_orientation(self):
        """POSITIVE-REGRESSION: global sign reversal uses m-k among scored only."""
        self.assertAlmostEqual(rp.stage_statistic("validation", rows(2000, 1900, 500))["p_val"], 1400/1900)

    def test_exact_draw_required_by_statistics(self):
        """POSITIVE-REGRESSION: a floor-sized sample is not an exact draw."""
        with self.assertRaisesRegex(rp.Refused, "EXACT-DRAW-SIZE"):
            rp.stage_statistic("validation", rows(1900, 1900, 1900))

    def test_tie_break_fewer_refusals(self):
        """POSITIVE-REGRESSION: equal objectives prefer fewer refusals."""
        candidates = [{"eligible": True, "p_val": .8, "r": 20, "config_index": 0},
                      {"eligible": True, "p_val": .8, "r": 10, "config_index": 1}]
        self.assertEqual(rp.choose_winner(candidates)["config_index"], 1)

    def test_tie_break_earlier_index(self):
        """POSITIVE-REGRESSION: equal objectives and refusal counts prefer earlier index."""
        candidates = [{"eligible": True, "p_val": .8, "r": 10, "config_index": 4},
                      {"eligible": True, "p_val": .8, "r": 10, "config_index": 1}]
        self.assertEqual(rp.choose_winner(candidates)["config_index"], 1)

    def test_nonrepeat_is_unscored(self):
        """POSITIVE-REGRESSION: unequal float32 bits never enter m or k."""
        est = fc.Estimator(fc.enumerate_configs()[0])
        with patch.object(est, "chi", side_effect=[np.float32(.1), np.float32(.2)]):
            result = rp.score_object(est, np.ones((128,128), dtype="<f4").tobytes(), 1)
        self.assertEqual(result["reason"], "NON-REPEAT")

    def test_tie_is_unscored(self):
        """POSITIVE-REGRESSION: zero is a measurement failure, not a sign."""
        est = fc.Estimator(fc.enumerate_configs()[0])
        with patch.object(est, "chi", return_value=np.float32(0)):
            result = rp.score_object(est, np.ones((128,128), dtype="<f4").tobytes(), 1)
        self.assertEqual(result["status"], "UNSCORED")

    def test_bad_tensor_is_integrity_failure(self):
        """POSITIVE-REGRESSION: missing tensor bytes are not silently unscored."""
        with self.assertRaisesRegex(rp.Refused, "TENSOR-INTEGRITY"):
            rp.score_object(fc.Estimator(), b"", 1)

    def make_inventory(self, stage, draw_pin, count=None):
        draw = rp.json_pin(draw_pin)
        identities = rp.json_pin(draw["bindings"]["drawn_lists"][stage])
        if count is not None:
            identities = identities[:count]
        yy, xx = np.indices((180,180), dtype=float)
        x, y = xx-89.5, yy-89.5
        radius = np.hypot(x, y)
        image = (2 + np.exp(-radius/45) * (1 + .7*np.cos(2*np.arctan2(y,x)+4*np.log1p(radius)))).astype(float)
        w = WCS(naxis=2)
        w.wcs.ctype = ["RA---TAN", "DEC--TAN"]
        w.wcs.crval = [40.,10.]
        w.wcs.crpix = [90.5,90.5]
        w.wcs.cd = np.array([[-.262/3600,0],[0,.262/3600]])
        planes = {}
        checks = []
        for name, arr in (("image-r",image), ("maskbits",np.zeros((180,180),dtype=np.int32)),
                          ("nexp-r",np.ones((180,180),dtype=np.int32))):
            stream = io.BytesIO()
            fits.PrimaryHDU(arr, header=w.to_header()).writeto(stream)
            pin = self.put(stage+"."+name+".fits", stream.getvalue())
            planes[name] = {**pin, "hdu": 0}
            checks.append(pin["sha256"]+"  legacysurvey-0400p100-"+name+".fits.fz\n")
        checksum = self.put(stage+".checksums.txt", "".join(checks).encode())
        labels = self.put_json(stage+".labels.json", {str(r["objid"]): 1 for r in identities})
        inventory = {"stage": stage, "C": self.C,
            "drawn_list": draw["bindings"]["drawn_lists"][stage], "labels": labels,
            "objects": [{"objid": r["objid"], "checksums": checksum, "planes": planes} for r in identities]}
        return identities, inventory

    def access(self, stage, pred_pin, inventory, **extra):
        previous = rp.json_pin(pred_pin)
        return self.put_json(stage+".access.json", {**self.anchor_fields, "stage": stage, "C": self.C,
            "predecessor": pred_pin, "published_sha256": pred_pin["sha256"],
            "bindings": previous["bindings"], "inventory": inventory, **extra})

    def test_real_renderer_and_all_96_estimators(self):
        """POSITIVE-REGRESSION: synthetic FITS reaches actual renderer and every config."""
        draw = self.synthetic_draw()
        identities, inv = self.make_inventory("tuning", draw, count=1)
        objects, _, _ = self.run._render("tuning", identities, inv)
        tensor = rp.read_pin(objects[0][2])
        results = [rp.score_object(fc.Estimator(cfg), tensor, 1) for cfg in fc.enumerate_configs()]
        self.assertEqual((len(results), {r["status"] for r in results}), (96, {"SCORED"}))

    def test_plane_digest_mismatch_is_fatal(self):
        """POSITIVE-REGRESSION: corrupted synthetic FITS cannot become a render refusal."""
        draw = self.synthetic_draw()
        identities, inv = self.make_inventory("tuning", draw, count=1)
        source = inv["objects"][0]["planes"]["image-r"]
        Path(source["path"]).write_bytes(b"synthetic corrupt plane")
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH"):
            self.run._render("tuning", identities, inv)

    def test_render_refusal_keeps_identity_and_no_tensor(self):
        """POSITIVE-REGRESSION: explicit render refusals retain identity without sentinels."""
        draw = self.synthetic_draw()
        identities, inv = self.make_inventory("tuning", draw, count=1)
        with patch("study_renderer.render_chain_v3.render_object",
                   return_value={"status":"REFUSED","reason":"synthetic central flag"}):
            _, receipts, outputs = self.run._render("tuning", identities, inv)
        self.assertEqual((receipts[0]["status"], any(k.startswith("tensor:") for k in outputs)),
                         ("RENDER-REFUSED", False))

    def test_access_inventory_digest_mismatch(self):
        """POSITIVE-REGRESSION: a changed data inventory refuses before rendering."""
        draw = self.synthetic_draw()
        inventory = self.bad_digest()
        access = self.access("tuning", draw, inventory)
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH"):
            self.run.tune(draw, access, inventory)

    def test_full_stage_orchestration_synthetic(self):
        """POSITIVE-REGRESSION: exact stages traverse 96 configs then the sole W winner."""
        draw = self.synthetic_draw()
        tensor = np.ones((128,128), dtype="<f4").tobytes()
        def rendered(*args):
            return {"status":"SCORED", "tensor":tensor, "tensor_sha256":rp.sha(tensor)}
        with patch("study_renderer.render_chain_v3.render_object", side_effect=rendered), \
             patch.object(fc.Estimator, "chi", return_value=np.float32(.25)):
            _, inv = self.make_inventory("tuning", draw)
            inv_pin = self.put_json("tuning.inventory.json", inv)
            tuning = self.run.tune(draw, self.access("tuning", draw, inv_pin), inv_pin)
            t = rp.json_pin(tuning)
            W = self.put_json("W.json", {**self.anchor_fields, "C":self.C,
                "bindings":t["bindings"], "winner":t["winner"], "tuning":tuning,
                "tuning_outputs":t["outputs"]})
            _, inv = self.make_inventory("holdout", draw)
            inv_pin = self.put_json("holdout.inventory.json", inv)
            access = self.access("holdout", tuning, inv_pin,
                winner=t["winner"], W=W, W_published_sha256=W["sha256"])
            holdout = self.run.holdout(tuning, access, inv_pin)
            _, inv = self.make_inventory("validation", draw)
            inv_pin = self.put_json("validation.inventory.json", inv)
            access = self.access("validation", holdout, inv_pin, winner=t["winner"],
                W=W, W_published_sha256=W["sha256"], custody_fetch_after_winner_freeze=True)
            validation = rp.json_pin(self.run.validate(holdout, access, inv_pin))
        self.assertEqual((t["n_configs"], validation["verdict"], validation["statistic"]["n"],
                          validation["statistic"]["denominator"]), (96, "PASS", 2000, 2000))


if __name__ == "__main__":
    unittest.main(verbosity=2)
