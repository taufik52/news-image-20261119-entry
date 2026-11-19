#!/usr/bin/env python3
"""Entry for make.fun news-image-20261119: sum up 19 November 2026 world news in one image.

The image (entry.png, JPEG bytes, 1024x1024, <1 MiB) is a newspaper front
page for Thursday 19 November 2026, built from that day's reported news:
Trump, Xi and Putin hold their first three-way talks at the APEC summit in
Shenzhen as Iran strikes US sites in Kuwait; the Gulf war widens, with Iran
hitting Kuwait and Bahrain after the US strike on Qeshm Island and three US
carrier groups now in the region; Democrats nominate Hakeem Jeffries, set to
be the first Black US Speaker, after the party's biggest Senate gains in
nearly 70 years; GTA VI launches worldwide after a 13-year wait, gamers
enter Vice City; and NASA's Voyager 1 reaches one light-day from Earth.
Ticker: Cyclone Akvan heads for India's east coast, Nvidia halts H-series
chips to China, the EU proposes a 45bn euro Ukraine loan, the Fed signals
more rate hikes, Russia accuses France of troops in Ukraine, and Australia
sanctions Israeli settlements. The program copies it to /output/entry.png
(or $MAKEFUN_OUTPUT_DIR/entry.png). Deterministic: same input bytes always
produce the same output bytes. No network, stdlib only.
"""
import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")
os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, OUT)


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


# Self-check: the copied file must be byte-identical to the source image.
# A partial or failed copy must fail loudly instead of scoring a corrupt image.
if _sha256(SRC) != _sha256(OUT):
    raise SystemExit("entry.png copy failed verification")
print("wrote {} ({} bytes, sha256 {})".format(OUT, os.path.getsize(OUT), _sha256(OUT)[:16]))
