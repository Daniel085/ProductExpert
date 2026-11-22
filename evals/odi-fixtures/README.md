# ODI output fixtures

Synthetic surveys for `odi-data-scientist` and `tools/odi/`. No row is a
real respondent. Each has 180 respondents, 24 outcomes rated 1–5 on
importance (`_imp`) and satisfaction (`_sat`), and `duration_min`.

- `noise.csv`
- `one-population.csv`
- `planted.csv`

What each contains and what must come back is in
[`expected/`](./expected/). An agent under test gets a copy of the CSV and
nothing else from this folder.

`generate.py` rebuilds all of them from a fixed seed.
