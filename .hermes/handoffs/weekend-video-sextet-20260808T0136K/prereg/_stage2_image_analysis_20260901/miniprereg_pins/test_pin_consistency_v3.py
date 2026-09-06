#!/usr/bin/env python3
"""Fixture tests for check_pin_consistency_v3.py; standard library only.

These are deletion probes. Each asserts the EXACT defect the checker is meant to
catch, and that the checker still passes a clean document -- so a broken checker
that refuses everything, or one that accepts everything, both fail here.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

import check_pin_consistency_v3 as cpc


class TestSupersession(unittest.TestCase):
    def test_higher_version_supersedes_lower(self):
        pins = {"d/a.json": "0" * 64, "d/a_v2.json": "1" * 64}
        self.assertEqual(cpc.superseded_siblings(pins), {"a.json": "a_v2.json"})

    def test_v3_supersedes_both_predecessors(self):
        pins = {"d/a.py": "0" * 64, "d/a_v2.py": "1" * 64, "d/a_v3.py": "2" * 64}
        self.assertEqual(cpc.superseded_siblings(pins),
                         {"a.py": "a_v3.py", "a_v2.py": "a_v3.py"})

    def test_a_lone_pin_is_never_superseded(self):
        self.assertEqual(cpc.superseded_siblings({"d/a.py": "0" * 64}), {})

    def test_unrelated_stems_do_not_form_a_family(self):
        pins = {"d/a.py": "0" * 64, "d/b_v2.py": "1" * 64}
        self.assertEqual(cpc.superseded_siblings(pins), {})

    def test_same_stem_in_different_directories_is_not_a_family(self):
        pins = {"d/a.py": "0" * 64, "e/a_v2.py": "1" * 64}
        self.assertEqual(cpc.superseded_siblings(pins), {})


class TestPinParsing(unittest.TestCase):
    def test_name_then_hash(self):
        text = "The renderer is `x/y.py`, SHA-256 `" + "a" * 64 + "`."
        self.assertEqual(cpc.pinned(text), {"x/y.py": "a" * 64})

    def test_hash_then_name(self):
        text = "SHA-256 `" + "b" * 64 + "` is the file `x/y.py`."
        self.assertEqual(cpc.pinned(text), {"x/y.py": "b" * 64})

    def test_a_bare_filename_cannot_capture_the_next_pin(self):
        """The V19 parser paired a prose mention of widget_v2.py with the NEXT
        pin's hash, silently dropping pkg/harness_v2.py from the set."""
        text = ("It supersedes `widget_v2.py`. The harness is "
                "`pkg/harness_v2.py`, SHA-256 `" + "c" * 64 + "`.")
        parsed = cpc.pinned(text)
        self.assertEqual(parsed, {"pkg/harness_v2.py": "c" * 64})
        self.assertNotIn("widget_v2.py", parsed)





class TestDeclaredSupersession(unittest.TestCase):
    """The rename case, and the failure that made prose-inference unusable."""

    def test_explicit_table_is_read(self):
        doc = "`a/old.py` -> `b/new_v3.py`"
        self.assertEqual(cpc.superseded_siblings({}, doc), {"old.py": "new_v3.py"})

    def test_prose_alone_declares_nothing(self):
        """A sentence merely containing the word does NOT mark a file superseded.
        Inferring it that way marked successors superseded and lost real defects."""
        doc = "The harness `a/new_v3.py` imports the renderer rather than the superseded module."
        self.assertEqual(cpc.superseded_siblings({}, doc), {})

    def test_table_and_version_family_combine(self):
        pins = {"d/a.json": "0" * 64, "d/a_v2.json": "1" * 64}
        doc = "`x/old.py` -> `x/new_v2.py`"
        self.assertEqual(cpc.superseded_siblings(pins, doc),
                         {"old.py": "new_v2.py", "a.json": "a_v2.json"})


class TestScanScope(unittest.TestCase):
    """Only executable text raises a finding; only genuine acknowledgement clears one."""

    def test_a_bare_use_is_not_acknowledged(self):
        self.assertFalse(cpc.acknowledges('CONFIG = "pkg/old_config.json"', "old_config.json"))

    def test_a_supersession_note_is_acknowledged(self):
        text = "It replaces old_config.json, which is superseded and retained."
        self.assertTrue(cpc.acknowledges(text, "old_config.json"))

    def test_one_unacknowledged_use_among_many_mentions_still_counts(self):
        text = ('# old_config.json is superseded and retained.\n'
                'CONFIG = "pkg/old_config.json"\n')
        self.assertFalse(cpc.acknowledges(text, "old_config.json"))


class TestImportScanning(unittest.TestCase):
    """A Python import never contains '.py'. The filename scan was blind to the
    likeliest form of a stale reference, and passed a document that had one."""

    def _write(self, body: str):
        import tempfile
        d = tempfile.mkdtemp()
        p = Path(d) / "m.py"
        p.write_text(body, encoding="utf-8")
        return p

    def test_plain_import_is_seen(self):
        p = self._write("import old_module\n")
        self.assertIn("old_module", cpc.imported_modules(p))

    def test_from_import_is_seen(self):
        p = self._write("from pkg.old_module import thing\n")
        mods = cpc.imported_modules(p)
        self.assertIn("old_module", mods)
        self.assertIn("pkg.old_module", mods)

    def test_dotted_package_import_records_the_leaf(self):
        p = self._write("import a.b.leaf_module\n")
        self.assertIn("leaf_module", cpc.imported_modules(p))

    def test_a_filename_scan_would_have_missed_all_of_these(self):
        """The exact blind spot, asserted so it cannot silently return."""
        body = "from anchor_gate.instrument_identity import validate_environment\n"
        p = self._write(body)
        filename = "instrument_identity" + ".py"   # built, not written: the literal
        self.assertNotIn(filename, body)           # would itself be a stale reference
        self.assertIn("instrument_identity", cpc.imported_modules(p))

    def test_unparseable_source_yields_no_imports_rather_than_crashing(self):
        p = self._write("def (\n")
        self.assertEqual(cpc.imported_modules(p), set())


class TestTheHarnessRunsEveryTest(unittest.TestCase):
    """V20 and V21 shipped this file with `unittest.main()` in the MIDDLE, left there
    when classes were appended after it. Run as a script it executed 8 of 19 tests and
    reported OK; the 11 it skipped were the AST import checks added to catch exactly the
    kind of defect this file exists to catch. A control that silently does not run is
    worse than no control, because the receipt says OK. Asserted here so it cannot recur."""

    def test_the_main_guard_is_the_last_top_level_statement(self):
        """Parsed with ast, not counted as text: an earlier version of this test
        counted occurrences of the call and failed on its own docstrings mentioning
        it. A check that trips over its own wording is not a check."""
        import ast, pathlib
        tree = ast.parse(pathlib.Path(__file__).read_text(encoding="utf-8"))
        last = tree.body[-1]
        self.assertIsInstance(last, ast.If, "the main guard is not the last statement")
        self.assertEqual(getattr(last.test.left, "id", None), "__name__")
        after_guard = [n for n in tree.body if n.lineno > last.lineno]
        self.assertEqual(after_guard, [], "code follows the guard; it will not run")

    def test_every_test_method_defined_in_the_file_is_collected(self):
        """In-process, deliberately: an earlier version of this test shelled out to
        re-run the file, which re-ran this test, which shelled out again. That was a
        fork bomb and it was mine. The property is structural and needs no subprocess."""
        import pathlib
        text = pathlib.Path(__file__).read_text(encoding="utf-8")
        defined = len(re.findall(r"^    def test_", text, re.M))
        loaded = unittest.defaultTestLoader.loadTestsFromName(
            pathlib.Path(__file__).stem).countTestCases()
        self.assertEqual(defined, loaded,
                         "tests are defined that the loader does not collect")


class TestRootLevelPins(unittest.TestCase):
    def test_tight_bare_name_is_a_pin(self):
        text = "The selection `SELECTION_20260905.csv`, SHA-256 `" + "d" * 64 + "` has 2,000 rows."
        self.assertEqual(cpc.pinned(text), {"SELECTION_20260905.csv": "d" * 64})

    def test_a_bare_name_far_from_a_hash_is_still_not_a_pin(self):
        """The V19 hijack must stay impossible: no adjacency, no pin."""
        text = "It supersedes `renderer_v2.py`. The harness is `x/h.py`, SHA-256 `" + "e" * 64 + "`."
        self.assertEqual(cpc.pinned(text), {"x/h.py": "e" * 64})

    def test_txt_lists_are_pins(self):
        text = "list `dir/_bricks.txt`, SHA-256 `" + "f" * 64 + "`."
        self.assertIn("dir/_bricks.txt", cpc.pinned(text))


class TestPackageInitClosure(unittest.TestCase):
    """V32: study_renderer/__init__.py, unpinned, imported the superseded renderer; every pinned
    module looked clean while the package symbol was stale. The relative import form is the one
    a package init uses, so it is the one asserted."""

    def test_relative_import_in_an_init_is_seen(self):
        import tempfile, pathlib
        d = pathlib.Path(tempfile.mkdtemp()); (d / "__init__.py").write_text("from .renderer import render_cutout\n")
        mods = cpc.imported_modules(d / "__init__.py")
        self.assertIn("renderer", mods)

    def test_a_current_init_is_clean(self):
        import tempfile, pathlib
        d = pathlib.Path(tempfile.mkdtemp()); (d / "__init__.py").write_text("from .renderer_v4 import render_cutout\n")
        self.assertNotIn("renderer", cpc.imported_modules(d / "__init__.py") - {"renderer_v4"})


class V3Additions(unittest.TestCase):
    def test_alias_import_is_seen(self):
        import pathlib, tempfile
        d = pathlib.Path(tempfile.mkdtemp()); f = d / "m.py"; f.write_text("from study_renderer import renderer_v4 as rv\nimport a.b as c\n")
        mods = cpc.imported_modules(f); self.assertIn("renderer_v4", mods); self.assertIn("study_renderer.renderer_v4", mods); self.assertIn("b", mods)
    def test_comparison_only_marker_parsed(self):
        self.assertEqual(cpc.comparison_only("x <!-- COMPARISON-ONLY: study_renderer/test_a.py, study_renderer/test_b.py --> y"), {"study_renderer/test_a.py", "study_renderer/test_b.py"})
        self.assertEqual(cpc.comparison_only("no marker"), set())
    def test_bare_pin_form_parsed(self):
        doc = "`x.py` `" + "a" * 64 + "` and `y.py`, SHA-256 `" + "b" * 64 + "`"            # bare names (no directory) in both tight forms
        found = {m.group(1): m.group(2) for m in cpc.BARE_RE.finditer(doc)}
        self.assertEqual(found, {"x.py": "a" * 64, "y.py": "b" * 64})
class V3BareResolution(unittest.TestCase):
    def test_bare_pin_resolves_to_unique_basename_under_pinned_dirs(self):
        doc = "`renderer_v4.py` `" + "a" * 64 + "` and `no_such_file_xyz.py` `" + "b" * 64 + "`"
        pins = cpc.pinned(doc)
        self.assertIn("study_renderer/renderer_v4.py", pins); self.assertEqual(pins["study_renderer/renderer_v4.py"], "a" * 64)
        self.assertIn("no_such_file_xyz.py", pins)                                          # unresolvable stays bare → reported MISSING
if __name__ == "__main__":
    unittest.main()
