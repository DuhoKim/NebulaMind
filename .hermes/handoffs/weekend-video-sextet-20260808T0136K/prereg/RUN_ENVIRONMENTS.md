# Run environments

No package installation, user-site injection, or `PYTHONPATH` dependency mixing is permitted.
Each gated stage is launched by the matching lane-root script below.

| Stage | Launcher | Interpreter | Required packages | Why |
|---|---|---|---|---|
| Cutout composition / IC-1..IC-7 tensor writing | `run_cutout_stage.sh` | `/usr/bin/python3` | numpy, astropy (through the pinned FITS read path) | System Python has the astronomy stack; this stage does not use torch. |
| Primary inference | `run_inference_stage.sh` | `venv_torch/bin/python` | numpy, torch | Frozen CE-ResNet inference and its committee metadata require torch; they do not use Pillow, cryptography, or astropy. |
| Independent committee batch | `run_committee_stage.sh` | `venv_torch/bin/python` | numpy, torch | Member-B is a frozen torch model; the batch consumes IC-6 tensors directly. |
| Tensor-to-PNG display rendering | `run_display_stage.sh` | `/usr/bin/python3` | numpy, Pillow | Display-only fixed rendering needs Pillow and never imports torch. |
| HC-1H prepare/check/reduce | `run_hc1h_stage.sh` | `/usr/bin/python3` | Pillow, cryptography | The hand-check harness reads PNGs and seals custody data; it never imports torch. |

No stage requires both torch and Pillow. The tensor is the boundary between machine stages
and the display renderer; the PNG is display-only and is forbidden as input to chi.

## Frozen role-name trap

`--real-population` is the HC-1H interface's frozen name for the accepted-population input.
It is not evidence that the rows are real observations. Every accepted-population JSONL must
have an adjacent `<filename>.provenance.json` with exactly:

- `population_role`: `accepted_population`
- `provenance`: exactly the rows' `data_class` (`synthetic` or `authorized_measurement`)

The blind-injection input must instead declare `population_role: blind_injection_pool` and
`provenance: synthetic`. Preparation refuses missing, swapped, or disagreeing sidecars. Thus
a synthetic campaign can be used in an explicitly synthetic rehearsal, but a synthetic pool
cannot silently occupy the accepted-population role in a production invocation.
