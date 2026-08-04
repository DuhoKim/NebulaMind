import importlib.util
import json
import shutil
import subprocess
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "run_weekend_journal_sprint.py"
spec = importlib.util.spec_from_file_location("weekend", SCRIPT)
weekend = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(weekend)


class WeekendSprintTests(unittest.TestCase):
    def setUp(self):
        self.tmp = ROOT / "tests" / "_tmp_weekend"
        if self.tmp.exists():
            shutil.rmtree(self.tmp)
        self.tmp.mkdir(parents=True)

    def tearDown(self):
        if self.tmp.exists():
            shutil.rmtree(self.tmp)
        for name in ["PREFLIGHT.json", "SPRINT_STATUS.json"]:
            path = ROOT / name
            if path.exists():
                path.unlink()

    def test_clean_candidate_copy_excludes_old_receipts_and_keeps_tex_figures(self):
        seed = self.tmp / "seed"
        keep_tex = seed / "flagship_rp1" / "aastex" / "rp1_flagship_polished.tex"
        keep_tex.parent.mkdir(parents=True)
        keep_tex.write_text("paper", encoding="utf-8")
        keep_fig = seed / "flagship_rp1" / "figures" / "real_figure.pdf"
        keep_fig.parent.mkdir(parents=True)
        keep_fig.write_bytes(b"%PDFfigure")
        excluded = [
            seed / "flagship_rp1" / "aastex" / "old.pdf",
            seed / "flagship_rp1" / "aastex" / "rp1_flagship_polished.aux",
            seed / "flagship_rp1" / "logs" / "run.log",
            seed / "flagship_rp1" / "CYCLE_49_SUMMARY.md",
            seed / "supplementary_denominator_atlas" / "aastex" / "BUILD_RECEIPT.json",
        ]
        for path in excluded:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("old", encoding="utf-8")
        supp = seed / "supplementary_denominator_atlas" / "aastex" / "supplementary_denominator_atlas.tex"
        supp.parent.mkdir(parents=True, exist_ok=True)
        supp.write_text("supp", encoding="utf-8")
        provenance = seed / "provenance" / "REAL_DATA_SOURCE_CUSTODY.json"
        provenance.parent.mkdir(parents=True)
        provenance.write_text('{"marker":"custody"}\n', encoding="utf-8")

        dest = self.tmp / "dest"
        copied = weekend.clean_candidate_copy(seed, dest)
        copied_paths = {r["path"] for r in copied}

        self.assertIn("flagship_rp1/aastex/rp1_flagship_polished.tex", copied_paths)
        self.assertIn("flagship_rp1/figures/real_figure.pdf", copied_paths)
        self.assertIn("supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex", copied_paths)
        self.assertIn("provenance/REAL_DATA_SOURCE_CUSTODY.json", copied_paths)
        self.assertFalse((dest / "flagship_rp1" / "aastex" / "old.pdf").exists())
        self.assertFalse((dest / "flagship_rp1" / "logs" / "run.log").exists())
        self.assertFalse((dest / "flagship_rp1" / "CYCLE_49_SUMMARY.md").exists())
        self.assertEqual(keep_tex.read_text(encoding="utf-8"), "paper")

    def test_report_validation_rejects_missing_tiny_truncated_and_missing_verdict(self):
        missing = self.tmp / "missing.md"
        ok, reasons = weekend.validate_report(missing)
        self.assertFalse(ok)
        self.assertIn("missing report", reasons)

        tiny = self.tmp / "tiny.md"
        tiny.write_text("JOURNAL_LEVEL_PASS: NO\n", encoding="utf-8")
        ok, reasons = weekend.validate_report(tiny)
        self.assertFalse(ok)
        self.assertTrue(any("tiny report" in r for r in reasons))

        truncated = self.tmp / "truncated.md"
        truncated.write_text("x" * 200 + "\n[TRUNCATED]\nJOURNAL_LEVEL_PASS: NO\n", encoding="utf-8")
        ok, reasons = weekend.validate_report(truncated)
        self.assertFalse(ok)
        self.assertIn("report contains [TRUNCATED]", reasons)

        no_verdict = self.tmp / "no_verdict.md"
        no_verdict.write_text("x" * 220, encoding="utf-8")
        ok, reasons = weekend.validate_report(no_verdict)
        self.assertFalse(ok)
        self.assertIn("missing JOURNAL_LEVEL_PASS verdict", reasons)

        good = self.tmp / "good.md"
        good.write_text("Concrete section advice.\n" + "x" * 220 + "\nJOURNAL_LEVEL_PASS: NO\n", encoding="utf-8")
        ok, reasons = weekend.validate_report(good)
        self.assertTrue(ok, reasons)

    def test_journal_metrics_counts_words_citations_equations_tables_figures(self):
        flagship = r"""
        \begin{abstract}""" + ("abstract " * 210) + r"""\end{abstract}
        \section{Intro} """ + ("word " * 5100) + r"""
        \citep{a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u}
        \begin{equation}x=1\end{equation}
        \[ y=2 \]
        \begin{deluxetable}{cc}\end{deluxetable}
        \begin{table}\end{table}
        \begin{table*}\end{table*}
        \begin{figure}\end{figure}
        \begin{figure*}\end{figure*}
        Prior work reports 1 published comparison value.
        8,146 -1.309 [-1.334,-1.283] 249,917 60,000 24.0
        """
        supplement = "supplement " * 4100
        metrics = weekend.journal_metrics(flagship, supplement)
        self.assertGreaterEqual(metrics["flagship_words_approx"], 5000)
        self.assertGreaterEqual(metrics["abstract_words_approx"], 200)
        self.assertEqual(metrics["citation_key_count"], 21)
        self.assertEqual(metrics["equation_count"], 2)
        self.assertEqual(metrics["table_count"], 3)
        self.assertEqual(metrics["figure_count"], 2)
        self.assertEqual(metrics["numeric_invariants_missing"], [])
        self.assertEqual(weekend.classify_quality_blockers(metrics), [])

    def test_strict_log_parsing_extracts_compile_issues(self):
        log = r"""
        ! LaTeX Error: File `missing.sty' not found.
        LaTeX Warning: Citation `Smith2020' undefined.
        LaTeX Warning: Reference `fig:a' undefined.
        Package aastex Warning: deprecated command.
        Overfull \hbox (1.0pt too wide)
        Underfull \vbox (badness 10000)
        Emergency stop.
        """
        parsed = weekend.parse_compile_log(log)
        self.assertTrue(parsed["fatal_errors"])
        self.assertTrue(parsed["undefined_citations"])
        self.assertTrue(parsed["undefined_references"])
        self.assertTrue(parsed["missing_includes"])
        self.assertTrue(parsed["aastex_deprecations"])
        self.assertEqual(parsed["overfull_box_count"], 1)
        self.assertEqual(parsed["underfull_box_count"], 1)

    def test_integrity_and_quality_blockers_are_separate(self):
        flagship = r"\begin{abstract}short\end{abstract} short \citep{a} 8,146 -1.309 [-1.334,-1.283] 249,917 60,000 24.0"
        supplement = "short"
        metrics = weekend.journal_metrics(flagship, supplement)
        compile_audit = {
            "build_ok": True,
            "clean_ok": True,
            "fatal_errors": [],
            "missing_includes": [],
            "undefined_citations": [],
            "undefined_references": [],
            "writer_scope_violations": [],
        }
        provenance = {"new_result_without_provenance": False}

        self.assertEqual(weekend.classify_integrity_blockers(metrics, compile_audit, provenance), [])
        quality = weekend.classify_quality_blockers(metrics)
        self.assertIn("flagship main text outside 5000-8000 target", quality)
        self.assertIn("supplement below 4000-word target", quality)

        compile_audit["build_ok"] = False
        integrity = weekend.classify_integrity_blockers(metrics, compile_audit, provenance)
        self.assertIn("strict compile failed", integrity)

    def test_negated_mock_data_phrase_is_not_an_integrity_failure(self):
        flagship = r"\begin{abstract}short\end{abstract} No mock, synthetic, placeholder, or toy data were used. 8,146 -1.309 [-1.334,-1.283] 249,917 60,000 24.0"
        metrics = weekend.journal_metrics(flagship, "supplement")
        self.assertEqual(metrics["bad_data_use_hits"], [])
        compile_audit = {
            "build_ok": True,
            "fatal_errors": [],
            "missing_includes": [],
            "undefined_citations": [],
            "undefined_references": [],
            "writer_scope_violations": [],
        }
        self.assertEqual(weekend.classify_integrity_blockers(metrics, compile_audit, {"new_result_without_provenance": False}), [])

    def test_candidate_custody_tracks_active_path_and_manuscript_hashes(self):
        candidate = self.tmp / "candidate"
        for rel in weekend.TEX_RELATIVES:
            path = candidate / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"paper {rel}\n", encoding="utf-8")
        weekend.write_candidate_provenance(candidate, self.tmp / "seed", [], {"counts": {"csv_json": 0}, "files": []})
        self.assertEqual(weekend.scan_provenance(candidate)["custody_errors"], [])

        (candidate / weekend.FLAGSHIP_TEX).write_text("changed\n", encoding="utf-8")
        self.assertTrue(weekend.scan_provenance(candidate)["custody_errors"])
        weekend.refresh_candidate_custody(candidate)
        self.assertEqual(weekend.scan_provenance(candidate)["custody_errors"], [])

    def test_writer_scope_reverts_outside_changes_and_preserves_allowed_changes(self):
        candidate = self.tmp / "candidate"
        backup = self.tmp / "backup"
        tex = candidate / weekend.FLAGSHIP_TEX
        tex.parent.mkdir(parents=True)
        tex.write_text("original", encoding="utf-8")
        other = candidate / "flagship_rp1" / "figures" / "real.pdf"
        other.parent.mkdir(parents=True)
        other.write_bytes(b"%PDF-original")
        shutil.copytree(candidate, backup)

        tex.write_text("allowed revision", encoding="utf-8")
        other.write_bytes(b"tampered")
        stray = candidate / "stray.txt"
        stray.write_text("not allowed", encoding="utf-8")

        violations = weekend.revert_outside_writer_scope(
            candidate,
            backup,
            {weekend.FLAGSHIP_TEX},
            {Path("analysis_extensions")},
        )

        self.assertEqual(tex.read_text(encoding="utf-8"), "allowed revision")
        self.assertEqual(other.read_bytes(), b"%PDF-original")
        self.assertFalse(stray.exists())
        self.assertEqual(violations, ["flagship_rp1/figures/real.pdf", "stray.txt"])

    def test_preflight_argument_behavior_avoids_provider_calls(self):
        seed = self.tmp / "seed"
        seed.mkdir()
        with mock.patch.object(weekend, "command_exists", return_value=False), mock.patch.object(subprocess, "run", side_effect=AssertionError("provider call")):
            rc = weekend.main(["--preflight", "--duration-seconds", "10", "--max-cycles", "2", "--slot-seconds", "5", "--seed-package", str(seed)])
        self.assertEqual(rc, 0)
        data = json.loads((ROOT / "PREFLIGHT.json").read_text(encoding="utf-8"))
        self.assertFalse(data["would_call_providers"])
        self.assertEqual(data["duration_seconds"], 10)
        self.assertEqual(data["max_cycles"], 2)
        self.assertEqual(data["slot_seconds"], 5)


if __name__ == "__main__":
    unittest.main()
