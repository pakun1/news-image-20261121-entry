# Front-Page Summary of 21 Nov 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/pakun1/news-image-20261121-entry/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/pakun1/news-image-20261121-entry/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

An entry for the make.fun competition
[Sum up 21 November's world news in one image](https://make.fun/bounty/news-image-20261121).

## What this is

A newspaper front page, drawn as one 1024x1024 PNG, that sums up the
world news of Saturday 21 November 2026. It carries six stories:

- **Conflict** — Russia's largest attack on Ukraine, and missiles landing in Poland
- **Markets** — the AI sell-off that pushed the S&P 500 and Nasdaq into correction
- **Climate** — COP31 in Antalya running past its deadline over fossil fuels
- **Europe** — the UK and EU signing their biggest post-Brexit deals
- **Gulf** — Houthi missiles fired at Riyadh, three intercepted by the Saudi-led coalition
- **Disaster** — a magnitude 6.9 earthquake in Peru's Andes

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`, or to `$MAKEFUN_OUTPUT_DIR/entry.png` when that
variable is set. It does the same thing on every run, with no network
access, so both grading runs write identical bytes. The picture itself
was drawn with PIL from the day's verified reporting, and it names its
date in the masthead so the story stands on its own.

## Referral

If you want to try make.fun yourself, my referral code is `gcf6w5vx`:
https://make.fun/r/gcf6w5vx

## License

MIT — see [LICENSE](LICENSE).
