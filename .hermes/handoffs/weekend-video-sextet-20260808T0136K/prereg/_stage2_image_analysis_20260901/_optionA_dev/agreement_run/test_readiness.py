"""V47 bounded readiness regressions; all mutations use synthetic fixtures.

The declared ids below are independent test expectations. A synthetic A1 is
explicitly bound as the fixture's reviewed revision, never as the real A1.
"""
import json
from pathlib import Path
import re
import unittest
from unittest.mock import patch

from _optionA_dev.agreement_run import run_path as rp
from _optionA_dev.agreement_run import test_run_path as fixtures

DECLARED = ("CORE_CONSUMER_RECONCILIATION", "MEDIUM_CURRENT_PREPARATION",
            "RUNTIME_REPRESENTATION")
A1_NAME = "AGREEMENT_RUN_AMENDMENT_A1_20260907.md"
SYNTHETIC_READY_A1 = (
    "The owner reports that the current module consumes CORE, refuses mismatched pins "
    "while naming the path, and blocks on readiness false (`run_path.py:301`).\n"
    "The producer was a current preparation obligation in v41/v42, not later-stage "
    "evidence; the owner's additional facts now report it produced.\n"
    "Runtime representation preparation work is resolved.\n"
    "**Runtime representation is a resolved current preparation obligation**.\n"
)


class ReadinessTests(unittest.TestCase):
    pin = fixtures.RunPathTests.pin
    put = fixtures.RunPathTests.put
    put_json = fixtures.RunPathTests.put_json

    def setUp(self):
        fixtures.RunPathTests.setUp(self)
        self.c = rp.json_pin(self.C)
        self.a1_path = self.code_root / A1_NAME
        self.a1_path.write_text(SYNTHETIC_READY_A1)
        self.c["files"] = [p for p in self.c["files"]
                           if p["path"] != str(self.a1_path.resolve())]
        self.c["a1_obligations_source"] = self.pin(self.a1_path)
        self.c["files"].append({**self.pin(self.a1_path), "status": "REAL"})
        self.c["current_preparation_obligations"] = [
            {"id": oid, "resolved": True} for oid in DECLARED]
        source_patch = patch.object(rp, "A1_REVIEWED_SHA256",
                                   self.pin(self.a1_path)["sha256"], create=True)
        source_patch.start()
        self.addCleanup(source_patch.stop)

    def remove(self, oid):
        self.c["current_preparation_obligations"] = [
            p for p in self.c["current_preparation_obligations"] if p["id"] != oid]

    def repin_a1(self, text):
        self.a1_path.write_text(text)
        pin = self.pin(self.a1_path)
        self.c["a1_obligations_source"] = pin
        self.c["files"] = [({**pin, "status": "REAL"}
                            if p["path"] == pin["path"] else p) for p in self.c["files"]]

    def test_delete_core_obligation(self):
        """FAIL-FIRST: deleting the declared CORE obligation fails by name."""
        self.remove("CORE_CONSUMER_RECONCILIATION")
        with self.assertRaisesRegex(rp.Refused, "MISSING-OBLIGATION: CORE_CONSUMER_RECONCILIATION"):
            rp._core(self.c)

    def test_delete_medium_obligation(self):
        """FAIL-FIRST: deleting the declared MEDIUM obligation fails by name."""
        self.remove("MEDIUM_CURRENT_PREPARATION")
        with self.assertRaisesRegex(rp.Refused, "MISSING-OBLIGATION: MEDIUM_CURRENT_PREPARATION"):
            rp._core(self.c)

    def test_delete_runtime_obligation(self):
        """FAIL-FIRST: deleting runtime preparation cannot make an incomplete list ready."""
        self.remove("RUNTIME_REPRESENTATION")
        with self.assertRaisesRegex(rp.Refused, "MISSING-OBLIGATION: RUNTIME_REPRESENTATION"):
            rp._core(self.c)

    def test_delete_all_obligations(self):
        """FAIL-FIRST: an empty obligations list fails with every declared missing id."""
        self.c["current_preparation_obligations"] = []
        with self.assertRaisesRegex(rp.Refused,
                "MISSING-OBLIGATION: CORE_CONSUMER_RECONCILIATION.*"
                "MISSING-OBLIGATION: MEDIUM_CURRENT_PREPARATION.*"
                "MISSING-OBLIGATION: RUNTIME_REPRESENTATION"):
            rp._core(self.c)

    def test_duplicate_obligation(self):
        """FAIL-FIRST: duplicates cannot substitute for a unique declaration."""
        self.c["current_preparation_obligations"].append({"id": DECLARED[0], "resolved": True})
        with self.assertRaisesRegex(rp.Refused, "DUPLICATE-OBLIGATION: CORE_CONSUMER_RECONCILIATION"):
            rp._core(self.c)

    def test_undeclared_obligation(self):
        """FAIL-FIRST: an additional resolved obligation must also be declared in code/A1."""
        self.c["current_preparation_obligations"].append({"id": "UNDECLARED", "resolved": True})
        with self.assertRaisesRegex(rp.Refused, "UNDECLARED-OBLIGATION: UNDECLARED"):
            rp._core(self.c)

    def test_runtime_unresolved_still_blocks(self):
        """POSITIVE-REGRESSION: present unresolved runtime work defeats a TRUE flag."""
        self.c["current_preparation_obligations"][-1].update(resolved=False, evidence="unfinished")
        with self.assertRaisesRegex(rp.Refused, "CORE-NOT-READY: RUNTIME_REPRESENTATION: unfinished"):
            rp._core(self.c)

    def test_a1_manifest_status_divergence(self):
        """FAIL-FIRST: matching declared ids with contradictory A1 status are detected."""
        text = SYNTHETIC_READY_A1.replace(
            "Runtime representation preparation work is resolved.",
            "Runtime representation remains current preparation work to be done.").replace(
            "Runtime representation is a resolved current preparation obligation",
            "Runtime representation remains a current preparation obligation to be done")
        self.repin_a1(text)
        with patch.object(rp, "A1_REVIEWED_SHA256", self.pin(self.a1_path)["sha256"], create=True):
            with self.assertRaisesRegex(rp.Refused, "A1-OBLIGATION-MISMATCH: RUNTIME_REPRESENTATION"):
                rp._core(self.c)

    def test_a1_deleted_statement_even_when_repinned(self):
        """FAIL-FIRST: removing an A1 declaration cannot be concealed by repinning A1."""
        self.repin_a1(SYNTHETIC_READY_A1.replace(
            "Runtime representation preparation work is resolved.\n", ""))
        with self.assertRaisesRegex(rp.Refused, "A1-OBLIGATION-SOURCE-CHANGED:"):
            rp._core(self.c)

    def test_a1_added_obligation_even_when_repinned(self):
        """FAIL-FIRST: unfamiliar new prose obligations require a reviewed mapping update."""
        self.repin_a1(SYNTHETIC_READY_A1 + "Additional runtime audit remains current preparation work.\n")
        with self.assertRaisesRegex(rp.Refused, "A1-OBLIGATION-SOURCE-CHANGED:"):
            rp._core(self.c)

    def test_a1_missing_source(self):
        """FAIL-FIRST: removing the A1 source binding cannot skip the cross-check."""
        del self.c["a1_obligations_source"]
        with self.assertRaisesRegex(rp.Refused, "MISSING-A1-OBLIGATIONS-SOURCE"):
            rp._core(self.c)

    def test_complete_resolved_fixture_passes(self):
        """POSITIVE-REGRESSION: a complete resolved fixture can pass the real CORE gate."""
        self.assertEqual(rp._core(self.c), self.c["inputs"])

    def test_recorded_readiness_is_false(self):
        """FAIL-FIRST: the actual authoring register records runtime-blocked readiness FALSE."""
        manifest = json.loads((fixtures.LANE /
            "_optionA_dev/agreement_run/INPUT_MANIFEST_A1_CORE.json").read_text())
        self.assertIs(manifest["ready_for_input_freeze"], False)

    def test_runtime_digest_rechecked_before_import(self):
        """FAIL-FIRST: a mutation after initial runtime hashing fails at the pre-use recheck."""
        runtime = rp.json_pin(self.inputs["runtime"])
        original = runtime["files"][1]
        substitute = self.put("synthetic-extension.so", Path(original["path"]).read_bytes())
        runtime["files"][1] = {**substitute, "module": original["module"]}
        runtime_pin = self.put_json("runtime-preuse.json", runtime)
        register = rp._file_register
        def mutate_after_check(entries, scope):
            result = register(entries, scope)
            if scope == "RUNTIME":
                Path(substitute["path"]).write_bytes(b"synthetic changed after first check")
            return result
        with patch.object(rp, "_file_register", side_effect=mutate_after_check):
            with self.assertRaisesRegex(rp.Refused, "DIGEST-MISMATCH: " + re.escape(substitute["path"])):
                rp._environment(self.inputs["env_lock"], runtime_pin)


if __name__ == "__main__":
    unittest.main(verbosity=2)
