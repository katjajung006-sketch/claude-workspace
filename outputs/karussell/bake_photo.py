#!/usr/bin/env python3
# Backt den Cover-/Schluss-Gradienten fest ins Foto (ein flaches Bild).
# Grund: Canva flacht beim PDF-Import den separaten Gradient-Layer zu Deckend ab und verdeckt das Foto.
# Loesung: Foto + Gradient als EIN Bild rendern (Headless-Chrome-Screenshot, bewaehrt) -> Canva zeigt es korrekt.

import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
PHOTO = os.path.join(HERE, "katja.jpg")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

COVER_GRAD = ("linear-gradient(to bottom,"
              "rgba(58,45,40,.15) 0%,rgba(58,45,40,.35) 48%,rgba(58,45,40,.86) 100%)")
CLOSE_GRAD = ("linear-gradient(to bottom,"
              "rgba(58,45,40,.30) 0%,rgba(58,45,40,.55) 40%,rgba(58,45,40,.92) 100%)")

TPL = """<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:#3A2D28;}}
.wrap{{position:relative;width:1080px;height:1350px;}}
.photo{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 22%;}}
.scrim{{position:absolute;inset:0;background:{grad};}}
</style></head><body>
<div class="wrap"><img class="photo" src="file://{photo}"><div class="scrim"></div></div>
</body></html>"""


def bake(name, grad):
    html_path = os.path.join(HERE, "_bake_" + name + ".html")
    png_path = os.path.join(HERE, name + ".png")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(TPL.format(grad=grad, photo=PHOTO))
    subprocess.run([
        CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", "--window-size=1080,1350",
        "--virtual-time-budget=5000", f"--screenshot={png_path}",
        f"file://{html_path}",
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove(html_path)
    print(name + ".png")


if __name__ == "__main__":
    bake("cover_bg", COVER_GRAD)
    bake("close_bg", CLOSE_GRAD)
