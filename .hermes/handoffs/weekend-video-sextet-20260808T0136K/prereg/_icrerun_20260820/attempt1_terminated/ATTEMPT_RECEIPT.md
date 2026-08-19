# Attempt 1 custody — infrastructure termination

The first execution was launched through the tracked background-process wrapper. It completed the 1,000-row identity record write, then the wrapper reported an exited/defunct process with no numeric exit code, no traceback, empty stdout, and no substantive stderr. No aggregate receipt had been written, so no scientific verdict existed. The complete partial artifact is preserved and was not used as evidence.

- `r1_r5_records.jsonl`: 1,000 rows; SHA-256 `65fa6dfe8ab43ea28053c3840126c98406a10ce137329446d1a3e5d38747ef1a`
- `run_stdout.log`: empty; SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `run_stderr.log`: blank newline only; SHA-256 `a53a5a1fba274596a55953f3429ecdf5a4d98ee080a31aa2b1883daa87602d09`

This was an execution-transport failure, not a failed probe or a changed definition. The next attempt uses the same runner, hashes, slots, seeds, and complete deterministic sequence in a foreground process with a bounded 600-second timeout. No probe is dropped or replaced.
