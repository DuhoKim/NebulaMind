# Kun live-readiness dry-run

Marker: RESOURCE_SURGE_EVIDENCE_TRUST_20260708T022147Z

Status: WARN

## Summary

Read-only dry-run completed. The working repo has three evidence-trust candidate directories under `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/*/evidence-trust-rebuild/`. The live-served target parent method directories exist under `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/...`, but all three target `evidence-trust-rebuild/` directories are absent. No copy was performed.

WARN because live target directories are absent and would need additive `mkdir -p` plus copy before live-served static preview parity exists.

## Inspected paths

Working candidate root:
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution`

Live-served target root:
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution`

Target status:
- `packet-gated-paper-to-wiki-reconciliation` parent exists; `evidence-trust-rebuild` absent.
- `source-first-paper-adjudication` parent exists; `evidence-trust-rebuild` absent.
- `debate-map-to-wiki-rebuild` parent exists; `evidence-trust-rebuild` absent.

## Candidate files and checksum expectations

After any future approved copy, each target file should match these SHA-256 values:

| Method | File | Bytes | SHA-256 |
|---|---:|---:|---|
| M1 | `evidence-trust-rebuild/evidence-trust-bindings-20260708T014205Z.md.json` | 17491 | `ea08877e9348f93bf8fe7671bf0fd634bc2a08448bd03b3399e52ec92865a024` |
| M1 | `evidence-trust-rebuild/manifest-20260708T014205Z.json` | 468 | `fc5238bcef58f34ed353bcf5b7af249da88e4a9f3b770ab985be25e95e5a90e7` |
| M1 | `evidence-trust-rebuild/evidence-trust-preview-20260708T014205Z.html` | 37763 | `70564e0ba8144ef5f28328745ec56a6928a4431bea3ddb964f867cd426fdf19e` |
| M2 | `evidence-trust-rebuild/page-content-20260708T014205Z.md` | 14073 | `52cf8bfb422df8096da866a9144bcfa2d546fb42003e02e5630d22f6da255407` |
| M2 | `evidence-trust-rebuild/manifest.json` | 978 | `7cf79edc6d21eb81ac57125b9518babe8883e57ee4ca9a448f1d1b3a95bde36c` |
| M2 | `evidence-trust-rebuild/evidence-trust-map-20260708T014205Z.json` | 7499 | `c9848105c1a279a1a888cb003844f9d5b16d39bbd534793b95218a4f6003f7df` |
| M2 | `evidence-trust-rebuild/wiki-format-preview-20260708T014205Z.html` | 13531 | `6b106e5eb67798f5460a4a233eda933d0a7924883993ded8cc8ce5bc387fce92` |
| M3 | `evidence-trust-rebuild/evidence-basis-20260708T014205Z.md` | 8091 | `45d1cc932083c91d903e799815ca77772789099cdc7eb57262ec0b5846e59947` |
| M3 | `evidence-trust-rebuild/page-content-evidence-trust-20260708T014205Z.md` | 17173 | `d908af489202ee08872352284f06fe6ae0235138fc09e4fd12e997364990542d` |
| M3 | `evidence-trust-rebuild/wiki-format-preview-evidence-trust-20260708T014205Z.html` | 14920 | `5e9236f56226b7252299adcb0e270964d5e19ac30859a25b2d254645a2c9150f` |

Total candidate payload: 10 files, 131987 bytes.

## Exact mkdir/cp that would be needed

Dry-run only. These commands were not executed:

```bash
mkdir -p /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild
cp -p /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/* /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/

mkdir -p /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild
cp -p /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/* /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/

mkdir -p /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild
cp -p /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/* /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/
```

Post-copy checksum expectation, if later approved:

```bash
find /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution -path '*/evidence-trust-rebuild/*' -type f -print0 | xargs -0 shasum -a 256
```

The output should match the SHA-256 table above.

## Commands run

- `find frontend/public/agent-reports/wiki-method-results/galaxy-evolution -maxdepth 3 -type d`
- `find /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution -maxdepth 3 -type d`
- `find frontend/public/agent-reports/wiki-method-results/galaxy-evolution -path '*/evidence-trust-rebuild/*' -type f`
- `find /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution -path '*/evidence-trust-rebuild/*' -type f`
- `find frontend/public/agent-reports/wiki-method-results/galaxy-evolution -path '*/evidence-trust-rebuild/*' -type f -print0 | xargs -0 shasum -a 256`
- Parent/target directory existence checks with `test -d`.
- Candidate size checks with `wc -c` and `stat`.

## Safety ledger

Read-only/static verification only. No copy/write into `NebulaMind-origin-main-live`; no `/api/pages`; no `page_versions`; no product DB/SQL; no git; no deploy/restart; no browser automation; no cloud/OAuth/secrets; no cron; no live publication. The only write was this `.hermes` report.
