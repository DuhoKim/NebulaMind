# T1 Assembly Rules

## Peek Log
- 2026-08-04: Drafted assembly rules before any VizieR reconnaissance or catalog contents were accessed.

## Inclusion Criteria (Measurement Classes)
1. **Auroral-Line Detection Class**: The catalog row must represent a galaxy with an explicitly detected auroral line (e.g., [O III] $\lambda 4363$) allowing direct electron temperature (Te) measurement, OR a robust Te-consistent limit.
2. **Redshift Cut**: The source must have a spectroscopic redshift $z > 3$.
3. **Declared-Scale Requirement**: The catalog must explicitly declare its metallicity calibration scale (must be Te-anchored, not an arbitrary strong-line calibration without declared conversion). If strong-line values are present, they must be cleanly convertible to the Te scale.
4. **Mass-Convention Fields Needed**: The catalog must provide stellar mass ($M_*$) estimates and explicitly state the assumed Initial Mass Function (IMF) and Spectral Energy Distribution (SED) fitting conventions, enabling homogenization to a single standard.

## Exclusion Criteria
- Sources with $z \le 3$ (except for explicitly selected low-redshift continuity anchor sets defined in the design).
- Sources lacking a direct Te measurement or a robust Te-consistent upper limit.
- Sources with undeclared metallicity scales or mass fitting conventions.
