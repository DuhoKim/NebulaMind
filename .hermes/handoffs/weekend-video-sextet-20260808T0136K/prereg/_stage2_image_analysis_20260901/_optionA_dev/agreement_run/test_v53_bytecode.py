"""V53 cache and packet refusals. Only retained synthetic fixtures are written.

No production pins/caches, A1 wording, or study-stage APIs are mutated.
"""
import ast
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import py_compile
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from _optionA_dev.agreement_run import bytecode_correspondence as bc

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "_optionA_dev/agreement_run"
INTERPRETER = "/Library/Developer/CommandLineTools/usr/bin/python3"


def pin(path):
    path = Path(path).resolve()
    return {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def read_pin(row):
    raw = Path(row["path"]).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == row["sha256"], "DIGEST-MISMATCH: " + row["path"])
    return raw


def directory():
    parent = BASE / "_v53_test_fixtures"
    parent.mkdir(exist_ok=True)
    return Path(tempfile.mkdtemp(dir=str(parent)))


class CorrespondenceTests(unittest.TestCase):
    def setUp(self):
        self.root = directory()
        self.source = self.root / "module.py"
        self.source.write_text('VALUE = "current"\nassert VALUE\n')
        self.code = {"module.py": pin(self.source)["sha256"]}
        self.home_patch = patch.object(Path, "home", return_value=self.root / "home")
        self.home_patch.start()
        self.addCleanup(self.home_patch.stop)
        self.prefix_patch = patch.object(sys, "pycache_prefix", str(self.root / "active-cache"))
        self.prefix_patch.start()
        self.addCleanup(self.prefix_patch.stop)
        tag = sys.implementation.cache_tag
        self.paths = [self.source.parent / "__pycache__" / ("module." + tag + ".pyc"),
                      self.root / "home/Library/Caches/com.apple.python" /
                      str(self.source.parent).lstrip("/") / ("module." + tag + ".pyc"),
                      Path(importlib.util.cache_from_source(str(self.source))),
                      self.source.with_suffix(".pyc")]
        self.files = {}
        for path in self.paths:
            py_compile.compile(str(self.source), cfile=str(path), doraise=True)
            self.register(path)

    def register(self, path):
        row = {**pin(path), "status": "REAL", "kind": "our_imported_bytecode", "source": "module.py"}
        self.files[row["path"]] = row

    def verify(self):
        return bc.verify(self.root, self.code, self.files, read_pin, require)

    def test_all_locations_correspond(self):
        self.assertEqual(set(map(str, self.paths)), set(self.verify()))

    def test_each_location_requires_registration(self):
        for path in self.paths:
            with self.subTest(path=path):
                row = self.files.pop(str(path))
                with self.assertRaisesRegex(ValueError, "MISSING-CORE-ENTRY: .*module"):
                    self.verify()
                self.files[str(path)] = row

    def test_digest_registered_wrong_code_refuses_each_location(self):
        wrong = self.root / "wrong-source.py"
        wrong.write_text('VALUE = "stale"\n')
        for path in self.paths:
            with self.subTest(path=path):
                py_compile.compile(str(wrong), cfile=str(path), dfile=str(self.source), doraise=True)
                self.register(path)  # Correct digest of the WRONG program.
                with self.assertRaises(ValueError) as caught:
                    self.verify()
                self.assertIn("CACHE-SOURCE-MISMATCH: " + str(path), str(caught.exception))
                self.assertIn("module=" + str(self.source), str(caught.exception))
                print("EXPECTED REFUSAL:", caught.exception)
                py_compile.compile(str(self.source), cfile=str(path), doraise=True)
                self.register(path)

    def test_corresponding_code_still_requires_digest(self):
        path = str(self.paths[0])
        self.files[path]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "DIGEST-MISMATCH"):
            self.verify()

    def test_relabeling_cache_does_not_waive_equality(self):
        self.files[str(self.paths[0])]["kind"] = "our_source_code"
        with self.assertRaisesRegex(ValueError, "CACHE-CORE-BINDING-MISMATCH"):
            self.verify()

    def test_optimization_variants_checked_at_their_own_level(self):
        for level in (1, 2):
            path = self.paths[0].with_name("module." + sys.implementation.cache_tag + ".opt-%d.pyc" % level)
            py_compile.compile(str(self.source), cfile=str(path), optimize=level, doraise=True)
            self.register(path)
        self.assertEqual(len(self.verify()), 6)


class PacketRefusalTests(unittest.TestCase):
    def setUp(self):
        self.root = directory()
        self.base = self.root / "_optionA_dev/agreement_run"
        self.base.mkdir(parents=True)
        c = json.loads((BASE / "INPUT_MANIFEST_A1_CORE.json").read_bytes())
        # A temporary candidate gives each rejection only one deliberate defect.
        tree = ast.parse((BASE / "run_path.py").read_bytes())
        code = next(ast.literal_eval(node.value) for node in tree.body
                    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "CODE" for t in node.targets))
        updates = []
        for rel in code:
            src = ROOT / rel
            dst = self.root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            if rel.endswith("/verify_core.py"):
                shutil.copyfile(src, dst)
            else:
                dst.symlink_to(src)
            row = pin(src)
            c["code"][rel] = row["sha256"]
            updates.append({**row, "status": "REAL", "kind": "our_source_code"})
            for path in bc.candidates(src):
                updates.append({**pin(path), "status": "REAL", "kind": "our_imported_bytecode", "source": rel})
        c["a1_obligations_source"] = pin(ROOT / "AGREEMENT_RUN_AMENDMENT_A1_20260907.md")
        updates.append({**c["a1_obligations_source"], "status": "REAL", "kind": "a1_obligation_source"})
        files = {str(Path(row["path"]).resolve()): row for row in c["files"]}
        files.update({row["path"]: row for row in updates})
        c["files"] = list(files.values())
        self.core = c
        self.env = dict(os.environ, PYTHONPATH=str(ROOT / "_optionA_dev/_venv_bls/lib/python3.9/site-packages"),
                        PYTHONDONTWRITEBYTECODE="1")

    def execute(self, defect, assembler=False, predecessor=False):
        c = copy.deepcopy(self.core)
        if defect == "a1":
            name = c["a1_obligations_source"]["path"]
            c["a1_obligations_source"]["sha256"] = "0" * 64
            for row in c["files"]:
                if row["path"] == name:
                    row["sha256"] = "0" * 64
        else:
            wrong = self.base / "wrong-source.py"
            wrong.write_text('raise RuntimeError("STALE CACHE MUST NEVER EXECUTE")\n')
            cache = self.base / ("run_path." + sys.implementation.cache_tag + ".pyc")
            py_compile.compile(str(wrong), cfile=str(cache), doraise=True)
            name = str(cache)
            c["files"].append({**pin(cache), "status": "REAL", "kind": "our_imported_bytecode",
                               "source": "_optionA_dev/agreement_run/run_path.py"})
        path = self.base / "INPUT_MANIFEST_A1_CORE.json"
        path.write_text(json.dumps(c))
        if assembler:
            script = self.root / "scripts/assemble_adoption_packet.py"
            script.parent.mkdir(exist_ok=True)
            shutil.copyfile(BASE / "_v52_original_assembler.txt" if predecessor else ROOT / "scripts/assemble_adoption_packet.py", script)
            command = [INTERPRETER, "-B", str(script)]
        else:
            command = [INTERPRETER, "-B", str(self.base / "verify_core.py"), str(path), pin(path)["sha256"]]
        result = subprocess.run(command, cwd=str(self.root), env=self.env, capture_output=True, text=True)
        expected = "DIGEST-MISMATCH: " + name if defect == "a1" else "CACHE-SOURCE-MISMATCH: " + name
        if predecessor:
            self.assertIn("`ready_for_input_freeze` = **True**", result.stdout)
            self.assertNotIn(expected, result.stdout)
            print("PREDECESSOR GAP:", defect, "stored readiness=True despite", expected)
        else:
            self.assertEqual(result.returncode, 2, result.stderr + result.stdout)
            self.assertIn(expected, result.stdout)
            self.assertNotIn("`ready_for_input_freeze` = **True**", result.stdout)
            print("EXPECTED REFUSAL:", "assembler" if assembler else "consumer", expected)

    def test_consumer_noncorresponding_cache(self):
        self.execute("cache")

    def test_consumer_stale_a1_pin(self):
        self.execute("a1")

    def test_assembler_noncorresponding_cache(self):
        self.execute("cache", assembler=True)

    def test_assembler_stale_a1_pin(self):
        self.execute("a1", assembler=True)

    def test_predecessor_reports_saved_true_for_both_defects(self):
        for defect in ("cache", "a1"):
            self.execute(defect, assembler=True, predecessor=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
