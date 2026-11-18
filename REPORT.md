# news-image-20261117 — entry report

## Image
A newspaper front page, "THE WORLD IN ONE IMAGE / TUESDAY · 17 NOVEMBER
2026": six panels, each with a flat drawn motif, a bold headline and a
short summary, plus a footer ticker. The judge has no news feed and
judges only what the image itself shows, so the cover is
self-explanatory — a viewer who missed the day can tell what happened
from picture + short labels. All text is PIL-drawn, so no AI-rendered
text anywhere; all motifs are simple flat shapes, no photos.

## The six stories (Tuesday 17 November 2026 — verified against the sources below; no detail invented)

1. **U.S. STRIKES IRAN** — U.S. warplanes hit a missile launch site on
   Qeshm Island after tanker attacks in the Strait of Hormuz; 24
   seafarers were evacuated (gas tanker Tara Gas, fire off Musandam;
   Oman announced the evacuation). Sources: Reuters via Profile News,
   17 Nov roundup; World News Tonight, 17 Nov 2026.
2. **KERCH BRIDGE HIT** — Ukrainian drones and missiles struck the
   Crimean Bridge; verified video shows the road arch collapsed into
   the strait. Sources: Reuters via Profile News; CNN-verified footage
   cited in the 17 Nov strategic brief.
3. **TRUMP HEADS TO CHINA SUMMIT** — President Trump travels to China
   for a trilateral summit with Xi Jinping and Vladimir Putin, after a
   Quad meeting in Manila. Sources: World News Tonight, 17 Nov 2026;
   17 Nov strategic brief.
4. **U.S. LOSES MEASLES-FREE STATUS** — The Pan American Health
   Organization says the U.S. has lost measles elimination status —
   the first time since 2000 (uninterrupted transmission for at least
   12 months). Source: PAHO via Profile News, 17 Nov roundup.
5. **OUTAGES HIT NSA, AIRPORTS, APPLE** — The NSA's classified network
   went offline amid outages at airports, banks and Apple services.
   The DNI denies a cyberattack. Sources: World News Tonight, 17 Nov
   2026; Apple status records via Profile News.
6. **JAPAN SCRAMBLES JETS** — Tokyo sent fighter jets up after two
   suspected Russian aircraft entered its airspace, and lodged a
   formal protest with Moscow. Sources: Asas Press digest, 17 Nov
   2026; The Incident Report, 17 Nov 2026.

Footer ticker (also verified 17 Nov): Wall Street falls as tech stocks
slide (S&P 500 down 1%, AP); winter rain floods shelters in Gaza (UN,
17 Nov summary); Depardieu admits assault charge in Paris (Asas Press
digest, 17 Nov).

Breadth: Middle East, Europe/Ukraine, Asia diplomacy, US health, US
tech/outages, Asia-Pacific security — 3+ regions, 5 fields. The
unverified "dirty bomb" claim reported on 17 Nov is deliberately NOT
in the image: Trump said he was taking the CNN report seriously, Iran
denied it, and the intelligence was unverified — it is not shown as
fact.

## Sources (all dated 17 Nov 2026, read 18 Nov 2026)
- https://www.profilenews.com/en/november-17-2026-world-news/ (roundup, cutoff 18 Nov 02:56 EST; cites Reuters, AP, PAHO, UN)
- https://podcastrex.com/shows/world-news-tonight-with-david-muir/full-episode-tuesday-november-17-2026
- https://asaspress.com/en/news/world-news-digest-top-stories-of-november-17-2026
- https://olgalautman.substack.com/p/the-incident-report-november-17-2026
- https://medium.com/all-voices-news/global-and-u-s-strategic-news-brief-november-17-2026-ebeb4180de89

## Files
- `entry.png`: PNG, 1024x1024 px, 104,631 bytes (limit 1,048,576).
- `main.py`: Python 3.13 stdlib only. Copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), then verifies
  size AND sha256 of the copy. No network, no randomness.
- `dev/compose.py`: the PIL build script (masthead, six panels with
  drawn motifs, auto-fit headline/body wrapping). Labels were fixed
  after visual checks: summaries shortened so no text is cut off,
  measles "2000" box widened, jets redrawn as silhouettes.

## Verification (done by the builder)
- Visual, full size: all six headlines and summaries spelled exactly
  as briefed, complete inside their panels, no garbled text, one clear
  composition, masthead readable.
- Visual, downscaled to 300x300: masthead readable, all six headlines
  readable as bold caps, panels + motifs distinguishable.
- Determinism: run main.py twice with MAKEFUN_OUTPUT_DIR=out1/out2 —
  both sha256 `70595ea690f3b656a81ee14136668e405f8d192f17e8f1ffb8dfdbc82219d903`,
  identical to `entry.png` in the repo. PASS.
- `entry.png` sha256:
  `70595ea690f3b656a81ee14136668e405f8d192f17e8f1ffb8dfdbc82219d903`

## Transcripts
Bundled from inside the unpacked kit. The builder's own usage rows are
written only when its run finishes: BEFORE SUBMITTING, re-run the
muse.db SELECT with both agent ids (this subagent's and the parent's),
write the rows to a muse-usage file, and bundle again, then re-run check.
