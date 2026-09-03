ACCESS_SHA=186748bfff9f5f8e3182516b3df7b6e03b6db9615db1dd1496a185740af6db6b

### TASK A: S1 CLOSURE WITH EVIDENCE

S1 (lossy exception masking) is now properly addressed. The refusal construction correctly captures the original exception class and string, inserting them into both the string representation and the structured payload:

```python
    except Exception as exc:
        exception_class = type(exc).__name__
        exception_text = str(exc)
        error = GateError(
            f"COMPLETENESS-FAIL: SWEEP-FITS-UNREADABLE: "
            f"{exception_class}: {exception_text}")
        error.payload = {"reason": "SWEEP-FITS-UNREADABLE",
                         "exception_class": exception_class,
                         "exception_text": exception_text}
        raise error from exc
```

By explicitly catching `Exception`, it correctly avoids swallowing `KeyboardInterrupt` and `SystemExit` (which inherit from `BaseException`). The test suite validates this payload generation.

Test via script form:
```
$ python3 completeness_gate/test_sweep_source.py
............
----------------------------------------------------------------------
Ran 12 tests in 0.315s

OK
```

Test via unittest form:
```
$ PYTHONPATH=. python3 -m unittest completeness_gate.test_sweep_source
............
----------------------------------------------------------------------
Ran 12 tests in 0.341s

OK
```

### TASK B: REGRESSION VS V1/V2

A git diff between the committed V2 and V3 demonstrates the change is strictly isolated:
- `completeness_gate/sweep_source.py`: Modified the exception block in `_read_identity_rows` to parse `Exception` as `exc`, append the type and string to the message and payload.
- `completeness_gate/test_sweep_source.py`: Modified `test_corrupt_truncated_fits_refuses_with_exact_reason` to use `mock.patch.object` on `fits.open` and assert the precise string output and payload dictionary.

There are no unintended changes to the logic, sweeping process, or other tests.

### TASK C: NEW DEFECTS (S2..Sn)

No new defects were identified in the changes.

SEAT: AGY
VERSION: SWEEP-SOURCE-REFEREE-V3
VERDICT: PINNABLE
S1: CLOSED
COUNT: 0
