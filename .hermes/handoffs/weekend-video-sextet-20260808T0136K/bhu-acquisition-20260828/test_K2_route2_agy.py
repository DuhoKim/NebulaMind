import subprocess
import sys
import unittest
from pathlib import Path


LANE = Path(__file__).resolve().parent
SCRIPT = LANE / "K2_route2_tori_repair.py"


class K2Route2ReceiptTest(unittest.TestCase):
    def test_route2_script_emits_complete_executable_receipt(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=LANE,
            check=False,
            capture_output=True,
            text=True,
        )

        required_lines = {
            "ROUTE2_RECEIPT=EXECUTED",
            "C1_OS_MASS_CONTINUITY=PASS",
            "C2_NULL_SHELL=PASS",
            "C3_EQUATOR_IDENTITY=PASS",
            "C4_DEC_DELETION=PASS",
            "ENTRY56_CELL=J_SMOOTH_EXPANDING",
            "PATHRIA_CELL=J_SHELL_UNPHYSICAL",
            "B3_NOSHELL=comoving-only",
            "ALL_ROUTE2_CHECKS=PASS",
        }
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(required_lines.issubset(set(result.stdout.splitlines())))


if __name__ == "__main__":
    unittest.main()
