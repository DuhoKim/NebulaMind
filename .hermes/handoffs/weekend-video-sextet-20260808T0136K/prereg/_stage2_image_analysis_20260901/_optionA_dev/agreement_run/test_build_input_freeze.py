"""Read-only verifier tests; no fixture files or study operations."""
import copy
from pathlib import Path
import unittest
import build_input_freeze as freeze


class FreezeVerifierTests(unittest.TestCase):
    def test_existing_file_is_freshly_verified(self):
        pin = freeze.fingerprint(Path(__file__).resolve())
        self.assertEqual(freeze.verify_pin(pin), pin)

    def test_changed_digest_refuses_with_actual_path(self):
        pin = freeze.fingerprint(Path(__file__).resolve())
        pin['sha256'] = '0' * 64
        with self.assertRaisesRegex(freeze.Blocked, 'SHA256-MISMATCH: ' + pin['path']):
            freeze.verify_pin(pin)

    def test_missing_file_refuses(self):
        pin = dict(path=str(Path(__file__).resolve() / 'absent'), sha256='0' * 64)
        with self.assertRaisesRegex(freeze.Blocked, 'MISSING-FILE:'):
            freeze.verify_pin(pin)

    def test_missing_digest_and_template_refuse(self):
        with self.assertRaisesRegex(freeze.Blocked, 'MISSING-DIGEST:'):
            freeze.verify_pin(dict(path=str(Path(__file__).resolve())))
        with self.assertRaisesRegex(freeze.Blocked, 'MISSING-ACTUAL-PATH:'):
            freeze.verify_pin(dict(path='OUT/draw.json', sha256='0' * 64))

    def test_changed_size_and_resolved_path_refuse(self):
        original = freeze.fingerprint(Path(__file__).resolve())
        for key, value in [('bytes', -1), ('resolved_path', '/incorrect')]:
            pin = dict(original, **{key: value})
            with self.assertRaisesRegex(freeze.Blocked, key.upper() + '-MISMATCH:'):
                freeze.verify_pin(pin)

    def test_real_manifest_groups_prevent_freeze(self):
        core = freeze.checked_json(freeze.CORE, freeze.CORE_SHA)
        problems = freeze.unresolved_groups(core)
        self.assertEqual(len(problems), 19)
        self.assertTrue(all('UNEXPANDED-OBLIGATION:' in p for p in problems))
        with self.assertRaisesRegex(freeze.Blocked, 'UNEXPANDED-OBLIGATION:'):
            freeze.require_complete(core)

    def test_deleting_obligations_does_not_bypass_gate(self):
        core = freeze.checked_json(freeze.CORE, freeze.CORE_SHA)
        core['placeholders'] = []
        self.assertEqual(len(freeze.unresolved_groups(core)), 5)
        with self.assertRaisesRegex(freeze.Blocked, 'OBLIGATION-MEMBERSHIP:'):
            freeze.require_complete(core)

    def test_readiness_flag_does_not_supply_missing_bindings(self):
        core = freeze.checked_json(freeze.CORE, freeze.CORE_SHA)
        changed = copy.deepcopy(core)
        changed['ready_for_input_freeze'] = True
        self.assertEqual(freeze.unresolved_groups(changed), freeze.unresolved_groups(core))


if __name__ == '__main__':
    unittest.main(verbosity=2)
