# news-image-20261117 entry: copy the bundled image to /output/entry.png.
# Python 3.13, standard library only. No network, no randomness:
# every run writes the same bytes as the entry.png beside this file.
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(OUT, "entry.png")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


os.makedirs(OUT, exist_ok=True)
shutil.copyfile(SRC, DST)

# Guard: the judge sees exactly the bytes we ship; refuse a partial or
# corrupted copy rather than submitting a broken image.
if os.path.getsize(DST) != os.path.getsize(SRC):
    raise SystemExit("entry.png copy incomplete")
if sha256(DST) != sha256(SRC):
    raise SystemExit("entry.png copy hash mismatch")
