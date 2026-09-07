"""V49 fail-first runtime evidence tests; mutations touch temporary copies only."""
import copy
from pathlib import Path
import re
import unittest

from _optionA_dev.agreement_run import run_path as rp
from _optionA_dev.agreement_run import runtime_binding as rb
from _optionA_dev.agreement_run import test_run_path as fixtures


class RuntimeBindingTests(unittest.TestCase):
    pin = fixtures.RunPathTests.pin
    put = fixtures.RunPathTests.put
    put_json = fixtures.RunPathTests.put_json

    def setUp(self):
        fixtures.RunPathTests.setUp(self)
        rb.preload(rp.CODE)
        self.runtime = rp.json_pin(self.inputs["runtime"])
        self.runtime["representation"] = rb.capture(lambda p: self.pin(Path(p)), rp.require)

    def check(self):
        pin = self.put_json("changed-runtime.json", self.runtime)
        return rp._environment(self.inputs["env_lock"], pin)

    def tamper_copy(self, predicate):
        evidence = self.runtime["representation"]
        original = next(p for p in evidence["files"] if predicate(p["path"]))
        target = self.put("copied-" + Path(original["path"]).name, Path(original["path"]).read_bytes())
        evidence["files"].append(target)
        Path(target["path"]).write_bytes(b"synthetic byte mutation\n")
        return re.escape(target["path"])

    def test_py_ecc_source_bytes_refuse_by_name(self):
        """FAIL-FIRST: changed py_ecc source bytes refuse by the artifact path."""
        name = self.tamper_copy(lambda p: "/py_ecc/" in p and p.endswith(".py"))
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH: " + name):
            self.check()

    def test_selected_cache_bytes_refuse_by_name(self):
        """FAIL-FIRST: a selected-import cache is byte-bound independently of source."""
        name = self.tamper_copy(lambda p: "/py_ecc/" in p and p.endswith(".pyc"))
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH: " + name):
            self.check()

    def test_native_library_bytes_refuse_by_name(self):
        """FAIL-FIRST: native library bytes beyond the two compact pins are verified."""
        name = self.tamper_copy(lambda p: p.endswith(".dylib"))
        with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH: " + name):
            self.check()

    def test_changed_shared_cache_uuid_refuses(self):
        """FAIL-FIRST: a changed active shared-cache UUID cannot pass runtime checks."""
        self.runtime["representation"]["shared_cache"]["uuid"] = "0" * 32
        with self.assertRaisesRegex(rp.Refused, "SHARED-CACHE-IDENTITY-MISMATCH"):
            self.check()

    def test_changed_os_build_refuses(self):
        """FAIL-FIRST: cache identity includes the kernel-reported OS build."""
        self.runtime["representation"]["shared_cache"]["os_build"] = "synthetic-other-build"
        with self.assertRaisesRegex(rp.Refused, "SHARED-CACHE-IDENTITY-MISMATCH"):
            self.check()

    def test_changed_cached_image_uuid_refuses_by_name(self):
        """FAIL-FIRST: each cached image has its own checked LC_UUID identity."""
        row = next(r for r in self.runtime["representation"]["images"] if r["binding"] == "DYLD-CACHE-FILE-SHA256")
        row["lc_uuid"] = "0" * 32
        with self.assertRaisesRegex(rp.Refused, "RUNTIME-IMAGE-IDENTITY-MISMATCH: " + re.escape(row["path"])):
            self.check()

    def test_deleted_import_artifact_refuses_by_name(self):
        """FAIL-FIRST: deleting a py_ecc artifact pin cannot conceal the loaded import."""
        evidence = self.runtime["representation"]
        path = next(r["path"] for r in evidence["modules"] if r["module"] == "py_ecc")
        evidence["files"] = [p for p in evidence["files"] if p["path"] != path]
        with self.assertRaisesRegex(rp.Refused, "MISSING-RUNTIME-ARTIFACT: " + re.escape(path)):
            self.check()

    def test_runtime_record_without_representation_refuses(self):
        """FAIL-FIRST: compact runtime pins cannot stand in for representation evidence."""
        del self.runtime["representation"]
        with self.assertRaisesRegex(rp.Refused, "MISSING-RUNTIME-EVIDENCE: RUNTIME_REPRESENTATION"):
            self.check()

    def test_obligation_cannot_resolve_without_evidence(self):
        """FAIL-FIRST: resolved prose and a TRUE flag cannot replace required evidence."""
        c = rp.json_pin(self.C)
        for row in c["current_preparation_obligations"]:
            if row["id"] == "RUNTIME_REPRESENTATION":
                row.pop("evidence_pin", None)
        with self.assertRaisesRegex(rp.Refused, "MISSING-RUNTIME-EVIDENCE: RUNTIME_REPRESENTATION"):
            rp._core(c)


if __name__ == "__main__":
    unittest.main(verbosity=2)
