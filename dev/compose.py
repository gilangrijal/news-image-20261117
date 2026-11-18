# Build script for the news-image-20261117 entry (dev tool, NOT the entrypoint).
# Composes entry.png (1024x1024) entirely with PIL: a newspaper front page
# with a masthead and six panels, each with a flat drawn motif, a bold
# headline and a short summary. No photos, no network, no randomness:
# every run writes the same bytes.
# Run: python3 dev/compose.py  (from repo root)
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

W, H = 1024, 1024
NAVY = (13, 27, 46)
PANEL = (22, 45, 68)
PANEL2 = (18, 38, 58)
GOLD = (242, 181, 68)
WHITE = (255, 255, 255)
GREY = (178, 190, 205)
LIGHT = (214, 226, 238)
RED = (198, 60, 48)
SKY = (46, 111, 164)
DUSK = (232, 126, 62)
SEA = (28, 78, 110)


def font(name, size):
    for path in (
        f"/usr/share/fonts/truetype/dejavu/{name}",
        f"/usr/share/fonts/truetype/liberation/{name}",
    ):
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size)


BOLD = "DejaVuSans-Bold.ttf"
REG = "DejaVuSans.ttf"
SERIFB = "DejaVuSerif-Bold.ttf"


def wrap(draw, text, f, max_w, max_lines):
    """Greedy word wrap; returns list of lines (at most max_lines)."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines[:max_lines]


def fit_headline(draw, text, max_w, max_lines=3, start=29):
    size = start
    while size >= 20:
        f = font(BOLD, size)
        lines = wrap(draw, text, f, max_w, max_lines)
        if len(lines) <= max_lines and all(
            draw.textlength(ln, font=f) <= max_w for ln in lines
        ):
            return f, lines
        size -= 1
    return font(BOLD, 20), wrap(draw, text, font(BOLD, 20), max_w, max_lines)


def fit_body(draw, text, max_w, max_lines=4, start=17):
    size = start
    while size >= 14:
        f = font(REG, size)
        lines = wrap(draw, text, f, max_w, max_lines)
        if len(lines) <= max_lines:
            return f, lines
        size -= 1
    return font(REG, 14), wrap(draw, text, font(REG, 14), max_w, max_lines)


# ---- drawn motifs: flat vector scenes, one per story (x, y, w, h) ----
def motif_hormuz(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(58, 74, 96))
    d.ellipse([x + w - 52, y + 14, x + w - 8, y + 58], fill=DUSK)  # low sun
    d.rectangle([x, y + h - 58, x + w, y + h], fill=SEA)  # strait
    d.rectangle([x + 28, y + h - 108, x + w - 28, y + h - 58], fill=(40, 44, 52))
    for cx in range(x + 44, x + w - 40, 34):
        d.rectangle([cx, y + h - 128, cx + 22, y + h - 108], fill=(120, 90, 60))
    d.polygon([(x + 60, y + h - 128), (x + 90, y + 26), (x + 96, y + 26),
               (x + 72, y + h - 128)], fill=(200, 200, 200))  # smoke plume
    d.ellipse([x + 78, y + 18, x + 118, y + 52], fill=(210, 210, 210))
    d.ellipse([x + 96, y + 8, x + 128, y + 36], fill=(225, 225, 225))
    d.polygon([(x + 96, y + 26), (x + 150, y + 60), (x + 108, y + 34)],
              fill=(255, 220, 120))  # missile arc
    d.polygon([(x + 150, y + 60), (x + 158, y + 52), (x + 166, y + 62),
               (x + 156, y + 68)], fill=(255, 255, 255))
    d.polygon([(x + 166, y + 58), (x + 178, y + 52), (x + 180, y + 64),
               (x + 168, y + 66)], fill=(255, 140, 60))  # exhaust flame
    d.line([x + 10, y + h - 40, x + w - 10, y + h - 40], fill=(120, 180, 210), width=2)
    d.line([x + 30, y + h - 24, x + w - 30, y + h - 24], fill=(120, 180, 210), width=2)


def motif_bridge(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(120, 150, 175))
    d.polygon([(x, y + 62), (x + w, y + 62), (x + w, y + h), (x, y + h)],
              fill=(70, 95, 120))  # water
    d.rectangle([x, y + 52, x + w, y + 66], fill=(60, 60, 66))  # deck
    d.arc([x + 30, y - 6, x + w - 30, y + 66], 180, 360, fill=(60, 60, 66), width=6)
    gap = x + w // 2
    d.rectangle([gap - 26, y + 52, gap + 26, y + 66], fill=(120, 150, 175))
    d.polygon([(gap - 26, y + 66), (gap - 8, y + 96), (gap + 4, y + 66)],
              fill=(90, 90, 96))  # fallen section
    d.ellipse([gap - 30, y + 88, gap + 30, y + 118], fill=(200, 200, 200))
    d.line([x + 16, y + 84, x + w - 16, y + 84], fill=(220, 230, 240), width=2)
    d.line([x + 40, y + 104, x + w - 40, y + 104], fill=(220, 230, 240), width=2)


def motif_summit(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(24, 60, 96))
    d.ellipse([x + w - 70, y + 10, x + w - 18, y + 62], fill=(240, 220, 180))
    d.rectangle([x, y + h - 34, x + w, y + h], fill=(90, 40, 40))  # table
    for i, (cx, kind) in enumerate([
        (x + 52, "us"), (x + w // 2, "cn"), (x + w - 52, "ru"),
    ]):
        d.line([cx, y + 18, cx, y + h - 34], fill=(220, 220, 220), width=3)
        if kind == "us":  # red stripes on white, blue canton
            d.rectangle([cx, y + 18, cx + 44, y + 52], fill=(255, 255, 255))
            for sy in (y + 22, y + 32, y + 42):
                d.rectangle([cx, sy, cx + 44, sy + 5], fill=(200, 40, 40))
            d.rectangle([cx, y + 18, cx + 20, y + 34], fill=(40, 60, 140))
        elif kind == "cn":  # red with yellow stars
            d.rectangle([cx, y + 18, cx + 44, y + 52], fill=(200, 40, 40))
            for sx, sy in [(cx + 8, y + 24), (cx + 20, y + 22),
                           (cx + 26, y + 32), (cx + 10, y + 36)]:
                d.ellipse([sx, sy, sx + 6, sy + 6], fill=(255, 220, 60))
        else:  # white / blue / red bands
            d.rectangle([cx, y + 18, cx + 44, y + 29], fill=(255, 255, 255))
            d.rectangle([cx, y + 29, cx + 44, y + 40], fill=(40, 90, 200))
            d.rectangle([cx, y + 40, cx + 44, y + 52], fill=(200, 40, 40))


def motif_measles(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(96, 28, 28))
    for cx, cy, r in [(x + 70, y + 62, 34), (x + 170, y + 44, 26),
                      (x + 240, y + 84, 30), (x + 120, y + 110, 22)]:
        for ang in range(0, 360, 30):
            import math
            x2 = cx + int((r + 12) * math.cos(math.radians(ang)))
            y2 = cy + int((r + 12) * math.sin(math.radians(ang)))
            d.line([cx, cy, x2, y2], fill=(240, 120, 110), width=3)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(198, 60, 48))
        d.ellipse([cx - r // 2, cy - r // 2, cx, cy], fill=(240, 140, 130))
    d.rectangle([x + w - 78, y + 18, x + w - 14, y + 62], outline=(255, 255, 255), width=4)
    d.text((x + w - 46, y + 30), "2000", font=font(BOLD, 15), fill=WHITE, anchor="ma")


def motif_outage(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(30, 34, 44))
    for i in range(3):
        rx = x + 30 + i * 78
        d.rectangle([rx, y + 20, rx + 62, y + h - 24], fill=(52, 58, 70))
        for j in range(3):
            d.rectangle([rx + 8, y + 30 + j * 34, rx + 54, y + 52 + j * 34],
                        fill=(20, 22, 28))
        d.ellipse([rx + 48, y + 28, rx + 56, y + 36], fill=(240, 60, 60))
    d.polygon([(x + w - 46, y + 16), (x + w - 78, y + 74), (x + w - 58, y + 74),
               (x + w - 84, y + 128), (x + w - 30, y + 58), (x + w - 52, y + 58)],
              fill=(255, 220, 60))  # lightning bolt


def motif_jets(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(140, 180, 210))
    d.ellipse([x + w - 84, y + 12, x + w - 12, y + 84], fill=(214, 48, 49))
    for jx, jy, s in [(x + 40, y + 78, 1.0), (x + 130, y + 30, 0.6)]:
        # jet: long fuselage, swept wings, tail fin
        d.polygon([(jx, jy + 10 * s), (jx + 96 * s, jy + 10 * s),
                   (jx + 108 * s, jy + 16 * s), (jx + 96 * s, jy + 22 * s),
                   (jx, jy + 22 * s)], fill=(40, 44, 52))
        d.polygon([(jx + 44 * s, jy + 10 * s), (jx + 60 * s, jy - 14 * s),
                   (jx + 72 * s, jy + 10 * s)], fill=(40, 44, 52))
        d.polygon([(jx + 44 * s, jy + 22 * s), (jx + 60 * s, jy + 44 * s),
                   (jx + 72 * s, jy + 22 * s)], fill=(40, 44, 52))
        d.polygon([(jx, jy + 10 * s), (jx + 8 * s, jy - 6 * s),
                   (jx + 18 * s, jy + 10 * s)], fill=(40, 44, 52))
    d.line([x + 16, y + h - 30, x + w - 16, y + h - 30], fill=(255, 255, 255), width=2)
    d.line([x + 40, y + h - 14, x + w - 40, y + h - 14], fill=(255, 255, 255), width=2)


STORIES = [
    ("MIDDLE EAST", "U.S. STRIKES IRAN",
     "Warplanes hit a missile site on Qeshm Island after tanker "
     "attacks in the Strait of Hormuz. 24 seafarers were evacuated.", motif_hormuz, (58, 74, 96)),
    ("EUROPE", "KERCH BRIDGE HIT",
     "Ukrainian drones and missiles struck the Crimean Bridge. "
     "Verified video shows the road arch collapsed into the strait.", motif_bridge, (120, 150, 175)),
    ("ASIA", "TRUMP HEADS TO CHINA SUMMIT",
     "President Trump travels to China for a trilateral summit "
     "with Xi Jinping and Vladimir Putin, after a Quad meeting "
     "in Manila.", motif_summit, (24, 60, 96)),
    ("HEALTH", "U.S. LOSES MEASLES-FREE STATUS",
     "The Pan American Health Organization says the U.S. has "
     "lost measles elimination status \u2014 the first time "
     "since 2000.", motif_measles, (96, 28, 28)),
    ("TECHNOLOGY", "OUTAGES HIT NSA, AIRPORTS, APPLE",
     "The NSA\u2019s classified network went offline amid outages "
     "at airports, banks and Apple. The DNI denies a cyberattack.", motif_outage, (30, 34, 44)),
    ("ASIA-PACIFIC", "JAPAN SCRAMBLES JETS",
     "Tokyo sent fighter jets up after two suspected Russian "
     "aircraft entered its airspace, and lodged a formal "
     "protest with Moscow.", motif_jets, (140, 180, 210)),
]

FOOTER_TICKER = ("ALSO: Wall Street falls as tech stocks slide  \u00b7  Winter rain "
                 "floods shelters in Gaza  \u00b7  Depardieu admits assault "
                 "charge in Paris")
FOOTER_SRC = "Sources: Reuters, AP, PAHO, UN  \u00b7  Tuesday 17 November 2026"


def main():
    canvas = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(canvas)

    # --- masthead ---
    d.text((W // 2, 30), "THE WORLD IN ONE IMAGE",
           font=font(SERIFB, 54), fill=WHITE, anchor="ma")
    d.text((W // 2, 96), "TUESDAY  \u00b7  17 NOVEMBER 2026",
           font=font(BOLD, 28), fill=GOLD, anchor="ma")
    d.line([20, 138, W - 20, 138], fill=GOLD, width=3)

    # --- six panels, 3 x 2 ---
    px, py = 20, 152
    pw, ph = 318, 400
    gx, gy = 14, 14
    for i, (kicker, headline, summary, motif, bg) in enumerate(STORIES):
        x = px + (i % 3) * (pw + gx)
        y = py + (i // 3) * (ph + gy)
        d.rectangle([x, y, x + pw, y + ph], fill=PANEL)
        d.rectangle([x, y, x + pw, y + ph], outline=(70, 95, 120), width=2)
        motif(d, x + 2, y + 2, pw - 4, 150)
        d.rectangle([x, y + 152, x + pw, y + 152], fill=GOLD, width=0)
        d.line([x, y + 152, x + pw, y + 152], fill=GOLD, width=3)
        d.text((x + 16, y + 168), kicker, font=font(BOLD, 16), fill=GOLD)
        hf, hlines = fit_headline(d, headline, pw - 32)
        ty = y + 194
        for ln in hlines:
            d.text((x + 16, ty), ln, font=hf, fill=WHITE)
            ty += hf.size + 4
        bf, blines = fit_body(d, summary, pw - 32)
        ty += 6
        for ln in blines:
            d.text((x + 16, ty), ln, font=bf, fill=LIGHT)
            ty += bf.size + 6

    # --- footer ticker ---
    d.line([20, 972, W - 20, 972], fill=(70, 95, 120), width=2)
    d.text((20, 982), FOOTER_TICKER, font=font(REG, 15), fill=GREY)
    d.text((20, 1002), FOOTER_SRC, font=font(BOLD, 14), fill=GOLD)

    out = os.path.join(HERE, "entry.png")
    canvas.save(out, "PNG", optimize=True)
    print(f"wrote {out} {os.path.getsize(out)} bytes")


if __name__ == "__main__":
    main()
