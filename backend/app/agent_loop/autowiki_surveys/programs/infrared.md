# AutoWiki Surveys Program — infrared band

## Reader persona
An infrared/near-IR astronomer selecting a survey for high-redshift galaxy photometry,
brown dwarf census, dust-obscured sources, or stellar population science.

## Priorities
1. `wavelength_range` MUST cite μm with both endpoints AND instrument/filter names
   (e.g. "0.6–28.3 μm: NIRCam, NIRISS, NIRSpec, MIRI" for JWST).
2. For photometric surveys, state limiting magnitude by band (e.g. "K~18.4 AB for 2MASS").
3. `current_data_release` for HST/JWST: cite the most recent observation cycle AND confirm
   archive accessibility (all public through MAST).
4. `flagship_programs` MUST list recognized survey programs (e.g. for JWST: CEERS, JADES,
   PRIMER, COSMOS-Web; for 2MASS: PSC, XSC, 6X; for WISE: AllWISE, unWISE CATWISE2020).
5. Distinguish space-based (JWST, HST, Spitzer, WISE) from ground-based (UKIDSS, VIKING).

## Hard rules
- `sky_coverage_deg2` for JWST/HST: note that coverage grows with each cycle; cite the
  DR-specific footprint, not "all-sky".
- Photometric bands must be named (J, H, Ks, W1, W2, F200W, etc.) not just wavelengths.
- Do not conflate imaging depth with spectroscopic depth.

## Banned moves
- Citing "infrared" as a flagship program.
- Quoting sensitivity in arbitrary units without the filter name.
- Marketing voice ("the most powerful space telescope ever built").
