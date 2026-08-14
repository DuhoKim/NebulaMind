#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "finalize_partitioned_variance_rerun.py"


def load():
    spec = importlib.util.spec_from_file_location("finalize_rerun", TARGET)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load()
    empty = module.classify_result(completed_partitions=0, partition_count=67, combined=None)
    assert empty == {"status": "UNRESOLVED", "threshold_verdict": "NONE"}

    partial = module.classify_result(
        completed_partitions=2,
        partition_count=67,
        combined={"n_cut6_dered": 100, "var_pop_cos_theta": Decimal("0.20")},
    )
    assert partial == {"status": "PARTIAL", "threshold_verdict": "NONE"}

    for variance, verdict in ((Decimal("0.14"), "FAIL"), (Decimal("0.15"), "PASS"), (Decimal("0.16"), "PASS")):
        complete = module.classify_result(
            completed_partitions=67,
            partition_count=67,
            combined={"n_cut6_dered": 832393, "var_pop_cos_theta": variance},
        )
        assert complete == {"status": "COMPLETE", "threshold_verdict": verdict}

    try:
        module.classify_result(
            completed_partitions=67,
            partition_count=67,
            combined={"n_cut6_dered": 832392, "var_pop_cos_theta": Decimal("0.20")},
        )
    except RuntimeError as exc:
        assert "population" in str(exc)
    else:
        raise AssertionError("full coverage with wrong population was accepted")
    print("partitioned_variance_finalizer_contract=PASS")


if __name__ == "__main__":
    main()
