# DONE_GPT2

Exact command run:

`python3 calc_leverage.py > fixture_results.txt`

SHA-256 (`shasum -a 256 calc_leverage.py fixture_results.txt`):

```text
d3a1e36cdeb03cb57b0d28b5575c2b44a913c714f89fafde7c53dba9f906445b  calc_leverage.py
c80985acca07248602b16fa4b67f6ae908ebd87f8b409ed355f847267d3ef1cb  fixture_results.txt
```

The restricted-sphere fixture sizes were not specified, so I used the same 200,000 points as the full-sphere fixture for both restricted cases. I interpreted POLAR(q) as accepting whole bricks, allowing the accepted galaxy count to overshoot the fractional threshold when the final brick has multiple galaxies, and used stable input order to break exact ties in |cos(theta)| deterministically.
