"""V46 synthetic consumer refusals and real, label-blind MEDIUM integration.

All mutations target temporary fixtures. No real study stage or network runs.
The predecessor log records which outcomes reproduce the old consumer gap.
"""
import io
import json
import marshal
from pathlib import Path
import re
import unittest
import sys
from contextlib import contextmanager
from unittest.mock import patch

from _optionA_dev.agreement_run import run_path as rp
from _optionA_dev.agreement_run import test_run_path as fixtures
from _optionA_dev.agreement_run import medium_perturbation as mp
from _optionA_dev.agreement_run.test_medium_perturbation import raster
from astropy.io import fits
from astropy.wcs import WCS, Sip
import numpy as np


@contextmanager
def observe_producer(callback):
    """Observe the real producer without replacing evidence-bound code."""
    code = mp.produce_tuning_disclosure.__code__
    previous = sys.getprofile()
    def profile(frame, event, arg):
        if frame.f_code is code:
            callback(frame, event, arg)
    sys.setprofile(profile)
    try:
        yield
    finally:
        sys.setprofile(previous)


class CoreConsumerTests(unittest.TestCase):
    setUp = fixtures.RunPathTests.setUp
    pin = fixtures.RunPathTests.pin
    put = fixtures.RunPathTests.put
    put_json = fixtures.RunPathTests.put_json

    def rewrite_core(self, mutate):
        c = rp.json_pin(self.C)
        mutate(c)
        Path(self.C["path"]).write_bytes(rp.canonical(c))
        self.C = self.pin(Path(self.C["path"]))
        self.run.C = self.C

    def change_runtime(self, mutate):
        runtime = rp.json_pin(self.inputs["runtime"])
        mutate(runtime)
        path = Path(self.inputs["runtime"]["path"])
        path.write_bytes(rp.canonical(runtime))
        self.inputs["runtime"] = self.pin(path)

    def test_core_register_is_consumed(self):
        """FAIL-FIRST: CORE readiness and all rows reach the bounded environment."""
        self.assertEqual(self.run._common()["schema"], "A1-INPUT-CORE-DRAFT-1")

    def test_core_code_tamper_names_path(self):
        """FAIL-FIRST: TAMPER of pinned driver bytes names that exact path."""
        path = (self.code_root / "_optionA_dev/agreement_run/run_path.py").resolve()
        path.write_bytes(path.read_bytes() + b"\n# synthetic tamper\n")
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH: " + re.escape(str(path))):
            self.run._common()

    def test_core_config_tamper_names_path(self):
        """FAIL-FIRST: TAMPER of a pinned render config is not ignored."""
        path = Path(self.inputs["render_config"]["path"])
        path.write_bytes(path.read_bytes() + b" ")
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH: " + re.escape(str(path))):
            self.run._common()

    def test_core_cache_tamper_names_path(self):
        """FAIL-FIRST: TAMPER of recorded bytecode refuses even with intact source."""
        source = self.code_root / "_optionA_dev/agreement_run/run_path.py"
        cache = self.put("synthetic.pyc", rp.importlib.util.MAGIC_NUMBER + b"\0"*12 +
            marshal.dumps(compile(source.read_bytes(), str(source), "exec", dont_inherit=True)))
        self.rewrite_core(lambda c: c["files"].append({**cache, "status": "REAL",
            "kind": "our_imported_bytecode", "source": "_optionA_dev/agreement_run/run_path.py"}))
        Path(cache["path"]).write_bytes(b"synthetic tampered cache")
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH: " + re.escape(cache["path"])):
            self.run._common()

    def test_rehashed_cache_must_equal_source(self):
        """FAIL-FIRST: a pinned but different cached program cannot impersonate source."""
        cache = self.put("wrong.pyc", rp.importlib.util.MAGIC_NUMBER + b"\0"*12 +
                         marshal.dumps(compile("pass", "wrong", "exec")))
        self.rewrite_core(lambda c: c["files"].append({**cache, "status": "REAL",
            "kind": "our_imported_bytecode", "source": "_optionA_dev/agreement_run/run_path.py"}))
        with self.assertRaisesRegex(rp.Refused, "CACHE-SOURCE-MISMATCH: " + re.escape(cache["path"])):
            self.run._common()

    def test_missing_core_entry_names_path(self):
        """FAIL-FIRST: an input alias cannot replace its missing authoritative CORE row."""
        path = self.inputs["render_config"]["path"]
        self.rewrite_core(lambda c: c.update(files=[p for p in c["files"] if p["path"] != path]))
        with self.assertRaisesRegex(rp.Refused, "MISSING-CORE-ENTRY: " + re.escape(path)):
            self.run._common()

    def test_missing_medium_entry_names_path(self):
        """FAIL-FIRST: the real MEDIUM producer must be an explicit CORE code input."""
        path = str((self.code_root / "_optionA_dev/agreement_run/medium_perturbation.py").resolve())
        self.rewrite_core(lambda c: c.update(files=[p for p in c["files"] if p["path"] != path]))
        with self.assertRaisesRegex(rp.Refused, "MISSING-CORE-ENTRY: .*medium_perturbation.py"):
            self.run._common()

    def test_missing_discoverable_cache_names_path(self):
        """FAIL-FIRST: deleting a currently discoverable local-code cache row refuses."""
        cache = next(p for p in rp.json_pin(self.C)["files"] if p.get("kind") == "our_imported_bytecode")
        self.rewrite_core(lambda c: c.update(files=[p for p in c["files"] if p != cache]))
        with self.assertRaisesRegex(rp.Refused, "MISSING-CORE-ENTRY: " + re.escape(cache["path"])):
            self.run._common()

    def test_false_readiness_blocks_public_tuning(self):
        """FAIL-FIRST: explicit FALSE blocks tune with its recorded reason before access."""
        def mutate(c):
            c["ready_for_input_freeze"] = False
            c["readiness"]["reason"] = "synthetic preparation pending"
        self.rewrite_core(mutate)
        with self.assertRaisesRegex(rp.Refused, "CORE-NOT-READY: synthetic preparation pending"):
            self.run.tune(None, None, None)

    def test_spoofed_true_does_not_clear_obligation(self):
        """FAIL-FIRST: readiness is recomputed from unresolved CORE obligations."""
        self.rewrite_core(lambda c: c["current_preparation_obligations"].append(
            {"id": "synthetic_obligation", "resolved": False, "evidence": "unfinished"}))
        with self.assertRaisesRegex(rp.Refused, "CORE-NOT-READY: UNDECLARED-OBLIGATION: synthetic_obligation"):
            self.run._common()

    def test_input_due_placeholder_blocks(self):
        """FAIL-FIRST: an INPUT placeholder cannot masquerade as future evidence."""
        self.rewrite_core(lambda c: c["placeholders"].append(
            {"name": "synthetic_input", "due_stage": "INPUT", "blocks_input_freeze": False}))
        with self.assertRaisesRegex(rp.Refused, "CORE-NOT-READY: INPUT placeholder: synthetic_input"):
            self.run._common()

    def test_later_placeholder_remains_later(self):
        """FAIL-FIRST: later evidence needs no fabricated INPUT digest."""
        self.rewrite_core(lambda c: c["placeholders"].append({"name": "synthetic_future",
            "due_stage": "tuning", "producing_stage": "tuning", "blocks_input_freeze": False,
            "path": None, "sha256": None}))
        self.assertTrue(self.run._common()["ready_for_input_freeze"])

    def test_core_alias_mismatch_refuses(self):
        """FAIL-FIRST: conflicting alias and CORE expected digests refuse."""
        self.rewrite_core(lambda c: c["inputs"]["render_config"].update(sha256="0"*64))
        with self.assertRaisesRegex(rp.Refused, "PIN-BINDING-MISMATCH: .*render_config_v2.json"):
            self.run._common()

    def test_bounded_runtime_does_not_require_sweep(self):
        """FAIL-FIRST: CORE runtime evidence works without the historical exhaustive inventory."""
        self.assertEqual(rp._environment(self.inputs["env_lock"], self.inputs["runtime"])["py_ecc"], "8.0.0")

    def test_python_version_mismatch_refuses(self):
        """FAIL-FIRST: the recorded Python version is independently enforced."""
        self.change_runtime(lambda r: r.update(python_version="synthetic-mismatch"))
        with self.assertRaisesRegex(rp.Refused, "ENV-MISMATCH: python_version: .*python.* in .*runtime.json"):
            rp._environment(self.inputs["env_lock"], self.inputs["runtime"])

    def test_numpy_version_mismatch_refuses(self):
        """FAIL-FIRST: the recorded NumPy version is independently enforced."""
        self.change_runtime(lambda r: r.update(numpy_version="synthetic-mismatch"))
        with self.assertRaisesRegex(rp.Refused, "ENV-MISMATCH: numpy_version: .*numpy.* in .*runtime.json"):
            rp._environment(self.inputs["env_lock"], self.inputs["runtime"])

    def test_py_ecc_version_mismatch_refuses(self):
        """FAIL-FIRST: the BLS version refusal names the package and runtime record."""
        self.change_runtime(lambda r: r.update(py_ecc_version="synthetic-mismatch"))
        with self.assertRaisesRegex(rp.Refused, "ENV-MISMATCH: py_ecc_version: .*py_ecc.* in .*runtime.json"):
            rp._environment(self.inputs["env_lock"], self.inputs["runtime"])

    def test_astropy_version_mismatch_refuses(self):
        """FAIL-FIRST: the previously ignored Astropy version now refuses on mismatch."""
        self.change_runtime(lambda r: r.update(astropy_version="synthetic-mismatch"))
        with self.assertRaisesRegex(rp.Refused, "ENV-MISMATCH: astropy_version: .*astropy.* in .*runtime.json"):
            rp._environment(self.inputs["env_lock"], self.inputs["runtime"])

    def test_runtime_missing_extension_refuses(self):
        """FAIL-FIRST: removing an explicitly pinned extension names its loaded path."""
        self.change_runtime(lambda r: r["files"].pop(1))
        with self.assertRaisesRegex(rp.Refused, "MISSING-RUNTIME-ENTRY: .*_multiarray_umath"):
            rp._environment(self.inputs["env_lock"], self.inputs["runtime"])

    def test_scientific_lock_mismatch_still_refuses(self):
        """POSITIVE-REGRESSION: platform drift still fails the original scientific lock."""
        with patch.object(rp.platform, "machine", return_value="synthetic-other"):
            with self.assertRaisesRegex(rp.Refused, "ENV-MISMATCH: scientific lock"):
                rp._environment(self.inputs["env_lock"], self.inputs["runtime"])

    def test_runtime_artifact_tamper_names_path(self):
        """POSITIVE-REGRESSION: extra recorded runtime bytes still require their digest."""
        pin = self.put("synthetic-extension.so", b"synthetic original")
        self.change_runtime(lambda r: r["files"].append(pin))
        Path(pin["path"]).write_bytes(b"synthetic modified")
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH: " + re.escape(pin["path"])):
            rp._environment(self.inputs["env_lock"], self.inputs["runtime"])

    def test_runtime_extension_path_mismatch(self):
        """FAIL-FIRST: hashing a different file cannot stand in for the loaded extension."""
        pin = self.put("substitute.so", b"synthetic substitute")
        def mutate(r):
            r["files"][1] = {**pin, "module": "numpy.core._multiarray_umath"}
        self.change_runtime(mutate)
        with self.assertRaisesRegex(rp.Refused, "ENV-MISMATCH: extension path: .*_multiarray_umath"):
            rp._environment(self.inputs["env_lock"], self.inputs["runtime"])

    def test_recorded_lock_value_mismatch(self):
        """FAIL-FIRST: runtime lock values are enforced independently of the lock file."""
        self.change_runtime(lambda r: r["env_lock_enforced_values"].update(machine="synthetic-other"))
        with self.assertRaisesRegex(rp.Refused, "ENV-MISMATCH: recorded lock machine: .*runtime.json"):
            rp._environment(self.inputs["env_lock"], self.inputs["runtime"])

    def test_wrong_invocation_still_refuses(self):
        """POSITIVE-REGRESSION: the required BLS PYTHONPATH remains exact."""
        with patch.dict(rp.os.environ, {"PYTHONPATH": "synthetic-wrong"}):
            with self.assertRaisesRegex(rp.Refused, "ENV-MISMATCH: invocation"):
                rp._environment(self.inputs["env_lock"], self.inputs["runtime"])

    def test_false_readiness_never_calls_medium(self):
        """FAIL-FIRST: readiness refusal occurs before the real MEDIUM call boundary."""
        self.rewrite_core(lambda c: c.update(ready_for_input_freeze=False))
        calls = []
        with observe_producer(lambda frame, event, arg: calls.append(event) if event == "call" else None):
            try:
                self.run.tune(None, None, None)
            except rp.Refused as exc:
                result = (str(exc).startswith("CORE-NOT-READY:"), len(calls))
        self.assertEqual(result, (True, 0))

    def synthetic_tuning(self):
        obj = raster(0, "flip")
        identity = {key: obj[key] for key in ("objid", "ra", "dec", "brick")}
        drawn = self.put_json("synthetic-identities.json", [identity])
        previous = self.put_json("synthetic-predecessor.json", {"C": self.C,
            "stage": "draw", "verdict": "PASS", "outputs": {},
            "bindings": {"drawn_lists": {"tuning": drawn}}})
        wcs = mp._source_wcs(obj)
        planes, checks = {}, []
        for name, field in (("image-r", "image"), ("maskbits", "maskbits"), ("nexp-r", "nexp")):
            stream = io.BytesIO()
            fits.PrimaryHDU(obj[field], header=wcs.to_header()).writeto(stream)
            pin = self.put(name + ".fits", stream.getvalue())
            planes[name] = {**pin, "hdu": 0}
            checks.append(pin["sha256"] + "  legacysurvey-0400p100-" + name + ".fits.fz\n")
        labels = self.put_json("synthetic-labels.json", {"0": 1})
        inv = self.put_json("synthetic-inventory.json", {"C": self.C, "stage": "tuning",
            "drawn_list": drawn, "labels": labels, "objects": [{"objid": 0,
                "checksums": self.put("synthetic-checksums.txt", "".join(checks).encode()), "planes": planes}]})
        access = self.put_json("synthetic-access.json", {**self.anchor_fields, "C": self.C,
            "stage": "tuning", "predecessor": previous, "published_sha256": previous["sha256"],
            "bindings": rp.json_pin(previous)["bindings"], "inventory": inv})
        return previous, access, inv, labels

    def test_tune_calls_real_medium_before_labels(self):
        """FAIL-FIRST: public tune retains actual two-arm results before label access."""
        previous, access, inv, labels = self.synthetic_tuning()
        events = []
        real_read, real_producer = rp.read_pin, mp.produce_tuning_disclosure
        def read(pin):
            if pin == labels:
                events.append("labels")
            return real_read(pin)
        def produce(frame, event, arg):
            if event == "return" and frame.f_locals.get("objects"):
                events.append("medium")
        # A single synthetic identity exercises orchestration; it cannot meet
        # the unchanged 380 floor and never creates a winner or later stage.
        with patch.dict(rp.SIZES, {"tuning": 1}), patch.object(rp, "read_pin", side_effect=read), \
             observe_producer(produce):
            record = rp.json_pin(self.run.tune(previous, access, inv))
        disclosure_pin = record["outputs"].get("medium_disclosure")
        disclosure = rp.json_pin(disclosure_pin) if disclosure_pin else {}
        self.assertEqual((events, disclosure.get("schema"),
            [c["sign_flip_rate"] for c in disclosure.get("configurations", [])]),
            (["medium", "labels"], "A1-MEDIUM-PERTURBATION-1", [1.0]*96))

    def test_medium_aggregate_matches_real_batch(self):
        """FAIL-FIRST: streaming aggregation retains actual batch rates and rows."""
        objects = (raster(1, "flip"), raster(2, "negative"), raster(3, "none"))
        total = mp.produce_tuning_disclosure(())
        for obj in objects:
            rp._merge_medium(total, mp.produce_tuning_disclosure((obj,)))
        self.assertEqual((total["objects"], [(r["flips"], r["eligible_objects"], r["unscored_pairs"])
                         for r in total["configurations"]]),
                         (mp.produce_tuning_disclosure(objects)["objects"], [(1, 2, 0)]*96))

    def test_later_render_never_calls_medium(self):
        """POSITIVE-REGRESSION: a later synthetic render cannot invoke the tuning producer."""
        previous, _, inv, _ = self.synthetic_tuning()
        identities = rp.json_pin(rp.json_pin(previous)["bindings"]["drawn_lists"]["tuning"])
        with patch.object(mp, "produce_tuning_disclosure", side_effect=AssertionError("TUNING ONLY")):
            _, _, outputs = self.run._render("validation", identities, rp.json_pin(inv))
        self.assertNotIn("medium_disclosure", outputs)

    def test_missing_plane_keeps_unresolved_medium_identity(self):
        """FAIL-FIRST: an unrenderable object remains explicitly unresolved in MEDIUM."""
        previous, _, inv, _ = self.synthetic_tuning()
        identities = rp.json_pin(rp.json_pin(previous)["bindings"]["drawn_lists"]["tuning"])
        inventory = rp.json_pin(inv)
        inventory["objects"][0]["checksums"] = self.put("absent-checksums.txt", b"")
        _, receipts, outputs = self.run._render("tuning", identities, inventory)
        medium = rp.json_pin(outputs["medium_disclosure"]) if "medium_disclosure" in outputs else {}
        self.assertEqual((receipts[0]["status"], medium.get("n_objects"),
                          medium.get("eligibility_unresolved_objects")), ("RENDER-REFUSED", 1, 1))

    def test_core_pins_rechecked_before_record(self):
        """FAIL-FIRST: a changed CORE config refuses a successful stage record."""
        self.run._common()
        path = Path(self.inputs["render_config"]["path"])
        path.write_bytes(path.read_bytes() + b" ")
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH: " + re.escape(str(path))):
            self.run._record("tuning", None, {"verdict": "PASS"})

    def test_medium_wcs_rejects_distortion(self):
        """FAIL-FIRST: a distorted WCS is never silently stripped for MEDIUM."""
        wcs = mp._source_wcs(raster())
        a = np.zeros((3, 3)); a[2, 0] = .01
        wcs.sip = Sip(a, np.zeros_like(a), None, None, wcs.wcs.crpix)
        with self.assertRaisesRegex(rp.Refused, "MEDIUM-WCS-UNSUPPORTED"):
            rp._medium_wcs(wcs)

    def test_medium_wcs_rejects_changed_frame(self):
        """FAIL-FIRST: extracting numeric TAN coordinates cannot erase a changed frame."""
        wcs = mp._source_wcs(raster())
        wcs.wcs.radesys = "FK5"
        wcs.wcs.equinox = 2000.0
        wcs.wcs.set()
        with self.assertRaisesRegex(rp.Refused, "MEDIUM-WCS-LOSSY"):
            rp._medium_wcs(wcs)


if __name__ == "__main__":
    unittest.main(verbosity=2)
