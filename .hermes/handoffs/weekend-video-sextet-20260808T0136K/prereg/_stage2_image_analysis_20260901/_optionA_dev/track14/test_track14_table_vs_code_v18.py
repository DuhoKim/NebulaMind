"""TRACK 14 — the table verified against the V34 code (v18 / v14), including DYNAMICALLY SELECTED codes (seat B B-2). THE TABLE IS A FIRST-CLASS OBJECT (Blanc 06:35, item 5): INDEPENDENCE is VERIFIED AGAINST THE CODE by this test, which fails when they diverge — not hand-maintained beside
it. From the driver source it extracts every `add(<class>, "<CODE>", …, "<stage>", "<check>")` and `_Blocked("<check>", …)` site, and every `stage("<name>", …, "<check>")`
declaration, and requires: every check name used in the code is a key of the table (and vice versa); every code literal contributed for a check is among the table's codes
for that check; the stage each check is declared to run in matches the stage named at its add() sites; every prerequisite named in `needs` is a key of PREREQUISITES; the
regressions' and controls' plant codes are in the table. Written against v17; run first against v16 (which has a different table and no check attribution) — it fails there."""
import re, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE.parent
sys.path.insert(0, str(D / "fourier_chirality")); sys.path.insert(0, str(D / "track2")); sys.path.insert(0, str(D / "beacon_v2")); sys.path.insert(0, str(D / "drand_only")); sys.path.insert(0, str(D / "corpus_identity")); sys.path.insert(0, str(D / "track13"))   # v3: the controls module is imported by test 4; the aggregate launches from _optionA_dev/, so track13/ must be on the path (the 06:4x 4/4 run was launched from inside track13/)
import run_configurations_v18 as rc
SRC = (D / "fourier_chirality" / "run_configurations_v18.py").read_text(encoding="utf-8")
BODY = SRC[SRC.index("def load_identity_composed("):SRC.index("def verify_split_from_catalogue(")]
PSRC = (D / "track2" / "provenance_designs_v14.py").read_text(encoding="utf-8"); PBODY = PSRC[PSRC.index("def history_findings_v14("):PSRC.index("def validate_continuation_v14(")]   # checks contributed through the S5 callback live here
CALLBACK_CHECKS = set(re.findall(r'add\("[A-Z-]+", "[^"]+", [^\n]*?, "([a-z-]+)"\)', PBODY))
class TableVsCode(unittest.TestCase):
    def test_every_dynamically_selected_code_is_declared_for_its_check(self):
        """v18 (seat B B-2): codes chosen through a map — `m = APPROVAL_OUTCOME_CODES[check]; cls, code = m[o]` — are invisible to a regex over add(...) sites. The
        reviewer's mutation control removed EVENT-FORGED from the table and all four v17 tests still passed. The maps are now DECLARED DATA and are verified both ways."""
        bad = []
        for check, m in rc.APPROVAL_OUTCOME_CODES.items():
            declared = rc.INDEPENDENCE[check]["codes"]
            for outcome, (cls, code) in m.items():
                if code not in declared: bad.append((check, outcome, code, "produced by the map, not declared in the table"))
            for code in declared:
                if code not in {c for _, c in m.values()} and not re.search(r'add\("[A-Z-]+", "' + re.escape(code) + r'"', BODY) and not re.search(r'DataIntegrityFail\(f?"' + re.escape(code), BODY):
                    bad.append((check, code, "declared in the table but produced nowhere"))
        self.assertEqual(bad, [], f"the declared codes and the code's own dynamic maps must agree exactly: {bad}")
    def test_every_check_used_in_code_is_declared_and_vice_versa(self):
        used = set(re.findall(r'add\("[A-Z-]+", "[^"]+", [^\n]*?, "S[0-9a-z-]+", "([a-z-]+)"', BODY)) | set(re.findall(r'_Blocked\("([a-z-]+)"', BODY)) | set(re.findall(r'stage\("[^"]+", [^\n]*?, "[a-z-]+", "([a-z-]+)"\)', BODY))
        used |= CALLBACK_CHECKS; used -= {"helpers", "resolver", "split"}                                                           # the import reporter, the resolver's own record, the unadopted split check
        self.assertEqual(sorted(used - set(rc.INDEPENDENCE)), [], f"checks used in code but not declared: {sorted(used - set(rc.INDEPENDENCE))}")
        self.assertEqual(sorted(set(rc.INDEPENDENCE) - used), [], f"checks declared but never used in code: {sorted(set(rc.INDEPENDENCE) - used)}")
    def test_every_contributed_code_is_declared_for_its_check(self):
        bad = []
        for m in re.finditer(r'add\("([A-Z-]+)", "([^"]+)", [^\n]*?, "(S[0-9a-z-]+)", "([a-z-]+)"', BODY):
            cls, code, stage, check = m.groups()
            if check in ("helpers", "resolver", "split"): continue
            if code not in rc.INDEPENDENCE[check]["codes"]: bad.append((check, code))
        # codes raised by DataIntegrityFail inside a stage body land on that stage's check via classify_refusal — check the literal raises too
        for m in re.finditer(r'def (S0[a-h]|S[1-5][ab]?)\(\):(.*?)\n    stage\("([^"]+)", \1, "[a-z-]+", "([a-z-]+)"\)', BODY, re.S):
            fn, body, sname, check = m.groups()
            for code in re.findall(r'DataIntegrityFail\(f?"([A-Z][A-Za-z0-9_{}-]*?)[ :"]', body) + re.findall(r'_raise\(f?"([A-Z][A-Za-z0-9_{}-]*?)[ :"]', body):
                code = re.sub(r"\{.*", "", code).rstrip("-")
                if code and not any(c.startswith(code) for c in rc.INDEPENDENCE[check]["codes"]): bad.append((check, code))
        for m in re.finditer(r'add\("([A-Z-]+)", "([^"]+)", [^\n]*?, "([a-z-]+)"\)', PBODY):
            cls, code, check = m.groups()
            if check in rc.INDEPENDENCE and code not in rc.INDEPENDENCE[check]["codes"]: bad.append((check, code, "via S5 callback"))
        self.assertEqual(bad, [], f"codes contributed by a check but not declared for it: {bad}")
    def test_declared_stage_matches_the_code(self):
        bad = []
        for check, spec in rc.INDEPENDENCE.items():
            stages_in_code = set(re.findall(r'add\("[A-Z-]+", "[^"]+", [^\n]*?, "(S[0-9a-z-]+)", "' + re.escape(check) + r'"', BODY)) | set(re.findall(r'stage\("(S[0-9a-z-]+)", [^\n]*?, "[a-z-]+", "' + re.escape(check) + r'"\)', BODY))
            stages_in_code -= {"sub"}
            if check in ("open-delivery-auth", "per-entry"): stages_in_code |= {"S5-history"}                      # contributed through the S5 callback
            if stages_in_code and spec["stage"] not in stages_in_code: bad.append((check, spec["stage"], sorted(stages_in_code)))
        self.assertEqual(bad, [], f"declared stage differs from the code: {bad}")
    def test_prerequisites_are_declared_and_all_pairs_generated(self):
        for check, spec in rc.INDEPENDENCE.items():
            for p in spec["needs"]: self.assertIn(p, rc.PREREQUISITES, (check, p))
        import test_track14_nsd_table_v18 as T
        pairs = {(P_, C) for P_ in rc.PREREQUISITES for C, spec in rc.INDEPENDENCE.items() if P_ not in spec["needs"] and C in T.DEFECTS and C != "snapshot"}
        self.assertEqual(len(pairs), len(T.PAIRS), "every independent (prerequisite, check) pair with a defect recipe is generated — no exemption")
        self.assertTrue(any(P_ == "identity-file" for P_, C in pairs), "identity-file pairs are included (codex V32-1)")
        self.assertEqual(sorted(set(rc.INDEPENDENCE) - set(T.DEFECTS) - {"snapshot"}), [], "every check has a defect recipe (snapshot is the retrieval itself)")
if __name__ == "__main__": unittest.main()
