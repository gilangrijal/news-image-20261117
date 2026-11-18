# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/gilangrijal/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/gilangrijal/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A program that sums up Tuesday 17 November 2026's world news in one
image: a newspaper front page — "THE WORLD IN ONE IMAGE" — with six
stories from that day: the U.S. strikes on Iran, the Kerch Bridge hit,
Trump's trip to the China summit, the U.S. losing measles elimination
status, the NSA / airports / Apple outages, and Japan scrambling jets.
The image is drawn entirely in code (PIL, flat vector motifs, no
photos), so every run produces the same bytes.

## Run it

```sh
python3 dev/compose.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png` and verifies size and sha256 of the copy. No
network, no randomness. `dev/compose.py` is the build script that
draws `entry.png` (1024x1024, ~105 KB, under the 1 MiB cap).

---

<sub>Entered on [make.fun](https://make.fun/?ref=bhskgd0y&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
