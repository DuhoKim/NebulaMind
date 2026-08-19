# Coverage census — 2026-08-19

COVERAGE_CENSUS_COMPLETE

- required: **60,308**
- receipted: **60,308**
- absent-by-coverage: **0**
- contradictions: **0**

Here `contradictions` means duplicate receipt URLs, non-`OK_CONFIRMED` outcomes, a receipt whose `image_r_listed` is not true, or disagreement between the receipt count and the completion record. A fresh line-by-line parse found 60,308 JSON receipts, 60,308 unique URLs, 60,308 `OK_CONFIRMED` outcomes, and 60,308 `image_r_listed: true` values.

## Frozen inputs

- `_tori_harvest_20260817/receipts.jsonl`
  - SHA-256: `d3ffc2c2a05d710f247ca253cb7b645b75acc83991042e6e1897e03be06e14ef`
- `_tori_harvest_20260817/HARVEST_COMPLETE.json`
  - SHA-256: `60559068783a32425aebfda81e4d5dd771fae33bef4e1dac39d9502cd37afe21`

## Harvest completion record, quoted exactly

> `{`
> `  "utc": "2026-08-19T05:10:02Z",`
> `  "completed": 60308,`
> `  "total": 60308`
> `}`

This census packages §11.4b only. It authorizes no transfer and moves no image bytes.
