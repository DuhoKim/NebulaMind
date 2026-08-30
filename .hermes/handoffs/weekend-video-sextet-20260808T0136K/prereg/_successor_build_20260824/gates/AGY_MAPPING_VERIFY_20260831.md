# Gain Mapping A Verification

Verification results for the BS-3g executable mapping A.

<!-- FINDINGS-BLOCK v1 -->
SEAT: AGY
VERSION: MAPA-V1
VERDICT: DEFECTIVE
COUNT: 2
F1 | HIGH | self-test | Control 6 is vacuous: it tests whether the output of an explicit np.clip respects its own bounds.
F2 | HIGH | identity | MAPPING_ID and file sha256 fail to capture v9.A_LONGO, allowing behavior to change without altering the identity.
<!-- END FINDINGS-BLOCK -->
