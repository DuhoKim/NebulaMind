#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import torch

import inference_runner as runner


HERE = Path(__file__).resolve().parent


def write_ic6(path: Path, image: np.ndarray) -> bytes:
    tensor = np.array(image, dtype=np.dtype("<f4"), order="C", copy=True).reshape(1, 128, 128)
    payload = tensor.tobytes(order="C")
    path.write_bytes(payload)
    return payload


class InferenceRunnerContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.model = runner.load_frozen_model(runner.WEIGHTS_PATH)

    def test_frozen_architecture_and_runtime_contract(self) -> None:
        self.assertFalse(self.model.training)
        self.assertEqual(torch.get_num_threads(), 1)
        self.assertTrue(torch.are_deterministic_algorithms_enabled())
        self.assertEqual(tuple(self.model.f[0].weight.shape), (32, 1, 3, 3))
        self.assertIsInstance(self.model.f[-1], torch.nn.Linear)
        self.assertEqual(self.model.f[-1].in_features, 256)
        self.assertEqual(self.model.f[-1].out_features, 1)
        self.assertFalse(any(isinstance(module, torch.nn.MaxPool2d) for module in self.model.modules()))
        blocks = [module for module in self.model.modules() if isinstance(module, runner.BasicBlock)]
        self.assertEqual(len(blocks), 8)

    def test_weight_hash_mismatch_refuses_before_torch_load(self) -> None:
        with tempfile.TemporaryDirectory(dir=HERE) as raw:
            bad = Path(raw) / "bad.pt"
            bad.write_bytes(b"not frozen weights")
            with mock.patch.object(torch, "load") as load:
                with self.assertRaises(runner.ContractError) as caught:
                    runner.load_frozen_model(bad)
            self.assertEqual(caught.exception.code, "REFUSED_WEIGHTS_SHA256")
            load.assert_not_called()

    def test_ic6_reader_matches_cutout_writer_byte_for_byte(self) -> None:
        with tempfile.TemporaryDirectory(dir=HERE) as raw:
            path = Path(raw) / "synthetic.f32le"
            image = np.arange(128 * 128, dtype=np.float32).reshape(128, 128) / 17.0
            payload = write_ic6(path, image)
            tensor, digest = runner.read_ic6_tensor(path, synthetic=True)
            self.assertEqual(tensor.shape, (1, 128, 128))
            self.assertEqual(tensor.dtype, torch.float32)
            self.assertEqual(tensor.numpy().dtype, np.dtype("<f4"))
            self.assertTrue(tensor.numpy().flags.c_contiguous)
            self.assertEqual(tensor.numpy().tobytes(order="C"), payload)
            self.assertEqual(digest, hashlib.sha256(payload).hexdigest())

    def test_ic6_reader_rejects_wrong_byte_length(self) -> None:
        with tempfile.TemporaryDirectory(dir=HERE) as raw:
            path = Path(raw) / "short.f32le"
            path.write_bytes(b"\0" * (runner.IC6_BYTES - 4))
            with self.assertRaises(runner.ContractError) as caught:
                runner.read_ic6_tensor(path, synthetic=True)
            self.assertEqual(caught.exception.code, "REFUSED_IC6_BYTE_LENGTH")

    def test_real_tensor_path_refused_before_any_open_without_authorization(self) -> None:
        forbidden = runner.REAL_TENSOR_ROOT / "must-not-open.f32le"
        with mock.patch("pathlib.Path.open", side_effect=AssertionError("real tensor opened")):
            with self.assertRaises(runner.ContractError) as caught:
                runner.read_ic6_tensor(forbidden, synthetic=False, authorization=None)
        self.assertEqual(caught.exception.code, "REFUSED_REAL_DATA_UNAUTHORIZED")

    def test_wrong_authorization_hash_refuses_real_path(self) -> None:
        with tempfile.TemporaryDirectory(dir=HERE) as raw:
            authorization = Path(raw) / "authorization.txt"
            authorization.write_text("not authorized", encoding="utf-8")
            with self.assertRaises(runner.ContractError) as caught:
                runner.guard_input_scope(
                    runner.REAL_TENSOR_ROOT / "must-not-open.f32le",
                    synthetic=False,
                    authorization=authorization,
                )
        self.assertEqual(caught.exception.code, "REFUSED_AUTHORIZATION_SHA256")

    def test_synthetic_flag_cannot_bypass_real_root_through_symlink(self) -> None:
        with tempfile.TemporaryDirectory(dir=HERE) as raw:
            alias = Path(raw) / "synthetic-looking.f32le"
            alias.symlink_to(runner.REAL_TENSOR_ROOT / "must-not-open.f32le")
            with self.assertRaises(runner.ContractError) as caught:
                runner.guard_input_scope(alias, synthetic=True, authorization=None)
        self.assertEqual(caught.exception.code, "REFUSED_REAL_DATA_UNAUTHORIZED")

    def test_mirror_is_width_index_reversal_and_involution(self) -> None:
        tensor = torch.arange(128 * 128, dtype=torch.float32).reshape(1, 128, 128)
        mirrored = runner.mirror_tensor(tensor)
        restored = runner.mirror_tensor(mirrored)
        self.assertTrue(torch.equal(restored, tensor))
        self.assertTrue(torch.equal(mirrored[:, :, 0], tensor[:, :, -1]))

    def test_chi_is_bit_exact_antisymmetric_and_deterministic(self) -> None:
        image, _ = runner.synthetic_sample(runner.VALIDATION_DOMAIN, 19)
        tensor = torch.from_numpy(image.reshape(1, 128, 128))
        first = runner.chi_bits(self.model, tensor)
        second = runner.chi_bits(self.model, tensor)
        mirrored = runner.chi_bits(self.model, runner.mirror_tensor(tensor))
        self.assertEqual(first, second)
        self.assertEqual(mirrored, runner.negated_float32_bits(first))

    def test_committee_state_is_metadata_and_does_not_receive_primary_chi(self) -> None:
        image, _ = runner.synthetic_sample(runner.VALIDATION_DOMAIN, 5)
        metadata = runner.Committee().classify(image)
        self.assertEqual(
            set(metadata),
            {"member_a_score", "member_a_sign", "member_b_score", "member_b_sign", "state"},
        )
        self.assertIn(metadata["state"], {"AGREE_CONFIDENT", "DISAGREE", "LOW_CONFIDENCE"})
        self.assertNotIn("chi", metadata)

    def test_input_manifest_loads_20000_ordered_paths_without_argv_transport(self) -> None:
        with tempfile.TemporaryDirectory(dir=HERE) as raw:
            manifest = Path(raw) / "inputs.txt"
            expected = [Path(f"tensor-{index:05d}.f32le") for index in range(20_000)]
            manifest.write_text("".join(f"{path}\n" for path in expected), encoding="utf-8")
            self.assertEqual(runner.resolve_input_paths(None, manifest), expected)

    def test_json_input_manifest_is_equivalent_to_legacy_inputs(self) -> None:
        with tempfile.TemporaryDirectory(dir=HERE) as raw:
            manifest = Path(raw) / "inputs.json"
            expected = [Path("a.f32le"), Path("b.f32le")]
            manifest.write_text(json.dumps([str(path) for path in expected]), encoding="utf-8")
            self.assertEqual(runner.resolve_input_paths(None, manifest), expected)
            self.assertEqual(runner.resolve_input_paths(expected, None), expected)

    def test_input_manifest_and_legacy_inputs_are_mutually_exclusive(self) -> None:
        with tempfile.TemporaryDirectory(dir=HERE) as raw:
            manifest = Path(raw) / "inputs.txt"
            manifest.write_text("a.f32le\n", encoding="utf-8")
            with self.assertRaises(runner.ContractError) as caught:
                runner.resolve_input_paths([Path("b.f32le")], manifest)
            self.assertEqual(caught.exception.code, "REFUSED_INPUT_TRANSPORT")

    def test_receipts_ledger_and_resume_are_append_only(self) -> None:
        with tempfile.TemporaryDirectory(dir=HERE) as raw:
            root = Path(raw)
            inputs = root / "inputs"
            inputs.mkdir()
            paths = []
            for index in range(2):
                image, _ = runner.synthetic_sample(runner.VALIDATION_DOMAIN, index)
                path = inputs / f"synthetic-{index}.f32le"
                write_ic6(path, image)
                paths.append(path)
            output = root / "output"
            first = runner.run_paths(paths, output, synthetic=True)
            ledger = output / "results.jsonl"
            before = ledger.read_bytes()
            second = runner.run_paths(paths, output, synthetic=True)
            self.assertEqual(first, {"processed": 2, "resumed": 0})
            self.assertEqual(second, {"processed": 0, "resumed": 2})
            self.assertEqual(ledger.read_bytes(), before)
            rows = [json.loads(line) for line in before.splitlines()]
            self.assertEqual(len(rows), 2)
            required = {"object_id", "input_tensor_sha256", "chi_value", "chi_bits_hex", "committee_state", "weights_sha256", "code_sha256", "receipt_sha256"}
            self.assertTrue(all(required <= set(row) for row in rows))
            self.assertEqual(len(list((output / "receipts").glob("*.json"))), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
