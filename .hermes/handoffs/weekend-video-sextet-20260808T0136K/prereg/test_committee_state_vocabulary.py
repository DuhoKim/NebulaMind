#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
import committee_state_vocabulary as vocabulary


class CommitteeStateVocabularyTests(unittest.TestCase):
    def test_mapping_is_total_and_injective(self) -> None:
        self.assertEqual(set(vocabulary.COMMITTEE_TO_HC1H), set(vocabulary.COMMITTEE_STATES))
        self.assertEqual(set(vocabulary.COMMITTEE_TO_HC1H.values()), set(vocabulary.HC1H_STATES))
        self.assertEqual(
            len(set(vocabulary.COMMITTEE_TO_HC1H.values())),
            len(vocabulary.COMMITTEE_TO_HC1H),
        )

    def test_committee_and_harness_import_the_shared_vocabulary(self) -> None:
        probes = (
            (
                ROOT / "venv_torch" / "bin" / "python",
                ROOT / "_committee_20260820",
                "committee",
                "COMMITTEE_STATES",
            ),
            (Path(sys.executable), ROOT / "handcheck", "nm_handcheck", "HC1H_STATES"),
        )
        observed = []
        for interpreter, module_dir, module_name, attribute in probes:
            script = (
                "import json,sys;"
                f"sys.path[:0]=[{str(ROOT)!r},{str(module_dir)!r}];"
                f"import {module_name} as target;"
                f"print(json.dumps(list(target.{attribute})))"
            )
            completed = subprocess.run(
                [str(interpreter), "-c", script],
                check=True,
                capture_output=True,
                text=True,
            )
            observed.append(tuple(json.loads(completed.stdout)))
        self.assertEqual(observed[0], vocabulary.COMMITTEE_STATES)
        self.assertEqual(observed[1], vocabulary.HC1H_STATES)

    def test_exact_bijection(self) -> None:
        self.assertEqual(vocabulary.to_hc1h("AGREE_CONFIDENT"), "agree-confident")
        self.assertEqual(vocabulary.to_hc1h("DISAGREE"), "disagree")
        self.assertEqual(vocabulary.to_hc1h("LOW_CONFIDENCE"), "low-confidence")


if __name__ == "__main__":
    unittest.main(verbosity=2)
