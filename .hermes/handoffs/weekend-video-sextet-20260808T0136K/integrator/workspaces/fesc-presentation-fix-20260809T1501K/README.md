# Durable audit workspace — FESC presentation fix 20260809T1501K

This directory is intentionally separate from every candidate and from `/tmp`.

Authority: `HWAO_FESC_PRESENTATION_FIX_ORDER.md`  
Authority SHA-256: `ec4561df5a270fc4318fbd5ccf83b2c73c3df16880c8b6c09031266cd1789e3b`

Frozen predecessor: `fesc-method-overhaul-canary-20260809T1420K`  
Predecessor MP4 SHA-256: `4c8115997e21689508f31587672a3dd7da9c902803427c43490603bad08309b9`

New candidate: `fesc-method-overhaul-canary-20260809T1501K`

Purpose:
- retain preview and encoded frame-review derivatives outside the candidate;
- preserve any rejected render or QA attempt without mutating a frozen directory;
- keep an auditable path rather than ephemeral `/tmp` output.

No scratch derivative may be written under either the 1420K predecessor or the 1501K candidate.
