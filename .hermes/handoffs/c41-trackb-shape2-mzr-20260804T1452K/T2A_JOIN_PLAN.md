# T2a Join Plan

## Objective
To assemble a $z>3$ Te-anchored mass-metallicity catalog by joining fragmented VizieR tables (spectroscopic metallicity/redshift tables with photometric/SPS stellar mass tables).

## Candidate Pairings

### 1. JADES (GOODS-N / GOODS-S)
- **Metallicity Tables**: `V/159/gngrat`, `V/159/gsgrat`, `V/159/gnprism`, `V/159/gsprism` (contain redshift and line fluxes / Te/O/H).
- **Mass/Photometry Tables**: `V/159/gnsample`, `V/159/gssample` (photometry/photo-z). If public stellar masses are absent in these specific tables, we fall back to coordinate matching against external GOODS-N/S mass catalogs (e.g., ASTRODEEP or 3D-HST fallback tables).
- **Join Key**: Object `ID` (exact internal JADES match) or `RA_ICRS` / `DE_ICRS` with a $0.5''$ tolerance.

### 2. CEERS
- **Metallicity Tables**: Candidate external auroral/Te compilations covering the EGS field.
- **Mass/Photometry Tables**: `J/ApJ/946/L16/table1`, `J/ApJ/960/104/table1`, `J/AJ/168/113/table1` (contain $z$ and $M_*$).
- **Join Key**: `RA` / `DEC` cross-matching ($0.5''$ tolerance) between external spec-z Te compilations and the CEERS mass catalogs.

### 3. GLASS / MACS (Lensed)
- **Metallicity Tables**: `J/ApJ/812/114/table3` (MACS J0717.5+3745 redshift/metal).
- **Mass/Photometry Tables**: Lensed cluster photometric catalogs for MACS J0717.
- **Join Key**: Coordinates ($0.5''$ tolerance).
- **Lensing Inheritance**: Must explicitly pull lens-model magnification ($\mu$) and propagate uncertainty into mass error per contract §5. If $\mu$ is missing, these default to `cluster-line-of-sight` and are excluded from the main MZR.

### 4. UNCOVER (Abell 2744)
- **Metallicity Tables**: Candidate spec compilations for A2744.
- **Mass/Photometry Tables**: `J/ApJS/270/12/spscat` (SPS stellar masses), joined to `J/ApJS/270/7/catalog` (photometry).
- **Join Key**: Internal `id` matching.
- **Lensing Inheritance**: Same as GLASS. Must declare magnification models.

## Contract Satisfaction vs. Declared Conversions
- Pairings that natively provide direct $T_e$-based $12+\log(\text{O/H})$ (Class A/B) satisfy the contract directly, requiring no metallicity conversion (though the 0.15 dex scale uncertainty applies).
- Pairings using strong-line calibrations (Class C) require explicit conversion formulas declared in the T2a conversion tables, mapped onto the unified Te scale.
- **F7 Fallback Tables**: If primary joins fail to yield statistically significant samples, we fall back to pre-JWST $z \sim 2-3$ continuity samples or integrated model prediction catalogs as baseline comparisons.
